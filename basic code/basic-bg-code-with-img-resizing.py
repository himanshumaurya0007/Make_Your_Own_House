# from tkinter import *
#
# from PIL import Image, ImageTk
#
#
# class App(Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.master = master
#         self.pack(fill=BOTH, expand=YES)
#
#         # Load the images
#         self.images = Image.open('../images/Picsart-main-login.jpg')
#         self.photo = ImageTk.PhotoImage(self.images)
#
#         # Create the background label and pack it
#         self.background_label = Label(self, images=self.photo)
#         self.background_label.pack(fill=BOTH, expand=YES)
#
#         # Allow the user to fit the images to the window size
#         self.bind("<Configure>", self.resize)
#
#     def resize(self, event):
#         # Resize the images
#         self.images = self.images.resize((event.width, event.height))
#         self.photo = ImageTk.PhotoImage(self.images)
#         self.background_label.config(images=self.photo)
#
#
# # Create the Tkinter window and run the application
# root = Tk()
# app = App(root)
# root.geometry('1366x768')
# root.mainloop()
