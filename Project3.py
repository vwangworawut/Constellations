import turtle
WIDTH = turtle.window_width() / 2.0

def convertXY(origX, origY, width):
       x = float(origX)*width
       y = float(origY)*width
       return (x, y)
       '''Takes origX and origY in the star coordinate system and returns
        x and y in the screen coordinate system'''
       # FILL IN CODE




       
def drawStar(origX, origY, t, brightness, col):
       (x, y) = convertXY(origX, origY, WIDTH)
       t.color(col)
       t.penup()
       t.goto(x, y)
       t.pendown()
       t.begin_fill()
       t.circle(brightness*0.25, 360)
       t.end_fill()
       
       
       """ First, calls convertXY to convert origX and origY to the screen
       coordinates. Then uses the turtle t and color col to draw a circle
       at position x,y and with radius proporional to the brightness."""
       # FILL IN CODE




       
      
       
def drawLine(origX1, origY1, origX2, origY2, t, col):
       (x1, y1) = convertXY(origX1, origY1, WIDTH)
       (x2, y2) = convertXY(origX2, origY2, WIDTH)
       t.color(col)
       t.penup()
       t.goto(x1,y1)
       t.pendown()
       t.goto(x2,y2)
##       t.penup()
       t.ht()
       
       '''First calls convertXY to convert (origX1, origY1) and (origX2, origY2)
       to screen coordinates (x1, y1) and (x2, y2).Then uses the turtle t
       to draw a line between points (x1,y1) and (x2, y2)'''
       # FILL IN CODE
       

def loadStars(filename, t):
       dictStars = {}
       file = open(filename, 'r')
       lines = file.readlines()
       brightestStar = 0

       for line in lines:
              split = line.split(" ")
              if len(split) < 7:
                     a = float(split[0])
                     b = float(split[1])
                     brightness = float(split[4])
                     drawStar(a, b, t, brightness, "yellow")

              if len(split) >= 7:
                     a = float(split[0])
                     b = float(split[1])
                     brightness = float(split[4])
                     drawStar(a, b, t, brightness, "yellow")
                     newLine = ""
                     for i in range(6,len(split)):
                            newLine += " " + split[i]
                     split2 = newLine.split(";")
                     for j in range(0,len(split2)):
                            split2[j] = split2[j].strip()
                     if len(split2) == 1:
                            e = split2[0].replace("\n", "")
                            dictStars[e] = (a, b), brightness
                     elif len(split2) == 2:
                            f = split2[0].replace("\n", "")
                            dictStars[f] = (a, b), brightness
                            g = split2[1].replace("\n", "")
                            dictStars[g] = (a, b), brightness
                     elif len(split2) == 3:
                            h = split2[0].replace("\n", "")
                            dictStars[h] = (a, b), brightness
                            i = split2[1].replace("\n", "")
                            dictStars[i] = (a, b), brightness
                            j = split2[2].replace("\n", "")
                            dictStars[j] = (a, b), brightness

                     

                     if brightestStar < brightness:
                            brightStar = e
                            brightestStar = brightness
                            x = a
                            y = b
       drawStar(x, y, t, brightestStar, "green")
       t.penup()
       t.goto(-350,300)
       t.pendown()
       t.color("white")
       t.write(str(brightStar) + " is the brightest star.", move = False, align = "left", font = ("Times", 12, "normal"))
                            
              

       ''' Reads stars from the file, calls drawStar for each star.
       Creates and returns a dictionary containing (key, value) pairs,
       where key is the name of the star, and value is (x, y) position.
       Also, it should compute which star is the brightest, write this
       message on the screen and highlight it in green.'''
       # FILL IN CODE
       return dictStars




def drawConstellation(dictStars, constelFilename, t):
       origX = 0
       origY = 0
       origX2 = 0
       origY2 = 0
       file = open(constelFilename, 'r')
       lines = file.readlines()
       for line in lines:
              names = line.split(",")
              names[1] = names[1].replace("\n","")
              star1 = names[0]
              star2 = names[1]
              origX, origY = dictStars[star1][0]
              origX2,origY2 = dictStars[star2][0]
              drawLine(origX, origY, origX2, origY2, t, "white")

              

       ''' Reads the constellation file and calls drawLine for
       each pair of stars'''
              

       
def main():
       
       # Create screen and turtle
       import turtle
       scr = turtle.Screen()
       scr.bgcolor("darkblue")
       wilfred = turtle.Turtle()
       # FILL IN CODE
       
       
       scr.tracer(0) # do not update the screen
       dictStars = loadStars("stars.txt", wilfred)
       print(dictStars)
       # Call loadStars and get the dictionary of stars
       # FILL CODE

       # Read constellation files (assumes they are in the current directory)
       import glob
       listFiles = glob.glob("*_lines.txt")
       for filename in listFiles:
           print(filename)
           drawConstellation(dictStars, filename, wilfred)
           # Call draw constellations here
           # FILL IN CODE
           
           
       scr.update() # update the screen
       scr.tracer(10)

main()   # call main
