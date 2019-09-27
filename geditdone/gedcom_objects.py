class Individual:

    def __init__(self, id, name=None, sex=None, birth=None, death=None, famc=None, fams=None):
        self.id = id
        self.name = name
        self.sex = sex
        self.birth = birth
        self.death = death
        self.famc = famc
        self.fams = fams

    def toString(self):
        return '%s %s' % (self.id, self.name)

class Family:

    def __init__(self, id, husband_id=None, wife_id=None, married=None, divorced=None):
        self.id = id
        self.child_ids = []
        self.husband_id = husband_id
        self.wife_id = wife_id
        self.married = married
        self.divorced = divorced

    def toString(self, individuals = None):
        ''' Returns a string representation of the family. If a dictionary of individuals are provided, will attempt to lookup names. Otherwise only IDs will be given. ''' 
        if individuals == None:
            return '%s HUSB %s WIFE %s' % (self.id, self.husband_id, self.wife_id)
        else:
            husband = individuals[self.husband_id]
            wife = individuals[self.wife_id]
            return '%s HUSB %s WIFE %s' % (self.id, husband.toString(), wife.toString())