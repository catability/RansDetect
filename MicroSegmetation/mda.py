import os


item_attribute_dict = {}


def print_tree(root_dir, indent="  "):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            print(f"{indent}+ {item}/\n{indent}    {item_attribute_dict[item_path]}")
            print_tree(item_path, indent + "  ")
        else:
            print(f"{indent}- {item}\n{indent}    {item_attribute_dict[item_path]}")


def set_attribute(root_dir, k=0, p=1):
    attribute_dict = {}

    attribute_dict[root_dir] = {
        "isDirectory": True,
        "msid": "ms1000000",
        "pid": "",  # None,
        "cdate": os.path.getctime(root_dir),
        "mdate": os.path.getmtime(root_dir),
    }

    for root, dirs, files in os.walk(root_dir):
        if not dirs and not files:
            continue

        k += 1
        p = 1
        pid = attribute_dict[root]["msid"]

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            msid = f"ms1{k:03d}{p:03d}"
            attribute_dict[dir_path] = {
                "isDirectory": True,
                "msid": msid,
                "pid": pid,
                "cdate": os.path.getctime(dir_path),
                "mdate": os.path.getmtime(dir_path),
            }
            p += 1

        for file in files:
            file_path = os.path.join(root, file)
            msid = f"ms1{k:03d}{p:03d}"
            attribute_dict[file_path] = {
                "isDirectory": False,
                "msid": msid,
                "pid": pid,
                "cdate": os.path.getctime(file_path),
                "mdate": os.path.getmtime(file_path),
            }
            p += 1

    return attribute_dict


root_directory = "C:\\test\\"
item_attribute_dict = set_attribute(root_directory)
# print_tree(root_directory)


def print_files_with_same_pid(data, pid):
    for path, attribute in data.items():
        if attribute["pid"] == pid and attribute["isDirectory"]:
            msid = attribute["msid"]
            print(f"msid: {msid}, pid: {pid}, Path: {path}")
            print_files_under_directory(data, msid)


def print_files_under_directory(data, msid):
    for path, attribute in data.items():
        if attribute["pid"] == msid:
            print(f"  - {path}")


# pid를 기준으로 파일 출력
unique_pids = set(attribute["pid"] for attribute in item_attribute_dict.values())
sorted_pids = sorted(list(unique_pids))

# for pid in sorted_pids:
#     print_files_with_same_pid(item_attribute_dict, pid)
#     print()

for pid in sorted_pids:
    for path, attribute in item_attribute_dict.items():
        if attribute["msid"] == pid:
            print(f"Same pid list\npid: {pid}, Path: {path}")
            for path, attribute in item_attribute_dict.items():
                if attribute["pid"] == pid:
                    msid = attribute["msid"]
                    print(f"msid: {msid}, pid: {pid}, Path: {path}")
    print()
