from tkinter import *
from random import randint
import time
from threading import Event

exit = Event()

def new_list():
    global L, is_pressed
    is_pressed = True
    exit.set()
    L = [randint(20, HAUTEUR_BARRES) for _ in range(NB_BARRES)]
    for i in range(NB_BARRES):
        canvas.coords(L_rect[i], 20+i*15, POSITION_BARRES-L[i], 30+i*15, POSITION_BARRES)
    selection_sort_button.config(state="normal")

def call_fonction_de_tri(fonction_de_tri):
    global is_pressed
    is_pressed = False
    fonction_de_tri(L)
    print(L)
        

def change_speed():
    global speed
    if speed == 1:
        speed = 2
    elif speed == 2:
        speed = 3
    elif speed == 3:
        speed = 4
    elif speed == 4:
        speed = 10
    else :
        speed = 1
    speed_button.config(text=f"Speed X{speed}")
    

def selection_sort(a=0):
    selection_sort_button.config(state='disabled')
    for i in range (NB_BARRES):
        if is_pressed:
            return 
        m=i
        for k in range (i, NB_BARRES):
            if L[k]<=L[m]:
                m=k
        swap(i,m)

def bubble_sort(a=0):
    sorted=False
    while not sorted:
        for i in range (NB_BARRES-1): 
            if is_pressed:
                return 
            if L[i]>L[i+1]:
                swap(i, i+1)
        for i in range (NB_BARRES-1):
            if L[i]>L[i+1]:
                break
            if i==NB_BARRES-2 and L[i]<=L[i+1]:
                sorted=True
        


def cocktail(a=0):
    sorted=False
    while not sorted:
        for i in range (0, NB_BARRES-1): 
            if is_pressed:
                return 
            if L[i]>L[i+1]:
                swap(i, i+1)
        for k in range (NB_BARRES-1, 0, -1): 
            if is_pressed:
                return 
            if L[k]<L[k-1]:
                swap(k, k-1)
        for i in range (NB_BARRES-1):
            if L[i]>L[i+1]:
                break
            if i==NB_BARRES-2 and L[i]<=L[i+1]:
                sorted=True

def merge(a, middle, b):
    left, right = L[a:middle], L[middle:b] 
    P = []
    while len(left)!=0 and len(right)!=0:
        if left[0] < right[0]:
            P.append(left.pop(0))
        else:
            P.append(right.pop(0))
    if len(left) == 0 :
        P = P + right
    else:
        P = P + left
    print(P)
    print(L[a:b])
    print()
    for i in range(0, b-a):
        mon_index = L.index(P[i], a+i, b)
        swap(a+i, mon_index)


    
def merge_sort(L, a, b):
    if b-a ==2:
        if L[a] > L[a+1]:
            swap(a, a+1)
            return
    elif b-a == 1:
        return
    middle = (a+b)//2
    merge_sort(L, a, middle)
    merge_sort(L, middle, b)
    return merge(a , middle, b)

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


NB_BARRES = 50
POSITION_BARRES = 295
HAUTEUR_BARRES = 275

window = Tk()
speed = 1
is_pressed = False   

window.geometry(f"{15*NB_BARRES+35}x600")
window.title("Sorting Algorithms")

canvas = Canvas(window, bg="#8C8C8C", highlightthickness=0)
canvas.place(anchor=NW, relx=0.0, rely=0.0, relheight=0.5, relwidth=1.0)

frame = Frame(window, bg="blue")
frame.place(anchor=NW, relx=0.0, rely=0.5, relheight=0.5, relwidth=1.0)

left_frame = Frame(frame, bg="#8C8C8C")
left_frame.pack(side="left",expand=True, fill="both")
left_frame.pack_propagate(0)

right_frame = Frame(frame, bg="#8C8C8C")
right_frame.pack(side="left",expand=True, fill="both")
right_frame.pack_propagate(0)

selection_sort_button = Button(left_frame, text="Tri par sÃ©lection", font=('Helvetica 16'), command=lambda : call_fonction_de_tri(selection_sort))
selection_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

merge_sort_button = Button(left_frame, text="Tri Fusion", font=('Helvetica 16'), command=lambda : merge_sort(L, 0, NB_BARRES))
merge_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

bubble_sort_button = Button(left_frame, text="Tri Bulle", font=('Helvetica 16'), command=lambda : call_fonction_de_tri(bubble_sort))
bubble_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

cocktail_sort_button = Button(left_frame, text="Tri COCKTAIL VODK RHUM MANZANA", font=('Helvetica 16'), command=lambda : call_fonction_de_tri(cocktail))
cocktail_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

new_list_button = Button(right_frame, text="New list", font=('Helvetica 16'), command=new_list)
new_list_button.pack(side=TOP, fill='x', padx=5, pady=5)

speed_button = Button(right_frame, text="Speed X1", font=('Helvetica 16'), command=change_speed)
speed_button.pack(fill="x", padx=5, pady=5)

L = [randint(20, HAUTEUR_BARRES) for _ in range(NB_BARRES)]
L_rect = []
for i in range(NB_BARRES):
    L_rect.append(canvas.create_rectangle(20+i*15, POSITION_BARRES-L[i], 30+i*15, POSITION_BARRES, fill='orange'))

window.mainloop()