from tkinter import *
from tkinter import ttk

w=Tk()
w.geometry('244x330')
w.resizable(width=False,height=False)
w.title('Calculator')
w.iconbitmap(r'Calculator Tkinter/Icon.ico')

lab=Frame(background='white')
lab.pack()

ent=Frame(background='white')
ent.pack()

btn=Frame(background='#202124')
btn.pack()

e=Entry(ent,width=23,font=('Arial','12'),background='#202124',border=1,foreground='white',insertbackground='white')
e.pack(side=LEFT,fill=X,expand=TRUE,pady=0,ipady=11,ipadx=17)

def result():
    a=e.get()
    if a=='':
        e.focus()
    elif '(' or ')' in a:
        x=a.split('(')
        for i in range(len(x)):
            if ')' in x[i]:
                q=x[i].split(')')
                for h in q:
                    if h!='':
                        for j in range(len(q)):
                            for k in q[j]:
                                if k=='+' or k=='-' or k=='/' or k=='*':
                                    q[j]=str(eval(q[j]))
                t='*'.join(q)
                x[i]=t
        for l in range(len(x)):
            if len(x[l])>1:
                if x[l][len(x[l])-1]=='*' or x[l][len(x[l])-1]=='+' or x[l][len(x[l])-1]=='-' or x[l][len(x[l])-1]=='/':
                    x[l]=x[l].replace('*','')
        for p in x:
            if p=='':
                x.remove(p)
        # for i in range(len(x)):
        #     if x[i][len(x[i])-1]=='+' or x[i][len(x[i])-1]=='-' or x[i][len(x[i])-1]=='*' or x[i][len(x[i])-1]=='/':
        #         x[i]=x[i]+x[i+1]
        # print(x)
        r='*'.join(x)
        res=eval(r)
        e.delete(0,END)
        e.insert(END,res)
    else:
        if a[len(a)-1]=='+' or a[len(a)-1]=='-' or a[len(a)-1]=='*' or a[len(a)-1]=='/':
                pass
        else:
                res=eval(a)
                e.delete(0,END)
                e.insert(END,res)
def clear():
    e.delete(0,END)
def one():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'1')
def two():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'2')
def three():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'3')
def four():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'4')
def five():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'5')
def six():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'6')
def seven():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'7')
def eight():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'8')
def nine():
    a=e.get()
    if len(a)>1:
        if a[len(a)-1]=='0' and a[len(a)-2]==')':
            e.delete(len(a)-1)
    e.insert(END,'9')
def zero():
    a=e.get()
    if len(a)==0 or a[len(a)-1]=='+' or a[len(a)-1]=='-' or a[len(a)-1]=='*' or a[len(a)-1]=='/' or a[len(a)-1]=='(' or a[len(a)-1]=='0':
        pass
    else:
        e.insert(END,'0')
def backspace():
    a=e.get()
    e.delete(len(a)-1)
def plus():
    a=e.get()
    if len(a)==0:
        pass
    elif len(a)>=1 and a[len(a)-1]=='+' or a[len(a)-1]=='-' or a[len(a)-1]=='*' or a[len(a)-1]=='/':
        e.delete(len(a)-1)
        e.insert(END,'+')
    else:
        e.insert(END,'+')
def sub():
    a=e.get()
    if len(a)==0:
        pass
    elif len(a)>=1 and a[len(a)-1]=='+' or a[len(a)-1]=='-' or a[len(a)-1]=='*' or a[len(a)-1]=='/':
        e.delete(len(a)-1)
        e.insert(END,'-')
    else:
        e.insert(END,'-')
def mult():
    a=e.get()
    if len(a)==0:
        pass
    elif len(a)>=1 and a[len(a)-1]=='+' or a[len(a)-1]=='-' or a[len(a)-1]=='*' or a[len(a)-1]=='/':
        e.delete(len(a)-1)
        e.insert(END,'*')
    else:
        e.insert(END,'*')
def div():
    a=e.get()
    if len(a)==0:
        pass
    elif len(a)>=1 and a[len(a)-1]=='+' or a[len(a)-1]=='-' or a[len(a)-1]=='*' or a[len(a)-1]=='/':
        e.delete(len(a)-1)
        e.insert(END,'/')
    else:
        e.insert(END,'/')
def barcketopen():
    a=e.get()
    if len(a)>=1 and a[len(a)-1]=='(':
        pass
    else:
        e.insert(END,'(')
def barcketclose():
    a=e.get()
    if len(a)>=1 and a[len(a)-1]==')':
        pass
    else:
        for i in range(len(a)-1,-1,-1):
            if a[i]=='(' and a[len(a)-1]!='(':
                e.insert(END,')')

b1=Button(btn,text='1',command=one,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b1.grid(row=3,column=0)

b2=Button(btn,text='2',command=two,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b2.grid(row=3,column=1)

b3=Button(btn,text='3',command=three,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b3.grid(row=3,column=2)

b4=Button(btn,text='4',command=four,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b4.grid(row=4,column=0)

b5=Button(btn,text='5',command=five,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b5.grid(row=4,column=1)

b6=Button(btn,text='6',command=six,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b6.grid(row=4,column=2)

b7=Button(btn,text='7',command=seven,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b7.grid(row=5,column=0)

b8=Button(btn,text='8',command=eight,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b8.grid(row=5,column=1)

b9=Button(btn,text='9',command=nine,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b9.grid(row=5,column=2)

b0=Button(btn,text='0',command=zero,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
b0.grid(row=6,column=1)

brackopen=Button(btn,text='(',command=barcketopen,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
brackopen.grid(row=2,column=0)

brackclose=Button(btn,text=')',command=barcketclose,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
brackclose.grid(row=2,column=1)

back=PhotoImage(file=r'Calculator Tkinter/Backspace.png')
bb=Button(btn,image=back,command=backspace,height=55,width=58,background='#202124',activebackground='#303134',border=0)
bb.grid(row=6,column=2)

br=Button(btn,text='=',command=result,height=2,width=5,font=('Arial','14'),background='#378CE7',foreground='white',activeforeground='white',activebackground='#303134',border=0)
br.grid(row=6,column=3)

bp=Button(btn,text='+',command=plus,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
bp.grid(row=5,column=3)

bs=Button(btn,text='-',command=sub,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
bs.grid(row=4,column=3)

bm=Button(btn,text='*',command=mult,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
bm.grid(row=3,column=3)

bd=Button(btn,text='/',command=div,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
bd.grid(row=2,column=3)

bc=Button(btn,text='C',command=clear,height=2,width=5,font=('Arial','14'),background='#202124',foreground='white',activeforeground='white',activebackground='#303134',border=0)
bc.grid(row=2,column=2)

w.mainloop()