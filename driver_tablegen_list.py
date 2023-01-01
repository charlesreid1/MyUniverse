import sys

from src.Generators.TableGenerator import TableGenerator


def main():
    g = TableGenerator()
    group_names = sorted(list(g.get_groups()))
    for group_name in group_names:
        print(f"* {group_name}")
        group = sorted(list(g.get_group(group_name)))
        for category in group:
            print(f"    * {category}")

if __name__=="__main__":
    main()

