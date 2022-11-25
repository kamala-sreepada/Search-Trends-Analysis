import matplotlib.pyplot as plt
while True:
    print("1:Education")
    print("2:Food")
    print("3:Sports")
    print("4:Travel")
    print("5:Technology")
    print("6:Entertainment")
    print("7:I'm done!")
    a=eval(input("PICK A TOPIC:"))
    if a==1:
        while True:
            print("1:Past month")
            print("2:Overall")
            print("3:I'm done")
            b=eval(input("PICK A TIME RANGE:"))
            if b==1:
                f2=open("edumon.txt","r")
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
                plt.plot(t,w,label="Math")
                plt.plot(t,y,label="Physics")
                plt.plot(t,q,label="Chemistry")
                plt.plot(t,b,label="Computer Science")
                plt.xlabel("Dates")
                plt.ylabel("Interest over time")
                plt.title("MONTHLY EDUCATION TRENDS")
                plt.legend()
                plt.show()
            elif b==2:
                f2=open("eduyear.txt","r")
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
                plt.plot(t,w,label="Math")
                plt.plot(t,y,label="Physics")
                plt.plot(t,q,label="Chemistry")
                plt.plot(t,b,label="Computer Science")
                plt.xlabel("Years")
                plt.ylabel("Interest over time")
                plt.title("ANNUAL EDUCATION TRENDS")
                plt.legend()
                plt.show()
            elif b==3:
                break
    elif a==2:
        while True:
            print("1:Past month")
            print("2:Overall")
            print("3:I'm done")
            b=eval(input("PICK A TIME RANGE:"))
            if b==1:
                f2=open("foodmon.txt","r")
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
                plt.plot(t,w,label="Chinese")
                plt.plot(t,y,label="Indian")
                plt.plot(t,q,label="Mexican")
                plt.plot(t,b,label="Italian")
                plt.xlabel("Dates")
                plt.ylabel("Interest over time")
                plt.title("MONTHLY FOOD TRENDS")
                plt.legend()
                plt.show()
            elif b==2:
                f2=open("foodyear.txt","r")
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
                plt.plot(t,w,label="Chinese")
                plt.plot(t,y,label="Indian")
                plt.plot(t,q,label="Mexican")
                plt.plot(t,b,label="Italian")
                plt.xlabel("Years")
                plt.ylabel("Interest over time")
                plt.title("ANNUAL FOOD TRENDS")
                plt.legend()
                plt.show()
            else:
                break
    elif a==3:
        while True:
            print("1:Past month")
            print("2:Overall")
            print("3:I'm done")
            b=eval(input("PICK A TIME RANGE:"))
            if b==1:
                f2=open("sportsmon.txt","r")
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
                plt.plot(t,w,label="Football")
                plt.plot(t,y,label="Basketball")
                plt.plot(t,q,label="Cricket")
                plt.plot(t,b,label="Tennis")
                plt.xlabel("Dates")
                plt.ylabel("Interest over time")
                plt.title("MONTHLY SPORTS TRENDS")
                plt.legend()
                plt.show()
            elif b==2:
                f2=open("sportsyear.txt","r")
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
                plt.plot(t,w,label="Football")
                plt.plot(t,y,label="Basketball")
                plt.plot(t,q,label="Cricket")
                plt.plot(t,b,label="Tennis")
                plt.xlabel("Years")
                plt.ylabel("Interest over time")
                plt.title("ANNUAL SPORTS TRENDS")
                plt.legend()
                plt.show()
            else:
                break
    elif a==4:
        while True:
            print("1:Past month")
            print("2:Overall")
            print("3:I'm done")
            b=eval(input("PICK A TIME RANGE:"))
            if b==1:
                f2=open("travelmon.txt","r")
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
                plt.plot(t,w,label="United States")
                plt.plot(t,y,label="India")
                plt.plot(t,q,label="Europe")
                plt.plot(t,b,label="Africa")
                plt.plot(t,s,label="China")
                plt.xlabel("Dates")
                plt.ylabel("Interest over time")
                plt.title("MONTHLY TRAVEL TRENDS")
                plt.legend()
                plt.show()
            elif b==2:
                f2=open("travelyear.txt","r")
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
                plt.plot(t,w,label="United States")
                plt.plot(t,y,label="India")
                plt.plot(t,q,label="Europe")
                plt.plot(t,b,label="Africa")
                plt.plot(t,s,label="China")
                plt.xlabel("Years")
                plt.ylabel("Interest over time")
                plt.title("ANNUAL TRAVEL TRENDS")
                plt.legend()
                plt.show()
            else:
                break
    elif a==5:
        while True:
            print("1:Social Media")
            print("2:Tech Giants")
            print("3:I'm done!")
            g=eval(input("PICK A TOPIC:"))
            if g==1:
                while True:
                    print("1:Past month")
                    print("2:Overall")
                    print("3:I'm done!")
                    b=eval(input("PICK A TIME RANGE:"))
                    if b==1:
                        f2=open("socialmon.txt","r")
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
                        plt.plot(t,w,label="Instagram")
                        plt.plot(t,y,label="Facebook")
                        plt.plot(t,q,label="Twitter")
                        plt.plot(t,b,label="Whatsapp")
                        plt.xlabel("Dates")
                        plt.ylabel("Interest over time")
                        plt.title("MONTHLY SOCIAL MEDIA TRENDS")
                        plt.legend()
                        plt.show()
                    elif b==2:
                        f2=open("socialyear.txt","r")
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
                        plt.plot(t,w,label="Instagram")
                        plt.plot(t,y,label="Facebook")
                        plt.plot(t,q,label="Twitter")
                        plt.plot(t,b,label="Whatsapp")
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL SOCIAL MEDIA TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
            elif g==2:
                while True:
                    print("1:Past month")
                    print("2:Overall")
                    print("3:I'm done!")
                    b=eval(input("PICK A TIME RANGE:"))
                    if b==1:
                        f2=open("techmon.txt","r")
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
                        plt.plot(t,w,label="Apple")
                        plt.plot(t,y,label="Microsoft")
                        plt.plot(t,q,label="Netflix")
                        plt.plot(t,b,label="Amazon")
                        plt.plot(t,s,label="Google")
                        plt.xlabel("Dates")
                        plt.ylabel("Interest over time")
                        plt.title("MONTHLY TECH TRENDS")
                        plt.legend()
                        plt.show()
                    elif b==2:
                        f2=open("techyear.txt","r")
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
                        plt.plot(t,w,label="Apple")
                        plt.plot(t,y,label="Microsoft")
                        plt.plot(t,q,label="Netflix")
                        plt.plot(t,b,label="Amazon")
                        plt.plot(t,s,label="Google")
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL TECH TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
            else:
                break
    elif a==6:
        while True:
            print("1:Music")
            print("2:Movies")
            print("3:Games")
            print("4:I'm done!")
            g=eval(input("PICK A TOPIC:"))
            if g==1:
                while True:
                    print("1:Past month")
                    print("2:Overall")
                    print("3:I'm done!")
                    b=eval(input("PICK A TIME RANGE:"))
                    if b==1:
                        f2=open("musicmon.txt","r")
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
                        plt.plot(t,w,label="Pop")
                        plt.plot(t,y,label="Hip Hop")
                        plt.plot(t,q,label="Country")
                        plt.plot(t,b,label="Rock")
                        plt.plot(t,s,label="Classical")
                        plt.xlabel("Dates")
                        plt.ylabel("Interest over time")
                        plt.title("MONTHLY MUSIC TRENDS")
                        plt.legend()
                        plt.show()
                    elif b==2:
                        f2=open("musicyear.txt","r")
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
                        plt.plot(t,w,label="Pop")
                        plt.plot(t,y,label="Hip Hop")
                        plt.plot(t,q,label="Country")
                        plt.plot(t,b,label="Rock")
                        plt.plot(t,s,label="Classical")
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL MUSIC TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
            elif g==2:
                while True:
                    print("1:Past month")
                    print("2:Overall")
                    print("3:I'm done!")
                    b=eval(input("PICK A TIME RANGE:"))
                    if b==1:
                        f2=open("moviemon.txt","r")
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
                        plt.plot(t,w,label="English")
                        plt.plot(t,y,label="Hindi")
                        plt.plot(t,q,label="Arabic")
                        plt.plot(t,b,label="Korean")
                        plt.xlabel("Dates")
                        plt.ylabel("Interest over time")
                        plt.title("MONTHLY MOVIE TRENDS")
                        plt.legend()
                        plt.show()
                    elif b==2:
                        f2=open("movieyear.txt","r")
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
                        plt.plot(t,w,label="English")
                        plt.plot(t,y,label="Hindi")
                        plt.plot(t,q,label="Arabic")
                        plt.plot(t,b,label="Korean")
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL MOVIE TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
            elif g==3:
                while True:
                    print("1:Past month")
                    print("2:Overall")
                    print("3:I'm done!")
                    b=eval(input("PICK A TIME RANGE:"))
                    if b==1:
                        f2=open("gamemon.txt","r")
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
                        plt.plot(t,w,label="Fortnite")
                        plt.plot(t,y,label="Minecraft")
                        plt.plot(t,q,label="Call of Duty")
                        plt.plot(t,b,label="Pokemon Go")
                        plt.plot(t,s,label="Grand Theft Auto")
                        plt.xlabel("Dates")
                        plt.ylabel("Interest over time")
                        plt.title("MONTHLY GAMING TRENDS")
                        plt.legend()
                        plt.show()
                    elif b==2:
                        f2=open("gameyear.txt","r")
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
                        plt.plot(t,w,label="Fortnite")
                        plt.plot(t,y,label="Minecraft")
                        plt.plot(t,q,label="Call of Duty")
                        plt.plot(t,b,label="Pokemon Go")
                        plt.plot(t,s,label="Grand Theft Auto")
                        plt.xlabel("Years")
                        plt.ylabel("Interest over time")
                        plt.title("ANNUAL GAMING TRENDS")
                        plt.legend()
                        plt.show()
                    else:
                        break
                
            else:
                break
    else:
        break

        
            
        
                
                                
