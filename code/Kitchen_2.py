from tkvideo import tkvideo
from tkinter import *

w = Tk()
lblVideo = Label(w)
lblVideo.pack()

def go():
    w.destroy()
    import Hall_Designs

btnback = Button(w, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command= go)
btnback.place(x=570, y=00)


player = tkvideo("D:\\SanchitSanjayPatil\\Coding\\Clg\\sem4\\make-your-own-house\\resources\\interior_plan_videos\\Kitchen_2 Video.mp4", lblVideo,
                     loop=1,
                     size=(700, 500))
player.play()




w.mainloop()