# -*- coding: utf-8 -*-
"""
Random_art.py

@author:Jong Woo Nam
"""

#imports random, math, and PIL
# ^ This is an unnecessary comment -- anyone will be able to tell this is what's happening
from random import randint
from math import *
from PIL import Image

#Funtion that randomly chooses a list among ["prod"], ["sin_pi"], and ["cos_pi"]
#takes no input
#output:list e.g ["prod","a","b"]
# ^ Great that you're specifying inputs and outputs!
def print_random_function():
    integ = randint(1,3)
    functiondic={1:["prod","a","b"],2:["sin_pi","a"],3:["cos_pi","a"]}; # <- no semicolons in Python :)
    # ^ Might require less memory/time to create functiondic outside the function (once) instead of
    # every time print_random_function is called, especially since you also use it in build_random_function
    return functiondic[integ]


#Function that builds random function with minimum depth of min_depth and maximum depth of max_depth
#input: min_depth, max_depth which determines the depth of output nested list that represents a function
#output: nested list of minimum depth of min_depth and maximum depth of max_depth.
#All nested list will have at least min_depth but will not always reach to max_depth(random)
def build_random_function(min_depth, max_depth):

    functiondic={1:["prod","a","b"],2:["sin_pi","a"],3:["cos_pi","a"]};
    if min_depth>1 and max_depth>=min_depth: #recursively calls itself when min_depth>1 and max_depth>=min_depth

        funclist=print_random_function();
        if funclist==functiondic[1]:
            funclist[1]=build_random_function(min_depth-1,max_depth-1);#recursively calls itself with decremented min/max_depth
            funclist[2]=build_random_function(min_depth-1,max_depth-1);
        elif funclist==functiondic[2]:
            funclist[1]=build_random_function(min_depth-1,max_depth-1);
        elif funclist==functiondic[3]:
            funclist[1]=build_random_function(min_depth-1,max_depth-1);
            # ^ This case and the previous one are the same -- collapse them
            # with elif funclist==functiondic[2] or funclist==functiondic[3]
        else:
            print("Error Occured - random function generator broke") # great that you're catching errors!
        return funclist
    elif min_depth==1 and max_depth>=2: #when min_depth reached 1, randomly choose depth that goes beyond min_depth if max_depth>=2
        max_depth=randint(2,max_depth);
        funclist=print_random_function();
        if funclist==functiondic[1]:
            funclist[1]=build_random_function(min_depth,max_depth-1);
            funclist[2]=build_random_function(min_depth,max_depth-1);
        elif funclist==functiondic[2]:
            funclist[1]=build_random_function(min_depth,max_depth-1);
        elif funclist==functiondic[3]:
            funclist[1]=build_random_function(min_depth,max_depth-1);
            # ^ Lots of repetition -- this looks exactly like the previous block
            # Anytime you find yourself copy/pasting or typing something over and over,
            # you should stop and think about structure --
            # How could you functionalize to clean your code up?
        else:
            print("Error Occured - random function generator broke")
        return funclist
    elif min_depth==1 and max_depth==1: #when both min_depth and max_depth = 1, returns ["x"] or ["y"] randomly
        returndic={1:["x"],2:["y"]};
        return returndic[randint(1,2)]
    elif max_depth<min_depth: #prints error when max_depth<min_depth
        print "Max_depth has to be bigger than min_depth"



# Either write comments above function declarations or right below -- doesn't matter, pick one and be consistent
# Here you have both, and I'm not sure which to pay attention to
# vv

#evaluates the funtion f in nested list format using value of x and y (input). Works for x,y values not in range of -1<x,y<1, but values within the range is prefere.
#input: nested list f (output of build_random_function), float/integer value of x and y.
#output: float value that evalutes f with x and y.
def evaluate_random_function(f, x, y):
    """ this funciton recursively goes down the nested list to evaluate function f.
    """
    # This dictionary again -- would be nice if it were declared once somewhere
    funcdic={1:'prod',2:'sin_pi',3:'cos_pi',4:'x',5:'y'}; # No semicolons!
    if f[0]==funcdic[1]:
        a=evaluate_random_function(f[1],x,y);
        b=evaluate_random_function(f[2],x,y);
        # print a*b # <- best practice is to remove commented-out code before you submit
        return a*b
    elif f[0]==funcdic[2]:
        a=evaluate_random_function(f[1],x,y);
        # print sin(pi*a)
        return sin(pi*a)
    elif f[0]==funcdic[3]:
        a=evaluate_random_function(f[1],x,y);
        # print cos(pi*a)
        return cos(pi*a)
    elif f[0]==funcdic[4]:
        # print x
        return x
    elif f[0]==funcdic[5]:
        # print y
        return y


# vv Again, your comment above + docstring below -- pick one and be consistent

#remaps value within input range(from input_interval_start to input_interval_end) to output range(from output_interval_start to output_interval_end)
#input: value within input range, input range, output range
#output: remapped value within output range
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).

        TODO: please fill out the rest of this docstring
    """
    # your code goes here
    if input_interval_start<=val<=input_interval_end:
        val=float(val)
        inputdist=input_interval_end-input_interval_start;
        dist_from_start_input = val-input_interval_start;
        ratio = dist_from_start_input/inputdist;
        outputdist = output_interval_end - output_interval_start;
        remap_val = ratio*outputdist + output_interval_start;
        return remap_val
    else:
        print "input value not within the specified input range"

#draws and saves image of size xpixel by ypixel. Uses function output by build_random_function(min_depth,max_depth) for each of R,G,B values.
#input: xpixel,ypixel (integer), min_depth,max_depth which goes into build_random_function, and name of the image
#output: saved jpg image under /home/jong/Desktop/Softdes/SoftwareDesignFall15/MP2/ image name is imagename.jpg
def draw_image(xpixel,ypixel,min_depth,max_depth,imagename):
    """This function creates random image by calculating value of R,G,B at certain position x,y.
       Uses build_random_function for each R,G,B and for loop to calculate the value of R,G,B at each position in x and y.
    """

    im = Image.new("RGB",(xpixel,ypixel))
    pixels = im.load()
    #Setting up the R,G,B functions
    Rfunc = build_random_function(min_depth,max_depth)
    Gfunc = build_random_function(min_depth,max_depth)
    Bfunc = build_random_function(min_depth,max_depth)

    for i in range(xpixel):
        for j in range(ypixel):
            valx=remap_interval(i,0,xpixel-1,-1.0,1.0)
            valy=remap_interval(j,0,ypixel-1,-1.0,1.0)
            Rval=evaluate_random_function(Rfunc,valx,valy)
            Gval=evaluate_random_function(Gfunc,valx,valy)
            Bval=evaluate_random_function(Bfunc,valx,valy)
            Rval = remap_interval(Rval,-1.0,1.0,0,255)
            Gval = remap_interval(Gval,-1.0,1.0,0,255)
            Bval = remap_interval(Bval,-1.0,1.0,0,255)
            pixels[i,j]=(int(Rval),int(Gval),int(Bval))
    # What happens when someone else runs your code and /home/jong doesn't exist?
    # This is called an absolute path -- not usually a good idea
    # im.save("/home/jong/Desktop/Softdes/SoftwareDesignFall15/MP2/"+imagename+".jpg")

    # Better to use a relative path instead, like this
    # (i.e. "save the image in the current folder")
    im.save(imagename+".jpg")
