import turtle
def main():
#exit on click, is args and descriptions right?
    window = turtle.Screen()
    window.bgcolor("blue")

    fish = turtle.Turtle()
    fish.penup()
    fish.setpos(20,20)
    fish.pendown()
    fish.shape("turtle")
    fish.speed(5)
    fish.color("cyan","green")
    fish.pensize(15)
    scale = .8
    smile = False
    draw_face(fish,scale,smile)
    #fish 1 draws the first face
    
    
    fish2 = turtle.Turtle()
    fish2.penup()
    fish2.setpos(100,-130)
    fish2.pendown()
    fish2.right(61)
    fish2.forward(30)
    fish2.speed(5)
    fish2.color("purple","green")
    fish2.pensize(9)
    fish2.shape("turtle")
    scale2 = .5
    smile2 = True
    draw_face(fish2,scale2,smile2)
    #fish 2 draws the second face

    fish3 = turtle.Turtle()
    fish3.penup()
    fish3.setpos(-80,40)
    fish3.pendown()
    fish3.right(200)
    fish3.speed(5)
    fish3.color("magenta","green")
    fish3.pensize(3)
    fish3.shape("turtle")
    scale3 = 1.1
    smile3 = False
    draw_face(fish3,scale3,smile3)
    #fish 3 draws the third face

    pattern = turtle.Turtle()
    pattern.penup()
    pattern.setpos(-340,-310)
    pattern.pendown()
    pattern.speed(15)
    pattern.shape("turtle")
    pattern.color("black","yellow")
    pattern.pensize(5)
    draw_pattern(pattern)
    
    #Args:
        #the function draws the head first
        #then it draws the frown or smile based on the True or False expression
        #then it draws the right eye, then the left eye
        #fish: this is the first parameter that draws the first smiley face
        #scale: this is the scale used for the first face
        #smile: this paramter uses a true or false expression to determine
                #to draw a smiley face or a frowney face

def draw_face(fish,scale,smile):
    fish.circle(150*scale)
    fish.penup()

    #this draws the head 
    
    if smile == False:
        fish.forward(74*scale)
        fish.left(90)
        fish.forward(40*scale)
        fish.pendown()
        fish.circle(70*scale,180)

    #this draws the frown smile

        fish.penup()
        fish.right(180)
        fish.forward(140*scale)
        fish.right(90)
        fish.forward(140*scale)
        fish.pendown()
        fish.color("red")
        fish.begin_fill()
        fish.circle(30*scale)
        fish.end_fill()
    #this draws the right eye, red if its a frown 

        fish.penup()
        fish.right(180)
        fish.forward(120*scale)
        fish.right(90)
        fish.forward(25*scale)
        fish.pendown()
        fish.color("red")
        fish.begin_fill()
        fish.circle(30*scale)
        fish.end_fill()
        fish.hideturtle()
    #this draws the left eye, red if its a frown
    #this hides the turtle after its drawn
        

    if smile == True:
        fish.backward(70*scale)
        fish.left(90)
        fish.forward(100*scale)
        fish.right(180)
        fish.pendown()
        fish.circle(70*scale,180)
    #this draws the smile

        fish.penup()
        fish.forward(80*scale)
        fish.right(90)
        fish.pendown()
        fish.color("green")
        fish.begin_fill()
        fish.circle(30*scale)
        fish.end_fill()
    #this draws the right eye, green if smile

        fish.penup()
        fish.backward(135*scale)
        fish.pendown()
        fish.color("green")
        fish.begin_fill()
        fish.circle(30*scale)
        fish.end_fill()
        fish.hideturtle()
    #this draws the left eye, green if smile
    #this hides the turtle after its drawn

def draw_pattern(pattern):
    for num in range(34):
        pattern.forward(10)
        pattern.left(90)
        pattern.forward(10)
        pattern.right(90)
        pattern.forward(10)
        pattern.right(90)
        pattern.forward(10)
        pattern.left(90)
    pattern.hideturtle()
    #Args:
        #the draw_pattern function uses its pattern parameter to draw a pattern
        #the pattern parameter is another turtle
        #this draws the pattern at the bottom, looping this function 34 times

if __name__ == "__main__":
    main()
    exitonclick()





