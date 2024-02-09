# from tkinter import *
# from tkinter import ttk
# from PIL import ImageTk
# def nextPagetoConstruct():
#     cd_material_window.destroy()
#     import construction
#
#
#
# # Create the Tkinter home_page and run the application
# cd_material_window = Tk()
# cd_material_window.geometry('1366x768')
# cd_material_window.title("Materials")
# # heading
# cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Make Your Own House.png')
# cd_bg_label = Label(cd_material_window, image=cd_bg_image)
# cd_bg_label.place(x=0, y=0)
# # label to be construced
# lbl1 = Label(cd_material_window, text="Floors to be constructed", fg='red', font=("Helvetica", 26))
# lbl1.place(x=30, y=70)
# # combobox
# comboa = ttk.Combobox(state="readonly", values=["1", "2", "3", "4"], font=("Helvetica", 19))
# comboa.place(x=490, y=70)
#
# # label house space
# lbl3 = Label(cd_material_window, text="House Space", fg='red', font=("Helvetica", 26))
# lbl3.place(x=30, y=130)
# # combobox
# combo2 = ttk.Combobox()
# combo2 = ttk.Combobox(state="readonly", values=["1RK", "1BHK", "2BHK", "3BHK"], font=("Helvetica", 19))
# combo2.place(x=490, y=130)
# # 1a
# lbl1a = Label(cd_material_window, text="Concrete", fg='black', font=("Helvetica", 26))
# lbl1a.place(x=30, y=210)
# txtfld1a = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld1a.place(x=250, y=210, height=40, width=130)
# # 1b
# lbl1b = Label(cd_material_window, text="Brick", fg='black', font=("Helvetica", 26))
# lbl1b.place(x=30, y=290)
# txtfld1b = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld1b.place(x=250, y=290, height=40, width=130)
# # 1c
# lbl1c = Label(cd_material_window, text="Steel", fg='black', font=("Helvetica", 26))
# lbl1c.place(x=30, y=370)
# txtfld1c = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld1c.place(x=250, y=370, height=40, width=130)
# # 1d
# lbl1d = Label(cd_material_window, text="Glass", fg='black', font=("Helvetica", 26))
# lbl1d.place(x=30, y=450)
# txtfld1d = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld1d.place(x=250, y=450, height=40, width=130)
# # 2a
# lbl2a = Label(cd_material_window, text="Wood", fg='black', font=("Helvetica", 26))
# lbl2a.place(x=530, y=210)
# txtfld2a = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld2a.place(x=750, y=210, height=40, width=130)
# # 2b
# lbl2b = Label(cd_material_window, text="Tiles", fg='black', font=("Helvetica", 26))
# lbl2b.place(x=530, y=290)
# txtfld2b = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld2b.place(x=750, y=290, height=40, width=130)
# # 2c
# lbl2c = Label(cd_material_window, text="Cement", fg='black', font=("Helvetica", 26))
# lbl2c.place(x=530, y=370)
# txtfld2c = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld2c.place(x=750, y=370, height=40, width=130)
# # 2d
# lbl2d = Label(cd_material_window, text="Aggregate", fg='black', font=("Helvetica", 26))
# lbl2d.place(x=530, y=450)
# txtfld2d = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld2d.place(x=750, y=450, height=40, width=130)
#
# lbl3a = Label(cd_material_window, text="Cost(rs)", fg='black', font=("Helvetica", 26))
# lbl3a.place(x=750, y=560)
# txtfld3a = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
# txtfld3a.place(x=900, y=560, height=40, width=250)
#
#
# # creating button estimate
# btn1b = Button(cd_material_window, text='Estimate', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
#                activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
# btn1b.place(x=900, y=110)
#
# btnback = Button(cd_material_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
#                  activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
#                  command=nextPagetoConstruct)
# btnback.place(x=1200, y=650)
#
# cd_material_window.mainloop()




from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

def nextPagetoConstruct():
    material_page.destroy()
    import Home_Page


