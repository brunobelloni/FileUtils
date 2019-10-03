import glob


class FileUtils:
    def __init__(self, path: str):
        self.path = path

    def get_all_files_in_path(self, file_type: str = '*', recursive: bool = False) -> list:
        return [f for f in glob.glob(pathname=self.path + f'**/*.{file_type}', recursive=recursive)]

    def rename_all_files(self) -> None:
        pass

    def delete_duplicated_images(self) -> None:
        pass

    def image_slice(self) -> None:
        pass
