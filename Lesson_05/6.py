import os


def scan_and_report(some_path):
    file_count = 0
    folder_count = 0
    for i in os.listdir(some_path):
        if os.path.isdir(some_path + i):
            folder_count += 1
        elif os.path.isfile(some_path + i):
            file_count += 1
    print("Files in the folder = ", file_count)
    print("Folders in the folder = ", folder_count)


scan_and_report("c:\\")