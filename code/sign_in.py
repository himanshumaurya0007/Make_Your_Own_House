from tkinter import *
from tkinter import messagebox
from resources.images_resources import *
from PIL import ImageTk
import subprocess
import pymysql


# -------------------------------------------------- MySQL DB Connection --------------------------------------------------
def sign_in_user():
    # if username_entry.get() == '' or password_entry.get() == '':
    #     messagebox.showerror('Error', 'All fields are required!')
    # else:
    #     try:
    #         con=pymysql.connect(host='localhost', user='root', password='Sanchit@2004')
    #         my_cursor = con.cursor()
    #     except():
    #         messagebox.showerror('Error', 'Database connectivity issue!\nPlease, try again')
    #         return
    #
    #     sql_query_to_fetch_data_from_created_db = 'USE sem4_py_mini_project'
    #     my_cursor.execute(sql_query_to_fetch_data_from_created_db)
    #     sql_query_to_search_username_and_password = 'SELECT * FROM user_sign_up WHERE username = %s and password = %s'
    #     my_cursor.execute(sql_query_to_search_username_and_password, (username_entry.get(), password_entry.get()))
    #
    #     row = my_cursor.fetchone()
    #     if row == None:
    #         messagebox.showerror('Error', 'Invalid username or password!')
    #     else:
    #         messagebox.showinfo('Welcome', 'Signed in successfully!')
    #         import home_page

    messagebox.showinfo('Welcome', 'Signed in successfully!')
    sign_in_window.destroy()
    import home_page

# -------------------------------------------------- linking of pages --------------------------------------------------
def forgot_page():
    sign_in_window.destroy()
    import forgot_password


def home_page():
    sign_in_window.destroy()
    subprocess.Popen(["python" , "home.py"])

def sign_up_page():
    sign_in_window.destroy()
    import sign_up


# -------------------------------------------------- Functionality --------------------------------------------------
def on_username_enter(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, END)


def on_password_enter(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, END)


def hide_password():
    open_eye.config(file='../resources/images_resources/close_eye.png')
    password_entry.config(show='*')
    open_eye_btn.config(command=show_password)


def show_password():
    open_eye.config(file='../images/resources/open_eye.png')
    password_entry.config(show='')
    open_eye_btn.config(command=hide_password)


# ---------------------------------------------------- GUI ----------------------------------------------------

# Create the Tkinter window and run the application
sign_in_window = Tk()
sign_in_window.title("Sign in")
sign_in_window.geometry('1366x768')
sign_in_window.iconbitmap('')
sign_in_window.resizable(False, False)

# set the window state to maximized
# sign_in_window.state('zoomed')

# Changing bb color to white
Label(sign_in_window, bg='white', height=1366, width=768).place(x=0, y=0)

cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Home_Page.png')
cd_bg_label = Label(sign_in_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# Heading Label
cd_head_lbl = Label(sign_in_window, text='USER LOGIN', font=('Times New Roman', 30, 'bold'), bg='white',
                    fg='firebrick1')
cd_head_lbl.place(x=593, y=120)

# Username input TextField
username_entry = Entry(sign_in_window, width=61, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
username_entry.place(x=261, y=240)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', on_username_enter)

# Username line for TextField
Frame(sign_in_window, width=860, height=2, bg='firebrick1').place(x=261, y=285)

# Password input TextField
password_entry = Entry(sign_in_window, width=61, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
password_entry.place(x=261, y=335)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', on_password_enter)

# Eye Btn - Hide and show
open_eye = PhotoImage(file="../resources/images_resources/open_eye.png")
open_eye_btn = Button(sign_in_window, image=open_eye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide_password)
open_eye_btn.place(x=1090, y=335)

# Password line for TextField
Frame(sign_in_window, width=860, height=2, bg='firebrick1').place(x=261, y=380)

# Forgot Password
cd_forget_pass_btn = Button(sign_in_window, text='Forgot Password?', bd=0, bg='white',
                            cursor='hand2', font=('Times New Roman', 13, 'bold'), fg='firebrick1', activebackground='white',
                            activeforeground='firebrick1', command=forgot_page)
cd_forget_pass_btn.place(x=980, y=390)

# Sign in Button
cd_login_btn = Button(sign_in_window, text='SIGNIN', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                      activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=50, height=1,
                      command=sign_in_user)
cd_login_btn.place(x=261, y=450)

# Sign up label
cd_sign_up_lbl = Label(sign_in_window, text="Don't have an account?", font=('Open sans', 15, 'bold'),
                       fg='firebrick1',
                       bg='white')
cd_sign_up_lbl.place(x=520, y=550)

# Sign up btn
cd_new_acc_btn = Button(sign_in_window, text='Create One Now', font=('Open Sans', 15, 'bold underline'), fg='blue',
                        bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0,
                        command=sign_up_page)
cd_new_acc_btn.place(x=750, y=545)

sign_in_window.mainloop()
