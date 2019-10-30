
from tkinter import *
import math

root = Tk()

root.title('Automata palindromo impar')
root.geometry('1000x700')

paint = Canvas(root, width=1000, height=600,)
paint.place(x=-1,y=100)

text_entry = StringVar()


Entry(root, width=40, textvariable=text_entry).place(x=300,y=15)
Button(root, text='Validar').place(x=625,y=10)


#estado 1
paint.create_line(50,450,94,450,width=3.0,arrow=LAST)
paint.create_arc( 105, 375,175.5 ,470,star=0,extent=180,style='arc',width=3.0)
paint.create_line(165,405,175,420,widt=3)
paint.create_line(185,405,175,420,widt=3)
paint.create_oval(95,495,185,405,width=1.5)
paint.create_text(140,450,text='q0',font=('calibri',20))

#estado2
paint.create_line(185,450,284,450,width=3.0,arrow=LAST)
paint.create_arc( 295, 375,365.5 ,470,star=0,extent=180,style='arc',width=3.0)
paint.create_line(355,405,365,420,widt=3)
paint.create_line(375,405,365,420,widt=3)
paint.create_oval(285,495,375,405,width=1.5)
paint.create_text(330,450,text='q1',font=('calibri',20))

#estado3
paint.create_line(375,450,474,450,width=3.0,arrow=LAST)
paint.create_oval(475,495,565,405,width=1.5)
paint.create_oval(485,485,555,415,width=1.5)
paint.create_text(520,450,text='q0',font=('calibri',20))



root.mainloop()
