import matplotlib.pyplot as plt
from tkinter import *
import Project
import os
import mysql.connector
lab1=""
lab2=""
lab3=""
lab4=""
lab5=""
lab6=""
obj=mysql.connector.connect(host="localhost",database="feedback",user="root",password="aka2003*")
c=obj.cursor()
c.execute("use feedback")
'''c.execute("create table trends(UserID integer primary key,Review varchar(100),Rate integer check(rate>=0 and rate<=5))")'''
while True:
    print("1:Show Google Trends")
    print("2:Edit Google Trends")
    print("3:User Review")
    print("4:Exit")
    aa=eval(input("ENTER CHOICE:"))
    print()
    if aa==1:
        while True:
            print("1:Education")
            print("2:Food")
            print("3:Sports")
            print("4:Social Media")
            print("5:Entertainment")
            print("6:I'm done!")
            a=eval(input("PICK A TOPIC:"))
            print()
            if a==1:
                while True:
                    v=[]
                    print("1:Overall")
                    print("2:I'm done")
                    b=eval(input("PICK:"))
                    print()
                    if b==1:
                        f2=open("1.txt","r")
                        x=f2.readlines()
                        r=[]
                        for i in x:
                            d=i.split()
                            e=[]
                            for j in d:
                                e.append(int(j))
                            r.append(e)
                        for i in r:
                            t=r[0]
                            w=r[1]
                            y=r[2]
                            q=r[3]
                            b=r[4]
                            if lab1!="":
                                v=r[5]
                            else:
                                continue
                        plt.plot(t,w,label="Math")
                        plt.plot(t,y,label="Physics")
                        plt.plot(t,q,label="Chemistry")
                        if v!=[]:
                            plt.plot(t,v,label=lab1)
                        plt.plot(t,b,label="Computer Science")
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL EDUCATION TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
            elif a==2:
                while True:
                    v=[]
                    print("1:Overall")
                    print("2:I'm done")
                    b=eval(input("PICK:"))
                    print()
                    if b==1:
                        f2=open("2.txt","r")
                        x=f2.readlines()
                        r=[]
                        for i in x:
                            d=i.split()
                            e=[]
                            for j in d:
                                e.append(int(j))
                            r.append(e)
                        for i in r:
                            t=r[0]
                            w=r[1]
                            y=r[2]
                            q=r[3]
                            b=r[4]
                            if lab2!="":
                                v=r[5]
                            else:
                                continue
                        plt.plot(t,w,label="Chinese")
                        plt.plot(t,y,label="Indian")
                        plt.plot(t,q,label="Mexican")
                        plt.plot(t,b,label="Italian")
                        if v!=[]:
                            plt.plot(t,v,label=lab2)
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL FOOD TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
            elif a==3:
                while True:
                    v=[]
                    print("1:Overall")
                    print("2:I'm done")
                    b=eval(input("PICK:"))
                    print()
                    if b==1:
                        f2=open("3.txt","r")
                        x=f2.readlines()
                        r=[]
                        for i in x:
                            d=i.split()
                            e=[]
                            for j in d:
                                e.append(int(j))
                            r.append(e)
                        for i in r:
                            t=r[0]
                            w=r[1]
                            y=r[2]
                            q=r[3]
                            b=r[4]
                            if lab3!="":
                                v=r[5]
                            else:
                                continue
                        plt.plot(t,w,label="Football")
                        plt.plot(t,y,label="Basketball")
                        plt.plot(t,q,label="Cricket")
                        plt.plot(t,b,label="Tennis")
                        if v!=[]:
                            plt.plot(t,v,label=lab3)
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL SPORTS TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
            elif a==4:
                while True:
                    v=[]
                    print("1:Social Media")
                    print("2:I'm done!")
                    b=eval(input("PICK:"))
                    print()
                    if b==1:
                        f2=open("4.txt","r")
                        x=f2.readlines()
                        r=[]
                        for i in x:
                            d=i.split()
                            e=[]
                            for j in d:
                                e.append(int(j))
                            r.append(e)
                        for i in r:
                            t=r[0]
                            w=r[1]
                            y=r[2]
                            q=r[3]
                            b=r[4]
                            if lab4!="":
                                v=r[5]
                            else:
                                continue
                        plt.plot(t,w,label="Instagram")
                        plt.plot(t,y,label="Facebook")
                        plt.plot(t,q,label="Twitter")
                        plt.plot(t,b,label="Whatsapp")
                        if v!=[]:
                            plt.plot(t,v,label=lab4)
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL SOCIAL MEDIA TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
            elif a==5:
                while True:
                    print("1:Music")
                    print("2:Movies")
                    print("3:I'm done!")
                    g=eval(input("PICK A TOPIC:"))
                    print()
                    if g==1:
                        while True:
                            v=[]
                            print("1:Overall")
                            print("2:I'm done!")
                            b=eval(input("PICK:"))
                            print()
                            if b==1:
                                f2=open("5.txt","r")
                                x=f2.readlines()
                                r=[]
                                for i in x:
                                    d=i.split()
                                    e=[]
                                    for j in d:
                                        e.append(int(j))
                                    r.append(e)
                                for i in r:
                                    t=r[0]
                                    w=r[1]
                                    y=r[2]
                                    q=r[3]
                                    b=r[4]
                                    if lab5!="":
                                        v=r[5]
                                    else:
                                        continue
                                plt.plot(t,w,label="Pop")
                                plt.plot(t,y,label="Hip Hop")
                                plt.plot(t,q,label="Rock")
                                plt.plot(t,b,label="Classical")
                                if v!=[]:
                                    plt.plot(t,v,label=lab5)
                                plt.xlabel("Years")
                                plt.ylabel("Interest over time")
                                plt.title("ANNUAL MUSIC TRENDS")
                                plt.legend()
                                plt.show()
                            else:
                                break
                    elif g==2:
                        while True:
                            v=[]
                            print("1:Overall")
                            print("2:I'm done!")
                            b=eval(input("PICK:"))
                            print()
                            if b==1:
                                f2=open("6.txt","r")
                                x=f2.readlines()
                                r=[]
                                for i in x:
                                    d=i.split()
                                    e=[]
                                    for j in d:
                                        e.append(int(j))
                                    r.append(e)
                                for i in r:
                                    t=r[0]
                                    w=r[1]
                                    y=r[2]
                                    q=r[3]
                                    b=r[4]
                                    if lab6!="":
                                        v=r[5]
                                    else:
                                        continue
                                plt.plot(t,w,label="English")
                                plt.plot(t,y,label="Hindi")
                                plt.plot(t,q,label="Arabic")
                                plt.plot(t,b,label="Korean")
                                if v!=[]:
                                    plt.plot(t,v,label=lab6)
                                plt.xlabel("Years")
                                plt.ylabel("Interest over time")
                                plt.title("ANNUAL MOVIE TRENDS")
                                plt.legend()
                                plt.show()
                            else:
                                break
                    else:
                        break
            else:
                break
    elif aa==2:
        while True:
            print("1:Add")
            print("2:Update")
            print("3:Delete")
            print("4:I'm done!")
            yo=eval(input("PICK:"))
            print()
            if yo==1:
                while True:
                    print("1:Education")
                    print("2:Food")
                    print("3:Sports")
                    print("4:Social Media")
                    print("5:Music")
                    print("6:Movies")
                    print("7:I'm done!")
                    n=eval(input("PICK A TOPIC: "))
                    print()
                    if n==1:
                        lab1=input("NAME OF SUBTOPIC:")
                        print()
                        Project.form(n)
                    elif n==2:
                        lab2=input("NAME OF SUBTOPIC:")
                        print()
                        Project.form(n)
                    elif n==3:
                        lab3=input("NAME OF SUBTOPIC:")
                        print()
                        Project.form(n)
                    elif n==4:
                        lab4=input("NAME OF SUBTOPIC:")
                        print()
                        Project.form(n)
                    elif n==5:
                        lab5=input("NAME OF SUBTOPIC:")
                        print()
                        Project.form(n)
                    elif n==6:
                        lab6=input("NAME OF SUBTOPIC:")
                        print()
                        Project.form(n)
                    else:
                        break
            elif yo==2:
                while True:
                    print("1:Education")
                    print("2:Food")
                    print("3:Sports")
                    print("4:Social Media")
                    print("5:Music")
                    print("6:Movies")
                    print("7:I'm done!")
                    n=eval(input("PICK A TOPIC: "))
                    print()
                    if n in [1,2,3,4,5,6]:
                        t=input("ENTER YEAR TO BE UPDATED:")
                        print()
                        if t=="2010":
                            bb=0
                        elif t=="2012":
                            bb=1
                        elif t=="2014":
                            bb=2
                        elif t=="2016":
                            bb=3
                        elif t=="2018":
                            bb=4
                        else:
                            bb=5
                        f=open("topics.txt","r")
                        x=f.readlines()
                        l=x[n-1].split()
                        k=open("newvalue.txt","w")
                        for i in l:
                            m=input(i)
                            k.write(m+"\n")
                        k.close()
                        j=open(str(n)+".txt","r+")
                        b=j.readlines()
                        h=[]
                        for i in b:
                            o=i.split()
                            h.append(o)
                        for i in range(1,5):
                            k=open("newvalue.txt","r")
                            p=k.readlines()
                            h[i][bb]=p[i-1][:-1]
                        ww=open("11.txt","w")
                        for i in h:
                            for j in i:
                                ww.write(j+" ")
                            ww.write("\n")
                        ww.close()
                        os.remove(str(n)+".txt")
                        os.rename("11.txt",str(n)+".txt")
                    else:
                        break
            elif yo==3:
                while True:
                    print("1:Education")
                    print("2:Food")
                    print("3:Sports")
                    print("4:Social Media")
                    print("5:Music")
                    print("6:Movies")
                    print("7:I'm done!")
                    n=eval(input("PICK A TOPIC: "))
                    print()
                    if n in [1,2,3,4,5,6]:
                        t=input("ENTER YEAR TO BE DELETED:")
                        if t=="2010":
                            d=0
                        elif t=="2012":
                            d=1
                        elif t=="2014":
                            d=2
                        elif t=="2016":
                            d=3
                        elif t=="2018":
                            d=4
                        else:
                            d=5
                        print()
                        f=open(str(n)+".txt","r")
                        h=[]
                        x=f.readlines()
                        for i in x:
                            b=i.split()
                            h.append(b)
                        for j in range(1,5):
                            h[j][d]="0"
                        ww=open("news.txt","w")
                        for i in h:
                            for j in i:
                                ww.write(j+" ")
                            ww.write("\n")
                        ww.close()
                        f.close()
                        os.remove(str(n)+".txt")
                        os.rename("news.txt",str(n)+".txt")
                    else:
                        break            
                
            else:
                break
    elif aa==3:
        userid=eval(input("Enter UserID: "))
        rev=input("Enter review: ")
        rate=eval(input("Rate your experience: "))
        c.execute("insert into trends values(%s,%s,%s)",(userid,rev,rate))
        obj.commit()
        while True:
            print("1:Display review table")
            print("2:Change rating and review")
            print("3:Delete your review")
            print("4:Exit")
            ccc=eval(input("Choose an option:"))
            if ccc==1:
                c=obj.cursor()
                c.execute("select * from trends")
                l=c.fetchall()
                for x in l:
                    print(x)
                    print()
                c.close()
            elif ccc==2:
                uus=eval(input("Enter UserID:"))
                rate=eval(input("Rate change:"))
                review=input("Review change:")
                c=obj.cursor()
                q="update trends set Rate=%s where UserID=%s"
                w="update trends set Review=%s where UserID=%s"
                c.execute(q,(rate,uus))
                c.execute(w,(review,uus))
                obj.commit()
                c.close()
            elif ccc==3:
                uus=eval(input("Enter UserID: "))
                c=obj.cursor()
                c.execute("delete from trends where UserID=%s",(uus,))
                obj.commit()
                c.close()
            else:
                break
    else:
        break
c.close()
obj.close()
