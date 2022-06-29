import os


def rename_with(dir_path=None, name="pybox"):
    """rename all files with temp in front of file name"""
    for count, f in enumerate(os.listdir(dir_path)):
        f_name, f_ext = os.path.splitext(f)
        f_name = name + str(count)
        new_name = f'{f_name}{f_ext}'
        os.rename(f"{dir_path}/{f}", new_name)


def rename_to_numbers(dir_path, show=False):
    """rename all files with numbers"""
    for count, f in enumerate(os.listdir(dir_path)):
        f_name, f_ext = os.path.splitext(f)
        f_name = str(count)
        new_name = f'{f_name}{f_ext}'
        os.rename(f"{dir_path}/{f}", new_name)
        if show:
            print(f'Old: {f}, New: {new_name}')

