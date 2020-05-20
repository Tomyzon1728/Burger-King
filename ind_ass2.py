# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:13:14 2020

@author: Ajayi Raymond T
"""

from tkinter import *
import os

def MainScreen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('MENU')
    Label(text = 'Burger King',bg = 'orange',width= '300',height= '2',font = ('calibri',13)).pack()
    Label( text = '').pack()
    entry =Entry(screen, text="0",width = 32,font = ('serif 15', 20, 'bold'), bd =3, insertwidth =20, bg = 'powder blue', justify = 'right')
    entry.pack()
    Label( text = '').pack()
    Button(text = 'Select Meat Choice with:\n Lettuuce\n Cucumber\n Onion',height = '5', fg='#F08080', bg='#FFFACD', width = '30', command=selector1).pack()
    Label( text = '').pack()
    Button(text = 'Select Meat Choice (ORDINARY)',height = '5', fg='#F08080', bg='#FFFACD', width = '30', command = selector1).pack()
    Label( text = '').pack()
    Button(text = 'Select Sauce',height = '5', fg='#F08080', bg='#FFFACD', width = '30', command = sauce).pack()
    Label( text = '').pack()
    Button(text = 'Ad-ons',height = '5', fg='#F08080', bg='#FFFACD', width = '30', command = ad).pack()
    Label( text = '').pack()
    
     
    screen.mainloop()
    
def price(values):
    global entry
    entry.insert(END,values)
    
def clear():
    entry.delete(0, END)
    #s_length = len(entry.get())
    #entry.insert(s_length,display)
    return
    
    
def selector1():
    global screen1
    global entry
    global clear
    screen1 = Toplevel(screen)
    screen1.title('STYLE')
    screen1.geometry('300x250')
    entry =Entry(screen1, text="0",width = 32,font = ('serif 15', 20, 'bold'), bd =3, insertwidth =20, bg = 'powder blue', justify = 'right')
    entry.pack()
    Button(screen1,text = 'Rare',height = '2', fg='#F08080', bg='#FFFACD', width = '30', command=lambda:[price("RM3.00"),selector2]).pack()
    Button(screen1,text = 'Medium',height = '2', fg='#F08080', bg='#FFFACD', width = '30', command = lambda:[price("RM1.00"),selector2]).pack() 
    Button(screen1,text = 'Full Cooked',height = '2', fg='#F08080', bg='#FFFACD', width = '30', command = lambda:[price("RM1.50"),selector2]).pack() 
    Button(screen1,text = 'CLR SCR',height = '2', fg='#F08080', bg='#FFFACD', width = '30',command=lambda:clear()).pack()
def selector2():
    global screen2
    global entry
    global clear
    screen2 = Toplevel(screen1)
    screen2.title('PLACE ORDER')
    screen2.geometry('300x250')
    entry =Entry(screen2, text="0",width = 32,font = ('serif 15', 20, 'bold'), bd =3, insertwidth =20, bg = 'powder blue', justify = 'right')
    entry.pack()
    Button(screen2,text = 'Beef',height = '2', fg='#F08080', bg='#FFFACD', width = '30',command=lambda:price("RM3.00")).pack()
    Button(screen2,text = 'Chicken',height = '2', fg='#F08080', bg='#FFFACD', width = '30',command=lambda:price("RM2.50")).pack() 
    Button(screen2,text = 'Pork',height = '2', fg='#F08080', bg='#FFFACD', width = '30',command=lambda:price("RM2.00")).pack()   
    Button(screen2,text = 'CLR SCR',height = '2', fg='#F08080', bg='#FFFACD', width = '30',command=lambda:clear()).pack()      
def sauce():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title('SAUCE')
    screen3.geometry('300x250')
    Button(screen3,text = 'Chilli',height = '2', fg='#F08080', bg='#FFFACD', width = '30').pack()
    Button(screen3,text = 'Tomato',height = '2', fg='#F08080', bg='#FFFACD', width = '30').pack() 
    Button(screen3,text = 'Mustard',height = '2', fg='#F08080', bg='#FFFACD', width = '30').pack() 
           
def ad():
    global screen4
    global entry
    global clear
    screen4 = Toplevel(screen)
    screen4.title('Freebies')
    screen4.geometry('300x250')
    entry =Entry(screen4, text="0",width = 32,font = ('serif 15', 20, 'bold'), bd =3, insertwidth =20, bg = 'powder blue', justify = 'right')
    entry.pack()
    Button(screen4,text = 'Muffin',height = '2', fg='#F08080', bg='#FFFACD', width = '30').pack()
    Button(screen4,text = 'Cookies',height = '2', fg='#F08080', bg='#FFFACD', width = '30',command=lambda:price("")).pack() 
    Button(screen4,text = 'Drinks',height = '2', fg='#F08080', bg='#FFFACD', width = '30',command=lambda:price("RM2.50")).pack() 
    Button(screen4,text = 'CLR SCR',height = '2', fg='#F08080', bg='#FFFACD', width = '30',command=lambda:clear()).pack()
   
    
MainScreen()