from random_art import *

a=build_random_function(3,3)
print a #testing build_random_function
print evaluate_random_function(a,0.1,0.4) #testing evaluate_random_function
draw_image(800,800,3,10) #testing draw_image