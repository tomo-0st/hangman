# http://tinyurl.com/zrmjape

class Orange:
    def __init__(self, w, c):
        """ Weight is gram."""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """ temp is sesshi"""
        self.mold = days * temp

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

# or1 = Orange(4, "light orange")
# or2 = Orange(8, "dark orange")
# or1 = Orange(14, "yellow")

# orl = Orange(10, "dark orange")
# orl.weight = 100
# orl.color = "light orange"

# print(orl.weight)
# print(orl.color)
