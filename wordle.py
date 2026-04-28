import tkinter as tk
import time
import random


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


def startGame():
    resetUI()
    global guess
    global lines
    guess = 0
    with open("wordlist.txt", "r") as file:
        content = file.read()
        lines = content.splitlines()
    global word
    word = random.choice(lines).upper()


# ----------- USER INTERFACE ------------------------------


def resetUI():
    for i in range(25):
        characters[i].config(state=tk.NORMAL)
        characters[i].delete(0, tk.END)
        btn.config(text="CHECK", state=tk.NORMAL)
    characters[0].focus_set()


def on_key(event, index):
    if len(event.keysym) > 1 and event.keysym != "BackSpace":
        return "break"

    entry = characters[index]

    if event.keysym == "BackSpace":
        entry.delete(0, tk.END)
        if index > 0:
            characters[index - 1].focus_set()
        return "break"

    entry.delete(0, tk.END)
    entry.insert(0, event.char.upper())

    if index < len(characters) - 1:
        characters[index + 1].focus_set()

    return "break"


characters = []
root = tk.Tk()
root.title("Wordle")

for i in range(25):
    e = tk.Entry(root, width=2, validate="key", font=("Arial", 18))
    e.grid(row=i // 5, column=i % 5)
    e.bind("<KeyPress>", lambda event, idx=i: on_key(event, idx))
    characters.append(e)

characters[0].focus_set()

btn = tk.Button(
    root,
    text="CHECK",
    width=10,
    height=4,
    bg="LIGHT GREEN",
    command=lambda: checkWord(word),
)
btn.grid(row=6, columnspan=5)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=startGame)
menubar.add_cascade(label="Game", menu=filemenu)

root.config(menu=menubar)


global word
startGame()
root.mainloop()
