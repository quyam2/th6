from tkinter import *
from PIL import ImageTk, Image
#thư viện đồ họa pillow

img=[0,0,0,0,0]

game = Tk()
game.title("Game bóng")                                 #tên game
canvas = Canvas(master=game, width=600 , height=400, background="Light blue")
#khung game
canvas.pack()
img[4]=ImageTk.PhotoImage(Image.open("x2.jpg"))                      # file hình nền
xx=canvas.create_image(0,-80,anchor=NW,image=img[4])
#vị trí hình nền
canvas.update()
game.mainloop()
