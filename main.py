from random import randint
import time
from tkinter import N, NW, TOP, IntVar
from ttkbootstrap.widgets import Progressbar, Label, Checkbutton
from ttkbootstrap import Window, Canvas, Button, Frame


def new_list():
    global L, is_next_list_pressed, is_list_sorted
    is_next_list_pressed = True
    is_list_sorted = False
    progress_bar['value'] = 0
    label.config(text="0%")
    time_left.config(text = "Time left : ")
    L = [randint(20, HAUTEUR_BARRES) for _ in range(NB_BARRES)]
    for i in range(NB_BARRES):
        canvas.coords(L_rect[i], 20+i*15, POSITION_BARRES-L[i], 30+i*15, POSITION_BARRES)
    for button in left_frame.winfo_children():
        button.config(state='normal')


def compte_swaps(*args):
    global nb_swaps
    nb_swaps+=1

def swap_and_count(a, b, M):
    global nb_swaps
    nb_swaps+=1
    M[a], M[b] = M[b], M[a]
    
def call_fonction_de_tri(fonction_de_tri):
    global is_next_list_pressed, nb_swaps, is_list_sorted
    if is_list_sorted:
        return
    is_next_list_pressed = False
    for button in left_frame.winfo_children():
        button.config(state='disabled')
    nb_swaps = 0
    fonction_de_tri(L[:], 0, NB_BARRES)
    is_list_sorted = False
    progress_bar.config(maximum=nb_swaps)
    progress_bar['value'] = 0
    nb_swaps = 0
    fonction_de_tri(L, 0, NB_BARRES, swap=swap)
    for button in left_frame.winfo_children():
        button.config(state='normal')
    


def gestion_progress_bar():
    if checkvar.get() == 1:
        progress_bar.place(anchor=N, relx=0.5, y=5, relwidth=0.5, height=10)
        label.place(anchor=NW, relx=0.76, y=0)
    else:
        progress_bar.place_forget()
        label.place_forget()


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
    elif speed == 10:
        speed = 25
    else :
        speed = 1
    speed_button.config(text=f"Speed X{speed}")
    

def selection_sort(*args, swap=compte_swaps):
    global is_next_list_pressed, is_list_sorted
    for i in range (NB_BARRES):
        if is_next_list_pressed:
            is_next_list_pressed = False
            return 
        m=i
        for k in range (i, NB_BARRES):
            if L[k]<=L[m]:
                m=k
        swap(i,m)
    is_list_sorted = True
    


def bubble_sort(L, *args, swap=swap_and_count):
    global is_next_list_pressed, is_list_sorted
    while not is_list_sorted:
        for i in range (NB_BARRES-1): 
            if is_next_list_pressed:
                is_next_list_pressed = False
                return 
            if L[i]>L[i+1]:
                swap(i, i+1, L)
        for i in range (NB_BARRES-1):
            if L[i]>L[i+1]:
                break
            if i==NB_BARRES-2 and L[i]<=L[i+1]:
                is_list_sorted=True


def cocktail(L, *args, swap=swap_and_count):
    global is_next_list_pressed, is_list_sorted
    while not is_list_sorted:
        for i in range (0, NB_BARRES-1): 
            if is_next_list_pressed:
                is_next_list_pressed = False
                return 
            if L[i]>L[i+1]:
                swap(i, i+1, L)
        for k in range (NB_BARRES-1, 0, -1): 
            if is_next_list_pressed:
                is_next_list_pressed = False
                return 
            if L[k]<L[k-1]:
                swap(k, k-1, L)
        for i in range (NB_BARRES-1):
            if L[i]>L[i+1]:
                break
            if i==NB_BARRES-2 and L[i]<=L[i+1]:
                is_list_sorted=True


def merge(L, a, middle, b, swap=swap_and_count):
    global is_next_list_pressed, is_list_sorted
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
    for i in range(b-a):
        if is_next_list_pressed:
            is_next_list_pressed = False
            return True
        mon_index = L.index(P[i], a+i, b)
        swap(a+i, mon_index, L)
    is_list_sorted = True

    
