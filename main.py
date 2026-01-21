import turtle

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
#shows the map
turtle.shape(image)

state_name = screen.textinput(title="Guess the state name",prompt="What's another state's name?")

