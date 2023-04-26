from tkinter import *
from tkinter import ttk, messagebox
image = 'https://www.silpa-mag.com/wp-content/uploads/2022/06/ภาพปก-กิ้งก่า.jpg'

GUI = Tk()
GUI.title('ขายของ')
GUI.geometry('700x700')

bg = PhotoImage(file='supercar.png')

image = Label(GUI, image=bg)
image.pack()

head = Label(GUI, text='กรุณากรอกจำนวนปลา ', font=('None', 20)).pack()

v_fish = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_fish, font=(None, 20))
E1.pack()

def Cal():
    try:
        quantity = float(v_fish.get())
        calculate = quantity * 32.5
        messagebox.showinfo('ราคาทั้งหมด', f'ราคากิโลละ 32.5 ราคาปลาทั้งหมด {calculate:.2f} บาท')
        E1.focus()
    except:
        messagebox.showwarning('Error', 'กรอกตัวเลขเท่านั้น')
        E1.focus()
        
Button1 = ttk.Button(GUI, text='คำนวณ', command=Cal)
Button1.pack(ipadx=30, ipady=20)
GUI.mainloop()