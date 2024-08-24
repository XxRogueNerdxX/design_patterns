from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent): 
        pass


class File(FileSystemComponent):
    def __init__(self, name:str):
        self.name = name 
    
    def show_details(self, indent=0):
        print(" " * indent + f"File :{self.name}")

class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name 
        self.children = [] 
    
    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)
    
    def show_details(self, indent=0):
        print(" "* indent + f"Folder: {self.name}")
        for child in self.children: 
            child.show_details(indent + 2) 


if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    # Create a folder and add files to it
    folder1 = Folder("folder1")
    folder1.add(file1)
    folder1.add(file2)

    # Create a main folder and add a file and folder to it
    main_folder = Folder("main_folder")
    main_folder.add(file3)
    main_folder.add(folder1)

    # Show the composite structure
    main_folder.show_details()

