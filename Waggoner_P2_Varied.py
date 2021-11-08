# PROJECT 2 Extra Credit COS 125
# File: Waggoner_P2_XC.py
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
    f = open('rect_xc.html','w')
    f.write(header)
    f.close()

    # rectangles: (topleft_x, topleft_y, x_width, y_width)
    def splitter(rect,canvas_dimensions):


        # Mandatory Four-Way Split

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

        elif rect[2] > 15 and random.randint(15,int((rect[2]*1.5))) < rect[2] and rect[3] > 15 and random.randint(15,int((rect[3]*1.5))) < rect[3]:

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

        elif rect[2] > 15 and random.randint(15,int((rect[2]*1.5))) < rect[2]:

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

        elif rect[3] > 15 and random.randint(15,int((rect[3]*1.5))) < rect[3]:

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


        # Draw the rectangle

        else:
            f = open('rect_xc.html','a')

            # Fill Color
            r = 0.01 * random.randint(0,100)
            # r is unused since i just set it to black at the bottom

        # These are different fill colors I was playing around with.
        # Right now I set the fill to black, but with blue/purple/red strokes (outlines) for the rectangles.

        # Scattered Colors (This one didn't look great, I didn't include a picture.)
            # if r < 0.1:
            #     color = "255,155,50" # Fall Orange
            # elif r < 0.2:
            #     color = "240,8,8" # Strong Red
            # elif r < 0.3:
            #     color =  "200,235,0" # Strong Green
            # elif r < 0.4:
            #     color =  "118,231,171" # Teal
            # elif r < 0.5:
            #     color =  "16,143,88" # Strong Green
            # elif r < 0.6:
            #     color =  "18,93,95" # Dark Ocean Blue
            # elif r < 0.7:
            #     color =  "117,97,195" # Timid Purple
            # elif r < 0.8:
            #     color =  "113,16,132" # Royal Purple
            # elif r < 0.9:
            #     color =  "178,124,33" # Leaf
            # else:
            #     color = "223,150,113" # Skin


        # Blues
        #     if r < 0.1:
        #         color =  "113,207,223"
        #     elif r < 0.2:
        #         color =  "98,186,202"
        #     elif r < 0.3:
        #         color =  "83,149,171"
        #     elif r < 0.4:
        #         color =  "89,166,190"
        #     elif r < 0.5:
        #         color =  "66,135,183"
        #     elif r < 0.6:
        #         color =  "66,123,159"
        #     elif r < 0.7:
        #         color =  "70,123,177"
        #     elif r < 0.8:
        #         color =  "101,164,224"
        #     elif r < 0.9:
        #         color =  "104,150,193"
        #     else:
        #         color = "104,118,193"

        # Random
        # this one doesn't work as I intended it to, but it makes the background black and the outlines gray like the death star
            #color = '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"' 

           
            color = "0,0,0"
            

            f.write('<rect x="'+ str(rect[0]) +'" y="'+ str(rect[1]) +'" width="'+ str(rect[2]) +'" height="'+ str(rect[3]) +'" style="fill:rgb('+color+');stroke-width:'+str(random.randint(1,12))+';stroke:rgb('+str(random.randint(1,255))+','+str(random.randint(1,6))+','+str(random.randint(1,255))+')"/>\n')
            f.close()



    splitter(canvas_rec,canvas_rec)

    footer = '</svg></body></html>'
    f = open('rect_xc.html','a')
    f.write(footer)
    f.close()


main()








# # Below is the one above, just with thicker outlines.
# # These are my favorite settings, which create a picture that isn't too Mondrian (so it
# # doesn't follow the extra credit guidelines) but one that I like the most.

# # PROJECT 2 COS 125
# # File: hw6c.py
# # Author: Sam Waggoner
# # Date: 12/01/2020
# # Section: 1006
# # E-mail samuel.waggoner@maine.edu
# # Description:
# # Create art similar to that of Mondrian.
# # Collaboration:
# # I did not discuss this assignment with anyone outside of the course staff. I got help from Matt.

# import random

# def main():



#     def dimensions():
#         xdimension = int(input("What is the horizontal width of the canvas (pixels)? "))
#         ydimension = int(input("What is the vertical height of the canvas (pixels)? "))
#         canvas_rec = [0,0,xdimension,ydimension]
#         return canvas_rec

#     canvas_rec = dimensions()

#     header = '<html><head></head><body><svg width="'+str(canvas_rec[2])+'" height="'+str(canvas_rec[3])+'">\n'
#     f = open('rect_xc.html','w')
#     f.write(header)
#     f.close()

#     # rectangles: (topleft_x, topleft_y, x_width, y_width)
#     def splitter(rect,canvas_dimensions):


#         # Mandatory Four-Way Split

#         if rect[2] > canvas_dimensions[2]/2 and rect[3] > canvas_dimensions[3]/2:

