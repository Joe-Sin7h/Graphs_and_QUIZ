import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
from tkinter import messagebox as msg
import numpy as n
import time
matplotlib.use('TkAgg')
root = Tk()
root.iconbitmap('j.ico')
root.geometry('1000x666')
# root.resizable(0, 0)
root.title('oyster_tec')
i = PhotoImage(file='pic1.png')
f3 = Frame(root)
f1 = Frame(root, bg='black')
f2 = Frame(root, bg='black')
f = Frame(root)
f.place(relwidth=1, relheight=1)
c1 = Canvas(f)
c1.create_image(0, 0, image=i, anchor=NW)
c1.place(relwidth=1, relheight=1)
f1.place(relwidth=1, relheight=1)

def reg():
    user = r.get()
    pas = p.get()
    file = open('demo.txt', 'a')
    file.write(user + ',')
    file.write(pas + '\n')
    file.close()
    r1.delete(0, END)
    p1.delete(0, END)

def log():
    username = t.get()
    password = v.get()
    e.delete(0, END)
    e1.delete(0, END)
    f = open('demo.txt', 'r')
    c = f.readlines()
    for i in c:
        j = i.split(',')
        if j[0] == username and j[1].replace('\n', '') == password:
            return loginsuc()
        elif i == c[len(c) - 1]:
            return fail()

def loginsuc():
    f3.place(relwidth=1, relheight=1)
    f3.tkraise()

def fail():
    l = Label(f1, text='Login_Failed', font=('Yu Gothic', 15, 'italic', 'bold'), fg='blue', bg='black')
    l.place(x=450, y=600)

def login():
    f1.tkraise()
    l11 = Label(f1, text='    Login_ID '
                , bg='grey', fg='darkblue', activebackground='darkblue', activeforeground='grey', cursor='plus',
                font=('Yu Gothic', 15, 'italic', 'bold'), highlightcolor='red')
    l11.place(x=300, y=200)
    l22 = Label(f1, text='  Password '
                , bg='grey', fg='darkblue', activebackground='darkblue', activeforeground='grey', cursor='plus',
                font=('Yu Gothic', 15, 'italic', 'bold',), justify='left', )
    l22.place(x=300, y=235)
    b3 = Button(f1, text='    Login    ', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
                activebackground='darkblue',
                activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
                justify='left', command=log
                )
    b3.place(x=450, y=500)
    global t
    global v
    global e
    global e1
    t = StringVar(f1)
    v = StringVar(f1)
    e = Entry(f1, textvariable=v, show='*', highlightthickness=2, highlightcolor='blue', font=('Yu Gothic', 13, 'bold'),
              highlightbackground='grey')
    e.place(x=420, y=235, width=260, height=32)
    e1 = Entry(f1, textvariable=t, highlightthickness=2, highlightcolor='blue', font=('Yu Gothic', 13, 'bold'),
               highlightbackground='grey')
    e1.place(x=420, y=200, height=32, width=260)

def register():
    f2.place(relwidth=1, relheight=1)
    f2.tkraise()
    Label(f2, text=' Register_ID ', bg='grey', fg='darkblue', activebackground='darkblue', activeforeground='grey',
          cursor='plus',
          font=('Yu Gothic', 15, 'italic', 'bold'), highlightcolor='red').place(x=300, y=200)
    Label(f2, text='    Password ', bg='grey', fg='darkblue', activebackground='darkblue', activeforeground='grey',
          cursor='plus',
          font=('Yu Gothic', 15, 'italic', 'bold'), highlightcolor='red').place(x=300, y=235)
    global r
    global p
    global r1
    global p1
    r = StringVar(f2)
    p = StringVar(f2)
    r1 = Entry(f2, textvariable=p, show='*', highlightthickness=2, highlightcolor='blue',
               font=('Yu Gothic', 13, 'bold'),
               highlightbackground='grey')
    r1.place(x=433, y=235, width=260, height=32)
    p1 = Entry(f2, textvariable=r, highlightthickness=2, highlightcolor='blue', font=('Yu Gothic', 13, 'bold'),
               highlightbackground='grey')
    p1.place(x=432, y=200, height=32, width=260)
    Button(f2, text=' Register ', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=reg
           ).place(x=450, y=500)

