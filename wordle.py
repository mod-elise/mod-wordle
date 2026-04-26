import tkinter as tk

def checkWord(word):
    print(characters[1].get())

#-----------------------------------------
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
root = tk.Tk()
root.title("Wordle")

vcmd = (root.register(validate), "%P")

r1c1 = tk.Entry(root, width=1, validate="key", validatecommand=vcmd, font=("Arial", 18))

for i in range(25):
    characters.append( tk.Entry(
        root, width=1, validate="key",  validatecommand=vcmd, font=("Arial", 18)
    ))
    characters[i].grid(row=i // 5, column=i % 5)

tk.Button(
    root,
    text="CHECK",
    width=10,
    height=4,
    bg="LIGHT GREEN",
    command=lambda: checkWord(word)
    ,
).grid(row=6, columnspan =5)

root.mainloop()
