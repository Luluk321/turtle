from turtle import *


def gambar_pemandangan():
   penup()
   goto(-200, -200)
   pendown()
   color('green', 'yellowgreen')
   begin_fill()
   for i in range(2):
       forward(400)
       left(90)
       forward(100)
       left(90)
   end_fill()


def gambar_langit():
   penup()
   goto(-200, -100)
   pendown()
   #color('paleturquoise')
   color('skyblue')
   begin_fill()
   for i in range(2):
       forward(400)
       left(90)
       forward(300)
       left(90)
   end_fill()


def gambar_jendela():
   color('yellow')
   begin_fill()
   for i in range(4):
       forward(20)
       left(90)  
   end_fill()


def gambar_blok_apartemen():
   penup()
   goto(-170, -170)
   pendown()
   color('black', 'gray')
   begin_fill()
   for i in range(2):
       forward(100)
       left(90)  
       forward(200)
       left(90)
   end_fill()
   penup()
   goto(-145, -145)
   pendown()
   gambar_jendela()
   penup()
   goto(-115, -145)
   pendown()
   gambar_jendela()
   penup()
   goto(-145, -85)
   pendown()
   gambar_jendela()
   penup()
   goto(-115, -85)
   pendown()
   gambar_jendela()
   penup()
   goto(-145, -35)
   pendown()
   gambar_jendela()
   penup()
   goto(-115, -35)
   pendown()
   gambar_jendela()


def gambar_matahari():
   penup()
   goto(140, 140)
   pendown()
   begin_fill()
   color('orange', 'yellow')
   for i in range(18):
       forward(40)
       left(100)
   end_fill()


def gambar_farmasi():
   penup()
   goto(120, -160)
   pendown()
   color('brown', 'goldenrod')
   begin_fill()
   for i in range(3):
       forward(70)
       left(90)  
   end_fill()
   penup()
   goto(140, -110)
   pendown()
   pensize(5)
   color('red')
   forward(15)
   penup()
   goto(150, -118)
   pendown()
   color('red')
   right(90)
   forward(20)