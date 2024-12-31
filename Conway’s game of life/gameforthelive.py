from tkinter import *


# create the grid
def damier():
    ligne_vert()
    ligne_hor()

# vertical line
def ligne_vert():
    c_x = 0
    while c_x != width:
        can1.create_line(c_x, 0, c_x, height, width=1, fill='black')
        c_x += c

# horizontal line
def ligne_hor():
    c_y = 0
    while c_y != height:
        can1.create_line(0, c_y, width, c_y, width=1, fill='black')
        c_y += c

# left click
def click_gauche(
        event):
    x = event.x - (event.x % c)
    y = event.y - (event.y % c)
    can1.create_rectangle(x, y, x + c, y + c, fill='black')
    dico_case[x, y] = 1

# right click
def click_droit(event):
    x = event.x - (event.x % c)
    y = event.y - (event.y % c)
    can1.create_rectangle(x, y, x + c, y + c, fill='white')
    dico_case[x, y] = 0

# change the speed of the game
def change_vit(event):
    global vitesse
    vitesse = int(eval(entree.get()))
    print(vitesse)

# create the canon
def canon():
    dico_case[0 * c, 5 * c] = 1
    dico_case[0 * c, 6 * c] = 1
    dico_case[1 * c, 5 * c] = 1
    dico_case[1 * c, 6 * c] = 1
    dico_case[10 * c, 5 * c] = 1
    dico_case[10 * c, 6 * c] = 1
    dico_case[10 * c, 7 * c] = 1
    dico_case[11 * c, 4 * c] = 1
    dico_case[11 * c, 8 * c] = 1
    dico_case[12 * c, 3 * c] = 1
    dico_case[12 * c, 9 * c] = 1
    dico_case[13 * c, 3 * c] = 1
    dico_case[13 * c, 9 * c] = 1
    dico_case[14 * c, 6 * c] = 1
    dico_case[15 * c, 4 * c] = 1
    dico_case[15 * c, 8 * c] = 1
    dico_case[16 * c, 5 * c] = 1
    dico_case[16 * c, 6 * c] = 1
    dico_case[16 * c, 7 * c] = 1
root = Tk()

# create the window
root.title('Jeu de la vie')
width = 700
height = 700
c = 10
vitesse = 100
can1 = Canvas(root, width=width, height=height, bg='white')
can1.pack(side=LEFT)
dico_case = {}

# create the grid
damier()
can1.bind('<Button-1>', click_gauche)
can1.bind('<Button-3>', click_droit)
entree = Entry(root)
entree.pack()
entree.bind('<Return>', change_vit)

# create the canon
canon()
root.mainloop()


