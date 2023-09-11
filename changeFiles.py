import os
import time
import argparse


def modify_file_contents(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "w") as f:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                new_content = f"{file}이 변경되었습니다. 변경시간: '{current_time}'\n"
                f.write(new_content)
                print(f"Modified: {file_path}")


def change_extension(directory, new_extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(new_extension):
                continue  # Skip files already with the new extension
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, os.path.splitext(file)[0] + new_extension)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Change file extensions in a directory and its subdirectories."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=os.path.join(os.environ["SystemDrive"], "\\test"),
        help="Path to the root directory (default: C:\\temp)",
    )
    parser.add_argument(
        "--new_extension",
        default=".test",
        help="New extension to apply (default: .test)",
    )

    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print("Error: Directory does not exist.")
        return

    modify_file_contents(args.directory)
    change_extension(args.directory, args.new_extension)

    # temp_directory = os.path.join(os.environ["SystemDrive"], "temp")
    # if not os.path.exists(temp_directory):
    #     print("Error: Temp directory does not exist.")
    # #     return

    # change_extension(temp_directory, args.new_extension)


if __name__ == "__main__":
    main()


# python script.py  (경로: C:\test  변경 확장자명: .test)
# python script.py C:\\path\\to\\directory --new_extension .test
