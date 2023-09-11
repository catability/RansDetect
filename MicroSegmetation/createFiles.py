import os
import random
import shutil
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def create_random_files(directory, extensions, num_files):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(num_files):
        extension = random.choice(extensions)
        file_name = f"random_file_{generate_random_string(5)}.{extension}"
        file_path = os.path.join(directory, file_name)

        with open(file_path, "w") as f:
            f.write("This is a random file.")


def create_random_directories(
    root_directory, num_directories, max_depth, extensions, max_files_per_dir
):
    for _ in range(num_directories):
        directory_name = f"random_dir_{generate_random_string(5)}"
        directory_path = os.path.join(root_directory, directory_name)
        os.makedirs(directory_path)

        num_files = random.randint(1, max_files_per_dir)
        create_random_files(directory_path, extensions, num_files)

        if max_depth > 0:
            sub_num_directories = random.randint(1, num_directories)
            create_random_directories(
                directory_path,
                sub_num_directories,
                max_depth - 1,
                extensions,
                max_files_per_dir,
            )


def main():
    root_directory = "C:\\test"
    extensions = ["exe", "txt", "png", "jpg", "pdf", "docx", "pptx", "xlsx"]
    num_directories = 5  # Change this to the desired number of directories
    max_depth = 2  # Maximum depth of subdirectories
    max_files_per_dir = 10  # Maximum number of files per directory

    # Remove existing root_directory and its contents
    if os.path.exists(root_directory):
        shutil.rmtree(root_directory)

    create_random_directories(
        root_directory, num_directories, max_depth, extensions, max_files_per_dir
    )
    print(f"{num_directories} random directories created in {root_directory}")


if __name__ == "__main__":
    main()
