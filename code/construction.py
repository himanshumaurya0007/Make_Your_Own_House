from tkinter import *
from PIL import ImageTk
def nextPagetoConstruct():
    cd_plans_window.destroy()
    import construction
def nextPagetoMaterials():
    cd_plans_window.destroy()
    import materials

# Create the Tkinter cd_plans_window and run the application
cd_plans_window = Tk()
cd_plans_window.geometry('1366x768')
cd_plans_window.title("Construction Page")
# heading

# functions
def nextPageto1BHK():
    cd_plans_window.destroy()
    import BHK_1
def nextPageto2BHK():
    cd_plans_window.destroy()
    import BHK_2

def nextPageto3BHK():
    cd_plans_window.destroy()
    import BHK_3

cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Construction_Page.png')
cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# main code - e.g. buttons, etc
btn = Button(cd_plans_window, text='1 BHK', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto1BHK)
btn.place(x=1050, y=280)
btn = Button(cd_plans_window, text='2 BHK', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK)
btn.place(x=1050, y=390)
btn = Button(cd_plans_window, text='3 BHK', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto3BHK)
btn.place(x=1050, y=500)
btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoConstruct)
btnback.place(x=1200, y=10)
btnback = Button(cd_plans_window, text='Materials', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoMaterials)
btnback.place(x=100, y=250)

cd_plans_window.mainloop()
