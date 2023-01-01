import sys

from src.Generators.StateGenerator import StateGenerator
#from src.Generators.SectorGenerator import SectorGenerator
#from src.Generators.SystemGenerator import SystemGenerator
#from src.Generators.PlanetGenerator import PlanetGenerator
#from src.Generators.CharacterGenerator import CharacterGenerator
#from src.Generators.PlanetImageGenerator import PlanetImageGenerator


def main():
    sg = StateGenerator()

    group_names = sorted(list(sg.get_groups()))
    for group_name in group_names:
        group = sorted(list(sg.get_group(group_name)))
        for category in group:
            try:
                s1 = sg.roll(category, 1)
                s2 = sg.roll(category, 1) 
                s3 = sg.roll(category, 1) 
            except:
                continue
            print("-"*40)
            print(category)
            print()
            print(' - ' + s1)
            print(' - ' + s2)
            print(' - ' + s3)
            print()


if __name__=="__main__":
    main()

