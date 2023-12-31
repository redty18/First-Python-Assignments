pi = 3.1415926

def area(radius):
    return pi * (radius * radius)

def volume(height, radius):
    return area(radius) * height

print(volume(5, 10))