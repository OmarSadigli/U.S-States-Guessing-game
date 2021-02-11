import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
is_game_on = True

data = pandas.read_csv("50_states.csv")
correct_answer = 0
guessed_states = 0
while is_game_on:

    answer_state = screen.textinput(title=f"{correct_answer}/50 Guess the State",
                                    prompt="What's another state's name?").title()

    for state in data.state:
        if state == answer_state:
            answer = data[data.state == answer_state]
            correct_answer += 1
            turtle.penup()
            turtle.goto(int(answer.x), int(answer.y))
            turtle.write(arg=answer_state, align="center", font=("Arial", 8, "normal"))

    guessed_states += 1

    if guessed_states > 50:
        is_game_on = False

# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
#
# turtle.mainloop()
#
