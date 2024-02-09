from tkinter import *
from PIL import ImageTk
def nextPagetoInterior():
    cd_interior_plans_window.destroy()
    import interior_design

cd_interior_plans_window = Tk()
cd_interior_plans_window.geometry('1366x768')
cd_interior_plans_window.title("Interior Plans")
# heading
cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Interior_Plans_Page.png')
cd_bg_label = Label(cd_interior_plans_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# functions

# main code - e.g. buttons, etc
btn = Button(cd_interior_plans_window, text="Plan A", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=180)
btn = Button(cd_interior_plans_window, text="Plan B", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=280)
btn = Button(cd_interior_plans_window, text="Plan C", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=380)
btn = Button(cd_interior_plans_window, text="Plan D", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=480)
btn = Button(cd_interior_plans_window, text="Plan E", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=580)

btnback = Button(cd_interior_plans_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoInterior)
btnback.place(x=1200, y=10)

cd_interior_plans_window.mainloop()

# Create the Tkinter cd_interior_plans_window and run the application
