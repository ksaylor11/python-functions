def is_triangle(a, b, c):
    if(((a+b) > c) & ((a+c) > b) & ((b+c) > a)):
        return True
    else:
        return False