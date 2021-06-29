from turtle import *


shape("turtle")
speed(0.5)

def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return
    
    length /= 3.0

    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

def create_snowflake(sides, lenght):
    
    for _ in range(sides):
        snowflake_side(lenght, sides)
        right(360/sides)

create_snowflake(4,200)
mainloop()