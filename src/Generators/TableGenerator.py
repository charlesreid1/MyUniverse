from .tablegen import table


class TableGenerator:
    def __init__(self):
        self.tablemanager = table.tableMgr()
        table.walktree('Data/Tables', self.tablemanager.addfile)
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
        
