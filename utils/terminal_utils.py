from os import system, name as __os_name


def clear_screen():
    '''Clears the terminal screen'''

    # For Windows
    if __os_name == 'nt':
        system('cls')

    # For macOS and Linux
    else:
        system('clear')
