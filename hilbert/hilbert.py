#Program that accepts as input the order, n, and draws an order n Hilbert curve
#For this program i have used help from stockoverflow
import sys
from turtle import Screen, Turtle

#Drwaing the hilbert curive using recursion
#A is the length of the lines, rule is for the inverting the direction, t for the turtle and n is for the order
#Reference Used: #https://stackoverflow.com/questions/53243985/hilbert-curve-using-turtle-graphics-and-recursion
def hilbert(A,rule,t,n):

    if n>=1:#if the input is greater or equal to 1
        if rule:
            t.left(90)# it will turn turtle left by 90 degrees
            hilbert(A,not rule,t, n-1)
            t.forward(A)#it will move the turtle forwared by the distance of lenght line, in the direction it is facing 
            t.right(90)#it will turn turtle right by 90 degrees
            hilbert(A, rule,t, n-1)
            t.forward(A)
            hilbert(A,rule,t, n-1)
            t.right(90)
            t.forward(A)
            hilbert(A,not rule,t, n-1)
            t.left(90)
        else:
            t.right(90)
            hilbert(A, not rule, t, n - 1)
            t.forward(A)
            t.left(90)
            hilbert(A, rule, t, n - 1)
            t.forward(A)
            hilbert(A, rule, t, n - 1)
            t.left(90)
            t.forward(A)
            hilbert(A, not rule, t, n - 1)
            t.right(90)
#main function which will ask for an input in the terminal
def main():
    if len(sys.argv) < 2:#if the user has not put the the order, it will print a message
        print("Input the order after calling the program name")
        return
        #declare the order in the terminal
    order = int(sys.argv[1])
    parity = 1
    def cal_length(order):
        if order == 1:
            return 1
        else:
            return 2 * cal_length(order - 1) + 1
    length = cal_length(order)
    # function which will rescale drwaing when  we change window size
    def resize():
        #setting  x and y coordinates
        screen.setworldcoordinates(0,0,length,length)

        # timer that calls resize function after 1000 milli seconds
        screen.ontimer(resize,1000)
    screen = Screen()
    screen.tracer(False)
    turtle = Turtle()

    resize()
    hilbert(.99,parity,turtle,order)
    #it will update the screen
    screen.update()
    screen.mainloop()

        
main()        

