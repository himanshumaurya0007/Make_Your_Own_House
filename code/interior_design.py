from tkinter import *
from PIL import ImageTk
def nextPagetoConstruct():
    cd_plans_window.destroy()
    import construction


# Create the Tkinter cd_plans_window and run the application
cd_plans_window = Tk()
cd_plans_window.geometry('1366x768')
cd_plans_window.title("Interior Design")
# heading

# functions
def nextPagetoHall():
    cd_plans_window.destroy()
    import Hall_Designs
def nextPagetoKitchen():
    cd_plans_window.destroy()
    import Kitchen_Designs

def nextPagetoBathroom():
    cd_plans_window.destroy()
    import Bathroom_Designs

def nextPagetoBedroom():
    cd_plans_window.destroy()
    import Bedroom_Designs

def nextPagetoNewPlans():
    cd_plans_window.destroy()
    import New_Ideas

cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Interior_Page.png')
cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# main code - e.g. buttons, etc
btn = Button(cd_plans_window, text='Hall', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPagetoHall)
btn.place(x=950, y=280)
btn = Button(cd_plans_window, text='Kitchen', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command=nextPagetoKitchen)
btn.place(x=950, y=390)
btn = Button(cd_plans_window, text='Bathroom', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command=nextPagetoBathroom)
btn.place(x=950, y=500)
btn = Button(cd_plans_window, text='Bedroom', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command=nextPagetoBedroom)
btn.place(x=950, y=610)
btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoConstruct)
btnback.place(x=1200, y=10)

btnback = Button(cd_plans_window, text='New Plans', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoNewPlans)
btnback.place(x=700, y=10)

cd_plans_window.mainloop()