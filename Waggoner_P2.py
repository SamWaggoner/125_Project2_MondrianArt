# PROJECT 2 COS 125
# File: waggoner_Project2.py
# Author: Sam Waggoner
# Date: 12/01/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Create art similar to that of Mondrian.
# Collaboration:
# I did not discuss this assignment with anyone outside of the course staff. I received guidance from Matt.

import random

def main():



    def dimensions():
        xdimension = int(input("What is the horizontal width of the canvas (pixels)? "))
        ydimension = int(input("What is the vertical height of the canvas (pixels)? "))
        canvas_rec = [0,0,xdimension,ydimension]
        return canvas_rec

    canvas_rec = dimensions()

    header = '<html><head></head><body><svg width="'+str(canvas_rec[2])+'" height="'+str(canvas_rec[3])+'">\n'
    f = open('rect.html','w')
    f.write(header)
    f.close()

    # rectangles: (topleft_x_coodinate, topleft_y_coordinate, x_width, y_height)

    def splitter(rect,canvas_dimensions):


        # Mandatory Four-Way Split
        # If both the length and width of the rectangle are larger than half the canvas

        if rect[2] > canvas_dimensions[2]/2 and rect[3] > canvas_dimensions[3]/2:

            x_split = rect[2] * 0.01 * random.randint(33,67)
            y_split = rect[3] * 0.01 * random.randint(33,67)

            # Rectangle in the top left corner
            rect1 = []
            rect1.append(rect[0]) # new_1x_coord
            rect1.append(rect[1]) # new_1y_coord
            rect1.append(x_split) # new_1x_width
            rect1.append(y_split) # new_1y_height
            splitter(rect1,canvas_dimensions)

            # Rectangle in the top right corner
            rect2 = []
            rect2.append(rect[0] + x_split) # new_2x_coord
            rect2.append(rect[1])           # new_2y_coord
            rect2.append(rect[2] - x_split) # new_2x_width
            rect2.append(y_split)           # new_2y_height
            splitter(rect2,canvas_dimensions)

            # Rectangle in the bottom left corner
            rect3 = []
            rect3.append(rect[0])           # new_3x_coord
            rect3.append(rect[1] + y_split) # new_3y_coord
            rect3.append(x_split)           # new_3x_width
            rect3.append(rect[3] - y_split) # new_3y_height
            splitter(rect3,canvas_dimensions)

            # Rectangle in the bottom right corner
            rect4 = []
            rect4.append(rect[0] + x_split) # new_3x_coord
            rect4.append(rect[1] + y_split) # new_3y_coord
            rect4.append(rect[2] - x_split) # new_3x_width
            rect4.append(rect[3] - y_split) # new_3y_height
            splitter(rect4,canvas_dimensions)


        # Mandatory Vertical Two-Way Split, X
        # If only the width (x) of the rectangle is larger than half the canvas

        elif rect[2] > canvas_dimensions[2]/2:

            x_split = rect[2] * 0.01 * random.randint(33,67)

            # Rectangle on the left
            rect1 = []
            rect1.append(rect[0]) # new_1x_coord
            rect1.append(rect[1]) # new_1y_coord
            rect1.append(x_split) # new_1x_width
            rect1.append(rect[3]) # new_1y_height
            splitter(rect1,canvas_dimensions)

            # Rectangle on the right
            rect2 = []
            rect2.append(rect[0] + x_split) # new_2x_coord
            rect2.append(rect[1])           # new_2y_coord
            rect2.append(rect[2] - x_split) # new_2x_width
            rect2.append(rect[3])           # new_2y_height
            splitter(rect2,canvas_dimensions)
    

        # Mandatory Horizontal Two-Way Split, Y
        # If only the length (y) of the rectangle is larger than half the canvas

        elif rect[3] > canvas_dimensions[3]/2:

            y_split = rect[3] * 0.01 * random.randint(33,67)

            # Rectangle on the top
            rect3 = [] 
            rect3.append(rect[0])           # new_3x_coord
            rect3.append(rect[1])           # new_3y_coord
            rect3.append(rect[2])           # new_3x_width
            rect3.append(y_split)           # new_3y_height
            splitter(rect3,canvas_dimensions)

            # Rectangle on the bottom
            rect4 = []
            rect4.append(rect[0])           # new_3x_coord
            rect4.append(rect[1] + y_split) # new_3y_coord
            rect4.append(rect[2]) # new_3x_width
            rect4.append(rect[3] - y_split) # new_3y_height
            splitter(rect4,canvas_dimensions)

        
        # Possible Four-Way Split
        # If both length and width are smaller than half the canvas but larger than 120 pixels

        elif rect[2] > 120 and random.randint(120,int((rect[2]*1.5))) < rect[2] and rect[3] > 120 and random.randint(120,int((rect[3]*1.5))) < rect[3]:

            x_split = rect[2] * 0.01 * random.randint(33,67)
            y_split = rect[3] * 0.01 * random.randint(33,67)

            # Rectangle in the top left corner
            rect1 = []
            rect1.append(rect[0]) # new_1x_coord
            rect1.append(rect[1]) # new_1y_coord
            rect1.append(x_split) # new_1x_width
            rect1.append(y_split) # new_1y_height
            splitter(rect1,canvas_dimensions)

            # Rectangle in the top right corner
            rect2 = []
            rect2.append(rect[0] + x_split) # new_2x_coord
            rect2.append(rect[1])           # new_2y_coord
            rect2.append(rect[2] - x_split) # new_2x_width
            rect2.append(y_split)           # new_2y_height
            splitter(rect2,canvas_dimensions)

            # Rectangle in the bottom left corner
            rect3 = []
            rect3.append(rect[0])           # new_3x_coord
            rect3.append(rect[1] + y_split) # new_3y_coord
            rect3.append(x_split)           # new_3x_width
            rect3.append(rect[3] - y_split) # new_3y_height
            splitter(rect3,canvas_dimensions)

            # Rectangle in the bottom right corner
            rect4 = []
            rect4.append(rect[0] + x_split) # new_3x_coord
            rect4.append(rect[1] + y_split) # new_3y_coord
            rect4.append(rect[2] - x_split) # new_3x_width
            rect4.append(rect[3] - y_split) # new_3y_height
            splitter(rect4,canvas_dimensions)


        # Possible Vertical Two-Way Split, X
        # If just the width (x) is smaller than half the canvas but larger than 120 pixels

        elif rect[2] > 120 and random.randint(120,int((rect[2]*1.5))) < rect[2]:

            x_split = rect[2] * 0.01 * random.randint(33,67)

            # Rectangle on the left
            rect1 = []
            rect1.append(rect[0]) # new_1x_coord
            rect1.append(rect[1]) # new_1y_coord
            rect1.append(x_split) # new_1x_width
            rect1.append(rect[3]) # new_1y_height
            splitter(rect1,canvas_dimensions)

            # Rectangle on the right
            rect2 = []
            rect2.append(rect[0] + x_split) # new_2x_coord
            rect2.append(rect[1])           # new_2y_coord
            rect2.append(rect[2] - x_split) # new_2x_width
            rect2.append(rect[3])           # new_2y_height
            splitter(rect2,canvas_dimensions)

        # Possible Horizontal Two-Way Split, Y
        # If just the length (y) is smaller than half the canvas but larger than 120 pixels

        elif rect[3] > 120 and random.randint(120,int((rect[3]*1.5))) < rect[3]:

            y_split = rect[3] * 0.01 * random.randint(33,67)

            # Rectangle on the top
            rect3 = [] 
            rect3.append(rect[0])           # new_3x_coord
            rect3.append(rect[1])           # new_3y_coord
            rect3.append(rect[2])           # new_3x_width
            rect3.append(y_split)           # new_3y_height
            splitter(rect3,canvas_dimensions)

            # Rectangle on the bottom
            rect4 = []
            rect4.append(rect[0])           # new_3x_coord
            rect4.append(rect[1] + y_split) # new_3y_coord
            rect4.append(rect[2]) # new_3x_width
            rect4.append(rect[3] - y_split) # new_3y_height
            splitter(rect4,canvas_dimensions)
            

        # If it makes it here,
            # 1) it is not mandatory to split the rectangle
            # 2) by the randint it failed to split again
            # 3) and it is now ready to draw

        # Draw

        else:
            f = open('rect.html','a')

            # Color
            r = 0.01 * random.randint(0,100)
            if r < 0.0833:
                color = "255,255,0" # Yellow
            elif r < 0.1667:
                color = "0,0,255" # Blue
            elif r < 0.25:
                color =  "255,0,0" # Red
            else:
                color = "255,255,255" # White

            # Write into the HTML file
            f.write('<rect x="'+ str(rect[0]) +'" y="'+ str(rect[1]) +'" width="'+ str(rect[2]) +'" height="'+ str(rect[3]) +'" style="fill:rgb('+str(color)+');stroke-width:3;stroke:rgb(0,0,0)"/>\n')
            f.close()




    splitter(canvas_rec,canvas_rec)

    footer = '</svg></body></html>'
    f = open('rect.html','a')
    f.write(footer)
    f.close()


