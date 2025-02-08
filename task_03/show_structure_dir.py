from pathlib import Path
import sys
from colorama import init, Fore, Style


# Inizialization colorama
init(autoreset=True)

# Icons for directories, files, and brunches
root_dir = chr(0x1F4E6)
folder_icon = chr(0x1F4C1)
file_icon = chr(0x1F4DC) 
horizontal_branch = chr(0x2501)
branch = chr(0x2523) + horizontal_branch
last_branch = chr(0x2517) + horizontal_branch
vertical_branch = chr(0x2503)


def display_directory_structure(path: Path, prefix='', is_root=True):
    """
    The function takes a directory path and visualizes the structure of that directory, 
    displaying the names of all subdirectories and files.

    Parameters:
        path: path to the directory.

    Returns:
        The function returns nothing. The function only prints the stucrure and names of directories and files
    """

    # Create Path oject for directory 
    directory = Path(path)

    try:
        # Getting list of files and subdirectories
        entries = list(directory.iterdir())
    except PermissionError:
        print(Fore.RED + "Немає доступу до цієї директорії")
        return
    except FileNotFoundError:
        print(Fore.RED + "Шлях не знайдено")
        return
    
    # Find the number of files and subdirectories 
    entries_count = len(entries)

    if entries_count == 0:
        print(f"{prefix}{last_branch if not is_root else root_dir} (empty directory)\n")
        return
    
    for i, item in enumerate(entries):

        # Check if the element is last in the list
        is_last = (i == entries_count - 1)
        needed_branch = last_branch if is_last else branch

        if item.is_dir():
            # Print directory with color format and correct branch
            print(f"{prefix}{needed_branch} {folder_icon}{Fore.YELLOW}{item.name} \n")

            # Add vertical branch if it's not last entry
            new_prefix = prefix + ("   " if is_last else f"{vertical_branch}  ")

            # Called recursively for nested directories
            display_directory_structure(item, new_prefix, is_root=False)

        else:
            # Print file with color format and correct branch 
            print(f"{prefix}{needed_branch} {file_icon}{Fore.GREEN}{item.name}\n")


def main():

    # Check if command line has an argument
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії як аргумент.")
        print(f"Приклад: {sys.argv[0]} /шлях/до/директорії")

        # An error occurred and the program did not complete as expected.
        sys.exit(1) 

    # Getting the path from a command line argument
    path = Path(sys.argv[1])

    # Checking the existence of a path
    if not path.exists():
        print(Fore.RED + f"Шлях {path.absolute()} не існує. Перевірте введений шлях.")
        sys.exit(1)

    print(Style.BRIGHT + Fore.BLUE + f"{root_dir} {path.name}\n")
    display_directory_structure(path)

if __name__ == "__main__":
    main()