import threading

NB_BARRES = 50
POSITION_BARRES = 320
HAUTEUR_BARRES = 275

speed = 1
is_next_list_pressed = False
nb_swaps = 0
event = threading.Event()
event.set()


def swap_and_count(a, b, M):
    global nb_swaps
    nb_swaps+=1
    M[a], M[b] = M[b], M[a]
    


def selection_sort(L, *args, swap=swap_and_count):
    global is_next_list_pressed
    for i in range (NB_BARRES):
        event.wait()
        if is_next_list_pressed:
            is_next_list_pressed = False
            return 
        m=i
        for k in range (i, NB_BARRES):
            if L[k]<=L[m]:
                m=k
        if is_next_list_pressed:
            is_next_list_pressed = False
        swap(i,m, L)
    


def bubble_sort(L, *args, swap=swap_and_count):
    global is_next_list_pressed
    is_list_sorted = False
    while not is_list_sorted:
        for i in range (NB_BARRES-1):
            event.wait() 
            if is_next_list_pressed:
                is_next_list_pressed = False
                return 
            if L[i]>L[i+1]:
                swap(i, i+1, L)
        for i in range (NB_BARRES-1):
            event.wait()
            if L[i]>L[i+1]:
                break
            if i==NB_BARRES-2 and L[i]<=L[i+1]:
                is_list_sorted=True


def cocktail(L, *args, swap=swap_and_count):
    global is_next_list_pressed
    is_list_sorted = False
    while not is_list_sorted:
        for i in range (0, NB_BARRES-1):
            event.wait() 
            if is_next_list_pressed:
                is_next_list_pressed = False
                return 
            if L[i]>L[i+1]:
                swap(i, i+1, L)
        for k in range (NB_BARRES-1, 0, -1):
            event.wait() 
            if is_next_list_pressed:
                is_next_list_pressed = False
                return 
            if L[k]<L[k-1]:
                swap(k, k-1, L)
        for i in range (NB_BARRES-1):
            event.wait()
            if L[i]>L[i+1]:
                break
            if i==NB_BARRES-2 and L[i]<=L[i+1]:
                is_list_sorted=True


def merge(L, a, middle, b, swap=swap_and_count):
    global is_next_list_pressed
    left, right = L[a:middle], L[middle:b] 
    P = []
    while len(left)!=0 and len(right)!=0:
        event.wait()
        if left[0] < right[0]:
            P.append(left.pop(0))
        else:
            P.append(right.pop(0))
    if len(left) == 0 :
        P = P + right
    else:
        P = P + left
    for i in range(b-a):
        event.wait()
        if is_next_list_pressed:
            is_next_list_pressed = False
            return True
        mon_index = L.index(P[i], a+i, b)
        swap(a+i, mon_index, L)

    
def merge_sort(L, a, b, swap=swap_and_count):
    global is_next_list_pressed
    event.wait()
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

def insertion(L, *args, swap=swap_and_count):
    global is_next_list_pressed
    for i in range(NB_BARRES):
        for k in range(i-1, -1, -1):
            if is_next_list_pressed:
                is_next_list_pressed = False
                return
            if L[i]<L[k]:
                swap(i, k, L)
                i=k