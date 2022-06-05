import os
from Ignore_directory import Ignore_directory


# give git pull command
def git_pull():
    os.system('git pull')


# change directory
def move_to_dir(path):
    os.chdir(path)


# check if is a directory
def is_dir(directory):
    return os.path.isdir(directory)


# get the actual path of the working directory
def get_path():
    return os.getcwd()


def ask_confirmation(path):
    print('Do you want to pull the repository in ' + path + '?')
    print('0. Yes')
    print('1. No')
    choice = input('Enter your choice: ')
    if choice != '0' and choice != '1':
        print('Invalid input')
        return ask_confirmation(path)
    return choice == '0'


# pull all repositories in the subdirectories
def pull_all(only_part, ignore_dir, script_path):
    if get_path() == script_path:
        return
    for i in os.listdir():
        if is_dir(i):
            if i == '.git' and (not only_part or ask_confirmation(get_path())):
                git_pull()
                print('Pulled ' + get_path())
            elif not ignore_dir.is_ignored(i):
                move_to_dir(i)
                pull_all(only_part, ignore_dir, script_path)
                move_to_dir('..')


def main():
    print('0. Do you want pull only part of the repositories')
    print('1. Do you want pull all repositories')
    only_part = input('Enter your choice: ')
    if only_part != '0' and only_part != '1':
        print('Invalid input')
        main()
        return

    only_part = only_part == '0'
    ignore_dir = Ignore_directory()
    script_path = get_path()
    move_to_dir('..')
    pull_all(only_part, ignore_dir, script_path)
    input('Press enter to exit')

main()
