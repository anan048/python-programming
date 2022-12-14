from tkinter import *
from PIL import Image, ImageTk
import csv
from os import system
import random
import time

class Karakter:
    def __init__(self, name, hp, attack, photo, index):
        HP=hp
        self._name = name
        self._hp = hp
        self._attack = attack
        self._photo = ImageTk.PhotoImage(Image.open(photo).resize((200,200)))
        self._index = index
    
    def getName(self):
        return self._name

    def getHp(self):
        return self._hp
    
    def getattack(self):
        return self._attack
    def getIndex(self):
        return self._index
    def setHp(self, hp):
        self._hp = hp
    def getPhoto(self):
        return self._photo
    def memukul(self, musuh):
        musuh.setHp(musuh.getHp() - self._attack)
        print(self._name + " memukul " + musuh.getName() + ". HP " + musuh.getName() + ": " + str(musuh.getHp()))
        if musuh.getHp() <= 0:
            print(musuh.getName() + " sudah kalah")
 


root = Tk()
root.title("League of Slot")


def login():
    
    def tofrm2():
        frm.destroy()
        regist()
    
    def loginn():
        a = E1.get()
        b = E2.get()
        print(f"{a} {b}")
        c = 0
        with open('akun.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if  a == row['NAMA'] and b == row ['PASSWORD']:
                    frm.destroy()
                    c=1
                    mulai(a)
        if c == 0 and a != ""  and b != "":
            hasil.config(text="Username or password incorrect")
        elif a == "" or b == "":
            hasil.config(text="Username or password is required")

        
    frm = Frame(root)
    frm.pack(pady=20, padx=10)
    
    Label(frm,text="Username").grid(column=0, row=0, sticky= N)
    
    var = StringVar()
    E1=Entry(frm, textvariable=var)
    E1.grid(column=0, row=2, sticky=EW)
    
    Label(frm,text="Password").grid(column=0, row=4, sticky= N)
    
    var2 = StringVar()
    E2=Entry(frm, textvariable=var2)
    E2.grid(column=0, row=6, sticky=EW)
    
    B1=Button(frm, text='login', command=loginn)
    B1.grid(column=0, row=8)
    
    
    register = Button(frm, text='register', fg='black', bd=0, command=tofrm2, activeforeground='grey')
    
    register.grid(column= 0, row= 10)
    hasil = Label(frm)
    hasil.grid(row = 11)
    
def mulai(akun):
    def next():
        frm1.destroy()
        play(akun)
    def exit():
        root.destroy()
    frm1 = Frame(root)
       
    frm1.pack(pady=20, padx=10)
    Button(frm1, text= 'Play', command=next).grid(row=0)
    Button(frm1, text= 'exit', command=exit).grid(row=1)
    
def play(akun):
    party=[]
    partyl=[]
    champion=[]
    button=[]
    index=0
    
    frame1 = Frame(root)
    frame1.pack(pady=20, padx=10)
    frame2 = Frame(root)
    frame2.pack(pady=20, padx=10, side=BOTTOM)
    
    Label(frame2, text='Party:').grid(sticky=EW, columnspan=4, row=0)
    
    with open('pa.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['USER'] == akun:
                champion.append(Karakter(row['NAMA'],int(row['HP']) , int(row['ATTACK']), row['PHOTO'], index))
      
    def masuk(z):
        
        if champion[z].getName() not in party:
            party.append(champion[z].getName())
            partyl[len(party)-1].config(image=champion[z]._photo)
        
            
    def find(party):
        if len(party) >= 3:
            frame1.destroy()
            frame2.destroy()
            findmatch(party, akun)
    
   
    for k in range(3):
        partyl.append(Label(frame2))
        partyl[k].grid(row=1, column=k)
    l=0    
    for j in range(len(champion)):
        
        button.append(Button(frame1, image=champion[j]._photo, bd=0, command=lambda n=j:masuk(n)))
        button[j].grid(row=0, column=l)
        Label(frame1, text='HP: '+str(champion[j].getHp())+'\nAttack: '+str(champion[j].getattack()), justify='left').grid(row=0, column=l+1)
        l=l+2
    
    Button(frame2, text='find match', command=lambda:find(party)).grid(row=2, columnspan=3)
    
    
def findmatch(party, akun):
    
    ally=[]
    enemy=[]
    bot=[]
    with open('pa.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['NAMA'] in party and row['USER']== akun:
                a=int(row['HP'])
                b=int(row['ATTACK'])
                c=row['USER']
                ally.append(Karakter(row['NAMA'], a, b, row['PHOTO'], 0))
                
    with open('pa.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['USER'] != akun and row['USER'] not in bot:
                bot.append(row['USER'])
    
    get = random.choice(bot)
    
    with open('pa.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader: 
            if row['USER'] == get:
                enemy.append(Karakter(row['NAMA'], int(row['HP']), int(row['ATTACK']), row['PHOTO'], 0))
                
    if len(enemy) >3:
        while 2>1:
            if len(enemy) == 3:
                break
            enemy.remove(random.choice(enemy))
            
    
    pilih=[0,1,2]
    pilihe=[0,1,2]
    label=[]
    button=[]
    labele=[] 

        
    def pukul(i, j):
        def back():
            hasil.destroy()
            mulai(akun)
        
        ally[i].memukul(enemy[j])
        labele[j].configure(text='HP: '+str(enemy[j].getHp())+'\nAttack: '+str(enemy[j].getattack()), justify='left')
        
        time.sleep(1)
        for i in pilihe:
            pen[i].config(bg='#F0F0F0')
        for i in pilih:
            button[i].config(bg='#F0F0F0')
            
        time.sleep(1)
        pen[j].config(bg='red')
        time.sleep(2)
        
        randally=random.choice(pilih)
        randenemy = random.choice(pilihe)
        enemy[randenemy].memukul(ally[randally])
        label[randally].config(text='HP: '+str(ally[randally].getHp())+'\nAttack: '+str(ally[randally].getattack()), justify='left')
        
        pen[randenemy].config(bg='blue')
        time.sleep(1)
        button[randally].config(bg='red')
        
        if enemy[j]._hp <= 0:
            pilihe.remove(j)
            labele[j].destroy()
            pen[j].destroy()
            
        if ally[randally]._hp <= 0:
            pilih.remove(randally)
            label[randally].destroy()
            button[randally].destroy()
            
            
        if len(pilih)==0 and len(pilihe)==0:
            main.destroy()
            Label(hasil, text="Draw", font=100).grid(row=0)
            Button(hasil, text="Continue", command=back).grid(row=1)
        if len(pilih)==0:
            main.destroy()
            Label(hasil, text="Defeat", font=100).grid(row=0)
            Button(hasil, text="Continue", command=back).grid(row=1)
        elif len(pilihe)==0:
            main.destroy()
            Label(hasil, text="Victory", font=100).grid(row=0)
            Button(hasil, text="Continue", command=back).grid(row=1)
            
    
    main = Frame(root)
    main.pack(pady=20, padx=10)
    hasil = Frame(root)
    hasil.pack(pady=20, padx=10)
    Label(main, text="", width=20).grid(row=0, column=1)
    Label(main, text=c, width=10).grid(row=0, column=0)
    Label(main, text=get, width=10, justify=CENTER).grid(row=0, column=3)
    
    for i in range(len(ally)):
        label.append(Label(main, text='HP: '+str(ally[i].getHp())+'\nAttack: '+str(ally[i].getattack()), justify='left'))
        label[i].grid(column=1)
        button.append(Button(main, image=ally[i]._photo, bd=0, activebackground='blue', command=lambda:pukul(i, random.choice(pilihe))))
        button[i].grid(row=i+1, column=0)
           
    for i in range(len(enemy)):
        labele.append(Label(main, text='HP: '+str(enemy[i].getHp())+'\nAttack: '+str(enemy[i].getattack()), justify='left'))
        labele[i].grid(row=i+1, column=4)
        
    pen=[]
    for i in range(len(enemy)):
        pen.append(Label(main, image=enemy[i]._photo, bd=0))
        pen[i].grid(row=i+1, column=3)
    
   
def regist():
    def tofrm():
        frm2.destroy()
        login()
        
    def reg():
        a = E1.get()
        b = E2.get()
        c = E3.get()
        d = 0
        karak=[]
        pilih=[]
        nama = ''
        HP = ''
        attack = ''
        photo = ''
        with open('akun.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if  a == row['NAMA'] :
                    d = 1
                    
        if a == "" or b == "" or c=="":
            msg.config(text="Username or password is required")
        if d == 1:
            msg.config(text='Username is already exist')
        else:
            if c != b:
                msg.config(text='Password incorrect')
            
            with open('karakter.csv', 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    karak.append(row['NAMA'])
           
            for i in range(3):
                random.shuffle(karak)
                p = karak.pop()
                
                pilih.append(p)
                
                with open('karakter.csv', 'r') as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        if row['NAMA']== pilih[i]:
                            nama = row['NAMA']
                            HP =  row['HP']
                            attack = row['ATTACK']
                            photo = row['PHOTO']
                            print(i)
                with open("pa.csv", "a", newline="") as file:
                    writer = csv.writer(file)
            
                    writer.writerow([nama, HP, attack, a, photo])
                    
            with open("akun.csv", "a", newline="") as file:
                writer = csv.writer(file)
        
                writer.writerow([a, b])

            frm2.destroy()        
            mulai(a)
            
    frm2 = Frame(root)
    frm2.pack(pady=20, padx=10)
    
    Label(frm2,text="Username").grid(column=0, row=0, sticky= N)
    
    var = StringVar()
    E1=Entry(frm2, textvariable=var)
    E1.grid(column=0, row=2, sticky=EW)
    
    Label(frm2,text="Password").grid(column=0, row=4, sticky= N)
    
    var2 = StringVar()
    E2=Entry(frm2, textvariable=var2)
    E2.grid(column=0, row=6, sticky=EW)
    
    Label(frm2,text="Confirm Password").grid(column=0, row=7, sticky= N)
    
    var3 = StringVar()
    E3=Entry(frm2, textvariable=var3)
    E3.grid(column=0, row=8, sticky=EW)
    
    B1=Button(frm2, text='register', command=reg)
    B1.grid(column=0, row=9)
    
    loginn = Button(frm2, text='login', fg='black', bd=0, command=tofrm, activeforeground='grey')
    
    loginn.grid(column= 0, row= 10)
    msg = Label(frm2)
    msg.grid(row=12)
    
 
login()

root.mainloop()