def calculate():
    floor = comboa.get()
    space = combo2.get()
    concrete = int(floor) * int(space) * 700 + 50
    txtfld1a.config(text="{} kg".format(concrete))
    brick = int(floor) * int(space) * 600 + 65
    txtfld1b.config(text="{} kg".format(brick))
    steel = int(floor) * int(space) * 1000 + 65
    txtfld1c.config(text="{} kg".format(steel))
    glass = int(floor) * int(space) * 100 + 5
    txtfld1d.config(text="{} kg".format(glass))
    wood = int(floor) * int(space) * 250 + 50
    txtfld2a.config(text="{} kg".format(wood))
    tiles = int(floor) * int(space) * 100
    txtfld2b.config(text="{} kg".format(tiles))
    stones = int(floor) * int(space) * 400 + 65
    txtfld2c.config(text="{} kg".format(stones))
    aagr = int(floor) * int(space) * 390 + 70
    txtfld2d.config(text="{} kg".format(aagr))
    cost = int(concrete) * 50 + int(brick) * 45 + int(steel) * 100 + int(glass) * 150 + int(wood) * 30 + int(
        tiles) * 200 + int(stones) * 40 + int(aagr) * 50
    txtfld3a.config(text="Rs {}".format(cost))


material_page = Tk()
material_page.geometry('1366x768')
material_page.title("Materials")
cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Price.png')
cd_bg_label = Label(material_page, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)

lbl1 = Label(material_page, text="Floors to be constructed", fg='black', font=("Helvetica", 26))
lbl1.place(x=30, y=70)
# combobox
options = ["1", "2", "3", "4"]
comboa = ttk.Combobox(state="readonly", values=options, font=("Helvetica", 19))
comboa.place(x=490, y=70)

# label house space
lbl3 = Label(material_page, text="House Space (in BHK)", fg='black', font=("Helvetica", 26))
lbl3.place(x=30, y=130)
# combobox
combo2 = ttk.Combobox()
options = ["1", "2", "3"]
combo2 = ttk.Combobox(state="readonly", values=options, font=("Helvetica", 19))
combo2.place(x=490, y=130)
# 1a
lbl1a = Label(material_page, text="Concrete", fg='black', font=("Helvetica", 26))
lbl1a.place(x=30, y=210)
txtfld1a = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld1a.place(x=250, y=210, height=40, width=130)
# 1b
lbl1b = Label(material_page, text="Brick", fg='black', font=("Helvetica", 26))
lbl1b.place(x=30, y=290)
txtfld1b = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld1b.place(x=250, y=290, height=40, width=130)
# 1c
lbl1c = Label(material_page, text="Steel", fg='black', font=("Helvetica", 26))
lbl1c.place(x=30, y=370)
txtfld1c = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld1c.place(x=250, y=370, height=40, width=130)
# 1d
lbl1d = Label(material_page, text="Glass", fg='black', font=("Helvetica", 26))
lbl1d.place(x=30, y=450)
txtfld1d = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld1d.place(x=250, y=450, height=40, width=130)
# 2a
lbl2a = Label(material_page, text="Wood", fg='black', font=("Helvetica", 26))
lbl2a.place(x=530, y=210)
txtfld2a = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld2a.place(x=750, y=210, height=40, width=130)
# 2b
lbl2b = Label(material_page, text="Tiles", fg='black', font=("Helvetica", 26))
lbl2b.place(x=530, y=290)
txtfld2b = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld2b.place(x=750, y=290, height=40, width=130)
# 2c
lbl2c = Label(material_page, text="Stones", fg='black', font=("Helvetica", 26))
lbl2c.place(x=530, y=370)
txtfld2c = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld2c.place(x=750, y=370, height=40, width=130)
# 2d
lbl2d = Label(material_page, text="Aggregate", fg='black', font=("Helvetica", 26))
lbl2d.place(x=530, y=450)
txtfld2d = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld2d.place(x=750, y=450, height=40, width=130)



# creating button estimate
btn1b = Button(material_page, text='Estimate Cost', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
               activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,
               command=calculate)
btn1b.place(x=250, y=560)

txtfld3a = Label(material_page, text="", fg='blue', font=("Helvetica", 26))
txtfld3a.place(x=570, y=560, height=40, width=250)

btnback = Button(material_page, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoConstruct)
btnback.place(x=00, y=0)

material_page.mainloop()