#             x_split = rect[2] * 0.01 * random.randint(33,67)
#             y_split = rect[3] * 0.01 * random.randint(33,67)

#             # Rectangle in the top left corner
#             rect1 = []
#             rect1.append(rect[0]) # new_1x_coord
#             rect1.append(rect[1]) # new_1y_coord
#             rect1.append(x_split) # new_1x_width
#             rect1.append(y_split) # new_1y_height
#             splitter(rect1,canvas_dimensions)

#             # Rectangle in the top right corner
#             rect2 = []
#             rect2.append(rect[0] + x_split) # new_2x_coord
#             rect2.append(rect[1])           # new_2y_coord
#             rect2.append(rect[2] - x_split) # new_2x_width
#             rect2.append(y_split)           # new_2y_height
#             splitter(rect2,canvas_dimensions)

#             # Rectangle in the bottom left corner
#             rect3 = []
#             rect3.append(rect[0])           # new_3x_coord
#             rect3.append(rect[1] + y_split) # new_3y_coord
#             rect3.append(x_split)           # new_3x_width
#             rect3.append(rect[3] - y_split) # new_3y_height
#             splitter(rect3,canvas_dimensions)

#             # Rectangle in the bottom right corner
#             rect4 = []
#             rect4.append(rect[0] + x_split) # new_3x_coord
#             rect4.append(rect[1] + y_split) # new_3y_coord
#             rect4.append(rect[2] - x_split) # new_3x_width
#             rect4.append(rect[3] - y_split) # new_3y_height
#             splitter(rect4,canvas_dimensions)


#         # Mandatory Vertical Two-Way Split, X

#         elif rect[2] > canvas_dimensions[2]/2:

#             x_split = rect[2] * 0.01 * random.randint(33,67)

#             # Rectangle on the left
#             rect1 = []
#             rect1.append(rect[0]) # new_1x_coord
#             rect1.append(rect[1]) # new_1y_coord
#             rect1.append(x_split) # new_1x_width
#             rect1.append(rect[3]) # new_1y_height
#             splitter(rect1,canvas_dimensions)

#             # Rectangle on the right
#             rect2 = []
#             rect2.append(rect[0] + x_split) # new_2x_coord
#             rect2.append(rect[1])           # new_2y_coord
#             rect2.append(rect[2] - x_split) # new_2x_width
#             rect2.append(rect[3])           # new_2y_height
#             splitter(rect2,canvas_dimensions)
    

#         # Mandatory Horizontal Two-Way Split, Y

#         elif rect[3] > canvas_dimensions[3]/2:

#             y_split = rect[3] * 0.01 * random.randint(33,67)

#             # Rectangle on the top
#             rect3 = [] 
#             rect3.append(rect[0])           # new_3x_coord
#             rect3.append(rect[1])           # new_3y_coord
#             rect3.append(rect[2])           # new_3x_width
#             rect3.append(y_split)           # new_3y_height
#             splitter(rect3,canvas_dimensions)

#             # Rectangle on the bottom
#             rect4 = []
#             rect4.append(rect[0])           # new_3x_coord
#             rect4.append(rect[1] + y_split) # new_3y_coord
#             rect4.append(rect[2]) # new_3x_width
#             rect4.append(rect[3] - y_split) # new_3y_height
#             splitter(rect4,canvas_dimensions)

        
#         # Possible Four-Way Split

#         elif rect[2] > 15 and random.randint(15,int((rect[2]*1.5))) < rect[2] and rect[3] > 15 and random.randint(15,int((rect[3]*1.5))) < rect[3]:

#             x_split = rect[2] * 0.01 * random.randint(33,67)
#             y_split = rect[3] * 0.01 * random.randint(33,67)

#             # Rectangle in the top left corner
#             rect1 = []
#             rect1.append(rect[0]) # new_1x_coord
#             rect1.append(rect[1]) # new_1y_coord
#             rect1.append(x_split) # new_1x_width
#             rect1.append(y_split) # new_1y_height
#             splitter(rect1,canvas_dimensions)

#             # Rectangle in the top right corner
#             rect2 = []
#             rect2.append(rect[0] + x_split) # new_2x_coord
#             rect2.append(rect[1])           # new_2y_coord
#             rect2.append(rect[2] - x_split) # new_2x_width
#             rect2.append(y_split)           # new_2y_height
#             splitter(rect2,canvas_dimensions)

#             # Rectangle in the bottom left corner
#             rect3 = []
#             rect3.append(rect[0])           # new_3x_coord
#             rect3.append(rect[1] + y_split) # new_3y_coord
#             rect3.append(x_split)           # new_3x_width
#             rect3.append(rect[3] - y_split) # new_3y_height
#             splitter(rect3,canvas_dimensions)

