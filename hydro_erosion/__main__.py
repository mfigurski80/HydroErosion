
import sys
from . utilities import readCSV, writeCSV
from . erodeLandscape import erodeMap

def main():
    args = sys.argv[1:]
    if len(args) != 4:
        print("Arguments: [source.csv] [rock.csv] [destination.csv] <#iterations>")
        quit()
    source = args[0]
    rock_source = args[1]
    destination = args[2]
    iterations = int(args[3])
    print(f"Running: ({source}, {rock_source}) #{iterations} => {destination}")
    base_map = readCSV(source)
    rock = readCSV(rock_source)
    height, hydration = erodeMap(base_map, rock, iterations)
    writeCSV(height, destination)
    writeCSV(hydration, "hydrationmap.csv")
    #  viewMap(height)

if __name__ == "__main__":
    main()