l = Button(f, text='  Login  ', command=login, font=('Yu Gothic', 17, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left',
           ).place(x=400, y=250, width=250)
l3b = Button(f, text=' Register ', font=('Yu Gothic', 17, 'italic', 'bold',), bg='grey', fg='darkblue',
             activebackground='darkblue',
             activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
             justify='left', command=register).place(x=400, y=350, width=250)
img = PhotoImage(file='images.png')
def fun():
    f.tkraise()

def fun1(event):
    f.tkraise()
root.bind('<Control-b>',fun1)

def exit():
    ms = msg.askquestion('exit??', 'do you really wanna exit +_+ ?')
    if ms == 'yes':
        root.destroy()
   
menu1 = Menu(root, bg='red', fg='blue', activeforeground='#209EFF', font=('Areial', 10))
sub1 = Menu(menu1, tearoff=0, activebackground='white', activeforeground='#209EFF', bg='white', )
sub1.add_command(label=' ', command=fun, image=img, compound=LEFT, accelerator='ctrl+b')
menu1.add_cascade(menu=sub1, label='Back')
menu1.add_command(label='EXIT>>', command=exit, activeforeground='orange')
root.config(menu=menu1)

def bck():
    f5.tkraise()

########################################################################################

def plot():
    global f5
    f5 = Frame(root, bg='black')
    f5.place(relwidth=1, relheight=1)
    f5.tkraise()
    Button(f5, text='Surface_plot1', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left',  command=pl1).grid(ipady=80,ipadx=88)

    Button(f5, text='Surface_plot2', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=pl2).grid(row=1,ipady=80,ipadx=88)
    Button(f5, text='Surface_plot3', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=pl3).grid(row=2,ipady=80,ipadx=88)
    Button(f5, text='Surface_plot4', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='red', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=pl4).grid(row=0,column=1,ipady=80,ipadx=88)
    Button(f5, text='Surface_plot5', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=pl5).grid(row=1,column=1,ipady=80,ipadx=88)
    Button(f5, text='Surface_plot6', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=pl6).grid(row=2,column=1,ipady=80,ipadx=88)
    Button(f5, text='Surface_plot7', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=pl7).grid(row=0,column=2,ipady=80,ipadx=88)
    Button(f5, text='Surface_plot8', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=pl8).grid(row=1,column=2,ipady=80,ipadx=88)
    Button(f5, text='Surface_plot9', font=('Yu Gothic', 15, 'italic', 'bold',), bg='grey', fg='darkblue',
           activebackground='darkblue',
           activeforeground='grey', cursor='plus', highlightcolor='red', bd=6, highlightbackground='red',
           justify='left', command=pl9).grid(row=2,column=2,ipady=80,ipadx=88)


root.wm_title('Oyster_tec')


def pl1():
    
    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#3496FF')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    X = n.linspace(-6, 6, 50)
    Y = n.linspace(-6, 6, 50)
    X, Y = n.meshgrid(X, Y)
    Z = n.sin(n.sqrt(X ** 2 + Y ** 2))
    ax = fm.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='winter')
    c.get_tk_widget().pack(side=TOP)
    t = NavigationToolbar2Tk(c, f6)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)
def pl2():
    
    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#5AC54A')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    v=n.linspace(0,180,110)
    X=n.sin(v)
    Y=n.cos(v)
    ax = fm.add_subplot(111, projection='3d')
    ax.scatter(X, Y, v, edgecolor='lightblue',color='darkblue',s=30)
    c.get_tk_widget().pack(side=TOP)
    t = NavigationToolbar2Tk(c, f6)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)
def pl3():
    
    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#3496FF')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    x=[120,220,330,440,550]
    y=[10,20,30,40,50]
    z=[100,100,100,100,100]
    dx=[20,20,20,20,20]
    dy=[50,50,50,50,50]
    dz=[20,20,20,20,20]
    ax = fm.add_subplot(111, projection='3d')
    ax.bar3d(x,y,z,dx,dy,dz,color='orange')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    c.get_tk_widget().pack(side=TOP)
    t = NavigationToolbar2Tk(c, f6)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)
def pl4():
    
    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#3496FF')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    ax = fm.add_subplot(111, projection='3d')
    u = n.linspace(0, 2 * n.pi, 100)
    v = n.linspace(0, n.pi, 100)
    xx = 10 * n.outer(n.sin(u), n.cos(v))
    yy = 10 * n.outer(n.cos(u), n.sin(v))
    zz = 10 * n.outer(n.ones(n.size(u)), n.sin(u))
    ax.plot_surface(xx, yy, zz, color='blue', rstride=4, cstride=4)
    c.get_tk_widget().pack(side=TOP)
    t = NavigationToolbar2Tk(c, f6)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)
def pl5():
    
    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#3496FF')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    ax = fm.add_subplot(111, projection='3d')
    u = n.linspace(0, 2 * n.pi, 100)
    v = n.linspace(0, n.pi, 100)
    xx = 10 * n.outer(n.sin(u), n.cos(v))
    yy = 10 * n.outer(n.cos(u), n.sin(v))
    zz = 10 * n.outer(n.ones(n.size(u)), n.sin(u))
    ax.plot_wireframe(xx, yy, zz, color='blue', rstride=4, cstride=4)
    c.get_tk_widget().pack(side=TOP)
    t = NavigationToolbar2Tk(c, f6)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)
