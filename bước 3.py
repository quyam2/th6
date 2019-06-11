from tkinter import *
from PIL import ImageTk, Image

img=[0,0,0,0,0]
game = Tk()

game.title("Game bóng") #tên game
canvas = Canvas(master=game ,width=600 , height=400, background="Light blue")   #khung
canvas.pack()
img[0]=ImageTk.PhotoImage(Image.open("bong.png"))
img[1]=ImageTk.PhotoImage(Image.open("un.png"))
img[2]=ImageTk.PhotoImage(Image.open("chim.jpg"))
img[3]=ImageTk.PhotoImage(Image.open("so.jpg"))
img[4]=ImageTk.PhotoImage(Image.open("x2.jpg"))
#các file nhân vật trong game
bong=canvas.create_image(10 ,370,anchor=NW,image=img[0])
tree=canvas.create_image(550,345,anchor=NW,image=img[1])
cloud=canvas.create_image(550,140,anchor=NW,image=img[2])
so=canvas.create_image(450,185,anchor=NW,image=img[3])
xx=canvas.create_image(0,-80,anchor=NW,image=img[4])
a=canvas.create_line(0,399,800,399,fill="blue")
#tọa độ nhân vật trong game

canvas.update()
game.mainloop()


