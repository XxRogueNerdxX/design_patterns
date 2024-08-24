#LSP 


class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width
        self.__test = height
    
    @property
    def test(self):
        return self.__test 
    
    # @test.setter
    # def test(self, value):
    #     self.__test = value

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, value):
        self._width= value
    
    @height.setter
    def height(self, value):
        self._height = value 
    
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self) -> str:
        return f"Width: {self.width}, height {self.height}"


rc = Rectangle(2, 4)
rc.height = 10 
# rc.test = 10
print(rc.test)

# def use_it(rc)
#     w = rc.width 
#     rc.height = 10 
