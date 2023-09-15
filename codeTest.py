# 코드 작성하기 전 올바르게 작동하는지 일부분 먼저 코드 테스트 해보는 스크립트 파일

import os

directory = "C:\\test\\"

folder_attribute_dict = {}

k = 0
msid = "ms1000000"
folder_attribute_dict[directory] = {
    "isDirectory": True,
    "msid": msid,
    "pid": None,
    "cdate": os.path.getctime(directory),
    "mdate": os.path.getmtime(directory),
}
print(folder_attribute_dict[directory]["cdate"])
# pid = msid
# for k, (root, dirs, files) in enumerate(os.walk(directory)):
for root, dirs, files in os.walk(directory):
    pid = folder_attribute_dict[root]["msid"]
    p = 1
    if dirs or files:
        k += 1
        print(f"{root} k: {k}")

    for dir in dirs:
        msid = f"ms1{k:03d}{p:03d}"
        dir_path = os.path.join(root, dir)
        folder_attribute_dict[dir_path] = {
            "isDirectory": True,
            "msid": msid,
            "pid": pid,
            "cdate": os.path.getctime(dir_path),
            "mdate": os.path.getmtime(dir_path),
        }
        # print(f"{dir_path}_msid: {msid}")
        p += 1

    for file in files:
        msid = f"ms1{k:03d}{p:03d}"
        file_path = os.path.join(root, file)
        folder_attribute_dict[file_path] = {
            "isDirectory": False,
            "msid": msid,
            "pid": pid,
            "cdate": os.path.getctime(file_path),
            "mdate": os.path.getmtime(file_path),
        }
        # print(f"{file_path}_msid: {msid}")
        p += 1

# for folder_name, folder_info in folder_attribute_dict.items():
#     print(f"Folder Name: {folder_name}")
#     print("Folder Info:", folder_info)


def print_tree(root_dir, indent=""):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            print(f"{indent}+ {item}/\n{indent}    {folder_attribute_dict[item_path]}")
            print_tree(item_path, indent + "  ")
        else:
            print(f"{indent}- {item}\n{indent}    {folder_attribute_dict[item_path]}")


print_tree(directory)


# import os


# def print_tree(root_dir, indent=""):
#     for item in os.listdir(root_dir):
#         item_path = os.path.join(root_dir, item)
#         if os.path.isdir(item_path):
#             print(f"{indent}+ {item}/")
#             print_tree(item_path, indent + "  ")
#         else:
#             print(f"{indent}- {item}")


# root_directory = "C:\\test"
# print_tree(root_directory)


# for i root,dirs,files in os.walk(directory):
#     for file in files:
#         file_path=os.path.join(root,file)


# for i, (root, dirs, files) in enumerate(os.walk(directory)):
#     print(f"Iteration {i}:")
#     print("Root:", root)
#     print("Directories:", dirs)
#     print("Files:", files)
#     print()


# for root, dirs, files in os.walk(directory):
#     print("Current directory:", root)
#     print("Subdirectories:", dirs)
#     print("Files:", files)


# contents = os.listdir(directory)
# print("Contents of", directory, ":", contents)

# for index, content in enumerate(contents):
#     folder_attribute_dict[content]={

#     }
#     print(f"Index: {index}, Content: {content}")
