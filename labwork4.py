import math

class Figures:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangles(Figures):
    def __init__(self, vertices):
        if len(vertices) != 8:
            raise ValueError("A rectangle must have 4 vertices with 8 coordinates (x1, y1, x2, y2, x3, y3, x4, y4).")
        self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3, self.__x4, self.__y4 = vertices
        if not self.__is_rectangle():
            raise ValueError("The provided vertices do not form a valid rectangle.")
    
    @property
    def vertices(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3, self.__x4, self.__y4)

    def __is_rectangle(self):
        vec1 = (self.__x2 - self.__x1, self.__y2 - self.__y1)
        vec2 = (self.__x3 - self.__x2, self.__y3 - self.__y2)

        dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]

        side1 = math.dist((self.__x1, self.__y1), (self.__x2, self.__y2))
        side2 = math.dist((self.__x2, self.__y2), (self.__x3, self.__y3))
        side3 = math.dist((self.__x3, self.__y3), (self.__x4, self.__y4))
        side4 = math.dist((self.__x4, self.__y4), (self.__x1, self.__y1))

        return dot_product == 0 and side1 == side3 and side2 == side4 and side1 > 0 and side2 > 0

    def area(self):
        side1 = math.dist((self.__x1, self.__y1), (self.__x2, self.__y2))
        side2 = math.dist((self.__x2, self.__y2), (self.__x3, self.__y3))
        return side1 * side2

    def perimeter(self):
        side1 = math.dist((self.__x1, self.__y1), (self.__x2, self.__y2))
        side2 = math.dist((self.__x2, self.__y2), (self.__x3, self.__y3))
        return 2 * (side1 + side2)


class Circle(Figures):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            raise ValueError("Radius must be a positive number")

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


def main():
    while True:
        print("\nChoose an option:")
        print("1. Calculate area and perimeter of a rectangle")
        print("2. Calculate area and perimeter of a circle")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            match choice:
                case 1:
                    print("Enter 8 coordinates for the rectangle's 4 vertices (x1 y1 x2 y2 x3 y3 x4 y4):")
                    vertices = list(map(float, input().split()))
                    rect = Rectangles(vertices)
                    print(f"Rectangle Area: {rect.area()}")
                    print(f"Rectangle Perimeter: {rect.perimeter()}")
                
                case 2:
                    radius = float(input("Enter the radius of the circle: "))
                    circle = Circle(radius)
                    print(f"Circle Area: {circle.area()}")
                    print(f"Circle Perimeter: {circle.perimeter()}")
                
                case 3:
                    print("Exiting the program.")
                    break
                
                case _:
                    print("Invalid choice. Please select a valid option.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
