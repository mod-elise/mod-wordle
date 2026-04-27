import tkinter as tk
import time


def getChars(adder):

    return [
        characters[adder].get(),
        characters[adder + 1].get(),
        characters[adder + 2].get(),
        characters[adder + 3].get(),
        characters[adder + 4].get(),
    ]


def checkWord(word):
    global guess
    adder = guess * 5
    wordle = list(word)
    guessed_letters = getChars(adder)
    word_colours = [0, 0, 0, 0, 0]

    # find greens and remove them from list
    for idx, guessed_letter in enumerate(guessed_letters):
        if wordle[idx] == guessed_letter:
            word_colours[idx] = 2
            wordle[idx] = "."

    # find yellows and remove them from list
    for idx, guessed_letter in enumerate(guessed_letters):
        print(idx, guessed_letter, wordle)
        if guessed_letter in wordle:
            word_colours[idx] = 1
            for jdx, scanned in enumerate(wordle):
                if scanned == guessed_letter:
                    wordle[jdx] = "."
                    break

    for idx, letter_color in enumerate(word_colours):
        time.sleep(0.3)
        if letter_color == 0:
            characters[idx + adder].config(
                disabledbackground="GREY", disabledforeground="BLACK", state=tk.DISABLED
            )
        if letter_color == 1:
            characters[idx + adder].config(
                disabledbackground="GOLDENROD",
                disabledforeground="BLACK",
                state=tk.DISABLED,
            )
        if letter_color == 2:
            characters[idx + adder].config(
                disabledbackground="GREEN",
                disabledforeground="BLACK",
                state=tk.DISABLED,
            )
        root.update()
    guess = guess + 1
    if sum(word_colours) == 10:
        btn.config(text="Won!", state=tk.DISABLED)


# ----------- USER INTERFACE ------------------------------
def validate(P):
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isalpha():
        return True
    else:
        # Anything else, reject it
        return False


def on_key(event, index):
    value = characters[index].get()
    if len(value) == 0 and event.keysym == "BackSpace":
        if index > 0:
            characters[index - 1].focus_set()
            characters[index - 1].delete(0, tk.END)
    else:
        characters[index].delete(0, tk.END)
        characters[index].insert(tk.END, value.upper())
        characters[index + 1].focus_set()
    root.update()


word = "SCARE"
characters = []
guess = 0
root = tk.Tk()
root.title("Wordle")

vcmd = (root.register(validate), "%P")

for i in range(25):
    e = tk.Entry(
        root, width=2, validate="key", validatecommand=vcmd, font=("Arial", 18)
    )
    e.grid(row=i // 5, column=i % 5)
    e.bind("<KeyRelease>", lambda event, idx=i: on_key(event, idx))
    characters.append(e)

btn = tk.Button(
    root,
    text="CHECK",
    width=10,
    height=4,
    bg="LIGHT GREEN",
    command=lambda: checkWord(word),
)
btn.grid(row=6, columnspan=5)

root.mainloop()
