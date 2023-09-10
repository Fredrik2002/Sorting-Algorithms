from ttkbootstrap.widgets import Progressbar, Label, Checkbutton
from ttkbootstrap import Window, Canvas, Button, Frame
from tkinter import N, NW, TOP, IntVar
from utils import *
from random import randint
import time

class App(Window):
    def __init__(self):
        super().__init__(scaling=2, themename='superhero')

        self.geometry(f"{15*NB_BARRES+35}x650")
        self.title("Sorting Algorithms")

        self.canvas = Canvas(self, bg="#8C8C8C", highlightthickness=0)
        self.canvas.place(anchor=NW, relx=0.0, rely=0.0, relheight=0.5, relwidth=1.0)

        self.progress_bar = Progressbar(self, bootstyle="success-striped")
        self.progress_bar.place(anchor=N, relx=0.5, y=5, relwidth=0.5, height=10)

        self.label = Label(self, bootstyle="success", font=("Helvetica 12 bold"), text="0%")
        self.label.place(anchor=NW, relx=0.76, y=0)

        self.frame = Frame(self)
        self.frame.place(anchor=NW, relx=0.0, rely=0.5, relheight=0.5, relwidth=1.0)

        self.left_frame = Frame(self.frame)
        self.left_frame.pack(side="left",expand=True, fill="both")
        self.left_frame.pack_propagate(0)

        self.right_frame = Frame(self.frame)
        self.right_frame.pack(side="left",expand=True, fill="both")
        self.right_frame.pack_propagate(0)

        self.option_frame = Frame(self.frame)
        self.option_frame.pack(side="left",expand=True, fill="both")
        self.option_frame.pack_propagate(0)

        self.selection_sort_button = Button(self.left_frame, text="Tri par s\u00E9lection", takefocus=False,
                                    command=lambda : self.call_fonction_de_tri(selection_sort))
        self.selection_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

        self.merge_sort_button = Button(self.left_frame, text="Tri Fusion", takefocus=False,command=lambda : self.call_fonction_de_tri(merge_sort))
        self.merge_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

        self.bubble_sort_button = Button(self.left_frame, text="Tri Bulle", takefocus=False,command=lambda : self.call_fonction_de_tri(bubble_sort))
        self.bubble_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

        self.cocktail_sort_button = Button(self.left_frame, text="Tri Cocktail", takefocus=False,command=lambda : self.call_fonction_de_tri(cocktail))
        self.cocktail_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

        self.insertion_sort_button = Button(self.left_frame, text="Tri par insertion", takefocus=False,command=lambda : self.call_fonction_de_tri(insertion))
        self.insertion_sort_button.pack(side=TOP, fill="x", padx=5, pady=5)

        self.new_list_button = Button(self.right_frame, text="Nouvelle liste", takefocus=False,command=self.new_list)
        self.new_list_button.pack(side=TOP, fill='x', padx=5, pady=5)

        self.speed_button = Button(self.right_frame, text="Speed X1", takefocus=False,command=self.change_speed)
        self.speed_button.pack(fill="x", padx=5, pady=5)


        self.checkvar = IntVar()
        self.checkbutton = Checkbutton(self.option_frame,text="Progress Bar", command=self.gestion_progress_bar, variable=self.checkvar, style="success.Roundtoggle.Toolbutton")
        self.checkvar.set(1)
        self.checkbutton.pack(fill="x", padx=5, pady=5)

        self.time_left = Label(self.option_frame, text="Time left :")
        self.time_left.pack(fill="x", padx=5, pady=5)

        self.L = [randint(20, HAUTEUR_BARRES) for _ in range(NB_BARRES)]
        self.L_rect = []
        for i in range(NB_BARRES):
           self.L_rect.append(self.canvas.create_rectangle(20+i*15, POSITION_BARRES-self.L[i], 30+i*15, POSITION_BARRES, fill='orange'))
        self.mainloop()

    def new_list(self):
        global L, is_next_list_pressed, is_list_sorted
        is_next_list_pressed = True
        is_list_sorted = False
        self.progress_bar['value'] = 0
        self.label.config(text="0%")
        self.time_left.config(text = "Time left : ")
        L = [randint(20, HAUTEUR_BARRES) for _ in range(NB_BARRES)]
        for i in range(NB_BARRES):
            self.canvas.coords(self.L_rect[i], 20+i*15, POSITION_BARRES-self.L[i], 30+i*15, POSITION_BARRES)
        for button in self.left_frame.winfo_children():
            button.config(state='normal')

    
    def call_fonction_de_tri(self, fonction_de_tri):
        global is_next_list_pressed, nb_swaps, is_list_sorted
        if is_list_sorted:
            return
        is_next_list_pressed = False
        for button in self.left_frame.winfo_children():
            button.config(state='disabled')
        nb_swaps = 0
        fonction_de_tri(self.L[:], 0, NB_BARRES)
        is_list_sorted = False
        self.progress_bar.config(maximum=nb_swaps)
        self.progress_bar['value'] = 0
        nb_swaps = 0
        fonction_de_tri(self.L, 0, NB_BARRES, swap=self.swap)
        for button in self.left_frame.winfo_children():
            button.config(state='normal')
    


    def gestion_progress_bar(self):
        if self.checkvar.get() == 1:
            self.progress_bar.place(anchor=N, relx=0.5, y=5, relwidth=0.5, height=10)
            self.label.place(anchor=NW, relx=0.76, y=0)
        else:
            self.progress_bar.place_forget()
            self.label.place_forget()


    def change_speed(self):
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
        self.speed_button.config(text=f"Speed X{speed}")


    def swap(self, a, b, *args):
        global nb_swaps
        if a<0:
            a+=NB_BARRES
        if b<0:
            b+=NB_BARRES
        assert a>=0 and b>=0, "Wrong a or b"
        m, M = min(a, b), max(a, b)
        d= M-m
        self.canvas.move(self.L_rect[m],d*15, 0)
        self.canvas.move(self.L_rect[M],-d*15, 0)
        self.L[a], self.L[b] = self.L[b], self.L[a]
        self.L_rect[a], self.L_rect[b] = self.L_rect[b], self.L_rect[a]
        time.sleep(0.2/speed)
        self.progress_bar['value'] += 1
        nb_swaps+=1
        self.time_left.config(text=f"Time left : {round(0.2*1.1/speed*(self.progress_bar.cget('maximum')-nb_swaps),1)}s")
        self.label.config(text=f"{int(nb_swaps*100/self.progress_bar.cget('maximum'))}%") 
        self.update()
        self.update_idletasks()

App()
        