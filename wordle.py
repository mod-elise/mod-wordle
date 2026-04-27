import tkinter as tk


def getChars():
    return [
        characters[0].get(),
        characters[1].get(),
        characters[2].get(),
        characters[3].get(),
        characters[4].get(),
    ]


def checkWord(word):
    wordle = list(word)
    guessed_letters = getChars()
    word_colours = [0, 0, 0, 0, 0]

    # find greens and remove them from list
    for idx, guessed_letter in enumerate(guessed_letters):
        if wordle[idx] == guessed_letter:
            word_colours[idx] = 1
            wordle[idx] = "."

    # find yellows and remove them from list
    for idx, guessed_letter in enumerate(guessed_letters):
        print(idx, guessed_letter, wordle)
        if guessed_letter in wordle:
            word_colours[idx] = 2
            for jdx, scanned in enumerate(wordle):
                if scanned == guessed_letter:
                    wordle[jdx] = "."
                    break

    for idx, letter_color in enumerate(word_colours):
        if letter_color == 1:
            characters[idx].config(bg="GREEN")
        if letter_color == 2:
            characters[idx].config(bg="goldenrod")


# -----------------------------------------
def validate(P):
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isalpha():
        return True
    else:
        # Anything else, reject it
        return False


word = "SCARE"
characters = []
guess = 1
root = tk.Tk()
root.title("Wordle")


vcmd = (root.register(validate), "%P")

r1c1 = tk.Entry(root, width=1, validate="key", validatecommand=vcmd, font=("Arial", 18))

for i in range(25):
    characters.append(
        tk.Entry(
            root, width=2, validate="key", validatecommand=vcmd, font=("Arial", 18)
        )
    )
    characters[i].grid(row=i // 5, column=i % 5)

tk.Button(
    root,
    text="CHECK",
    width=10,
    height=4,
    bg="LIGHT GREEN",
    command=lambda: checkWord(word),
).grid(row=6, columnspan=5)

root.mainloop()
