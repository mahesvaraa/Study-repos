# Papers, Please

https://www.codewars.com/kata/59d582cafbdd0b7ef90000a0

![](https://i.imgur.com/mYgmiOz.jpg)

Papers, Please is an indie video game where the player takes on a the role of a border crossing immigration officer in
the fictional dystopian Eastern Bloc-like country of Arstotzka in the year 1982. As the officer, the player must review
each immigrant and returning citizen's passports and other supporting paperwork against a list of ever-increasing rules
using a number of tools and guides, allowing in only those with the proper paperwork, rejecting those without all proper
forms, and at times detaining those with falsified information.

**Objective**

Your task is to create a constructor function (or class) and a set of instance methods to perform the tasks of the
border checkpoint inspection officer. The methods you will need to create are as follow:

**Method**: receiveBulletin

Each morning you are issued an official bulletin from the Ministry of Admission. This bulletin will provide updates to
regulations and procedures and the name of a wanted criminal.

The bulletin is provided in the form of a string. It may include one or more of the following:

* Updates to the list of nations (comma-separated if more than one) whose citizens may enter (begins empty, before the
  first bulletin):

```
example 1: Allow citizens of Obristan
example 2: Deny citizens of Kolechia, Republia
```

* Updates to required documents

```
example 1: Foreigners require access permit
example 2: Citizens of Arstotzka require ID card
example 3: Workers require work pass
```

* Updates to required vaccinations

```
example 1: Citizens of Antegria, Republia, Obristan require polio vaccination
example 2: Entrants no longer require tetanus vaccination
```

* Update to a currently wanted criminal

```
example 1: Wanted by the State: Hubert Popovic
```

**Method**: inspect

Each day, a number of entrants line up outside the checkpoint inspection booth to gain passage into Arstotzka.
The `inspect` method will receive an object representing each entrant's set of identifying documents. This object will
contain zero or more properties which represent separate documents. Each property will be a string value. These
properties may include the following:

* Applies to all entrants:
  `passport`
  certificate_of_vaccination
* Applies only to citizens of Arstotzka
  `ID_card`
* Applies only to foreigners:
  `access_permit`
  `work_pass`
  `grant_of_asylum`
  `diplomatic_authorization`

The `inspect` method will return a result based on whether the entrant passes or fails inspection:

**Conditions for passing inspection**

* All required documents are present
* There is no conflicting information across the provided documents
* All documents are current (ie. none have expired) -- a document is considered expired if the expiration date
  is `November 22, 1982` or earlier
* The entrant is not a wanted criminal
* If a `certificate_of_vaccination` is required and provided, it must list the required vaccination
* A "worker" is a foreigner entrant who has `WORK` listed as their purpose on their access permit
* If entrant is a foreigner, a `grant_of_asylum` or `diplomatic_authorization` are acceptable in lieu of
  an `access_permit`. In the case where a `diplomatic_authorization` is used, it must include `Arstotzka` as one of the
  list of nations that can be accessed.

If the entrant passes inspection, the method should return one of the following string values:

* If the entrant is a citizen of Arstotzka:` Glory to Arstotzka.`
* If the entrant is a foreigner: `Cause no trouble.`

If the entrant fails the inspection due to expired or missing documents, or their `certificate_of_vaccination` does not
include the necessary vaccinations, return `Entry denied`: with the reason for denial appended.

```python
Example 1: Entry denied: passport expired.
Example 2: Entry denied: missing required vaccination.
Example 3: Entry denied: missing required access permit.
```

If the entrant fails the inspection due to mismatching information between documents (causing suspicion of forgery) or
if they're a wanted criminal, return `Detainment:` with the reason for detainment appended.

* If due to information mismatch, include the mismatched item. e.g.`Detainment: ID number mismatch.`
* If the entrant is a wanted criminal: `Detainment: Entrant is a wanted criminal.`
* **NOTE**: One wanted criminal will be specified in each daily bulletin, and must be detained when received for that
  day only. For example, if an entrant on Day 20 has the same name as a criminal declared on Day 10, they are not to be
  detained for being a criminal.
  Also, if any of an entrant's identifying documents include the name of that day's wanted criminal (in case of
  mismatched names across multiple documents), they are assumed to be the wanted criminal.

In some cases, there may be multiple reasons for denying or detaining an entrant. For this exercise, you will only need
to provide one reason.

* If the entrant meets the criteria for both entry denial and detainment, priority goes to detaining.
  For example, if they are missing a required document and are also a wanted criminal, then they should be detained
  instead of turned away.
* In the case where the entrant has mismatching information and is a wanted criminal, detain for being a wanted
  criminal.

**Test Example**

```python
bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""

inspector = Inspector()
inspector.receive_bulletin(bulletin)

entrant1 = {
    "passport": """ID#: GC07D-FU8AR
    NATION: Arstotzka
    NAME: Guyovich, Russian
    DOB: 1933.11.28
    SEX: M
    ISS: East Grestin
    EXP: 1983.07.10"""
}

inspector.inspect(entrant1) #=> 'Glory to Arstotzka.'
```

**Additional Notes**

* Inputs will always be valid.
* There are a total of 7 countries: `Arstotzka`, `Antegria`, `Impor`, `Kolechia`, `Obristan`, `Republia`,
  and `United Federation`.
* Not every single possible case has been listed in this Description; use the test feedback to help you handle all
  cases.
* The concept of this kata is derived from the video game of the same name, but it is not meant to be a direct
  representation of the game.

If you enjoyed this kata, be sure to check out my other katas.

# Solution

```python
import re
from collections import namedtuple
from datetime import datetime, timedelta

IDCard = namedtuple("IDCard", "name dob height weight")
AccessPermit = namedtuple("AccessPermit", "name nation id purpose duration height weight exp")
VaccinationCertificate = namedtuple("VaccinationCertificate", "name id vaccines")
DiplomaticAuthorization = namedtuple("DiplomaticAuthorization", "name nation id access")
AsylumGrant = namedtuple("AsylumGrant", "name nation id dob height weight exp")
Passport = namedtuple("Passport", "id nation name dob sex iss exp")
WorkPass = namedtuple("WorkPass", "name field exp")


def to_date(date_str):
    return datetime.strptime(date_str, "%Y.%m.%d")


class Entrance:
    def __init__(self):
        self.id_card = None
        self.access_permit = None
        self.certificate_of_vaccination = None
        self.diplomatic_authorization = None
        self.grant_of_asylum = None
        self.passport = None
        self.work_pass = None
        self.docs = []

    def save_info(self, documents):
        for doc_type, doc_string in documents.items():
            info = re.findall(r"(?<=: ).+", doc_string)

            if doc_type == "ID_card":
                self.id_card = IDCard(*info)
                
            elif doc_type == "access_permit":
                self.access_permit = AccessPermit(*info)
                
            elif doc_type == "certificate_of_vaccination":
                self.certificate_of_vaccination = VaccinationCertificate(*info)
                
            elif doc_type == "diplomatic_authorization":
                self.diplomatic_authorization = DiplomaticAuthorization(*info)
                
            elif doc_type == "grant_of_asylum":
                if len(info) == 6:
                    info.insert(3, None)
                self.grant_of_asylum = AsylumGrant(*info)
                
            elif doc_type == "passport":
                self.passport = Passport(*info)
                
            elif doc_type == "work_pass":
                self.work_pass = WorkPass(*info)

            self.docs = [
                self.id_card,
                self.access_permit,
                self.certificate_of_vaccination,
                self.diplomatic_authorization,
                self.grant_of_asylum,
                self.passport,
                self.work_pass,
            ]

    @property
    def name(self):
        return {doc.name for doc in self.docs if doc}

    @property
    def dob(self):
        return {doc.dob for doc in self.docs if doc and hasattr(doc, "dob") and doc.dob}

    @property
    def nation(self):
        return {doc.nation for doc in self.docs if doc and hasattr(doc, "nation")}

    @property
    def id(self):
        return {doc.id for doc in self.docs if doc and hasattr(doc, "id")}

    @property
    def have_access(self):
        return any(
            (
                self.access_permit,
                self.grant_of_asylum,
                self.diplomatic_authorization and "Arstotzka" in self.diplomatic_authorization.access,
            )
        )


class Inspector:
    current_date = datetime.strptime("1982.11.22", "%Y.%m.%d")

    def __init__(self):
        self.rules = []
        self.wanted_by_state = []
        self.foreigners_require = []
        self.require_vaccination = []
        
        self.allow_citizens = set()
        
        self.wanted_by_state_date = None
        self.citizens_require_id_card = False
        self.entrants_require_passport = False
        self.workers_require_work_pass = False
        self.foreigners_require_access_permit = False

    def receive_bulletin(self, bulletin):
        self.rules = bulletin.split("\n")

        for string in self.rules:
            match = re.search(r"Allow citizens of (.+)", string)
            if match:
                self.allow_citizens |= {country.strip() for country in match.group(1).split(",")}
                
            match = re.search(r"Deny citizens of (.+)", string)
            if match:
                self.allow_citizens -= {country.strip() for country in match.group(1).split(",")}
                
            match = re.search(r"Entrants require (.+) vaccination", string)
            if match:
                self.require_vaccination.append(match.group(1))
                
            match = re.search(r"Entrants no longer require (.+) vaccination", string)
            if match:
                self.require_vaccination = list(set(self.require_vaccination) - set(match.group(1)))
                
            match = re.search(r"Wanted by the State: (.+)", string)
            if match:
                self.wanted_by_state.append(", ".join(match.group(1).split()[::-1]))
                self.wanted_by_state_date = self.current_date

            match = re.search(r"Foreigners require (.+) vaccination", string)
            if match:
                self.foreigners_require.append(match.group(1))
                
            match = re.search(r"Foreigners no longer require (.+) vaccination", string)            
            if match:
                self.foreigners_require = list(set(self.foreigners_require) - set(match.group(1)))
                
            match = re.search(r"Foreigners no longer require (.+) vaccination", string)
            if match:
                self.foreigners_require = list(set(self.foreigners_require) - set(match.group(1)))
                
            match = re.search(r"Entrants no longer require (.+) vaccination", string)
            if match:
                self.require_vaccination = list(set(self.require_vaccination) - set(match.group(1)))
                
            if "Citizens of Arstotzka require ID card" in string:
                self.citizens_require_id_card = True
                
            if "Entrants require passport" in string:
                self.entrants_require_passport = True
                
            if "Workers require work pass" in string:
                self.workers_require_work_pass = True
                
            if "Foreigners require access permit" in string:
                self.foreigners_require_access_permit = True
        Inspector.current_date += timedelta(days=1)

    def inspect(self, entrance):
        _entrance = Entrance()
        _entrance.save_info(entrance)
        print(self.rules, _entrance.docs)

        if self.entrants_require_passport and not _entrance.passport and not _entrance.id_card:
            return "Entry denied: missing required passport."

        if len(_entrance.id) != 1:
            return "Detainment: ID number mismatch."

        if _entrance.name & set(self.wanted_by_state):
            return "Detainment: Entrant is a wanted criminal."

        if len(_entrance.dob) != 1:
            return "Detainment: date of birth mismatch."

        if len(_entrance.name) != 1:
            return "Detainment: name mismatch."

        if len(_entrance.nation) != 1:
            return "Detainment: nationality mismatch."

        if to_date(_entrance.passport.exp) < Inspector.current_date:
            return "Entry denied: passport expired."

        if self.entrants_require_passport and not _entrance.passport:
            return "Entry denied: missing required passport."

        if _entrance.passport.nation == "Arstotzka":
            if self.citizens_require_id_card and not _entrance.id_card:
                return "Entry denied: missing required ID card."
            if self.require_vaccination:
                if not _entrance.certificate_of_vaccination:
                    return "Entry denied: missing required certificate of vaccination."
                if not set(self.require_vaccination).issubset(_entrance.certificate_of_vaccination.vaccines.split(", ")):
                    return "Entry denied: missing required vaccination."

        else:
            if self.foreigners_require_access_permit and not _entrance.have_access:
                if _entrance.diplomatic_authorization and "Arstotzka" not in _entrance.diplomatic_authorization.access:
                    return "Entry denied: invalid diplomatic authorization."
                return "Entry denied: missing required access permit."
            
            if _entrance.access_permit and to_date(_entrance.access_permit.exp) < Inspector.current_date:
                return "Entry denied: access permit expired."
            
            if _entrance.grant_of_asylum and to_date(_entrance.grant_of_asylum.exp) < Inspector.current_date:
                return "Entry denied: grant of asylum expired."
            
            if _entrance.work_pass and to_date(_entrance.work_pass.exp) < Inspector.current_date:
                return "Entry denied: work pass expired."

            if _entrance.nation.pop() not in self.allow_citizens:
                return "Entry denied: citizen of banned nation."

            if self.workers_require_work_pass and _entrance.access_permit and _entrance.access_permit.purpose == "WORK" and not _entrance.work_pass:
                return "Entry denied: missing required work pass."

            if self.foreigners_require:
                if not _entrance.certificate_of_vaccination:
                    return "Entry denied: missing required certificate of vaccination."
                
                if not set(self.foreigners_require).issubset(_entrance.certificate_of_vaccination.vaccines.split(", ")):
                    return "Entry denied: missing required vaccination."
                
        return "Glory to Arstotzka." if _entrance.passport.nation == "Arstotzka" else "Cause no trouble."

```
