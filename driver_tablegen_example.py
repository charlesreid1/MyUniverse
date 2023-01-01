import sys

from src.Generators.TableGenerator import TableGenerator


def main():
    g = TableGenerator()
    group_names = sorted(list(g.get_groups()))
    for group_name in group_names:
        group = sorted(list(g.get_group(group_name)))
        for category in group:
            try:
                s1 = g.roll(category, 1)
                s2 = g.roll(category, 1) 
                s3 = g.roll(category, 1) 
            except:
                continue
            print("-"*40)
            print(category)
            print()
            print(' - ' + s1)
            print(' - ' + s2)
            print(' - ' + s3)
            print()
        print()
        print("="*40)
        print()

if __name__=="__main__":
    main()


