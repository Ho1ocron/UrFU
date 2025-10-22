class Book:
    """
    Text
    """
    __title: str
    author: str
    year: int

    def __init__(self, title, author, year):
        self.__title = title
        self.author = author
        self.year = year

    def info(self):
        """Text"""
        return f"Title: {self.__title=}, author: {self.author}, year: {self.year}"
    

class Vector():
    x: float
    y: float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __add__(self, other: "Vector") -> "Vector":
        """Оператор сложения"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar: int) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    

vec1 = Vector(1, 2)
vec2 = Vector(3, 4)

# print(vec1 + vec2)
vec1 *= 2
print(vec1)