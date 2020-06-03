from tkinter import *
m=Tk()
m.title('simple calculator')
def add():
    e3.delete(0,END)
    res=int(e1.get())+ int(e2.get())
    e3.insert(0,res)
def sub():
    e3.delete(0,END)
    res=int(e1.get())- int(e2.get())
    e3.insert(0,res)
def mul():
    e3.delete(0,END)
    res=int(e1.get())*int(e2.get())
    e3.insert(0,res)
def div():
    e3.delete(0,END)
    res=int(e1.get())/int(e2.get())
    e3.insert(0,res)
def mod():
    e3.delete(0,END)
    res=int(e1.get())% int(e2.get())
    e3.insert(0,res)
def pow():
    e3.delete(0,END)
    res=int(e1.get())** int(e2.get())
    e3.insert(0,res)
def cls():
    e3.delete(0,END)
    e1.delete(0, END)
    e2.delete(0, END)

c=Canvas(m,width=350,height=400,bg='grey')
c.pack()
l1=Label(m,text='Simple calculator',font=('times',14,'bold'),bg='green')
c.create_window(160,40,window=l1)
l2=Label(m,text='Enter no1',font=('times',12,),bg='pink',width=14)
c.create_window(100,100,window=l2)
l3=Label(m,text='Enter no2',font=('times',12),bg='pink',width=14)
c.create_window(100,140,window=l3)
l4=Label(m,text='Result',font=('times',12,'bold'),bg='gold',width=14)
c.create_window(100,180,window=l4)

e1=Entry(m,bd=4)
c.create_window(260,100,window=e1)
e2=Entry(m,bd=4)
c.create_window(260,140,window=e2)
e3=Entry(m,bd=4)
c.create_window(260,180,window=e3)

b1=Button(text="+",command=add,bg='purple',fg='white',font=('times',12,'bold'),width=5)
c.create_window(40,250,window=b1)
b2=Button(text="-",command=sub,bg='purple',fg='white',font=('times',12,'bold'),width=5)
c.create_window(80,250,window=b2)
b3=Button(text="*",command=mul,bg='purple',fg='white',font=('times',12,'bold'),width=5)
c.create_window(120,250,window=b3)
b4=Button(text="/",command=div,bg='purple',fg='white',font=('times',12,'bold'),width=5)
c.create_window(160,250,window=b4)
b5=Button(text="%",command=mod,bg='purple',fg='white',font=('times',12,'bold'),width=5)
c.create_window(200,250,window=b5)
b6=Button(text="^",command=pow,bg='purple',fg='white',font=('times',12,'bold'),width=5)
c.create_window(240,250,window=b6)
b7=Button(text="CLS",command=cls,bg='purple',fg='white',font=('times',12,'bold'),width=5)
c.create_window(280,250,window=b7)
b8=Button(text="close",command=m.destroy,bg='purple',fg='white',font=('times',12,'bold'),width=5)
c.create_window(160,330,window=b8)


m.mainloop()