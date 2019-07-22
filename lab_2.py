##In order complete this challenge you need to debug the following code.
##It may be easier to do so if you improve the code quality. 
##copy and paste this code into a new file named “debugging.py”

import turtle # imports the turtle library

yp7 = turtle.clone() #this creates a new turtle and stores it in a variable
t = 200
b = -200

#draw the letter ‘A’

turtle.hideturtle() # this hides the arrow of the turtle called turtle

yp7.penup()



yp7.goto(-100,0)
yp7.pendown()
yp7.pendown()
yp7.penup()

a,c = yp7.pos()

yp7.goto(a,c)

yp7.pendown()
yp7.goto(a+100, c+300)
turtle.penup()
yp7.goto(a+200, c)
yp7.penup()
yp7.goto(a+30, c+100)
yp7.pendown()

yp7.goto(a+180, c+100)

turtle.mainloop() # all turtle commands must go before this line!!!

