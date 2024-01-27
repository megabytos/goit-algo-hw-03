from pathlib import Path
import argparse
import shutil
import sys

def parse_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", type=Path, required=True)
    parser.add_argument("-d", "--destination", type=Path, default=Path("dist"))
    return parser.parse_args()


def recursive_copy(source: Path, destination: Path):
    for el in source.iterdir():
        if el.is_dir():
            recursive_copy(el, destination)
        else:            
            target = destination / Path(el.name).suffix[1:]
            target.mkdir(exist_ok=True, parents=True)
            try:
                shutil.copy(el, target)
            except IOError as e:
                print("Unable to copy file. %s" % e)
            except:
                print("Unexpected error:", sys.exc_info())
            

def main():
    args = parse_argv()
    recursive_copy(args.source, args.destination)
    


if __name__ == "__main__":
    main()