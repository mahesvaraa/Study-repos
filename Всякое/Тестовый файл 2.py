import re
from datetime import timedelta, date


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
            assert entrance.passport, 'Entry denied: missing required passport.'
            if 'Arstotzka' in entrance.nation:
                assert all(
                    map(lambda x: x not in self.wanted, entrance.name)), 'Detainment: Entrant is a wanted criminal.'
                assert len(entrance.name) == 1, 'Detainment: name mismatch.'
                assert len(entrance.dob) == 1, 'Detainment: date of birth mismatch.'
                assert len(entrance.nation) == 1, 'Detainment: nationality mismatch.'
                assert len(entrance.id) == 1, 'Detainment: ID number mismatch.'
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
                assert all(
                    map(lambda x: x not in self.wanted, entrance.name)), 'Detainment: Entrant is a wanted criminal.'
                assert len(entrance.dob) == 1, 'Detainment: date of birth mismatch.'
                assert len(entrance.nation) == 1, 'Detainment: nationality mismatch.'
                assert len(entrance.id) == 1, 'Detainment: ID number mismatch.'
                if self.requirements['access_permit']:
                    assert entrance.access_permit or entrance.diplomatic_authorization or entrance.grant_of_asylum, 'Entry denied: missing required access permit.'
                assert START_DATE < date(*map(int, entrance.passport_exp.split('.'))), 'Entry denied: passport expired.'
                if entrance.access_permit:
                    assert START_DATE < date(
                        *map(int, entrance.access_permit_exp.split('.'))), 'Entry denied: access permit expired.'
                if entrance.grant_of_asylum:
                    assert START_DATE < date(
                        *map(int, entrance.grant_of_asylum_exp.split('.'))), 'Entry denied: grant of asylum expired.'
                if entrance.work_pass:
                    assert START_DATE < date(
                        *map(int, entrance.work_pass_exp.split('.'))), 'Entry denied: work pass expired.'
                if entrance.diplomatic_authorization:
                    assert entrance.access, 'Entry denied: invalid diplomatic authorization.'
                assert tuple(entrance.nation)[0] in self.allow_nations, 'Entry denied: citizen of banned nation.'
                if self.requirements['certificate_of_vaccination']:
                    assert self.vaccinations['Arstotzka'].issubset(
                        set(entrance.vacs)), 'Entry denied: missing required vaccination.'
                if entrance.purpose == 'WORK':
                    assert bool(entrance.work_pass) == self.requirements[
                        'work_pass'], 'Entry denied: missing required work pass.'
                return 'Cause no trouble.'
        except AssertionError as inst:
            return inst.args[0]
