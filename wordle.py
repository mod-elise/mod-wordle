import tkinter as tk



def validate(P):
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isalpha():
        return True
    else:
        # Anything else, reject it
        return False
    

root = tk.Tk()
root.title("Wordle")

vcmd = (root.register(validate), '%P')

r1c1 = tk.Entry(root, width=1, validate="key", validatecommand=vcmd, font=("Arial", 18))

for i in range(25):
    character = tk.Entry(root, width=1, validate="key", validatecommand=vcmd, font=("Arial", 18))
    character.grid(row=i // 5, column=i%5)






root.mainloop()