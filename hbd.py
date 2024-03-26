import turtle
import time
import random
import math

turtle.title('Happy Birthday my love!')
# Function to display text and additional birthday elements
def display_text_with_birthday(text, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(text, align="center", font=("Great Vibes", 24, "normal"))
    turtle.pendown()
    draw_confetti(x-200, y - 50)  # Draw confetti underneath the text

# Function to draw confetti moving horizontally and then turning 90 degrees
def draw_confetti(x, y):
    turtle.penup()
    turtle.goto(x, y)
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]  # Define colors for confetti
    for _ in range(20):
        turtle.color(random.choice(colors))  # Randomly choose a color for each confetti piece
        turtle.dot(10)  # Draw a dot as confetti
        turtle.forward(20)  # Move forward for the next confetti piece
        if _ == 19:  # After some points, turn 90 degrees
            turtle.left(90)
            for _ in range(8):
                turtle.color(random.choice(colors))  # Randomly choose a color for each confetti piece
                turtle.dot(10)  # Draw a dot as confetti
                turtle.forward(20)  # Move forward for the next confetti piece
                if _ == 7:  # After some points, turn 90 degrees
                    turtle.left(90)
                    for _ in range(20):
                        turtle.color(random.choice(colors))  # Randomly choose a color for each confetti piece
                        turtle.dot(10)  # Draw a dot as confetti
                        turtle.forward(20)  # Move forward for the next confetti piece
                        if _ == 19:  # After some points, turn 90 degrees
                            turtle.left(90)
                            for _ in range(8):
                                turtle.color(random.choice(colors))  # Randomly choose a color for each confetti piece
                                turtle.dot(10)  # Draw a dot as confetti
                                turtle.forward(20)  # Move forward for the next confetti piece
                                if _ == 7:  # After some points, turn 90 degrees
                                    turtle.left(90)

# Function to draw letters "I" and "U"
def draw_letters():
    turtle.penup()
    turtle.goto(-200,0)
    turtle.pendown()
    turtle.color("black")
    turtle.write("I", align="center", font=("Arial", 24, "normal"))

    turtle.penup()
    turtle.goto(200,0)
    turtle.pendown()
    turtle.color("black")
    turtle.write("U", align="center", font=("Arial", 24, "normal"))

# Function to draw a cake with striped red and black pattern
def draw_cake(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    # Draw alternating red and black stripes
    for _ in range(5):
        if _ % 2 == 0:
            turtle.color("red")
        else:
            turtle.color("black")
        turtle.begin_fill()
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(150)
        turtle.end_fill()
        turtle.left(90)
        turtle.forward(50)
    

    # Draw candles on the cake
    draw_candles(x+20, y + 160, 7)  # Adjust positions to place candles on the top side of the cake

# Function to draw candles on the cake
def draw_candles(x, y, num_candles):
    for _ in range(num_candles):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("yellow")  # Set color for the candle flame
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.circle(5)  # Draw candle flame
        turtle.end_fill()

        # Move to draw candle body
        turtle.color("black")
        turtle.penup()
        turtle.goto(x, y - 5)
        turtle.pendown()
        turtle.goto(x, y - 10)  # Draw candle body
        x += 30  # Move to the next candle position (increased from 20 to 30)

# Function to clear the screen
def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

# Main function
def main():
    turtle.speed(3)
    turtle.bgcolor("cyan")

    # First slide: Happy Birthday to Tajie
    display_text_with_birthday("Happy Birthday Tajie!", 0, 100)
    # Draw cake
    draw_cake(-100, -200)
    time.sleep(3)
    clear_screen()
    display_text_with_birthday("Enjoy this day to the fullest", 0, 100)
    clear_screen()
    display_text_with_birthday("Wishing you all the best for today!", 0, 100)
    turtle.goto(0,-100)
    turtle.write("May this special day bring you immense joy, happiness, and countless blessings. You deserve every bit of it!",align="center", font=("Great Vibes", 15, "normal"))
    time.sleep(3)
    clear_screen()
    display_text_with_birthday("Missing you as always...", 0, 100)
    time.sleep(2)
    clear_screen()
    display_text_with_birthday("And one more thing I wanted to say....", 0, 100)
    time.sleep(2)
    clear_screen()
    # Draw letters "I" and "U"
    draw_letters()
# Create a turtle object
    t = turtle.Turtle()

# Set the speed of the turtle
    t.speed(1)

# Draw the heart shape
    t.fillcolor('red')
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Hide the turtle
    t.hideturtle()
    # Hide turtle and exit
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
