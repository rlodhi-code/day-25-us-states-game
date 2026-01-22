import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
#shows the map
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

correct_guesses = 0

answer_state = screen.textinput(title="Guess the state name",prompt="What's another state's name?")

if answer_state in all_states:
    correct_guesses += 1
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_date = data[data.state == answer_state]
    t.goto(state_date.x.item(), state_date.y.item())
    t.write(answer_state, """font=("Arial", 20, "bold")""")

# print(data)

# while correct_guesses < 50:
screen.exitonclick()