#             # Rectangle in the bottom right corner
#             rect4 = []
#             rect4.append(rect[0] + x_split) # new_3x_coord
#             rect4.append(rect[1] + y_split) # new_3y_coord
#             rect4.append(rect[2] - x_split) # new_3x_width
#             rect4.append(rect[3] - y_split) # new_3y_height
#             splitter(rect4,canvas_dimensions)


#         # Possible Vertical Two-Way Split, X

#         elif rect[2] > 15 and random.randint(15,int((rect[2]*1.5))) < rect[2]:

#             x_split = rect[2] * 0.01 * random.randint(33,67)

#             # Rectangle on the left
#             rect1 = []
#             rect1.append(rect[0]) # new_1x_coord
#             rect1.append(rect[1]) # new_1y_coord
#             rect1.append(x_split) # new_1x_width
#             rect1.append(rect[3]) # new_1y_height
#             splitter(rect1,canvas_dimensions)

#             # Rectangle on the right
#             rect2 = []
#             rect2.append(rect[0] + x_split) # new_2x_coord
#             rect2.append(rect[1])           # new_2y_coord
#             rect2.append(rect[2] - x_split) # new_2x_width
#             rect2.append(rect[3])           # new_2y_height
#             splitter(rect2,canvas_dimensions)

#         # Possible Horizontal Two-Way Split, Y

#         elif rect[3] > 15 and random.randint(15,int((rect[3]*1.5))) < rect[3]:

#             y_split = rect[3] * 0.01 * random.randint(33,67)

#             # Rectangle on the top
#             rect3 = [] 
#             rect3.append(rect[0])           # new_3x_coord
#             rect3.append(rect[1])           # new_3y_coord
#             rect3.append(rect[2])           # new_3x_width
#             rect3.append(y_split)           # new_3y_height
#             splitter(rect3,canvas_dimensions)

#             # Rectangle on the bottom
#             rect4 = []
#             rect4.append(rect[0])           # new_3x_coord
#             rect4.append(rect[1] + y_split) # new_3y_coord
#             rect4.append(rect[2]) # new_3x_width
#             rect4.append(rect[3] - y_split) # new_3y_height
#             splitter(rect4,canvas_dimensions)
            

#         # Draw the rectangle

#         else:
#             f = open('rect_xc.html','a')

#             # Color
#             r = 0.01 * random.randint(0,100)

#         # Random
#             # if r < 0.1:
#             #     color = "255,155,50" # Fall Orange
#             # elif r < 0.2:
#             #     color = "240,8,8" # Strong Red
#             # elif r < 0.3:
#             #     color =  "200,235,0" # Strong Green
#             # elif r < 0.4:
#             #     color =  "118,231,171" # Teal
#             # elif r < 0.5:
#             #     color =  "16,143,88" # Strong Green
#             # elif r < 0.6:
#             #     color =  "18,93,95" # Dark Ocean Blue
#             # elif r < 0.7:
#             #     color =  "117,97,195" # Timid Purple
#             # elif r < 0.8:
#             #     color =  "113,16,132" # Royal Purple
#             # elif r < 0.9:
#             #     color =  "178,124,33" # Leaf
#             # else:
#             #     color = "223,150,113" # Skin


#         # # Blues
#         #     if r < 0.1:
#         #         color =  "113,207,223"
#         #     elif r < 0.2:
#         #         color =  "98,186,202"
#         #     elif r < 0.3:
#         #         color =  "83,149,171"
#         #     elif r < 0.4:
#         #         color =  "89,166,190"
#         #     elif r < 0.5:
#         #         color =  "66,135,183"
#         #     elif r < 0.6:
#         #         color =  "66,123,159"
#         #     elif r < 0.7:
#         #         color =  "70,123,177"
#         #     elif r < 0.8:
#         #         color =  "101,164,224"
#         #     elif r < 0.9:
#         #         color =  "104,150,193"
#         #     else:
#         #         color = "104,118,193"

#         # # Random
#         #     if r < 0.1:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     elif r < 0.2:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     elif r < 0.3:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     elif r < 0.4:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     elif r < 0.5:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     elif r < 0.6:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     elif r < 0.7:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     elif r < 0.8:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     elif r < 0.9:
#         #         color =  '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
#         #     else:
#         #         color = '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'
           
#             color = "0,0,0"
#             #color = '"'+str(random.randint(1,255))+','+str(random.randint(1,255))+','+str(random.randint(1,255))+'"'

        

#             f.write('<rect x="'+ str(rect[0]) +'" y="'+ str(rect[1]) +'" width="'+ str(rect[2]) +'" height="'+ str(rect[3]) +'" style="fill:rgb('+color+');stroke-width:'+str(random.randint(1,250))+';stroke:rgb('+str(random.randint(1,255))+','+str(random.randint(1,6))+','+str(random.randint(1,255))+')"/>\n')
#             f.close()



#     splitter(canvas_rec,canvas_rec)

#     footer = '</svg></body></html>'
#     f = open('rect_xc.html','a')
#     f.write(footer)
#     f.close()


# main()