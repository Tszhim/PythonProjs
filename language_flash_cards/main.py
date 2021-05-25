from tkinter import *
from word_generator import WordGenerator

# Globals
BACKGROUND_COLOR = "#B1DDC6"
waiting_period = False
previous_pair = None

# Button command when user clicks correct button.
def correct():
    global waiting_period
    global previous_pair

    # Only executes if the flashcard is finished.
    if not waiting_period:
        # If the user already knows the word, delete it from the list.
        if previous_pair is not None:
            word_generator.remove_word_pair(previous_pair["Cantonese"], previous_pair["English"])
            previous_pair = None
        # Exit the program if all the words are exhausted.
        if len(word_generator.cantonese_word_list) == 0:
            word_generator.save()
            window.destroy()
        # Updates UI and calls flip() after 5 seconds.
        else:
            previous_pair = word_generator.random_word()
            canvas.itemconfig(card_image, image=card_front)
            canvas.itemconfig(word, text=previous_pair["English"], fill="Black", font=("Arial", 60, "bold"))
            canvas.itemconfig(language_type, text="English", fill="Black")
            waiting_period = True
            window.after(5000, flip, previous_pair["Cantonese"])
    # Updates text to tell user to wait for flashcard to finish.
    else:
        canvas.itemconfig(language_type, text="Please wait until current flashcard is finished.", fill="Black",
                          font=("Arial", 20, "italic"))

# Button command when user clicks incorrect button.
def incorrect():
    global waiting_period
    
    # Only executes if the flashcard is finished.
    if not waiting_period:
        # Updates UI and calls flip() after 5 seconds.
        pair = word_generator.random_word()
        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(word, text=pair["English"], fill="Black", font=("Arial", 60, "bold"))
        canvas.itemconfig(language_type, text="English", fill="Black")
        waiting_period = True
        window.after(5000, flip, pair["Cantonese"])
    # Updates text to tell user to wait for flashcard to finish.
    else:
        canvas.itemconfig(language_type, text="Please wait until current flashcard is finished.", fill="Black",
                          font=("Arial", 20, "italic"))

# Flips flashcard after 5 seconds to show the word in Cantonese.
def flip(cantonese_word):
    global waiting_period

    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(word, text=cantonese_word, fill="White")
    canvas.itemconfig(language_type, text="Cantonese", fill="White")
    waiting_period = False


# Window setup.
window = Tk()
window.title("Language Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup.
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
language_type = canvas.create_text(400, 150, text="Cantonese-English Flashcards", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Press either button to begin.", font=("Arial", 20, "bold"))

# Button setup.
check_mark = PhotoImage(file="images/right.png")
check_button = Button(image=check_mark, highlightthickness=0, command=correct)
x_mark = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_mark, highlightthickness=0, command=incorrect)

# Positioning elements via grid.
canvas.grid(row=0, column=0, columnspan=2)
x_button.grid(row=1, column=0)
check_button.grid(row=1, column=1)

# Word generator object to retrieve words and create review file for future use.
word_generator = WordGenerator()

window.mainloop()
