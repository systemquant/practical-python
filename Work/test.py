class Shape:
    pass

class Circle(Shape):
    def __init__(self, size):
        self.size = size
    

if __name__ == '__main__':
    c = Circle(4.0)
    print(isinstance(c, Shape))
    print(type(Circle), type(Shape))
    
