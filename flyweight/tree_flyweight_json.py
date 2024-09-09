from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent): 
        pass


class File(FileSystemComponent):
    _file_cache = {}

    def __new__(cls, name: str):
        if name not in cls._file_cache:
            instance = super(File, cls).__new__(cls)
            cls._file_cache[name] = instance
        return cls._file_cache[name]

    def __init__(self, name: str):
        self.name = name
    
    def show_details(self, indent=0):
        print(" " * indent + f"File :{self.name}")


class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name 
        self.children = {}  # Store children in a dictionary
    
    def add(self, name: str, component: FileSystemComponent):
        self.children[name] = component

    def remove(self, name: str):
        del self.children[name]
    
    def show_details(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for name, child in self.children.items(): 
            child.show_details(indent + 2) 


if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    # Create a folder and add files to it
    folder1 = Folder("folder1")
    folder1.add("file1.txt", file1) 
    folder1.add("file2.txt", file2)

    # Create a main folder and add a file and folder to it
    main_folder = Folder("main_folder")
    main_folder.add("file3.txt", file3)
    main_folder.add("folder1", folder1)

    # Show the composite structure
    main_folder.show_details()

    # Create the same file again to demonstrate Flyweight pattern
    file4 = File("file1.txt")
    print(f"file1 is file4: {file1 is file4}")  # True, as they refer to the same instance
