import os


def scan_and_report(some_path):
    file_count = 0
    folder_count = 0
    for i in os.listdir(some_path):
        if os.path.isfile(some_path + i):
            file_count += 1
        elif os.path.isdir(some_path + i):
            folder_count += 1
            a, b = scan_and_report(some_path + i + "\\")
            file_count += a
            folder_count += b

    return file_count, folder_count


a, b = scan_and_report("D:\\")
print("Files in the folder = ", a)
print("Folders in the folder = ", b)