main()







# My original misguided and abandoned attempt, nothing important is below:

# import random

# def main():

#     def decide_x_split(x_dist, canvas_rec):
#         if x_dist > canvas_rec[2]/2:
#             return 'split'
#         if x_dist < 120:
#             return 'no split'
#         else:
#             num = random.randint(120,(x_dist*2))
#             if num < x_dist:
#                 return 'split'
#             else:
#                 return 'no split'
    
#     def decide_y_split(y_dist, canvas_rec):
#         if y_dist > canvas_rec[3]/2:
#             return 'split'
#         if y_dist < 120:
#             return 'no split'
#         else:
#             num = random.randint(120,(y_dist*2))
#             if num < y_dist:
#                 return 'split'
#             else:
#                 return 'no split'

#     # print(decide_x_split(100,[0,0,800,800]))

#     def where_to_split_x (x_dist):
#         num = 0.01 * random.randint(33,67)
#         split_point = num * x_dist
#         return split_point

#     def where_to_split_y (y_dist):
#         num = 0.01 * random.randint(33,67)
#         split_point = num * y_dist
#         return split_point
#         # this will be inverted on the y axis
    
#     def color():
#         r = 0.01 * random.randint(0,100)
#         if r < 0.0833:
#             return "0,255,255"
#             # Yellow
#         elif r < 0.1667:
#             return "0,0,255"
#             # Blue
#         elif r < 0.25:
#             return "255,0,0"
#             # Red
#         else:
#             return "255,255,255"
#             # white

