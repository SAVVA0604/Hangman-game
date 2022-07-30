from random import randint
from english_words import english_words_lower_set
from googletrans import Translator
from tkinter import *
import os

# from playsound import playsound
# playsound(r'C:\\Users\\spete\\Desktop\\py_proj\\hangman_game\\км - ля.mp3')

n = 6
w1 = list(english_words_lower_set)[randint(0, len(english_words_lower_set))]  # len = 25000
u = ["-"] * len(w1)
u_st = "".join(u)
translator = Translator()
result = translator.translate(w1, dest="ru")

window = Tk()
window.title("Hangman game")
window.geometry('500x500')
window.wm_attributes("-topmost", 1)
window.resizable(0, 0)
window.iconbitmap(r"C:\Users\spete\Desktop\py_proj\hangman_game\Images.ico")

canv = Canvas(window, width=1000, height=1000, bg='white')
canv.place(x=0, y=0)
img = PhotoImage(file=r"C:\Users\spete\Desktop\py_proj\hangman_game\white-elegant-texture-background_scale-2_00x.png")
canv.create_image(0, 0, anchor=NW, image=img)

canv2 = Canvas(window, width=156, height=200, bg='white')
canv2.place(x=0, y=300)
img1 = PhotoImage(file=r"C:\Users\spete\Desktop\py_proj\hangman_game\animegirl-art-scale-0_28x.png")
canv2.create_image(0, 0, anchor=NW, image=img1)

lab_unlin = Label(text="Word: " + u_st, height=2, width=24, font="Calibri 14", justify='left', background='white')
lab_unlin.place(x=120, y=150)


def destroy():
    window.destroy()


def restart():
    window.destroy()
    os.startfile("main.py")


def get(self):
    global l, n, txt

    lab_unlin = Label()
    lab_unlin.destroy()
    l = txt.get()
    if w1.find(l) == -1:
        n -= 1
        lab_at = Label(text=f"You have {n} more attempts!", font="Calibri 14", background='white', width=24)
        lab_at.place(x=120, y=200)
        txt.delete(0, END)
        if n == 0:
            lab_rez = Label(text=f"You lost!\n The word is {w1}\n ({result.text}).\n Do you want to play again?",
                            font="Calibri 14", height=5, width=29, background='white')
            lab_rez.place(x=180, y=300)
            yes_but = Button(text="Yes", height=1, width=3, font="Calibri 14", command=restart, background='white')
            yes_but.place(x=267, y=425)
            no_but = Button(text="No", height=1, width=3, font="Calibri 14", command=destroy, background='white')
            no_but.place(x=327, y=425)
            txt = Entry(window, width=10, font='Calibri 14', state='disabled', background='white')

    else:
        for i in range(len(w1)):
            if w1[i] == l:
                u[i] = l
        u_st = "".join(u)
        txt.delete(0, END)
        lab_unlin = Label(text="Word: " + u_st, width=24, height=2, font="Calibri 14", background='white')
        lab_unlin.place(x=120, y=150)

        if u_st.find('-') == -1:
            lab_rez = Label(text="Congratulations! You won!\n Do you want to play again?", font="Calibri 14", height=5,
                            width=29, background='white')
            lab_rez.place(x=180, y=300)
            yes_but = Button(text="Yes", height=1, width=3, font="Calibri 14", command=restart, background='white')
            yes_but.place(x=267, y=425)
            no_but = Button(text="No", height=1, width=3, font="Calibri 14", command=destroy, background='white')
            no_but.place(x=327, y=425)
            # print('Congratulations! You won!')


txt = Entry(window, width=10, font='Calibri 14', background='white')  # , justify= "center")
txt.place(x=260, y=110)
txt.bind('<Return>', get)

lab_in = Label(text="Input a letter:", width=12, height=2, font="Calibri 14", background='white')
lab_in.place(x=120, y=100)

window.mainloop()