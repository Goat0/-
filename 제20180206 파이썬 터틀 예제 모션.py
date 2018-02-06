Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> 
>>> t.pensize(3)
>>> 
>>> 
>>> #삼각형 만들기
>>> t.penup()
>>> t.goto(-200, -50)
>>> t.pendown()
>>> t.circle(40, steps = 3)
>>> 
>>> #사각형 만들기
>>> t.penup()
>>> t.goto(-100,-50)
>>> t.pendown()
>>> t.circle(40, steps = 4)
>>> 
>>> #오각형 만들기
>>> t.penup()
>>> t.goto(0,-50)
>>> t.pendown()
>>> t.circle(40, steps = 5)
>>> 
>>> #육각형 만들기
>>> t.penup()
>>> t.goto(100,-50)
>>> t.pendown()
>>> t.circle(40, steps = 6)
>>> 
>>> #원 만들기
>>> t.penup()
>>> t.goto(200,-50)
>>> t.pendown()
>>> t.circle(40)
>>> 
