from .tablegen import table
from state import *

class StateGenerator:
    def __init__(self):
        self.tablemanager = table.tableMgr()
        table.walktree('Data/Tables', self.tablemanager.addfile)
        self.parameters = dict()
        self.parameters['Seed'] = ['', '0']
        self.parameters['Group'] = self.GetGeneratorGroups()
        self.parameters['Generators'] = []
        self.pList = ['Seed', 'Group', 'Generators']

    def get_groups(self):
        return self.tablemanager.groups()

    def get_group(self, group):
        return self.tablemanager.group[group]

    #def GetGeneratorGroups(self):
    #    # Get list of generators
    #    groupList = []
    #    for t in self.tablemanager.groups():
    #        groupList.append(t)
    #    groupList.sort()
    #    return groupList

    #def GetGeneratorList(self, p):
    #    # Get list of generators
    #    genList = []
    #    for x in self.tablemanager.group[p]:
    #        genList.append(x)
    #    genList.sort()
    #    return genList

    def roll(self, category, numRolls):
        results = ''
        for j in range(numRolls):
            results += self.tablemanager.roll(category)
            results += '\n'
        return results
        
