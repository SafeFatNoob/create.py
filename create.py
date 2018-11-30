'''
create.py
cs111-02
amy czimar dalal
hashir safdar
19th november 2018
'''

from graphics import *
import math

class Brush:

    def __init__(self, image, brushType):
        self.image = image
        self.brushType = brushType

    def draw(self, win, im):
        """
        core logic function

        PARAMETERS
        win - GraphWin being drawn on
        im - Image being drawn on
        """

        color = [255, 0, 0]
        thickness = 10

        # loop continues until image is saved
        while True:
            
            # save and quit if save was pressed
            if self.brushType == "save":
                im.save("creation.png")
                break

            # getting mouse input to do something with
            point1 = win.getMouse()
            point2 = win.getMouse()

            # if double clicked, start the panel, get input, and continue to next loop
            if point1.getX() == point2.getX() and point1.getY() == point2.getY():
                panel = BrushPanel()

                self.brushType = panel.getInput()
                color = panel.getColor()
                thickness = panel.getThickness()

                panel.closeWindow()
                continue

            # number of steps - number of sets of pixel manipulations to do, based on thickness
            steps = 3 * int(math.sqrt((point1.getX() - point2.getX()) ** 2 + (point1.getY() - point2.getY()) ** 2) / thickness) + 1

            # creates a direction vector with a magnitude relative to thickness
            direction = [(point2.getX() - point1.getX())/steps, (point2.getY() - point1.getY())/steps]

            # loops through a set of rectangles around points on the line, using thickess and direction
            for i in range(steps):
                for x in range(int(point1.getX() - 0.5 * thickness + i*direction[0]), int(point1.getX() + 0.5 * thickness + i*direction[0]), 1):
                    for y in range(int(point1.getY() - 0.5 * thickness + i*direction[1]), int(point1.getY() + 0.5 * thickness + i*direction[1]), 1):
                        
                        if self.brushType == "greyscale":
                            color = self.greyscale(im.getPixel(x,y))
                        elif self.brushType == "darken":
                            color = self.darken(im.getPixel(x,y))
                        elif self.brushType == "lighten":
                            color = self.lighten(im.getPixel(x,y))
                        elif self.brushType == "saturate":
                            color = self.lighten(im.getPixel(x,y))
                        elif self.brushType == "draw":
                            color = color
                        
                        im.setPixel(x, y, color_rgb(color[0], color[1], color[2]))

    def greyscale(self, colors):
        """
        greyscale function - converts normal pixel to greyscale

        PARAMETERS:
        a list of RGB values

        RETURNS:
        a list of RGB values that have been greyscaled
        """
        average = int(sum(colors) / 3)
        colors = [average, average, average]

        return colors

    def darken(self, colors):
        """
        darken function - converts normal pixel to darkened version

        PARAMETERS:
        a list of RGB values

        RETURNS:
        a list of RGB values that have been darkened
        """

        for i in range(len(colors)):
            if colors[i] < 40:
                colors[i] = 0
            else:
                colors[i] -= 40
                
        return colors

    def lighten(self, colors):
        """
        lighten function - converts normal pixel to lightened version

        PARAMETERS:
        a list of RGB values

        RETURNS:
        a list of RGB values that have been lightened
        """
        for i in range(len(colors)):
            if colors[i] > 215:
                colors[i] = 255
            else:
                colors[i] += 40
                
        return colors

    def saturate(self, colors):
        """
        saturate function - converts normal pixel to saturated version

        this function includes code written by Silas Rhyneer as part of our 'imageFun' in-class lab

        PARAMETERS:
        a list of RGB values

        RETURNS:
        a list of RGB values that have been saturated
        """
        rgbVal = []
        for k in colors:
            newColor = int((k - 177) * 100 + k)
            
            # accounts for extreme values
            if newColor > 255:
                newColor = 255
            elif newColor < 0:
                newColor = 0

            rgbVal.append(newColor)
        return rgbVal

''' 
    def drawLine(self, window, colors, thickness, point1, point2):
        
        # make a basic line, draw function
        # basically a set of circles on the line made form the two points
        
        
        # number of steps - number of circles to make
        steps = 2 * int(abs((point1.getX() - point2.getX()) / thickness))
        # creates a direction vector with a magnitude relative to thickness
        direction = [(point2.getX() - point1.getX())/steps, (point2.getY() - point1.getY())/steps]

        # loops through and draws circles using direction vector
        for i in range(steps):
            c = Circle(Point(point1.getX()+ (i*direction[0]), point1.getY() + (i*direction[1])), thickness)
            c.setFill(color)
            c.setOutline(color)
            c.draw(win)

        win.getMouse()
'''

class BrushPanel:

    def __init__(self):
        self.status = True           # holds whether action is done or not
        self.color = "red"
        self.thickness = 10
        self.win = 0

        self.createPanel()

    def createPanel(self):
        """
        function to create panel with all text and entry boxes
        """

        self.win = GraphWin("Brush Panel", 150, 350)
        im = Image(Point(75,175), "panel.gif")
        im.draw(self.win)

        # draw text for each button
        save = Text(Point(75, 25), "Save")
        save.draw(self.win)

        greyscale = Text(Point(75, 75), "Greyscale")
        greyscale.draw(self.win)

        darken = Text(Point(75, 125), "Darken")
        darken.draw(self.win)

        lighten = Text(Point(75, 175), "Lighten")
        lighten.draw(self.win)

        saturate = Text(Point(75, 225), "Saturate")
        saturate.draw(self.win)

        # drawing in boxes for draw function
        drawLabel = Text(Point(75, 260), "Draw")
        drawLabel.draw(self.win)
        self.red = Entry(Point(30, 285), 3)
        self.red.setText("255")
        self.red.draw(self.win)
        self.green = Entry(Point(75, 285), 3)
        self.green.setText("255")
        self.green.draw(self.win)
        self.blue = Entry(Point(120, 285), 3)
        self.blue.setText("255")
        self.blue.draw(self.win)

        # same for thickness
        thickLabel = Text(Point(75, 310), "Thickness")
        thickLabel.draw(self.win)
        self.thick = Entry(Point(75,335), 2)
        self.thick.setText(str(self.thickness))
        self.thick.draw(self.win)

    def getInput(self):
        """
        function to get input from panel

        RETURNS:
        string representing what button was selected
        """

        coord = self.win.getMouse().getY()

        # depending on the y coordinate, finds out what button was pressed and returns appropriately
        if coord < 50:
            return "save"
        elif coord > 50 and coord < 100:
            return "greyscale"
        elif coord > 100 and coord < 150:
            return "darken"
        elif coord > 150 and coord < 200:
            return "lighten"
        elif coord > 200 and coord < 250:
            return "saturate"
        elif coord > 250 and coord < 300:
            return "draw"
        elif coord > 350 and coord < 400:
            return "draw"

    def getColor(self):
        self.color = [int(self.red.getText()), int(self.green.getText()), int(self.blue.getText())]
        return self.color

    def getThickness(self):
        self.thickness = int(self.thick.getText())
        return self.thickness

    def closeWindow(self):
        self.win.close()

def main():
    imageFile = input("What file would you like to create on? ")

    im = Image(Point(475,250), imageFile)
    win = GraphWin("create.py", im.getWidth(), im.getHeight())
    im.draw(win)

    brush = Brush(im, "draw")
    brush.draw(win, im)

main()