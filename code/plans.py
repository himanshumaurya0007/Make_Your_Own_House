from tkinter import *
from PIL import ImageTk
def nextPagetoConstruct():
    cd_plans_window.destroy()
    import construction


# Create the Tkinter cd_plans_window and run the application
cd_plans_window = Tk()
cd_plans_window.geometry('1366x768')
cd_plans_window.title("Plans Page")
# heading

# functions
cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Contruction_Plans_Page.png')
cd_bg_label = Label(cd_plans_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# main code - e.g. buttons, etc
btn = Button(cd_plans_window, text='Plan A', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=180)
btn = Button(cd_plans_window, text='Plan B', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=290)
btn = Button(cd_plans_window, text='Plan C', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=400)
btn = Button(cd_plans_window, text='Plan D', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=510)
btn = Button(cd_plans_window, text='Plan E', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=620)

btnback = Button(cd_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoConstruct)
btnback.place(x=1200, y=10)

cd_plans_window.mainloop()
