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
from datetime import timedelta, date
import re


class Entrance:

    def __init__(self, documents):
        self.name = set()
        self.id = set()
        self.dob = set()
        self.nation = set()
        # passport
        self.passport = False
        self.passport_exp = None
        # id card
        self.id_card = False
        # access permit
        self.access_permit = False
        self.purpose = None
        self.access_permit_exp = None
        self.access = False
        # work pass
        self.work_pass = False
        self.work_pass_exp = None
        # vaccination
        self.certificate_of_vaccination = False
        self.vacs = []
        # grant of asylum
        self.grant_of_asylum = False
        self.grant_of_asylum_exp = None
        # diplomatic auth
        self.diplomatic_authorization = False

        self.documents = {}

        for doc in documents:
            self.documents[doc] = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in documents[doc].split('\n')}

        self.passport = self.documents.get('passport', False)
        if self.passport:
            self.id.add(self.passport['ID#'])
            self.dob.add(self.passport['DOB'])
            self.name.add(self.passport['NAME'])
            self.nation.add(self.passport['NATION'])
            self.passport_exp = self.passport['EXP']

        self.access_permit = self.documents.get('access_permit', False)
        if self.access_permit:
            self.id.add(self.access_permit['ID#'])
            self.name.add(self.access_permit['NAME'])
            self.access_permit_exp = self.access_permit['EXP']
            self.purpose = self.access_permit['PURPOSE']
            self.nation.add(self.access_permit['NATION'])

        self.work_pass = self.documents.get('work_pass', False)
        if self.work_pass:
            self.name.add(self.work_pass['NAME'])
            self.work_pass_exp = self.work_pass['EXP']

        self.diplomatic_authorization = self.documents.get('diplomatic_authorization', False)
        if self.diplomatic_authorization:
            self.id.add(self.diplomatic_authorization['ID#'])
            self.name.add(self.diplomatic_authorization['NAME'])
            self.nation.add(self.diplomatic_authorization['NATION'])
            self.access = 'Arstotzka' in self.diplomatic_authorization['ACCESS']

        self.certificate_of_vaccination = self.documents.get('certificate_of_vaccination', False)
        if self.certificate_of_vaccination:
            self.id.add(self.certificate_of_vaccination['ID#'])
            self.name.add(self.certificate_of_vaccination['NAME'])
            self.vacs = self.certificate_of_vaccination['VACCINES'].split(', ')

        self.grant_of_asylum = self.documents.get('grant_of_asylum', False)
        if self.grant_of_asylum:
            self.id.add(self.grant_of_asylum['ID#'])
            self.name.add(self.grant_of_asylum['NAME'])
            self.nation.add(self.grant_of_asylum['NATION'])
            self.grant_of_asylum_exp = self.grant_of_asylum['EXP']

        self.id_card = self.documents.get('ID_card', False)
        if self.id_card:
            self.dob.add(self.id_card['DOB'])
            self.name.add(self.id_card['NAME'])


START_DATE = date(1982, 11, 21)


