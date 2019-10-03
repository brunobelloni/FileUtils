from file_utils.api import FileUtils


def main():
    file_utils = FileUtils(path='C:\\Users\\bruno.belloni\\Desktop\\Nova pasta\\')
    file_utils.get_all_files_in_path(file_type='json', recursive=True)


if __name__ == '__main__':
    main()
