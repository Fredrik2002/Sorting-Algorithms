from tkinter import *
from random import randint
import time

def new_list():
    global L
    L = [randint(20, 200) for _ in range(NB_BARRES)]
    for i in range(NB_BARRES):
        canvas.coords(L_rect[i], 20+i*15, 250-L[i], 30+i*15, 250)
    selection_sort_button.config(state="normal")

def change_speed():
    global speed
    if speed == 1:
        speed = 2
    elif speed == 2:
        speed = 4
    else :
        speed = 1
    speed_button.config(text=f"Speed X{speed}")
    

def selection_sort():
    selection_sort_button.config(state='disabled')
    for i in range (NB_BARRES):
        m=i
        for k in range (i, NB_BARRES):
            if L[k]<=L[m]:
                m=k
        swap(i,m)
    

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
    time.sleep(0.2/speed)
    window.update()
    window.update_idletasks()


NB_BARRES = 49

window = Tk()
speed = 1   

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

selection_sort_button = Button(left_frame, text="Tri par sélection", font=('Helvetica 20'), command=selection_sort)
selection_sort_button.pack(side=TOP, fill="x")

new_list_button = Button(right_frame, text="New list", font=('Helvetica 20'), command=new_list)
new_list_button.pack(side=TOP, fill='x')

speed_button = Button(right_frame, text="Speed X1", font=('Helvetica 20'), command=change_speed)
speed_button.pack(fill="x")

L = [randint(20, 200) for _ in range(NB_BARRES)]
L_rect = []
print(L)
for i in range(NB_BARRES):
    L_rect.append(canvas.create_rectangle(20+i*15, 250-L[i], 30+i*15, 250, fill='orange'))

window.mainloop()