#     header = '<html><head></head><body><svg width="800" height="800">'
#     rect = '<rect x="'+ x +'" y="'+ y +'" width='+ width +'" height="'+ height +'" style="fill:rgb('+red+','+green+','+blue+');stroke-width:3;stroke:rgb(0,0,0)"/>'
#     footer = '</svg></body></html>'

#     f = open('rect.html','w')
#     f.write(header)
#     f.close()

#     # rectangles: [x top corner, y top corner, x dimension, y dimension]

#     def recursive(rect):
#         f = open('rect.html','w')
#         rect = '<rect x="'+ rect[0] +'" y="'+ rect[1] +'" width='+ rect[2] +'" height="'+ rect[3] +'" style="fill:rgb('color()');stroke-width:3;stroke:rgb(0,0,0)"/>'
#         f.write(rect)
#         f.close()
#         x_decision = decide_x_split(rect)
#         print("X-decision =",x_decision)
#         y_decision = decide_y_split(rect)
#         print("Y-decision =",y_decision)
#         if x_decision == 'split' and y_decision == 'split':
#             x_split = rect[0] + where_to_split_x(rect[2])
#             y_split = rect[1] + where_to_split_y(rect[2])
#             f = open('rect.html','a')
#             f.write("\n")
#         elif x_decision == 'split':
#             # split on x
#         elif y_decision == 'split':
#             # split on y
    
#     canvas_rec = dimensions()
#     recursive(canvas_rec)





#     def write(x,y,width,height):
#         rect = '<rect x="'+ x +'" y="'+ y +'" width='+ width +'" height="'+ height +'" style="fill:rgb('+red+','+green+','+blue+');stroke-width:3;stroke:rgb(0,0,0)"/>'
#         return (rect)

#     def split(x,y,length,width):
#         reclist.append(write(x,y,length,width))
    
#     def recursivesplitter(reclist):
#         #print('Current rectangle list:\n')
#         for i in range(len(reclist)):
#             #print(reclist[i])
#             horiz_or_vert = random.randint(3,4)
#             if horiz_or_vert == 3:
#                 #print("Decides to split on x")
#                 if decidesplit(reclist[i][3]) == 'split':
#                     #print("Decides to split")
#                     split_on_x = random.randint((reclist[i][0]+120),(reclist[i][3]-120))
#                     #print("Splits on",split_on_x)
#                     reclist.append(x,y,split_on_x,)

#     # def innerrecursive():
#     #     x = "not written yet"

#     # def outerrecursive():
#     #     for i in range(len(reclist)):
#     #         if reclist[i][2] > 120 and reclist[i][3] > 120:
#     #             innerrecursive()
#     #             outerrecursive()


#     #                 write(x_origin,y_origin,x,y)
#     #         # if 4
#     #         recursivesplitter()

#     def copy_to_html(reclist):
#         header = '<html><head></head><body><svg width="800" height="800">'
#         rect = '<rect x="'+ x +'" y="'+ y +'" width='+ width +'" height="'+ height +'" style="fill:rgb('+red+','+green+','+blue+');stroke-width:3;stroke:rgb(0,0,0)"/>'
#         footer = '</svg></body></html>'
#         with open('rect.html','w') as f:
#             #f.write(header)
#             for i in reclist:
#                 f.write(i)
#                 # need to individually put in for paramaters? single i doesn't suffice?
#             #f.write(footer)


#     # canvas_rec = dimensions() was used at the top
#     reclist = recursivesplitter(canvas_rec)
#     copy_to_html(reclist)

# main()