def pl6():
    d=Image.open('11.2.png')
    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#3496FF')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    xx=n.random.rand(2,100)
    yy=n.random.rand(2,100)
    ax = fm.add_subplot()
    ax.imshow(d)       
    c.get_tk_widget().pack(side=TOP)
    t = NavigationToolbar2Tk(c, f6)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)
def pl7():

    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#3496FF')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    X = n.linspace(-6, 6, 50)
    Y = n.linspace(-6, 6, 50)
    X, Y = n.meshgrid(X, Y)
    Z = n.sin(n.sqrt(X ** 2 + Y ** 2))
    ax = fm.add_subplot(111, projection='3d')
    ax.plot_wireframe(X, Y, Z, rstride=4,cstride=4)
    c.get_tk_widget().pack(side=TOP)
    t = NavigationToolbar2Tk(c, f6)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)
def pl8():
   
    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#3496FF')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    x=[3,7,10,14,18,21,26,30,34,39,43,48,53]
    y=[100,12,32,45,90,67,80,90,10,50,60,70,30]
    ax = fm.add_subplot(111)
    ax.plot([3,7,10,14,18,21,26,30,34,39,43,48,53],[100,12,32,45,90,67,80,90,10,50,60,70,30])
    ax.fill_between(x,y, 45,facecolor='#1AA0B6',alpha=0.5)
    c.get_tk_widget().pack(side=TOP)
    t = NavigationToolbar2Tk(c, f6)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)
def pl9():
    f6 = Frame(root)
    fm = Figure(figsize=(5, 5), facecolor='#3496FF')
    plt.style.use('dark_background')
    c = FigureCanvasTkAgg(fm, f6)
    ax=fm.add_subplot(111)
    ax.plot([],[],label='-1-',color='red')
    ax.plot([], [], label='-2-',color='blue')
    ax.plot([], [], label='-3-',color='darkblue')
    ax.legend(loc=1, facecolor='grey', framealpha=0.5,frameon=1,  edgecolor='darkred',
               title='legend')
    ax.stackplot([12,23,34,45,56,67],[10,14,9,25,34,40],[15,23,34,20,30,40],[40,50,60,30,10,35],colors=['red','blue','darkblue',])
    t = NavigationToolbar2Tk(c, f6)
    c.get_tk_widget().pack(side=TOP)
    c.draw()
    t.update()
    c._tkcanvas.place(relwidth=1, relheight=1)
    Button(f6, text='<<<', command=bck).pack(side=TOP, anchor=NW)
    f6.place(relwidth=1, relheight=1)