class Inspector:
    START_DATE += timedelta(days=1)

    def __init__(self):
        self.rights = []
        self.allow_nations = []
        self.deny_nations = []
        self.wanted = []

        self.requirements = {
            'passport': False,
            'certificate_of_vaccination': False,
            'ID_card': False,
            'access_permit': False,
            'work_pass': False,
            'grant_of_asylum': False,
            'diplomatic_authorization': False
        }
        self.vaccinations = {
            'Arstotzka': set(),
            'Antegria': set(),
            'Impor': set(),
            'Kolechia': set(),
            'Obristan': set(),
            'Republia': set(),
            'United Federation': set()
        }

    def receive_bulletin(self, bulletin):
        self.rights += bulletin.split('\n')
        self.requirements['passport'] = 'Entrants require passport' in self.rights

        """Updates to the list of nations"""
        allow_nations = list(filter(lambda x: 'Allow citizens of ' in x or 'Deny citizens of ' in x, self.rights))
        for i in allow_nations:
            if 'Allow citizens of ' in i:
                self.allow_nations += i[18:].split(', ')
            if 'Deny citizens of ' in i:
                self.allow_nations = list(set(filter(lambda x: x not in i[17:].split(', '), self.allow_nations)))

        """Updates to required documents"""
        self.requirements['access_permit'] = 'Foreigners require access permit' in self.rights
        self.requirements['ID_card'] = 'Citizens of Arstotzka require ID card' in self.rights
        self.requirements['work_pass'] = 'Workers require work pass' in self.rights

        """Updates to required vaccinations"""
        citizens_vac = list(filter(lambda x: 'Citizens of ' in x and 'vaccination' in x, self.rights))
        entrants_vac = list(filter(lambda x: 'Entrants require ' in x and 'vaccination' in x, self.rights))
        no_citizens_vac = list(filter(lambda x: 'Citizens of ' in x and 'no longer' in x, self.rights))
        no_entrants_vac = list(filter(lambda x: 'Entrants ' in x and 'no longer' in x, self.rights))

        if citizens_vac:
            for vact in citizens_vac:
                vac = re.search(r'(?<=require )(.+?)(?= vaccination)', vact)[0]
                res = re.search(r'(?<=Citizens of )(.+?)(?= (no longer require|require))', vact)
                countries_vac = res[0].split(', ')
                for country in countries_vac:
                    self.vaccinations[country].add(vac)
        if entrants_vac:
            for vact in entrants_vac:
                vac = re.search(r'(?<=require )(.+?)(?= vaccination)', vact)[0]
                for country in self.vaccinations.keys():
                    self.vaccinations[country].add(vac)

        if no_citizens_vac:
            for vact in no_citizens_vac:
                vac = re.search(r'(?<=require )(.+?)(?= vaccination)', vact)[0]
                res = re.search(r'(?<=Citizens of )(.+?)(?= (no longer require))', vact)
                no_citizens_vac = res[0].split(', ')
                for country in no_citizens_vac:
                    self.vaccinations[country].remove(vac)

        if no_entrants_vac:
            for vact in no_entrants_vac:
                vac = re.search(r'(?<=require )(.+?)(?= vaccination)', vact)[0]
                for country in self.vaccinations.keys():
                    self.vaccinations[country].remove(vac)                    
        self.requirements['certificate_of_vaccination'] = any(self.vaccinations.values())
        
        """Update to a currently wanted criminal"""
        wanted_people = list(filter(lambda x: "Wanted by the State: " in x, self.rights))
        self.wanted = list(map(lambda x: x[21:], wanted_people))
        self.wanted += list(map(lambda x: x.split(' ')[1] + ', ' + x.split(' ')[0], self.wanted))

    def inspect(self, entrance):
        entrance = Entrance(entrance)
        try:
            assert all(map(lambda x: x not in self.wanted, entrance.name)), 'Detainment: Entrant is a wanted criminal.'
            assert entrance.passport and not all((entrance.grant_of_asylum, entrance.diplomatic_authorization, entrance.access_permit)) , 'Entry denied: missing required passport.'
            if 'Arstotzka' in entrance.nation:
                assert all(map(lambda x: x not in self.wanted, entrance.name)), 'Detainment: Entrant is a wanted criminal.'
                assert len(entrance.name) == 1, 'Detainment: name mismatch.'
                assert len(entrance.dob) == 1, 'Detainment: date of birth mismatch.'
                assert len(entrance.nation) == 1, 'Detainment: nationality mismatch.'
                assert len(entrance.id) == 1, 'Detainment: ID number mismatch.'
                assert entrance.passport, 'Entry denied: missing required passport.'
                assert START_DATE < date(*map(int, entrance.passport_exp.split('.'))), 'Entry denied: passport expired.'
                
                if self.requirements.get('ID_card', False):
                    assert bool(entrance.id_card) == self.requirements[
                        'ID_card'], 'Entry denied: missing required ID card.'

                if self.requirements['certificate_of_vaccination']:
                    assert self.vaccinations['Arstotzka'].issubset(
                        set(entrance.vacs)), 'Entry denied: missing required vaccination.'
                return 'Glory to Arstotzka.'

            else:

                assert len(entrance.name) == 1, 'Detainment: name mismatch.'
                assert all(map(lambda x: x not in self.wanted, entrance.name)), 'Detainment: Entrant is a wanted criminal.'
                assert len(entrance.dob) == 1, 'Detainment: date of birth mismatch.'
                assert len(entrance.nation) == 1, 'Detainment: nationality mismatch.'
                assert len(entrance.id) == 1, 'Detainment: ID number mismatch.'
                assert entrance.passport, 'Entry denied: missing required passport.'
                if self.requirements['access_permit']:
                    assert entrance.access_permit or entrance.diplomatic_authorization or entrance.grant_of_asylum, 'Entry denied: missing required access permit.'
                assert START_DATE < date(*map(int, entrance.passport_exp.split('.'))), 'Entry denied: passport expired.'
                if entrance.access_permit:
                    assert START_DATE < date(*map(int, entrance.access_permit_exp.split('.'))), 'Entry denied: access permit expired.'
                if entrance.grant_of_asylum:
                    assert START_DATE < date(*map(int, entrance.grant_of_asylum_exp.split('.'))), 'Entry denied: grant of asylum expired.'
                if entrance.work_pass:
                    assert START_DATE < date(*map(int, entrance.work_pass_exp.split('.'))), 'Entry denied: work pass expired.'
                if entrance.diplomatic_authorization:
                    assert entrance.access, 'Entry denied: invalid diplomatic authorization.'
                assert tuple(entrance.nation)[0] in self.allow_nations, 'Entry denied: citizen of banned nation.'
                if self.requirements['certificate_of_vaccination']:
                    assert bool(entrance.certificate_of_vaccination), 'Entry denied: missing required certificate of vaccination.'
                    assert self.vaccinations['Arstotzka'].issubset(set(entrance.vacs)), 'Entry denied: missing required vaccination.'
                if entrance.purpose == 'WORK':
                    assert bool(entrance.work_pass) == self.requirements['work_pass'], 'Entry denied: missing required work pass.'
                return 'Cause no trouble.'
        except AssertionError as inst:
            return inst.args[0]
```