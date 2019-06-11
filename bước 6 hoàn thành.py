from tkinter import *
from PIL import ImageTk, Image
from time import sleep


img=[0,0,0,0,0]


game = Tk()
game.title("Game bóng")
# tạo tên cho game``

canvas = Canvas(master=game, width=600 , height=450, background="Light blue")

canvas.pack()
# tạo khung cho game

img[0]=ImageTk.PhotoImage(Image.open("bong.png"))
img[1]=ImageTk.PhotoImage(Image.open("un.png"))
img[2]=ImageTk.PhotoImage(Image.open("chim.jpg"))
img[3]=ImageTk.PhotoImage(Image.open("so.jpg"))
img[4]=ImageTk.PhotoImage(Image.open("x2.jpg"))
# đưa file vào game , tất cả file đều do nhóm tìm kiếm


bong=canvas.create_image(10 ,420,anchor=NW,image=img[0])
tree=canvas.create_image(550,390,anchor=NW,image=img[1])
cloud=canvas.create_image(550,140,anchor=NW,image=img[2])
so=canvas.create_image(450,185,anchor=NW,image=img[3])
xx=canvas.create_image(0,-80,anchor=NW,image=img[4])
a=canvas.create_line(0,449,600,449,fill="blue")
# tọa độ và thông số cái file đã đưa vào


canvas.update()
def moveXX():
    global xx
    canvas.move(xx,-5,0) 
    if canvas.coords(xx)[0]<-450:
       canvas.delete(xx)
       xx = canvas.create_image(0,-80, anchor=NW, image=img[4])

    canvas.update()
# hàm để hinh nền di chuyển
def moveCloud():
    global cloud
    canvas.move(cloud,-5,0)
    if canvas.coords(cloud)[0]<-20:
       canvas.delete(cloud)
       cloud = canvas.create_image(550, 220, anchor=NW, image=img[2])

    canvas.update()
# hàm để chim di chuyển

def moveSo():
    global so
    canvas.move(so,-5,0)
    if canvas.coords(so)[0]<-20:
       canvas.delete(so)
       so = canvas.create_image(450, 185, anchor=NW, image=img[3])

    canvas.update()
# hàm để may bay di chuyển

score = 0
text_score = canvas.create_text(540, 280, text="Điểm:" + str(score), fill="blue", font=("Times", 13))

def moveTree():
    global tree,score,text_score
    canvas.move(tree,-5,0)
    if canvas.coords(tree)[0]<-20:
       score=score+1
       canvas.itemconfig(text_score,text="Điểm:" + str(score))
       canvas.delete(tree)
       tree = canvas.create_image(550, 390, anchor=NW, image=img[1])

    canvas.update()
# hàm để cái tường di chuyển


check_jump=False


def jump():
    global check_jump
    if check_jump==False:
        check_jump=True
        for i in range(0, 30):
           canvas.move(bong,0,-5)
           moveCloud()
           moveTree()
           moveSo()
           moveXX()
           canvas.update()
           sleep(0.01)
        for i in range(0, 30):
           canvas.move(bong, 0, 5)
           moveCloud()
           moveTree()
           moveSo()
           moveXX()
           canvas.update()
           sleep(0.01)
        check_jump=False
# hàm để quả bóng di chuyển lên xuống cùng với các nhân vật


def KeyPress(event):
    if event.keysym=="space":
        jump()

canvas.bind_all("<KeyPress>",KeyPress)

gameOver=False

# hàm điều khiển và tương tác vs bàn phím để quả bóng di chuyển

def check_gameOver():
    global gameOver
    coords_tree=canvas.coords(tree)
    coords_bong=canvas.coords(bong)


    if coords_bong[1]>370 and coords_tree[0]<50:
        gameOver=True
    game.after(100,check_gameOver)
    if coords_bong[1]>370 and coords_tree[0]<50:
       canvas.create_text(300, 110, text="Game Over", fill="red", font=('Times', 40))


check_gameOver()

#hàm dùng để kết thúc trờ chơi
while not gameOver:
   moveCloud()
   moveTree()
   moveSo()
   moveXX()
   sleep(0.01)

#tránh bị khựng khi quá bóng đang di chuyển
game.mainloop()