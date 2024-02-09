from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk
from tkinter import ttk

# -------------------------------------------------- MySQL DB Functions --------------------------------------------------
def clear_entities():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)



# -------------------------------------------------- MySQL DB Connection --------------------------------------------------
def connect_to_mysql_db():
    if name_entry.get() == '' or email_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '' :
        messagebox.showerror('Error', 'All fields are required!')
    else:
        try:
            #con = pymysql.connect(host='localhost', user='root', password='Sanchit@2004', database='sem4_py_mini_project')
            con = pymysql.connect(host='localhost', user='root', password='Sanchit@2004')
            my_cursor = con.cursor()
        except():
            messagebox.showerror('Error', 'Database connectivity issue!\nPlease, try again')
            return
        try:
            #sql_query_to_create_db11 = 'CREATE DATABASE sem4_py_mini_project'
            #my_cursor.execute(sql_query_to_create_db11)
            sql_query_to_select_created_db11 = 'USE sem4_py_mini_project'
            my_cursor.execute(sql_query_to_select_created_db11)
            #sql_query_to_create_table = 'CREATE TABLE user_sign_up(id INT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL, interio_type VARCHAR(50) NOT NULL, room_style VARCHAR(50) NOT NULL, Area VARCHAR(30) UNIQUE NOT NULL, Requirements VARCHAR(200) NOT NULL)'
            #my_cursor.execute(sql_query_to_create_table)
        except():
            my_cursor.execute('USE user_sign_up')

        sql_query_to_check_if_username_already_exists = 'SELECT * FROM user_sign_up WHERE username = %s'
        my_cursor.execute(sql_query_to_check_if_username_already_exists, (username_entry.get()))

        row = my_cursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exists\nPlease, try choosing another one.')
        else:
            sql_query_to_insert_data_into_table = 'INSERT INTO user_sign_up(name, email, username, password) VALUES(%s, %s, %s, %s)'
            my_cursor.execute(sql_query_to_insert_data_into_table, (name_entry.get(), email_entry.get(), username_entry.get(), password_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Done!')
            clear_entities()
            extra_window.destroy()
            import sign_in


# -------------------------------------------------- linking of pages --------------------------------------------------
def sign_in_page():
    extra_window.destroy()
    #import interior_design


# ---------------------------------------------------- GUI ----------------------------------------------------

# Create the Tkinter window and run the application
extra_window = Tk()
extra_window.geometry('1366x768')
extra_window.title('New_Ideas Page')
extra_window.iconbitmap('')
extra_window.resizable(False, False)


# set the window state to maximized
#extra_window.state('zoomed')

# Changing bb color to white
Label(extra_window, bg='white', height=1366, width=768).place(x=0, y=0)
cd_bg_image = ImageTk.PhotoImage(file='D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\Back_Images\\Register_Page.png')
cd_bg_label = Label(extra_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# Heading Label
cd_head_lbl = Label(extra_window, text='New Views', font=('Times New Roman', 30, 'bold'), bg='white',
                    fg='firebrick1')
cd_head_lbl.place(x=490, y=85)

# Name Label
Label(extra_window, text="Interio Type", bg='white', fg='firebrick1', font=('Times New Roman', 20)).place(x=261, y=140)

# Name input TextField

options = ["Hall", "Kitchen", "Bedroom", "Bathroom"]
name_entry = ttk.Combobox(state="readonly", values=options,width=59, font=("Helvetica", 19))
name_entry.place(x=261, y=180)
# Email Label
Label(extra_window, text="Room Style", bg='white', fg='firebrick1', font=('Times New Roman', 20)).place(x=261, y=230)

options2 = ["Neo-Chinese", "Light Luxury", "Italian", "Mashup" , "American(Simple)", "Modern Simplicity" , "Southeast Asian"]
email_entry = ttk.Combobox(state="readonly", values=options2,width=59,font=("Helvetica", 19))
email_entry.place(x=261, y=270)
# Username Label
Label(extra_window, text="Area", bg='white', fg='firebrick1', font=('Times New Roman', 20)).place(x=261, y=320)

# Username input TextField
username_entry = Entry(extra_window, width=61, font=('Times New Roman', 20), bd=0, fg='white', bg='firebrick1')
username_entry.place(x=261, y=360)

# Password Label
Label(extra_window, text="Requirements", bg='white', fg='firebrick1', font=('Times New Roman', 20)).place(x=261, y=410)

# Password input TextField
password_entry = Entry(extra_window, width=61, font=('Times New Roman', 20), bd=0, fg='white', bg='firebrick1')
password_entry.place(x=261, y=450)

# Sign up Button
Button(extra_window, text='Confirm', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
       activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=50, height=1,
       command=connect_to_mysql_db).place(x=261,
                                          y=590)
Button(extra_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
       activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=10, height=1,
       command=sign_in_page).place(x=1200,y=10)

extra_window.mainloop()
