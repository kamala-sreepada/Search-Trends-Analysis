from tkinter import *
def form(n):
    def save_info():
        n1=t1.get()
        n2=t2.get()
        n3=t3.get()
        n4=t4.get()
        n5=t5.get()
        n6=t6.get()
        n1=str(n1)
        n2=str(n2)
        n3=str(n3)
        n4=str(n4)
        n5=str(n5)
        n6=str(n6)
        l=[n1,n2,n3,n4,n5,n6]
        if n in [1,2,3,4]:
            file=open(str(n)+".txt","a")
            l=[n1,n2,n3,n4,n5,n6]
            for i in l:
                file.write(i+" ")
            file.close()
            
    screen=Tk()
    screen.geometry("500x500")
    screen["background"]="#ddffe7"
    screen.title("Python Form")
    heading=Label(text="Type in your values",bg="#ddffe7",fg="#167d7f",width="500",height="3",font="Georgia 15 bold")
    heading.pack()


    y1=Label(text="2010 *",font="Georgia 10",)
    y2=Label(text="2012 *",font="Georgia 10",)
    y3=Label(text="2014 *",font="Georgia 10")
    y4=Label(text="2016 *",font="Georgia 10")
    y5=Label(text="2018 *",font="Georgia 10")
    y6=Label(text="2020 *",font="Georgia 10")
    y1.place(x=15,y=80)
    y2.place(x=15,y=150)
    y3.place(x=15,y=210)
    y4.place(x=15,y=270)
    y5.place(x=15,y=330)
    y6.place(x=15,y=390)

    t1=IntVar()
    t2=IntVar()
    t3=IntVar()
    t4=IntVar()
    t5=IntVar()
    t6=IntVar()
    e1=Entry(textvariable=t1,width="30")
    e2=Entry(textvariable=t2,width="30")
    e3=Entry(textvariable=t3,width="30")
    e4=Entry(textvariable=t4,width="30")
    e5=Entry(textvariable=t5,width="30")
    e6=Entry(textvariable=t6,width="30")

    e1.place(x=15,y=110)
    e2.place(x=15,y=180)
    e3.place(x=15,y=240)
    e4.place(x=15,y=300)
    e5.place(x=15,y=360)
    e6.place(x=15,y=420)

    register = Button(screen,text="Register",width="30",height="2",command=save_info,bg="#167d7f",fg="#ddffe7",font="Georgia 10")
    register.place(x=15,y=450)
    screen.mainloop()


