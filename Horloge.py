import time
from tkinter import Label, Tk 
import tkinter as tk
from tkinter import *
from time import strftime
import webbrowser
import input

w = Entry
fenetre = Tk()
fenetre.title("Hologe")
fenetre.geometry("365x190") 
fenetre.resizable(0,0)
text_font= ("roman", 47, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25
label = Label(fenetre, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)



def Heure():
   global time_live
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, Heure)


def Alarme():
# Creation de l'alarme
# Demandez à l'utilisateur de saisir l'heure de réveil désirée
      alarm_time = w

# Boucle jusqu'à ce que l'heure de réveil soit atteinte
      while True:
         if time_live == alarm_time:
            webbrowser.open("https://www.qwant.com/?client=brz-moz&t=videos&q=bip+alarme&o=0%3A4UBiIRdxqJY")
            break
Heure()
fenetre.mainloop()