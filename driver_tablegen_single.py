import sys

from src.Generators.TableGenerator import TableGenerator


def main():
    category = 'Film Noir Monologue'
    g = TableGenerator()
    for i in range(10):
        import pdb; pdb.set_trace()
        s = g.roll(category, 1)
        print(s)
        print()

if __name__=="__main__":
    main()
