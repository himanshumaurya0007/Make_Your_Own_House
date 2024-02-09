from tkinter import *
from PIL import ImageTk
# Create the Tkinter cd_home_window and run the application
cd_home_window = Tk()
cd_home_window.geometry('1366x768')
cd_home_window.title("Home Page")

cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Price.png')
cd_bg_label = Label(cd_home_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)



def next_page_to_construction():
    cd_home_window.destroy()
    import RoadEstimate


def next_page_to_interior_design():
    cd_home_window.destroy()
    import MaterialEstimate


# Home page label
cd_lbl = Label(cd_home_window, text="Home Page", fg='red', font=("Times New Roman", 31))
cd_lbl.place(x=560, y=50)



# Construction Button
btn = Button(cd_home_window, text='Material Estimate', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,
             command=next_page_to_construction)
btn.place(x=955, y=400)

# Interior design button
btn = Button(cd_home_window, text='Road Estimate', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,
             command=next_page_to_interior_design)
btn.place(x=955, y=500)

cd_home_window.mainloop()
