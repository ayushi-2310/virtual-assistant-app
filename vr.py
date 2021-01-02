from tkinter import  *
from PIL import ImageTk ,Image
from tkinter import ttk
import tkinter.font as font
import os


root=Tk()
root.title('SAS')
root.configure(bg='#BCD5E5')
root.geometry('700x690')


frameCnt = 30
frames = [PhotoImage(file='giphy.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)

root.after(0, update, 0)


text1=Label(root,text="HELLO",bg='#BCD5E5')


lspace3=Label(text="              ",bg='#BCD5E5')
lspace3.grid(row=0,column=0)

my_img1 = ImageTk.PhotoImage(Image.open("voice1.png"))
cbutton = Button(root, image =my_img1 ,bg='#BCC6CE',padx=10,pady=10, command=lambda: speak(audio))

        
playbutton=Button(root,text = "1")


buttonguide=Button(root,text="GUIDE",bg='#BCC6CE',padx=10,pady=10)



img1 = ImageTk.PhotoImage(Image.open("note.png"))
buttonscratch = Button(root, image = img1 ,command=lambda: os.startfile('demo.txt'))


lspace3=Label(text="              ",bg='#BCD5E5')
lspace4 = Label(text="              ",bg='#BCD5E5')
lspace5 = Label(text="              ",bg='#BCD5E5')
lspace6 = Label(text="              ",bg='#BCD5E5')

#positions
label.grid(row=0,column=1)
lspace3.grid(row=1,column=1)
text1.grid(row=2,column=1)
lspace4.grid(row=3,column=0)
lspace5.grid(row=5,column=0)
cbutton.grid(column=2, row=6)
lspace6.grid(row=6,column=0)
playbutton.grid(row=4,column=2)
buttonguide.grid(row=8,column=1)
buttonscratch.grid(row=8,column=2)







root.mainloop()
