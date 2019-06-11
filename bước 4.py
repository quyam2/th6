from tkinter import *
from PIL import ImageTk, Image
from time import sleep #thư viên time


img=[0,0,0,0,0]

game = Tk()
game.title("Game bóng")
# tạo tên cho game

canvas = Canvas(master=game, width=600 , height=400, background="Light blue")# khung và thông số khung
canvas.pack()
# tạo khung cho game
img[0]=ImageTk.PhotoImage(Image.open("bong.png"))
img[1]=ImageTk.PhotoImage(Image.open("un.png"))
img[2]=ImageTk.PhotoImage(Image.open("chim.jpg"))
img[3]=ImageTk.PhotoImage(Image.open("so.jpg"))
img[4]=ImageTk.PhotoImage(Image.open("x2.jpg"))
# đưa file vào game , tất cả file
bong=canvas.create_image(10 ,370,anchor=NW,image=img[0])
tree=canvas.create_image(550,345,anchor=NW,image=img[1])
cloud=canvas.create_image(550,140,anchor=NW,image=img[2])
so=canvas.create_image(450,185,anchor=NW,image=img[3])
xx=canvas.create_image(0,-80,anchor=NW,image=img[4])
a=canvas.create_line(0,399,800,399,fill="blue")
# tọa độ và thông số cái file đã đưa vào
canvas.update()
def moveXX():
    global xx
    canvas.move(xx,-5,0)
    if canvas.coords(xx)[0]<-450:
       canvas.delete(xx)
       xx = canvas.create_image(0,-80, anchor=NW, image=img[4])
    canvas.update()
#hàm cho hình nền di chuyển
def moveCloud():
    global cloud
    canvas.move(cloud,-5,0)
    if canvas.coords(cloud)[0]<-20:
       canvas.delete(cloud)
       cloud = canvas.create_image(550, 220, anchor=NW, image=img[2])
    canvas.update()
# hàm cho con chim di chuyển
def moveSo():
    global so
    canvas.move(so,-5,0)
    if canvas.coords(so)[0]<-20:
       canvas.delete(so)
       so = canvas.create_image(450, 185, anchor=NW, image=img[3])
# hàm cho máy bay di chuyển
    canvas.update()
score = 0
text_score = canvas.create_text(550, 30, text="Điểm:" + str(score), fill="blue", font=("Times", 13))
# tính điểm
def moveTree():
    global tree,score,text_score
    canvas.move(tree,-3,0)
    if canvas.coords(tree)[0]<-20:
       score=score+1
       canvas.itemconfig(text_score,text="Điểm:" + str(score)) # điểm tăng dần khi vượt qua chướng ngại vạt
       canvas.delete(tree)
       tree = canvas.create_image(550, 345, anchor=NW, image=img[1])

    canvas.update()
gameOver=False
# hàm cho bức tường di chuyển
while not gameOver:
   moveCloud()
   moveTree()
   moveSo()
   moveXX()
   sleep(0.01)
game.mainloop()

