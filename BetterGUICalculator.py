from tkinter import *

root = Tk()
root.geometry("405x405")
root.resizable(width=False, height=False)
root.configure(background="#17161b")

equation = ""


def show(value):
    global equation
    equation += value
    resultLabel.config(text=equation)


def clear():
    global equation
    equation = ""
    resultLabel.config(text="")


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except ZeroDivisionError:
            result = "Cannot divide by zero!"
        except SyntaxError:
            result = "Invalid syntax!"
        except Exception as e:
            result = f"Error: {str(e)}"
        resultLabel.config(text=result)


resultLabel = Label(root, width=70, height=5, text="", font=("arial", 10, "bold"))
resultLabel.pack()

Button(root, text="C", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#ff6600", fg="#ffffff",
       command=lambda: clear()).place(x=5, y=90)
Button(root, text="/", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("/")).place(x=105, y=90)
Button(root, text="%", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("%")).place(x=205, y=90)
Button(root, text="*", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("*")).place(x=305, y=90)

Button(root, text="7", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("7")).place(x=5, y=153)
Button(root, text="8", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("8")).place(x=105, y=153)
Button(root, text="9", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("9")).place(x=205, y=153)
Button(root, text="-", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("-")).place(x=305, y=153)

Button(root, text="4", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("4")).place(x=5, y=216)
Button(root, text="5", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("5")).place(x=105, y=216)
Button(root, text="6", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("6")).place(x=205, y=216)
Button(root, text="+", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("+")).place(x=305, y=216)

Button(root, text="1", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("1")).place(x=5, y=279)
Button(root, text="2", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("2")).place(x=105, y=279)
Button(root, text="3", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("3")).place(x=205, y=279)

Button(root, text="0", font=("arial", 12, "bold"), width=18, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show("0")).place(x=5, y=342)

Button(root, text=".", font=("arial", 12, "bold"), width=8, height=2, bd=5, bg="#2a2d36", fg="#ffffff",
       command=lambda: show(".")).place(x=205, y=342)

Button(root, text="=", font=("arial", 12, "bold"), width=8, height=5, bd=5, bg="#ff6600", fg="#ffffff",
       command=lambda: calculate()).place(x=305, y=279)

root.mainloop()