def merge_sort(L, a, b, swap=swap_and_count):
    global is_next_list_pressed, is_list_sorted
    if is_next_list_pressed:
        is_next_list_pressed = False
        return True 
    if b-a ==2:
        if L[a] > L[a+1]:
            swap(a, a+1, L)
            return
    elif b-a == 1:
        return
    middle = (a+b)//2
    if merge_sort(L, a, middle, swap):
        return True
    if merge_sort(L, middle, b, swap):
        return True
    if merge(L, a , middle, b, swap):
        return True
    is_list_sorted = True


def insertion(L, *args, swap=swap_and_count):
    global is_list_sorted
    for i in range(NB_BARRES):
        for k in range(i-1, -1, -1):
            if L[i]<L[k]:
                swap(i, k, L)
                i=k
    is_list_sorted = True

def swap(a, b, *args):
    global nb_swaps
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
    progress_bar['value'] += 1
    nb_swaps+=1
    time_left.config(text=f"Time left : {round(0.2*1.1/speed*(progress_bar.cget('maximum')-nb_swaps),1)}s")
    label.config(text=f"{int(nb_swaps*100/progress_bar.cget('maximum'))}%") 
    window.update()
    window.update_idletasks()

NB_BARRES = 50
POSITION_BARRES = 320
HAUTEUR_BARRES = 275


x='Helvetica 12'

window = Window(scaling=2, themename='superhero')
speed = 1
is_next_list_pressed = False
is_list_sorted = False
nb_swaps = 0   

window.geometry(f"{15*NB_BARRES+35}x650")
window.title("Sorting Algorithms")

canvas = Canvas(window, bg="#8C8C8C", highlightthickness=0)
canvas.place(anchor=NW, relx=0.0, rely=0.0, relheight=0.5, relwidth=1.0)

progress_bar = Progressbar(window, bootstyle="success-striped")
progress_bar.place(anchor=N, relx=0.5, y=5, relwidth=0.5, height=10)

label = Label(window, bootstyle="success", font=("Helvetica 12 bold"), text="0%")
label.place(anchor=NW, relx=0.76, y=0)

frame = Frame(window)
frame.place(anchor=NW, relx=0.0, rely=0.5, relheight=0.5, relwidth=1.0)

left_frame = Frame(frame)
left_frame.pack(side="left",expand=True, fill="both")
left_frame.pack_propagate(0)

right_frame = Frame(frame)
right_frame.pack(side="left",expand=True, fill="both")
right_frame.pack_propagate(0)

option_frame = Frame(frame)
option_frame.pack(side="left",expand=True, fill="both")
option_frame.pack_propagate(0)

selection_sort_button = Button(left_frame, text="Tri par s\u00E9lection", takefocus=False,
                               command=lambda : call_fonction_de_tri(selection_sort))
selection_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

merge_sort_button = Button(left_frame, text="Tri Fusion", takefocus=False,command=lambda : call_fonction_de_tri(merge_sort))
merge_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

bubble_sort_button = Button(left_frame, text="Tri Bulle", takefocus=False,command=lambda : call_fonction_de_tri(bubble_sort))
bubble_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

cocktail_sort_button = Button(left_frame, text="Tri Cocktail", takefocus=False,command=lambda : call_fonction_de_tri(cocktail))
cocktail_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

insertion_sort_button = Button(left_frame, text="Tri par insertion", takefocus=False,command=lambda : call_fonction_de_tri(insertion))
insertion_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

new_list_button = Button(right_frame, text="Nouvelle liste", takefocus=False,command=new_list)
new_list_button.pack(side=TOP, fill='x', padx=5, pady=5)

speed_button = Button(right_frame, text="Speed X1", takefocus=False,command=change_speed)
speed_button.pack(fill="x", padx=5, pady=5)


checkvar = IntVar()
checkbutton = Checkbutton(option_frame,text="Progress Bar", command=gestion_progress_bar, variable=checkvar, style="success.Roundtoggle.Toolbutton")
checkvar.set(1)
checkbutton.pack(fill="x", padx=5, pady=5)

time_left = Label(option_frame, text="Time left :")
time_left.pack(fill="x", padx=5, pady=5)

L = [randint(20, HAUTEUR_BARRES) for _ in range(NB_BARRES)]
L_rect = []
for i in range(NB_BARRES):
    L_rect.append(canvas.create_rectangle(20+i*15, POSITION_BARRES-L[i], 30+i*15, POSITION_BARRES, fill='orange'))

window.mainloop()