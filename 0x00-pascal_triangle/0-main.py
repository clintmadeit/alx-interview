#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        
        print({'[{",".join([str(x) for x in row])}]'.format(row)})  


if __name__ == "__0-main__":
    print_triangle(pascal_triangle(5))