from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

def calender():
    pg.click(x=26, y=21)
def google():
    webbrowser.open('https://www.google.com')
    
GUI = Tk()
GUI.title('โปรแกรมสั่งกดปฎิทิน')
GUI.geometry('500x500')


B1 = Button(GUI, text = 'Calender1', command=calender)
B1.pack()

B2 = ttk.Button(GUI, text = 'Calendet2', command=google)
B2.pack()

B3 = ttk.Button(GUI, text = 'Google', command=google)
B3.pack()
GUI = mainloop()