
class CEO: 
    __shared_state = {
        "name": "Steve", 
        "age": 55
    }

    def __init__(self): 
        self.__dict__ = self.__shared_state
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Moonstate:
    __shared_state = {} 

    def __new__(self, *args, **kwargs):
        obj = super(Moonstate, self).__new__(self, *args, **kwargs)
        obj.__dict__ = self.__shared_state
        return obj 

class CFO(Moonstate):
    def __init__(self):
        self.name = ""
        self.money_managed = 0 
    
    def __str__(self): 
        return f"{self.name} manages {self.money_managed}"
    
if __name__ == "__main__":
    cfo1 = CFO()
    cfo1.name = "Sheryl"
    cfo1.money_managed = 1 
    print(cfo1) 

    cfo2 = CFO() 
    cfo2.name = "Ruth"
    cfo2.money_managed= 10
    print(cfo1)
    print(cfo2) 
