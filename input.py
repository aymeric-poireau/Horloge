from tkinter import *
fenetre=Tk()

def caps(event):
    v.set(v.get().upper())

Label(fenetre, text="Regler l'alarme:").pack(side=LEFT)
v = StringVar()
w = Entry(fenetre, width=20, textvariable=v)
w.pack(side=LEFT)
w.bind("<KeyRelease>", caps)

mainloop()