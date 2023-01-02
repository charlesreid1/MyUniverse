import sys

from src.Generators.TableGenerator import TableGenerator


def main():
    category = 'Film Noir Monologue'
    g = TableGenerator(datadir='Data.small/Tables')
    # g.tablemanager.importTables() # <-- not needed, TableGenerator constructor should handle .tab files already
    for i in range(1000):
        _ = g.roll(category, 1)
        #print(s)
        #print()


if __name__=="__main__":
    main()

