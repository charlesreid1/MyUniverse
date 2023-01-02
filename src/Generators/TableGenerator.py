import os
from .tablegen import table


class TableGenerator:
    def __init__(self, datadir='Data/Tables'):
        self.tablemanager = table.tableMgr()
        if not os.path.exists(datadir) or not os.path.isdir(datadir):
            raise Exception(f"Error: data dir {datadir} does not exist or is not a dir")
        table.walktree(datadir, self.tablemanager.addfile)
        self.parameters = dict()
        self.parameters['Seed'] = ['', '0']
        self.pList = ['Seed', 'Group']

    def get_groups(self):
        return self.tablemanager.groups()

    def get_group(self, group):
        return self.tablemanager.group[group]

    def roll(self, category, numRolls):
        results = ''
        for j in range(numRolls):
            results += self.tablemanager.roll(category)
            results += '\n'
        return results
        
