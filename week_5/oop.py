# my base class

# Base class
class Hair:
    def __init__(self, type, color, brand):
        self.type = type
        self.color = color
        self.brand = brand

    # Methods (actions)
    def wash(self):
        return f"Washing {self.color} {self.type} hair with {self.brand} shampoo"

    def dye(self, new_color):
        self.color = new_color
        return f"Dyed hair to {self.color}"

    def __repr__(self):
        return f"Hair(type={self.type}, color={self.color}, brand={self.brand})"


# Inherited class
class CurlyHair(Hair):
    def __init__(self, color, brand):
# Call parent constructor with type="curly"
        super().__init__("curly", color, brand)

    def style(self):
        return f"Styling curly {self.color} hair with mousse"


class StraightHair(Hair):
    def __init__(self, color, brand):
        super().__init__("straight", color, brand)

    def style(self):
        return f"Styling straight {self.color} hair with flat iron"


hair1 = Hair("braided", "black", "Dove")
print(hair1)
print(hair1.wash())
print(hair1.dye("red"))

hair2 = CurlyHair("brown", "SheaMoisture")
print(hair2)
print(hair2.style())

hair3 = StraightHair("blonde", "L'Oreal")
print(hair3)
print(hair3.style())
