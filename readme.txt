create.py
19th November 2018
CS111.02 - Amy Czimar Dalal
Author: Hashir Safdar
----------------------------

Welcome to the simulation of a canvas! In this simulation, you take control of your art.
Load up the program by running 'create.py' within the folder, and enter in the image file you wish to use. 'white.gif', 'black.gif', 'rainbow.gif', 'nature.gif' are provided. If you wish to use your own image, ensure it is sized around 950 x 500 and is in .gif format.
By default, the draw tool will be selected with the color red.
Press on one point on the window, and then another point to perform your action.
To change the brush being used, double click anywhere on the window. You can also save your creation here.
Quit the program by saving your creation.


KNOWN BUGS:
saturating a certain set of pixels may cause the program to crash as RGB values are out of bound, despite being controlled
saving may be an issue if the image is too complex
when gifs are loaded that are not 950 x 500, may be buggy
if an action is performed near the edge of the window, will crash

NOT IMPLEMENTED:
using circles instead of rectangles for smoother editing - was too intensive for graphics.py
rotate/flip