import os
import shutil

def rename_with(dir_path="", name="pybox"):
    """rename all files with temp in front of file name"""
    if dir_path == "":
        dir_path = os.getcwd()

    for count, f in enumerate(os.listdir(dir_path)):
        f_name, f_ext = os.path.splitext(f)
        f_name = name + str(count)
        new_name = f'{f_name}{f_ext}'
        os.rename(f"{dir_path}/{f}", f"{dir_path}/{new_name}")


def rename_to_numbers(dir_path="", show=False):
    """rename all files with numbers"""
    if dir_path == "":
        dir_path = os.getcwd()

    for count, f in enumerate(os.listdir(dir_path)):
        f_name, f_ext = os.path.splitext(f)
        f_name = str(count)
        new_name = f'{f_name}{f_ext}'
        os.rename(f"{dir_path}/{f}", f"{dir_path}/{new_name}")
        if show:
            print(f'Old: {f}, New: {new_name}')



def remove_(path, type_):
    if type_ == "file":
        os.remove(path)
    elif type_ == "dir":
        os.rmdir(path)


def search(name="", dir_name="", type_="file", remove=False, print_=True):
    if dir_name == "":
        dir_name = os.getcwd()

    dir_path = os.path.dirname(os.path.realpath(dir_name))

    for root, dirs, files in os.walk(dir_path):
        type_to_search = None

        if type_ == "file":
            type_to_search = files
        elif type_ == "dir":
            type_to_search = dirs

        for item in type_to_search:
            try:
                if item.endswith(name):
                    path = root + '/' + str(item)
                    print(path)
                    if remove:
                        remove_(path, type_)

            except:
                if item == name:
                    path = root + '/' + str(item)
                    print(path)
                    if remove:
                        remove_(path, type_)


def move(source, destination, num=0):
    files = os.listdir(source)
    n = 0
    if num == 0:
        num = len(files)
    for file in files:
        shutil.move(f"{source}/{file}", f"{destination}/{file}")
        n += 1
        if n == num:
            break


