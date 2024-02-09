from tkinter import *
from PIL import ImageTk
from tkvideo import  tkvideo

def nextPagetoConstruct():
    plans_page.destroy()
    import interior_design


def nextPageto2BHK1():
    plans_page.destroy()
    cd_plans_window = Tk()
    cd_plans_window.geometry('500x500')
    # heading
    def nextPagetoConstruct():
        cd_plans_window.destroy()
        import Hall_Designs
    # functions
    cd_bg_image = ImageTk.PhotoImage(
        file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\360 QR\\Bathroom_1 360.png')
    cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
    cd_bg_label.place(x=140, y=140)
    btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=nextPagetoConstruct)
    btnback.place(x=350, y=10)
    cd_plans_window.mainloop()

def nextPageto2BHK2():
    plans_page.destroy()
    cd_plans_window = Tk()
    cd_plans_window.geometry('500x500')

    # heading
    def nextPagetoConstruct():
        cd_plans_window.destroy()
        import Hall_Designs

    # functions
    cd_bg_image = ImageTk.PhotoImage(
        file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\360 QR\\Bedroom_2.png')
    cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
    cd_bg_label.place(x=140, y=140)
    btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=nextPagetoConstruct)
    btnback.place(x=350, y=10)
    cd_plans_window.mainloop()

def nextPageto2BHK3():
    plans_page.destroy()
    cd_plans_window = Tk()
    cd_plans_window.geometry('500x500')

    # heading
    def nextPagetoConstruct():
        cd_plans_window.destroy()
        import Hall_Designs

    # functions
    cd_bg_image = ImageTk.PhotoImage(
        file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\360 QR\\Bedroom_3.png')
    cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
    cd_bg_label.place(x=140, y=140)
    btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=nextPagetoConstruct)
    btnback.place(x=350, y=10)
    cd_plans_window.mainloop()

def nextPageto2BHK4():
    plans_page.destroy()
    import Hall_4

def nextPageto2BHK5():
    plans_page.destroy()
    import Hall_5
# Create the Tkinter plans_page and run the application
plans_page = Tk()
plans_page.geometry('1366x768')
plans_page.title("Bathroom Designs")
# heading
cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Interior_Plans_Page.png')
cd_bg_label = Label(plans_page, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# functions

# main code - e.g. buttons, etc
btn = Button(plans_page, text='Plan A', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK1)
btn.place(x=100, y=180)
btn = Button(plans_page, text='Plan B', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK2)
btn.place(x=100, y=290)
btn = Button(plans_page, text='Plan C', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK3)
btn.place(x=100, y=400)
btn = Button(plans_page, text='Plan D', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK4)
btn.place(x=100, y=510)
btn = Button(plans_page, text='Plan E', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK5)
btn.place(x=100, y=620)

btnback = Button(plans_page, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoConstruct)
btnback.place(x=1200, y=10)

plans_page.mainloop()
