from graphics import *
from random import randint

# Read in and print out the data in the data file

data = []

datafile = open("data.txt",'r')

change_d = randint(-500,100)
x_speed = randint(-2,2)
y_speed = randint(-2,2)


for line in datafile:
    data.append( float(line))

window = GraphWin("Visualisation", 700, 700)


#  Make Circles
ball0 = Circle(Point(350,350), data[0]*3)
ball1 = Circle(Point(350,350), data[1]*3)
ball2 = Circle(Point(350,350), data[2]*3)
ball3 = Circle(Point(350,350), data[3]*3)
ball4 = Circle(Point(350,350), data[4]*3)
ball5 = Circle(Point(350,350), data[5]*3)
ball6 = Circle(Point(350,350), data[6]*3)
ball7 = Circle(Point(350,350), data[7]*3)
ball8 = Circle(Point(350,350), data[8]*3)
ball9 = Circle(Point(350,350), data[9]*3)
ball10 = Circle(Point(350,350), data[10]*3)
ball11 = Circle(Point(350,350), data[11]*3)
ball12 = Circle(Point(350,350), data[12]*3)
ball13 = Circle(Point(350,350), data[13]*3)
ball14 = Circle(Point(350,350), data[14]*3)
ball15 = Circle(Point(350,350), data[15]*3)
ball16 = Circle(Point(350,350), data[16]*3)
ball17 = Circle(Point(350,350), data[17]*3)
ball18 = Circle(Point(350,350), data[18]*3)
ball19 = Circle(Point(350,350), data[19]*3)
ball20 = Circle(Point(350,350), data[20]*3)
ball21 = Circle(Point(350,350), data[21]*3)
ball22 = Circle(Point(350,350), data[22]*3)
ball23 = Circle(Point(350,350), data[23]*3)
ball24 = Circle(Point(350,350), data[24]*3)
ball25 = Circle(Point(350,350), data[25]*3)
ball26 = Circle(Point(350,350), data[26]*3)
ball27 = Circle(Point(350,350), data[27]*3)
ball28 = Circle(Point(350,350), data[28]*3)
ball29 = Circle(Point(350,350), data[29]*3)
ball30 = Circle(Point(350,350), data[30]*3)
ball31 = Circle(Point(350,350), data[31]*3)


#  Make draw on Visualisation window
ball0.draw(window)
ball1.draw(window)
ball2.draw(window)
ball3.draw(window)
ball4.draw(window)
ball5.draw(window)
ball6.draw(window)
ball7.draw(window)
ball8.draw(window)
ball9.draw(window)
ball10.draw(window)
ball11.draw(window)
ball12.draw(window)
ball13.draw(window)
ball14.draw(window)
ball15.draw(window)
ball16.draw(window)
ball17.draw(window)
ball18.draw(window)
ball19.draw(window)
ball20.draw(window)
ball21.draw(window)
ball22.draw(window)
ball23.draw(window)
ball24.draw(window)
ball25.draw(window)
ball26.draw(window)
ball27.draw(window)
ball28.draw(window)
ball29.draw(window)
ball30.draw(window)
ball31.draw(window)
  


#  Move Circles
while True:

    ball0.move(randint(-2,2), randint(-2,2))
    ball1.move(randint(-2,2), randint(-2,2))
    ball2.move(randint(-2,2), randint(-2,2))
    ball3.move(randint(-2,2), randint(-2,2))
    ball4.move(randint(-2,2), randint(-2,2))
    ball5.move(randint(-2,2), randint(-2,2))
    ball6.move(randint(-2,2), randint(-2,2))
    ball7.move(randint(-2,2), randint(-2,2))
    ball8.move(randint(-2,2), randint(-2,2))
    ball9.move(randint(-2,2), randint(-2,2))
    ball10.move(randint(-2,2), randint(-2,2))
    ball11.move(randint(-2,2), randint(-2,2))
    ball12.move(randint(-2,2), randint(-2,2))
    ball13.move(randint(-2,2), randint(-2,2))
    ball14.move(randint(-2,2), randint(-2,2))
    ball15.move(randint(-2,2), randint(-2,2))
    ball16.move(randint(-2,2), randint(-2,2))
    ball17.move(randint(-2,2), randint(-2,2))
    ball18.move(randint(-2,2), randint(-2,2))
    ball19.move(randint(-2,2), randint(-2,2))
    ball20.move(randint(-2,2), randint(-2,2))
    ball21.move(randint(-2,2), randint(-2,2))
    ball22.move(randint(-2,2), randint(-2,2))
    ball23.move(randint(-2,2), randint(-2,2))
    ball24.move(randint(-2,2), randint(-2,2))
    ball25.move(randint(-2,2), randint(-2,2))
    ball26.move(randint(-2,2), randint(-2,2))
    ball27.move(randint(-2,2), randint(-2,2))
    ball28.move(randint(-2,2), randint(-2,2))
    ball29.move(randint(-2,2), randint(-2,2))
    ball30.move(randint(-2,2), randint(-2,2))
    ball31.move(randint(-2,2), randint(-2,2))
    
   
    















