def circle(radius):
    return 3*14*radius*radius
def square(side):
    return side*side
def rectangle(l,b):
    return l*b
def triangle(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**(0.5)
    return area