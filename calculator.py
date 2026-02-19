import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.resizable(False, False)
root.configure(bg="#1e1e1e")
expression = ""

def update(val):
    display_var.set(val)
    
def press(val):
    global expression
    expression += str(val)
    update(expression)
    
def clear():
    global expression
    expression = ""
    update("0")
    
def backspace():
    global expression
    expression = expression[:-1]
    update(expression if expression else "0")

def equal():
    global expression
    try:
        result = str(eval(expression))
        expression = result
        update(result)
    except:
        update("Error")
        expression = ""
        
def square():
    global expression
    try:
        result = str(eval(expression) ** 2)
        expression = result
        update(result)
    except:
        update("Error")
        
def sqrt():
    global expression
    try:
        result = str(math.sqrt(eval(expression)))
        expression = result
        update(result)
    except:
        update("Error")

def percent():
    try:
        result = str(eval(expression) / 100)
        expression = result
        update(result)
    except:
        update("Error")
        expression = ""
        
mode_label = tk.Label(
    root,
    text= "Standard",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)
mode_label.pack(anchor="w", padx=15, pady=5)

display_var = tk.StringVar(value="0")
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 28),
    bg="#1e1e1e",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="x", ipadx=10, ipady=20, padx=10, pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both", padx=10, pady=10)

def create_btn(text, r, c, cmd=None, color="#2d2d2d", colspan=1):
    b = tk.Button(
        frame,
        text=text,
        font=("Arial", 16),
        bg=color,
        fg="white",
        bd=2,
        relief="raised",
        activebackground="#3d3d3d",
        activeforeground="white",
        highlightthickness=1,
        highlightbackground="#555",
        command=cmd
    )
    b.grid(row=r, column=c, columnspan=colspan,
           sticky="nsew", padx=5, pady=5)
    
for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)
        
create_btn("C", 0,0, clear, "#b00020")
create_btn("⌫", 0,1, backspace)
create_btn("%", 0,2, percent)
create_btn("x²", 0,3, square)
    
create_btn("7", 1, 0, lambda: press("7"))
create_btn("8", 1, 1, lambda: press("8"))
create_btn("9", 1, 2, lambda: press("9"))
create_btn("√", 1, 3, sqrt)
    
create_btn("4", 2, 0, lambda: press("4"))
create_btn("5", 2, 1, lambda: press("5"))
create_btn("6", 2, 2, lambda: press("6"))
create_btn("÷", 2, 3, lambda: press("/"))
    
create_btn("1", 3, 0, lambda: press("1"))
create_btn("2", 3, 1, lambda: press("2"))
create_btn("3", 3, 2, lambda: press("3"))
create_btn("x", 3, 3, lambda: press("*"))
    
create_btn("0", 4, 0, lambda: press("0"), colspan=2)
create_btn(".", 4, 2, lambda: press("."))
create_btn("-", 4, 3, lambda: press("-"))
    
create_btn("+", 5, 3, lambda: press("+"))
create_btn("=", 5, 0, equal, "#0078d7", colspan=3)

def key_event(event):
    key = event.char

    if key in "0123456789.+-*/":
        press(key)
    elif event.keysym == "Return":
        equal()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

root.bind("<Key>", key_event)
    
root.mainloop()         