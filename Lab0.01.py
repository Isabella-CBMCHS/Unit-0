'''
############
# Lab 0.01 #
############

In this lab we will create a class that will represent colors 
and build a function to combine two colors.


1.  Create a class, Color.
2.  Instantiate at least 3 colors.
3.  Add attributes of r, g, and b to those instances.
4.  Create a function, add_color, which takes in two colors 
    and returns a color that is the sum of the two reds, greens, 
    and blues. Don't forget: the maximum value for R, G, or B is 255.
'''

class Color():
    def __init__(self, red, green, blue):
        self.r = red  
        self.g = green  
        self.b = blue
        
    def add_color(self):
        sum color1 + color2
        return sum
    
sum = add_color(color1, color2)
    
color1 = Color(230, 12, 40)
color2 = Color(2, 200, 10)
color3 = Color(0, 40, 140)

print(color1)
