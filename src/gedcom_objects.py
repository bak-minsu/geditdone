class Individual:
    def __init__(self, id):
        self.id = id

    def toString(self):
        return '%s %s' % (self.id, self.name)

class Family:
    def __init__(self, id):
        self.id = id
        self.child_ids = []

    def toString(self, individuals = None):
        ''' Returns a string representation of the family. If a dictionary of individuals are provided, will attempt to lookup names. Otherwise only IDs will be given. ''' 
        if individuals == None:
            return '%s HUSB %s WIFE %s' % (self.id, self.husband_id, self.wife_id)
        else:
            husband = individuals[self.husband_id]
            wife = individuals[self.wife_id]
            return '%s HUSB %s WIFE %s' % (self.id, husband.toString(), wife.toString())