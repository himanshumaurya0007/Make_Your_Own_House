from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

def nextPagetoConstruct():
    roadest_page.destroy()
    #import Construct

def calculate():
    thickness = comboa.get()
    lanes = combo2.get()
    length=txtfld.get()

    Loam = int(thickness) * int(lanes) * int(length) * 3100
    txtfld1a.config(text="{} kg".format(Loam))
    Gravel = int(thickness) * int(lanes) * int(length) * 1300
    txtfld1b.config(text="{} kg".format(Gravel))
    Rock = int(thickness) * int(lanes) * int(length) * 2400
    txtfld1c.config(text="{} kg".format(Rock))
    Tar = int(thickness) * int(lanes) * int(length) * 2100
    txtfld1d.config(text="{} kg".format(Tar))

    cost = (Loam * 6 + Gravel * 14 + Rock * 18 + Tar * 80 )/5
    txtfld3a.config(text="Rs {}".format(cost))




# Create the Tkinter home_page and run the application
roadest_page = Tk()
roadest_page.title("Road Making Price Estimator")
roadest_page.geometry('1366x768')
# heading
cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Price.png')
cd_bg_label = Label(roadest_page, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)

lbl1 = Label(roadest_page, text="Road Length", fg='red', font=("Helvetica", 26))
lbl1.place(x=30, y=30)
# combobox
txtfld = Entry(roadest_page, text=" In Kms  ", bd=5, font=("Helvetica", 28))
txtfld.place(x=490, y=30, height=40, width=300)


# label to be construced
lbl1 = Label(roadest_page, text="Road Thickness (In Inches)", fg='red', font=("Helvetica", 26))
lbl1.place(x=30, y=90)
# combobox
options = ["2", "3", "4"]
comboa = ttk.Combobox(state="readonly", values=options, font=("Helvetica", 19))
comboa.place(x=490, y=90)

# label house space
lbl3 = Label(roadest_page, text="Road Lanes", fg='red', font=("Helvetica", 26))
lbl3.place(x=30, y=150)
# combobox
combo2 = ttk.Combobox()
options = ["1", "2", "3"]
combo2 = ttk.Combobox(state="readonly", values=options, font=("Helvetica", 19))
combo2.place(x=490, y=150)
# 1a
lbl1a = Label(roadest_page, text="Loam", fg='black', font=("Helvetica", 26))
lbl1a.place(x=30, y=210)
txtfld1a = Label(roadest_page, text="", fg='blue', font=("Helvetica", 26))
txtfld1a.place(x=250, y=210, height=40, width=200)
# 1b
lbl1b = Label(roadest_page, text="Gravel", fg='black', font=("Helvetica", 26))
lbl1b.place(x=30, y=290)
txtfld1b = Label(roadest_page, text="", fg='blue', font=("Helvetica", 26))
txtfld1b.place(x=250, y=290, height=40, width=200)
# 1c
lbl1c = Label(roadest_page, text="Basalt", fg='black', font=("Helvetica", 26))
lbl1c.place(x=30, y=370)
txtfld1c = Label(roadest_page, text="", fg='blue', font=("Helvetica", 26))
txtfld1c.place(x=250, y=370, height=40, width=200)
# 1d
lbl1d = Label(roadest_page, text="Tar", fg='black', font=("Helvetica", 26))
lbl1d.place(x=30, y=450)
txtfld1d = Label(roadest_page, text="", fg='blue', font=("Helvetica", 26))
txtfld1d.place(x=250, y=450, height=40, width=200)


lbl3a = Label(roadest_page, text="Cost(rs)", fg='black', font=("Helvetica", 26))
lbl3a.place(x=750, y=560)
txtfld3a = Label(roadest_page, text="", fg='blue', font=("Helvetica", 26))
txtfld3a.place(x=900, y=560, height=40, width=250)

# creating button estimate
btn1b = Button(roadest_page, text='Estimate', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
               activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,
               command=calculate)
btn1b.place(x=900, y=110)

btnback = Button(roadest_page, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoConstruct)
btnback.place(x=1200, y=10)

roadest_page.mainloop()
