import turtle
from answer_tracker import AnswerTracker
from text_updater import TextUpdater
from time_checker import TimeChecker

# Setting up window.
screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# Creating objects for game.
answer_checker = AnswerTracker()
text_updater = TextUpdater()
time_checker = TimeChecker()

# Game Loop
while True:
    screen.update()

    # Get user input.
    question = screen.textinput(title="Question", prompt="What's another state's name?")
    valid = answer_checker.valid_answer(question, screen, answer_checker)

    # Update time.
    if time_checker.curr_sec() < 10:
        text_updater.draw_timer(str(time_checker.curr_min()) + ":0" + str(time_checker.curr_sec()))
    else:
        text_updater.draw_timer(str(time_checker.curr_min()) + ":" + str(time_checker.curr_sec()))

    # Checking answer validity.
    if valid:
        text_updater.draw_score(answer_checker.user_score)
        text_updater.label_state(answer_checker.answers[-1])

    # Player loses.
    if time_checker.times_up():
        text_updater.draw_lose()
        break

    # Player wins.
    if answer_checker.completed_quiz():
        text_updater.draw_win()
        break


