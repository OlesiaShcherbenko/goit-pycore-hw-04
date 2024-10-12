import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def print_directory_structure(path: Path, indent: str = " "):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.GREEN}{item.name}/")
                print_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.WHITE}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Permission Denied] {path.name}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: pathon {sys.argv[0]} <directory_path>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Error: The path '{directory_path}' does not exist.")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"{Fore.RED} Error: The path '{directory_path}' is not a directory.")

    print(f"{Fore.YELLOW}Directory structure of {directory_path}:\n")
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()