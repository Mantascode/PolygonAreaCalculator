class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ''
        for i in range(self.height):
            for j in range(self.width):
                picture += '*'
            picture += '\n'

        return picture

    def get_amount_inside(self, shape):

        how_many_width = self.width // shape.width
        how_many_height = self.height // shape.height

        return how_many_width * how_many_height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'




class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'


rect = Rectangle(15, 10)
kvadrtas = Rectangle(16, 1)
print(rect.get_amount_inside(kvadrtas))
