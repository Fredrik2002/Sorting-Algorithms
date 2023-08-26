from tkinter import *
from random import randint

def new_list():
    L = [randint(20, 200) for _ in range(NB_BARRES)]
    for i in range(NB_BARRES):
        canvas.coords(L_rect[i], 20+i*15, 250-L[i], 30+i*15, 250)

def first_algorithm():
    first_algorithm_button.config(state='disabled')
    pass

def swap(a, b):
    if a<0:
        a+=NB_BARRES
    if b<0:
        b+=NB_BARRES
    assert a>=0 and b>=0, "Wrong a or b"
    m, M = min(a, b), max(a, b)
    d= M-m
    canvas.move(L_rect[m],d*15, 0)
    canvas.move(L_rect[M],-d*15, 0)
    L[a], L[b] = L[b], L[a]
    L_rect[a], L_rect[b] = L_rect[b], L_rect[a]


NB_BARRES = 50

window = Tk()   

window.geometry(f"{15*NB_BARRES+35}x600")
window.title("Sorting Algorithms")

canvas = Canvas(window)
canvas.place(anchor=NW, relx=0.0, rely=0.0, relheight=0.5, relwidth=1.0)

frame = Frame(window, bg="blue")
frame.place(anchor=NW, relx=0.0, rely=0.5, relheight=0.5, relwidth=1.0)

left_frame = Frame(frame, bg="red")
left_frame.pack(side="left",expand=True, fill="both")

right_frame = Frame(frame, bg="yellow")
right_frame.pack(side="left",expand=True, fill="both")

first_algorithm_button = Button(left_frame, text="First algorithm", font=('Helvetica 20'), command=first_algorithm)
first_algorithm_button.pack(side=TOP, fill="x")

new_list_button = Button(right_frame, text="New list", font=('Helvetica 20'), command=lambda : swap(0,1))
new_list_button.pack(side=TOP, fill='x')

L = [randint(20, 200) for _ in range(NB_BARRES)]
L_rect = []
print(L)
for i in range(NB_BARRES):
    L_rect.append(canvas.create_rectangle(20+i*15, 250-L[i], 30+i*15, 250, fill='orange'))

window.mainloop()