f4 = Frame(root)
ii=PhotoImage(file='11.1.png')
c11=Canvas(f4)
c11.create_image(0,0,image=ii,anchor=NW)
c11.place(relwidth=1, relheight=1)
def play():
    f4.place(relwidth=1, relheight=1)
    f41=Frame(f4,bg='white')
    f41.place(relwidth=0.4,relheight=0.5,x=330,y=240)
    f4.tkraise()

    q = ['what is my name ', 'who is greatest of all times ?','who is the captain of madrid fc ?','5th generation computer are based on ?','Video conferencing is done through','which is telecommunication device','which of these is a input device','world\'s first electronic computer','Laughing gas is ?','teflon is the common name of _ ','participant of which sports are called pugilist','Who was the 1st speaker of loksabha','what is normal tenure of a punchayat','Who doesn\'t take oath of the office','Fascism believes in ? ','The treaty of Yandaboo wsa signed in','Bahmani kingdom wsa founded in','world economic forum was founded by-','1st payment bank has been launched by','operation clean money is started by-','Ngultrum is the currency of-']
    a1 = [['jogendra ', 'idk ', 'great ', 'cr7 '], ['neymar ', 'messi ', 'cr7 ', 'maradona '], ['mesi ','marcello ','sergio_ramos ','jogendra '],['AI ','PI ','sys knowledge ','VVLSI '],['Telephone network ','Ip network ','TV ','NOTA '],['Telephone ','Telegraph ','Computer withnetwork ','all of these '],['Plotter ','Printer ','Monitor ','Scanner '],['PARAM ','CRAY-1 ','PASCALINE ','ENIAC '],['Hydrogen peroxide ','nitrous oxide ','carbon monoxide ','sulphor dioxide '],['polytetrafluoro ethylene ','ployvinyl chloride ','ployviny fluoride ','dichlorodifluoro methane '],['sprinter ','Boxing ','Wrestling ','javelin throw '],['Hukum singh ','M.A.Ayyangar ','G.V. Mavalankar ','G.M.C.Balyogi '],['3 years ','4 years ','2 years ','5 years '],['President ','Vice President ','Prime Minister ','Speaker '],['Dignity of individual ','propaganda','Socialism ','Force '],['1826','1825,','1824','1823'],['15th century AD','14th century AD','13th century AD','16th century AD'],['Klaus Schwab','Paul Krugman','Bill Gates','Peter Thiel'],['Airtel ','cholamandalam ','Tech Mahindra ','NOTA '],['NITI Ayog','I tax Department','Ministry of finance','Central Board of \n Direct Taxes'],['Thailand',' republic of Nepal','Bhutan','Malaysia']]
    a = [1, 2,3,1,2,4,4,4,2,1,2,3,4,4,4,1,2,1,1,2,3]
    t = IntVar()
    t.set(0)
    c = [0]
    i = [0]

    def start(b=0):

        global r1, r2, r3, r4
        r1 = Radiobutton(f4, activebackground='#6DFFF5',fg='#2058B6', activeforeground='#0C00FF',bg=f4.cget('bg'), text=a1[b][0], variable=t,
                         value=1, justify='left', font=('Myanmar Text', 17, 'bold',
                                                        'italic'))
        r2 = Radiobutton(f4, activebackground='#6DFFF5',fg='#2058B6', activeforeground='#0C00FF', text=a1[b][1], variable=t,
                         value=2, justify='left', font=('Myanmar Text', 17, 'bold',
                                                        'italic'))
        r3 = Radiobutton(f4, activebackground='#6DFFF5',fg='#2058B6', activeforeground='#0C00FF', text=a1[b][2], variable=t,
                         value=3, justify='left', font=('Myanmar Text', 17, 'bold',
                                                        'italic'))
        r4 = Radiobutton(f4, activebackground='#6DFFF5',fg='#2058B6', activeforeground='#0C00FF', text=a1[b][3], variable=t,
                         value=4, justify='left', font=('Myanmar Text', 17, 'bold',
                                                        'italic'))
        r1.place(x=10,y=150)
        r2.place(x=10, y=220)
        r3.place(x=10, y=290)
        r4.place(x=10, y=360)

    def ques():

        t.set(0)
        r1.config(text=str(a1[i[0]][0]))
        r2.config(text=str(a1[i[0]][1]))
        r3.config(text=str(a1[i[0]][2]))
        r4.config(text=str(a1[i[0]][3]))

    def diplay(b=i[0]):
        global l1
        l1 = Label(f4, text=q[b],font=('Arial',26,'bold'),)
        l1.place(x=120,y=30)

        return start(b)

    l2 = Label(f41, text='',font=('Segoe Print',20,'bold'),bg='white',activebackground='white')
    l2.pack()

    def check():
        try:
            l2.config(state='active',bg='white')

            if t.get() == a[i[0]]:

                l2.config(text='correct')
            else:

                l2.config(text='wrong')

        except:
            print()

    def nextt():

        l2.config(state='disabled', disabledforeground=f41.cget('bg'))
        try:

            if i[0] <= len(q) - 1:
                if t.get() == a[i[0]]:
                    c[0] += 1

                i[0] += 1
                l1.config(text=str(q[i[0]]))
                return ques()
        except:

            Label(f41,text='Game over ^_^',font=('Segoe Print',30,'bold'),bg='white',activebackground='white').place(x=50,y=170)

    def result():
        Label(f41, text='Score:'+''+str(c[0]),font=('Arial',20,'bold'),bg='white').place(x=100,y=90)

    diplay()

    Button(f4, text='Check', command=check,bg=('#272726'),activebackground='#D1D1CC',fg='#D1D1CC',activeforeground='#272726',font=('Segoe Print',15,'bold')).place(x=900,relwidth=0.1,relheight=0.32)
    Button(f4, text='Next', command=nextt,bg='#272726',activebackground='#D1D1CC',fg='#D1D1CC',activeforeground='#272726',font=('Segoe Print',15,'bold')).place(x=900,y=207,relwidth=0.1,relheight=0.34)
    Button(f4, text='Score', command=result,bg='#272726',activebackground='#D1D1CC',fg='#D1D1CC',activeforeground='#272726',font=('Segoe Print',15,'bold')).place(x=900,y=427,relheight=0.335,relwidth=0.1)

can = Canvas(f3)
bcf3 = Button(can, text='PLAY', width=19, font=('Segoe Print', 15, 'bold', 'italic'), bg='#282827', fg='#B4B4B0',
              activebackground='#B4B4B0', activeforeground='#282827', cursor='spider',
               command=play)
bcf32 = Button(can, text='PLOT', width=19, font=('Segoe Print', 15, 'bold', 'italic'), bg='#282827', fg='#B4B4B0',
               activebackground='#B4B4B0', activeforeground='#282827', cursor='spider',
                command=plot)
j1=PhotoImage(file='j2.png')
can.create_image(0,0,image=j1,anchor=NW)
can.place(relwidth=1,relheight=1)
bcf32.place(x=330, y=150,relwidth=0.4)
bcf3.place(x=330, y=300,relwidth=0.4)
root.mainloop()
