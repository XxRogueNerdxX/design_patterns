



class Car(): 
    def __init__(self) -> None:
        self.car_parts = [] 
    
    def __str__(self) -> str:
        return " ".join(self.car_parts)



class CarBuilder(): 
    def __init__(self) -> None:
        self.car = Car() 
    
    def set_make(self, make):
        self.car.car_parts.append(make) 
        return self
    
    def set_year(self, year): 
        self.car.car_parts.append(year)
        return self 
    
    def build(self):
        return self.car

builder = CarBuilder() 
car = (builder
       .set_make("2004")
       .set_year("test")
       .build())
print(car)
