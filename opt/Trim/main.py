#!/usr/bin/env python

from Tkinter import *
import trim
import sys

app = Tk()
app.title("Trim")
app.geometry("350x500")
app.resizable(width=0, height=0)

btn0 = PhotoImage(file="images/off.png")
btn1 = PhotoImage(file="images/on.png")

statusbar = Label(app, text="...", bd=1,relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

def onoffInicial():
    if trim.statusTrim() == 1:
        statusbar.config(text="Ativado")
        return btn1
    else:
        statusbar.config(text="Desativado")
        return btn0
       
def onOff(event):
    if trim.statusTrim() == 1:
        trimbtn.config(image=btn0)
        statusbar.config(text="Desativado")
        trim.changeTrim()
    else: 
        trimbtn.config(image=btn1)
        statusbar.config(text="Ativado")
        trim.changeTrim()
        
trimbtn = Label(app, image=onoffInicial())
trimbtn.bind("<Button-1>", onOff)
trimbtn.place(x=145,y=300)

log = Text(app, wrap=WORD, width=41, height= 7, bg="#c3c3c3", fg='#494949')
log.config()
filename='/opt/Trim/logs/trim.log'
with open(filename, 'r') as l:
    log.insert(INSERT, l.read())
log.place(x=8,y=350)
log.config(state=DISABLED)



logo = PhotoImage(file="images/logo.png")
l_logo = Label(app, image=logo)
l_logo.place(x=60, y=10)



app.mainloop()
