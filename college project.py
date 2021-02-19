import sys
import turtle
import winsound as ws
import time

#Alarm Clock Screen

md = turtle.Screen()
md.setup(width=400, height=300)
md.bgcolor("white")
md.title("ALARM CLOCK")
md.tracer(0)

#Pen 1

p1 = turtle.Turtle()
p1.speed(0)
p1.penup
p1.hideturtle()

#Pen 2

p2=turtle.Turtle()
p2.speed(0)
p2.penup
p2.hideturtle()

#Pen 3

p3=turtle.Turtle()
p3.speed(0)
p3.penup
p3.hideturtle()

#Time Variable

Time = time.strftime("%H:%M:%S")

#Displaying time

print("")
print("CURRENT TIME "+Time)
Alarm=input("Set Alarm")
print("")

#SETTING ALARM

print("Alarm Time : "+Alarm)
confirmation=str(input("You want to confirm the Alarm? [Yes/No]")).lower()
print("")

#Structure of clock

def d_clock():
    p1.pencolor("gray")
    p1.pensize(5)
    o = p1.xcor = -75
    n = p1.ycor = 45
    p1.goto(o, n)
    p1.pendown()
    for i in range(2):
        p1.fd(150)
        p1.rt(90)
        p1.fd(50)
        p1.rt(90)
    p1.penup()
    p2.penup()
    p2.goto(o-15, n+15)
    p2.pencolor("black")
    p2.pensize(25)
    p2.pendown()
    for i in range(2):
        p2.fd(180)
        p2.rt(90)
        p2.fd(80)
        p2.rt(90)
def c_time():
    p3.pencolor("red")
    p3.goto(0, 0)
    p3.clear()
    p3.write(h+":"+m+":"+s, font=("D", 25, "normal"), align="center")
    p3.penup()
    p3.goto(0, -32)
    p3.pendown()
    p3.write(d, font=("D", 15, "normal"), align="center")


#Loops

if confirmation == "n" or confirmation == "no":
    print("")
    print("At this moment it is"+Alarm)
    Alarm=input("Set Alarm")
    print("")
    print("Alarm will ring at"+Alarm)
    confirmation = str(input("Would you like to confirm? [Yes/No]")).lower()
    print("")

while confirmation == "y" or confirmation == "yes":
    while Time != Alarm:
        Time = time.strftime("%H:%M:%S")
        h = time.strftime("%H")
        m = time.strftime("%M")
        s = time.strftime("%S")
        d = time.strftime("%D")
        c_time()
        d_clock()
        time.sleep(1)
        md .update()
        if Time == Alarm:
            ws.PlaySound("BabyElephantWalk60", ws.SND_FILENAME)
md.mainloop()    
    
                  

