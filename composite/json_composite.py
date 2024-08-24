from abc import ABC, abstractmethod
from typing import Any


class JSONComponent(ABC): 
    @abstractmethod
    def __str__(self) -> str:
        pass

class JSONComposite(ABC):
    @abstractmethod
    def add_member(self, member: JSONComponent) -> None: 
        pass


class JSONLeaf(JSONComponent): 
    def __init__(self, key, value) -> None:
        self.key = key 
        self.value = value  
    
    def __str__(self, level=0) -> str:
        return f"{self.key}: {self.value}\n"

class JSONObject(list, JSONComponent, JSONComposite): 
    def __init__(self, key) -> None:
        self.key = key

    def add_member(self, member): 
        self.append(member)
    
    def __str__(self, level=0) -> str:
        indent = " " * level
        string = ",\n".join(member.__str__(level + 1) for member in self) 
        return f'{indent}"{self.key}": {{\n{string}\n{indent}}}'


key1 = JSONLeaf("key1", "value1")
key2 = JSONLeaf("key2", "value2")
bigkey1 = JSONObject("bigkey1")
bigkey1.add_member(key2)
evenbigkey2 = JSONObject("evenbigkey1")
evenbigkey2.add_member(bigkey1)
evenbigkey2.add_member(key1)
print(evenbigkey2)