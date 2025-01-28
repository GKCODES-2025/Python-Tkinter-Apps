from customtkinter import *
from tkinter import messagebox

root = CTk()
root.geometry("320x515")
root.title("Calculator")
root.resizable(False, False)
root.configure(fg_color="azure")
root.iconbitmap("icon.ico")

c = StringVar()

textbox = CTkEntry(root,
                   height=78,
                   width=316,
                   font=("arial", 36, "bold"),
                   border_color="black",
                   border_width=2,
                   corner_radius=4,
                   textvariable=c)
textbox.place(x=2, y=4)

mainframe = CTkFrame(root,
                     width=316,
                     height=422,
                     fg_color="azure")
mainframe.place(x=2, y=90)


def calculator():
    try:
        result = eval(c.get())
        c.set(result)
    except Exception as e:
        c.set("")
        messagebox.showerror("Syntax Error", "Invalid syntax")


current_value = textbox.get()


def update_entry(value):
    textbox.insert(END, current_value + value)


def _1():
    update_entry("1")


def _2():
    update_entry("2")


def _3():
    update_entry("3")


def _4():
    update_entry("4")


def _5():
    update_entry("5")


def _6():
    update_entry("6")


def _7():
    update_entry("7")


def _8():
    update_entry("8")


def _9():
    update_entry("9")


def _0():
    update_entry("0")


def _subraction():
    update_entry("-")


def _divide():
    update_entry("/")


def _add():
    update_entry("+")


def _multiplication():
    update_entry("*")


def _clear():
    c.set("")


def _zero():
    update_entry("0")


button_1 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     fg_color="ivory4",
                     text="1",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     command=_1
                     )
button_1.place(x=5, y=5)

button_2 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     text="2",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     fg_color="ivory4",
                     command=_2
                     )
button_2.place(x=108, y=5)

button_3 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     text="3",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     fg_color="ivory4",
                     command=_3
                     )
button_3.place(x=213, y=5)

button_4 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     fg_color="ivory4",
                     text="4",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     command=_4
                     )
button_4.place(x=5, y=75)

button_5 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     text="5",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     fg_color="ivory4",
                     command=_5
                     )
button_5.place(x=108, y=75)

button_6 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     text="6",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     fg_color="ivory4",
                     command=_6
                     )
button_6.place(x=213, y=75)

button_7 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     fg_color="ivory4",
                     text="7",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     command=_7
                     )
button_7.place(x=5, y=145)

button_8 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     text="8",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     fg_color="ivory4",
                     command=_8
                     )
button_8.place(x=108, y=145)

button_9 = CTkButton(mainframe,
                     width=98,
                     height=60,
                     text="9",
                     font=("arial", 16, "bold"),
                     text_color="black",
                     hover_color="ivory3",
                     fg_color="ivory4",
                     command=_9
                     )
button_9.place(x=213, y=145)

button_add = CTkButton(mainframe,
                       width=98,
                       height=60,
                       fg_color="ivory4",
                       text="+",
                       font=("arial", 16, "bold"),
                       text_color="black",
                       hover_color="ivory3",
                       command=_add
                       )
button_add.place(x=5, y=215)

button_sub = CTkButton(mainframe,
                       width=98,
                       height=60,
                       text="-",
                       font=("arial", 16, "bold"),
                       text_color="black",
                       hover_color="ivory3",
                       fg_color="ivory4",
                       command=_subraction
                       )
button_sub.place(x=108, y=215)

button_mul = CTkButton(mainframe,
                       width=98,
                       height=60,
                       text="x",
                       font=("arial", 16, "bold"),
                       text_color="black",
                       hover_color="ivory3",
                       fg_color="ivory4",
                       command=_multiplication
                       )
button_mul.place(x=213, y=215)

button_div = CTkButton(mainframe,
                       width=98,
                       height=60,
                       fg_color="ivory4",
                       text="/",
                       font=("arial", 16, "bold"),
                       text_color="black",
                       hover_color="ivory3",
                       command=_divide
                       )
button_div.place(x=5, y=285)

button_zero = CTkButton(mainframe,
                        width=98,
                        height=60,
                        text="0",
                        font=("arial", 16, "bold"),
                        text_color="black",
                        hover_color="ivory3",
                        fg_color="ivory4",
                        command=_zero
                        )
button_zero.place(x=108, y=285)

button_clear = CTkButton(mainframe,
                         width=98,
                         height=60,
                         text="CE",
                         font=("arial", 16, "bold"),
                         text_color="black",
                         hover_color="ivory3",
                         fg_color="ivory4",
                         command=_clear
                         )
button_clear.place(x=213, y=285)

button_equal = CTkButton(mainframe,
                         width=306,
                         height=60,
                         text="=",
                         font=("arial", 16, "bold"),
                         text_color="black",
                         hover_color="ivory3",
                         fg_color="green",
                         command=calculator
                         )
button_equal.place(x=5, y=355)

root.mainloop()
