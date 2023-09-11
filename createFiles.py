import os
import time
import shutil


def create_example_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        # Remove all existing files and subdirectories
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

    for i in range(1, 6):
        file_path = os.path.join(directory, f"initial_test{i}.txt")
        with open(file_path, "w") as f:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            content = f"This is initial test file {i}, created at {current_time}"
            f.write(content)

    # Create subdirectories and files
    for i in range(1, 4):
        subdir = os.path.join(directory, f"testDir{i}")
        os.makedirs(subdir)  # Create subdirectory

        for j in range(1, 6):
            file_path = os.path.join(subdir, f"testFile{j}.txt")
            with open(file_path, "w") as f:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                content = f"This is test file {j} in Dir{i}, created at {current_time}"
                f.write(content)

        for k in range(1, 4):
            subdir2 = os.path.join(subdir, f"testDir{k}")
            os.makedirs(subdir2)  # Create subdirectory

            for l in range(1, 6):
                file_path = os.path.join(subdir2, f"testFile{l}.txt")
                with open(file_path, "w") as f:
                    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    content = (
                        f"This is test file {l} in Dir{k}, created at {current_time}"
                    )
                    f.write(content)


def main():
    test_directory = os.path.join(os.environ["SystemDrive"], "\\test")
    print(f"Directory path ==> {test_directory}")
    create_example_files(test_directory)
    print("Example files created.")


if __name__ == "__main__":
    main()
