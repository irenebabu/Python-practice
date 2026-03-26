#find vertex of a quadratic equation

def find_vertex(a, b, c):
    x = -b/(2*a)
    y = a*(x**2) + b*x + c
    return x,y
    

print(find_vertex(2,-4,2))

