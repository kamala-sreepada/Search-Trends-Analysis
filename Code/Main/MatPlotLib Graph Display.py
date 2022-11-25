import matplotlib.pyplot as plt
from tkinter import *
import Project
import os
lab=""
while True:
    print("1:Show Google Trends")
    print("2:Edit Google Trends")
    aa=eval(input("ENTER CHOICE:"))
    if aa==1:
        while True:
            print("1:Education")
            print("2:Food")
            print("3:Sports")
            print("4:Social Media")
            print("5:Entertainment")
            print("6:I'm done!")
            a=eval(input("PICK A TOPIC:"))
            if a==1:
                while True:
                    v=[]
                    print("1:Overall")
                    print("2:I'm done")
                    b=eval(input("PICK:"))
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
                            if lab!="":
                                v=r[5]
                            else:
                                continue
                        plt.plot(t,w,label="Math")
                        plt.plot(t,y,label="Physics")
                        plt.plot(t,q,label="Chemistry")
                        if v!=[]:
                            plt.plot(t,v,label=lab)
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
                            if lab!="":
                                v=r[5]
                            else:
                                continue
                        plt.plot(t,w,label="Chinese")
                        plt.plot(t,y,label="Indian")
                        plt.plot(t,q,label="Mexican")
                        plt.plot(t,b,label="Italian")
                        if v!=[]:
                            plt.plot(t,v,label=lab)
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
                            if lab!="":
                                v=r[5]
                            else:
                                continue
                        plt.plot(t,w,label="Football")
                        plt.plot(t,y,label="Basketball")
                        plt.plot(t,q,label="Cricket")
                        plt.plot(t,b,label="Tennis")
                        if v!=[]:
                            plt.plot(t,v,label=lab)
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
                            if lab!="":
                                v=r[5]
                            else:
                                continue
                        plt.plot(t,w,label="Instagram")
                        plt.plot(t,y,label="Facebook")
                        plt.plot(t,q,label="Twitter")
                        plt.plot(t,b,label="Whatsapp")
                        if v!=[]:
                            plt.plot(t,v,label=lab)
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
                    if g==1:
                        while True:
                            v=[]
                            print("1:Overall")
                            print("2:I'm done!")
                            b=eval(input("PICK:"))
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
                                    s=r[5]
                                    if lab!="":
                                        v=r[6]
                                    else:
                                        continue
                                plt.plot(t,w,label="Pop")
                                plt.plot(t,y,label="Hip Hop")
                                plt.plot(t,q,label="Country")
                                plt.plot(t,b,label="Rock")
                                plt.plot(t,s,label="Classical")
                                if v!=[]:
                                    plt.plot(t,v,label=lab)
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
                                    if lab!="":
                                        v=r[5]
                                    else:
                                        continue
                                plt.plot(t,w,label="English")
                                plt.plot(t,y,label="Hindi")
                                plt.plot(t,q,label="Arabic")
                                plt.plot(t,b,label="Korean")
                                if v!=[]:
                                    plt.plot(t,v,label=lab)
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
            yo=eval(input("PICK:"))
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
                    if n in [1,2,3,4,5,6]:
                        lab=input("NAME OF SUBTOPIC:")
                        Project.thewholething(n)
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
                    if n in [1,2,3,4,5,6]:
                        t=input("ENTER YEAR TO BE UPDATED:")
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
                        print(h)
                        for i in range(1,5):
                            k=open("newvalue.txt","r")
                            p=k.readlines()
                            print(p)
                            h[i][bb]=p[i-1][:1]
                        print(h)
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
                            
                
            else:
                break
    else:
        break
 
        
        


