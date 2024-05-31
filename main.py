# Get the color pallet from a certain image
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.png', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# canvass_size = 10x10
# dot_size = 20
# dot_space 50

import random
import turtle as t
from turtle import Screen

t.colormode(255)
color_list = [(243, 241, 237), (208, 150, 93), (43, 103, 139), (226, 236, 230), (139, 68, 99), (132, 181, 149), (146, 77, 49), (129, 164, 187), (197, 135, 159), (230, 204, 116), (176, 159, 35), (42, 131, 74), (190, 90, 130), (70, 163, 105), (235, 221, 226), (58, 39, 30), (47, 158, 175), (213, 225, 230), (8, 103, 76), (127, 32, 59), (108, 115, 173), (222, 82, 51), (61, 37, 46), (171, 206, 184), (27, 60, 90), (233, 208, 6), (39, 53, 106), (9, 64, 47), (174, 20, 7), (70, 80, 31)]
t_position = t.pos()

x_axis = -250
y_axis = -250


def draw_row():
    for _ in range(10):
        global x_axis
        global y_axis
        random_color = random.choice(color_list)
        t.penup()
        t.dot(20, random_color)
        t.forward(50)
        y_axis += 5


for _ in range(10):
    t.teleport(x_axis, y_axis)
    draw_row()

screen = Screen()
screen.exitonclick()


