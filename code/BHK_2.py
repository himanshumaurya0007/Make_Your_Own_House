from tkinter import *

from PIL import ImageTk



def nextPagetoConstruct():
    plans_page.destroy()

def nextPageto2BHK1():
    plans_page.destroy()
    cd_plans_window = Tk()
    cd_plans_window.geometry('1366x768')
    # heading
    def nextPagetoConstruct():
        cd_plans_window.destroy()
        import BHK_1
    # functions
    cd_bg_image = ImageTk.PhotoImage(
        file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Construction_Plans\\2BHK1.jpg')
    cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
    cd_bg_label.place(x=0, y=0)
    btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=nextPagetoConstruct)
    btnback.place(x=1200, y=10)
    cd_plans_window.mainloop()

def nextPageto2BHK2():
    plans_page.destroy()
    cd_plans_window = Tk()
    cd_plans_window.geometry('1366x768')
    def nextPagetoConstruct():
        cd_plans_window.destroy()
        import BHK_1
    # heading

    # functions
    cd_bg_image = ImageTk.PhotoImage(
        file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Construction_Plans\\2BHK2.jpg')
    cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
    cd_bg_label.place(x=0, y=0)
    btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=nextPagetoConstruct)
    btnback.place(x=1200, y=10)
    cd_plans_window.mainloop()

def nextPageto2BHK3():
    plans_page.destroy()
    cd_plans_window = Tk()
    cd_plans_window.geometry('1366x768')
    # heading
    def nextPagetoConstruct():
        cd_plans_window.destroy()
        import BHK_1

    # functions
    cd_bg_image = ImageTk.PhotoImage(
        file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Construction_Plans\\2BHK3.jpg')
    cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
    cd_bg_label.place(x=0, y=0)
    btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=nextPagetoConstruct)
    btnback.place(x=1200, y=10)
    cd_plans_window.mainloop()

def nextPageto2BHK4():
    plans_page.destroy()
    cd_plans_window = Tk()
    cd_plans_window.geometry('1366x768')
    # heading
    def nextPagetoConstruct():
        cd_plans_window.destroy()
        import BHK_1

    # functions
    cd_bg_image = ImageTk.PhotoImage(
        file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Construction_Plans\\2BHK4.jpg')
    cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
    cd_bg_label.place(x=0, y=0)
    btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=nextPagetoConstruct)
    btnback.place(x=1200, y=10)
    cd_plans_window.mainloop()

def nextPageto2BHK5():
    plans_page.destroy()
    cd_plans_window = Tk()
    cd_plans_window.geometry('1366x768')
    # heading
    def nextPagetoConstruct():
        cd_plans_window.destroy()
        import BHK_1

    # functions
    cd_bg_image = ImageTk.PhotoImage(
        file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Construction_Plans\\2BHK5.jpg')
    cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
    cd_bg_label.place(x=0, y=0)
    btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=nextPagetoConstruct)
    btnback.place(x=1200, y=10)
    cd_plans_window.mainloop()




# Create the Tkinter plans_page and run the application
plans_page = Tk()
plans_page.geometry('1366x768')
plans_page.title("BHK 2")
# heading
cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Contruction_Plans_Page.png')
cd_bg_label = Label(plans_page, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# functions

# main code - e.g. buttons, etc
btn = Button(plans_page, text='Plan A', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK1)
btn.place(x=900, y=180)
btn = Button(plans_page, text='Plan B', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK2)
btn.place(x=900, y=290)
btn = Button(plans_page, text='Plan C', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK3)
btn.place(x=900, y=400)
btn = Button(plans_page, text='Plan D', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK4)
btn.place(x=900, y=510)
btn = Button(plans_page, text='Plan E', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command= nextPageto2BHK5)
btn.place(x=900, y=620)

btnback = Button(plans_page, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoConstruct)
btnback.place(x=1200, y=10)

plans_page.mainloop()
