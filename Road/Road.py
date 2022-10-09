# класс Road

class Road:
    def __init__(self, lenght:int, width: int, height:int, weight: int) -> None:
        self.__lenght = lenght
        self.__width = width
        self.__height = height
        self.__weight = weight

    
    def calculate(self) -> float:
        return self.__height * self.__weight * self.__width * self.__lenght
        