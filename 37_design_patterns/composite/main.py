import abc
import typing as t


class Item(abc.ABC):
    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def search(self, name: str) -> t.List['Item']:
        pass

    def __repr__(self) -> str:
        return self.name

class File(Item):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def search(self, name: str) -> t.List['Item']:
        return [self.name] if self.name == name else []


class Folder(Item):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def get_size(self):
        sum = 0
        for child in self.children:
            sum += child.get_size()

        return sum

    def search(self, name: str) -> t.List['Item']:
        result = []
        if self.name == name:
            result.append(self)

        for child in self.children:
            result.extend(child.search(name))

        return result

    def add(self, item: Item):
        self.children.append(item)

    def remove(self, item: Item):
        self.children.remove(item)

    def list(self):
        print(self.children)


def load_structure():
    """The structure looks like this:
    root/
    ├── file01
    ├── file02
    ├── folder1
    │   └── file11
    └── folder2
        ├── file21
        └── folder21
            └── file22
    """
    root = Folder("root")

    folder1 = Folder("folder1")
    folder2 = Folder("folder2")
    folder21 = Folder("folder21")

    folder1.add(File("file11", size=10))
    folder2.add(File("file21", size=20))
    folder2.add(folder21)
    folder21.add(File("file22", size=30))

    root.add(File("file01", size=40))
    root.add(File("file02", size=50))
    root.add(folder1)
    root.add(folder2)

    return root


if __name__ == '__main__':
    root = load_structure()
    print("root.get_size", root.get_size())
    print("root content:", root.list())

    found_files = root.search("file11")
    print('Found items for name "file11": ', found_files)

    found_folders = root.search("folder21")
    folder21 = found_folders[0]
    print("folder21 content:", folder21.list())
    print("Size of folder21:", folder21.get_size())
