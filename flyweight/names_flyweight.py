import string 
import random 


class User: 
    def __init__(self, name) -> None:
        self.name = name 
    
class User2: 
    strings = [] 
    def __init__(self, full_name) -> None:
        def get_or_add(s): 
            if s in self.strings: 
                return self.strings.index(s) 
            else: 
                self.strings.append(s)
                return len(self.strings) - 1 
        self.names = [get_or_add(x) 
                    for x in full_name.spit(" ")]



def random_string(): 
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for x in range(8)])
            

if __name__ == "main": 
    
