from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import random
import sys



class LoginWindow(Frame):
    catchUser=0

    def __init__(self,parent):
        self.parent=parent
        self.parent.title('Математичні тренування')
        self.parent.configure(background="#DAFF75")
        self.parent.resizable(False, False) #stop resizing window
        self.centeredWindow()
        self.loginFrame()
        #self.parent.wm_attributes('-alpha', 0.7) # transparent window

    def loginFrame(self):
        #variables
        self.inputedLogin=StringVar()
        self.inputedPassword=StringVar()
        
        self.infoText=StringVar()
        self.infoText.set('')
        #Frame
        self.loginFrame=Frame(self.parent,background="#DFEBD4",width=380,height=370)
        self.loginFrame.pack()
        self.loginFrame.place(x=60,y=80)

        self.buttonsFrame=Frame(self.loginFrame,background="#DFEBD4", width=80,height=300)
        self.buttonsFrame.pack()
        self.buttonsFrame.place(x=4,y=240)

        self.createButton=Button(self.buttonsFrame, text="Створити",font="Times 19",background="#00b2d9", command=self.userForm)
        self.createButton.pack(side="left",padx=30)   

        self.signButton=Button(self.buttonsFrame, text="Увійти",font="Times 19",background="#00b2d9", width=8,command=self.checkLogin)
        self.signButton.pack(side="left",padx=30)  

        self.authorizeLabel=Label(self.parent, text="Авторизація",bg='#DFEBD4',font="Times 24")
        self.authorizeLabel.pack()
        self.authorizeLabel.place(x=160,y=115)

        self.authorizeLabel=Label(self.parent, text="Логін:",bg='#DFEBD4',fg='red',font="Times 14")
        self.authorizeLabel.pack()
        self.authorizeLabel.place(x=92,y=158)

        self.authorizeLabel=Label(self.parent, text="Пароль:",bg='#DFEBD4',fg='red',font="Times 14")
        self.authorizeLabel.pack()
        self.authorizeLabel.place(x=92,y=228)

        self.load = Image.open("D:\\PythonSoft\\Lv-416.PythonCore\\myGame\\roman\\loginIcon3.png").resize((120,100))
        self.img = ImageTk.PhotoImage(self.load)
        self.imageLabel=Label(self.parent,image=self.img)
        self.imageLabel.configure(width=70,height=75)
        self.imageLabel.image=self.img
        self.imageLabel.place(x=210,y=35)

        self.enterLogin=Entry(self.parent,font="Times 28",width=16,textvariable=self.inputedLogin)
        self.enterLogin.pack()
        self.enterLogin.place(x=95,y=180)

        self.enterPassword=Entry(self.parent,font="Times 28",width=16, textvariable=self.inputedPassword,show='*')
        self.enterPassword.pack()
        self.enterPassword.place(x=95,y=250)

        self.noUserL=Label(self.parent,background='#DFEBD4', foreground='red', textvariable=self.infoText,font='Times 20') 
        self.noUserL.pack(side='bottom')
        self.noUserL.place(x=130,y=395)
    
    def userForm(self):
        def on_entry_click_login(event):
            """function that gets called whenever entry is clicked"""
            if self.loginEntry.get() == 'Введіть логін тут':
                self.loginEntry.delete(0, "end") # delete all the text in the entry
                self.loginEntry.insert(0, '') #Insert blank for user input
                self.loginEntry.config(fg = 'black')

        def on_focusout_login(event):
            if self.loginEntry.get() == '':
                self.loginEntry.insert(0, "Введіть логін тут")
                self.loginEntry.config(fg = 'grey')

        def on_entry_click_password(event):    
            if self.passwordEntry.get() == 'Введіть пароль тут':
                self.passwordEntry.delete(0, "end") # delete all the text in the entry
                self.passwordEntry.insert(0, '') #Insert blank for user input
                self.passwordEntry.config(fg = 'black')

        def on_focusout_password(event):
            if self.passwordEntry.get() == '':
                self.passwordEntry.insert(0, "Введіть пароль тут")
                self.passwordEntry.config(fg = 'grey')
        
        self.userForm=Toplevel()
        self.userForm.title("Реєстрація")
        self.userForm.configure(background="#FF8080")
        window_width=300
        window_height=200
        screen_width=self.parent.winfo_screenwidth()
        screen_height=self.parent.winfo_screenheight()
        x_coordinate = (screen_width/2)-(window_width/2)
        y_coordinate = (screen_height/2-(window_height/2))
        self.userForm.geometry("%dx%d+%d+%d" % (window_width,window_height,x_coordinate,y_coordinate))
        
        #variables 
        self.userLogin=StringVar()
        self.userPassword=StringVar()
        
        self.userAddPoints=IntVar()
        self.userSubPoints=IntVar()
        self.userMultiPoints=IntVar()
        self.userDevPoints=IntVar()
        
        self.userAddPoints.set(0)
        self.userSubPoints.set(0)
        self.userMultiPoints.set(0)
        self.userDevPoints.set(0)
        
        #Frame
        self.contentFrame=Frame(self.userForm,background="#FF8080")
        self.contentFrame.pack()
        self.contentFrame.place(x=40,y=30)
        
        
        self.loginEntry=Entry(self.contentFrame,width=16,font="Times 20",textvariable=self.userLogin)
        self.loginEntry.grid(row=0,column=1,pady=10)
        self.loginEntry.insert(0, 'Введіть логін тут')
        self.loginEntry.bind('<FocusIn>', on_entry_click_login)
        self.loginEntry.bind('<FocusOut>', on_focusout_login)
        self.loginEntry.config(fg = 'grey')
        
        self.passwordEntry=Entry(self.contentFrame,width=16,font="Times 20",textvariable=self.userPassword)
        self.passwordEntry.grid(row=1,column=1)
        self.passwordEntry.insert(0, 'Введіть пароль тут')
        self.passwordEntry.bind('<FocusIn>', on_entry_click_password)
        self.passwordEntry.bind('<FocusOut>', on_focusout_password)
        self.passwordEntry.config(fg = 'grey')

        self.submit=Button(self.userForm,text="Підтвердити",font="Times 16",background="#00b2d9",command=self.signIn)
        self.submit.pack()
        self.submit.place(x=85,y=150)

    def signIn(self):
        self.dataLogin=self.userLogin.get()
        self.dataPassword=self.userPassword.get()
        self.dataAdd=self.userAddPoints.get()
        self.dataSub=self.userSubPoints.get()
        self.dataMulti=self.userMultiPoints.get()
        self.dataDev=self.userDevPoints.get()
        
        # looking in DB if user name exists
        self.conn=sqlite3.connect('D:\\readyProjects\\math\\MathUsers.db')
        with self.conn:    
            self.cur=self.conn.cursor()
            self.cur.execute('SELECT Login FROM MathUsersDB WHERE Login=? OR Password=?',(self.userLogin.get(),self.userPassword.get()))
            self.conn.commit()
        self.checkResult=self.cur.fetchone()#var hold result of hunting on query about name if it in DB
        
        if self.userLogin.get()=='Введіть логін тут' or self.userPassword.get()=='Введіть пароль тут':
            self.infoText.set("Пусте поле!")
        
        elif self.userLogin.get()=='' or self.userPassword.get()=='':
            self.infoText.set("Пусте поле!")
        
        elif self.userLogin.get()!='' and self.userPassword.get()!='':
            
            if self.checkResult:
                self.infoText.set("Користувач вже існує!")

            else:
                self.conn=sqlite3.connect('D:\\readyProjects\\math\\MathUsers.db')
                with self.conn:
                    cursor=self.conn.cursor()
                    cursor.execute('CREATE TABLE IF NOT EXISTS MathUsersDB(Login TEXT,Password TEXT,ScoreAdd INTEGER,ScoreSub INTEGER,ScoreMulti INTEGER,ScoreDev INTEGER)')
                    cursor.execute('INSERT INTO MathUsersDB (Login,Password,ScoreAdd,ScoreSub,ScoreMulti,ScoreDev) VALUES(?,?,?,?,?,?)',(self.dataLogin,self.dataPassword,self.dataAdd,self.dataSub,self.dataMulti,self.dataDev))
                    self.conn.commit()
                    self.infoText.set("Створено користувача!")
                self.userForm.destroy()

        
    def checkLogin(self):
    
        self.conn=sqlite3.connect('D:\\readyProjects\\math\\MathUsers.db')
        with self.conn:    
            self.cur=self.conn.cursor()
            self.cur.execute('SELECT Login,Password,ScoreAdd,ScoreSub,ScoreMulti,ScoreDev FROM MathUsersDB WHERE Login=? AND Password=?',(self.inputedLogin.get(),self.inputedPassword.get()))
            self.conn.commit()
        self.catchResult=self.cur.fetchone()#finded info about user if it is in DB
        LoginWindow.catchUser=self.catchResult
        print("catchUser is ",LoginWindow.catchUser)
        AdditionWindow.userLogined=LoginWindow.catchUser
        AdditionWindow.currentUser=self.inputedLogin.get()
        AdditionWindow.currentPassword=self.inputedPassword.get()
        
        SubtractionWindow.userLogined=LoginWindow.catchUser
        SubtractionWindow.currentUser=self.inputedLogin.get()
        SubtractionWindow.currentPassword=self.inputedPassword.get()
        
        MultiplycationWindow.userLogined=LoginWindow.catchUser
        MultiplycationWindow.currentUser=self.inputedLogin.get()
        MultiplycationWindow.currentPassword=self.inputedPassword.get()

        DevisionWindow.userLogined=LoginWindow.catchUser
        DevisionWindow.currentUser=self.inputedLogin.get()
        DevisionWindow.currentPassword=self.inputedPassword.get()
        
        # print(self.catchResult)

        if self.catchResult:
            login_window.destroy() # destroyed login menu
            MainMenu.scoreDict.update({'addScore':self.catchResult[2]}) #assign user score progress
            MainMenu.scoreDict.update({'subScore':self.catchResult[3]}) 
            MainMenu.scoreDict.update({'multiScore':self.catchResult[4]}) 
            MainMenu.scoreDict.update({'devScore':self.catchResult[5]})
            print(MainMenu.scoreDict)
            MainMenu.userName=self.catchResult[0]
                
            #creating app menu if we pass login
            my_window=Tk()
            app=MainMenu(my_window)
            my_window.mainloop()

        else:
            self.infoText.set("Створіть користувача!")
            # print("Please signIn")
        
    def centeredWindow(self):
        """Put app window in the center os screen"""
        window_width=500
        window_height=500
        screen_width=self.parent.winfo_screenwidth()
        screen_height=self.parent.winfo_screenheight()
        x_coordinate = (screen_width/2)-(window_width/2)
        y_coordinate = (screen_height/2-(window_height/2))
        self.parent.geometry("%dx%d+%d+%d" % (window_width,window_height,x_coordinate,y_coordinate))
        # self.parent.overrideredirect(True)

class MainMenu(Frame):

    usreName=''
    scoreDict={
        'addScore':0,
        'subScore':0,
        'multiScore':0,
        'devScore':0,
        }
    userLvl=1
    addScore=0
    subScore=0
    multiScore=0
    devScore=0
    
    def __init__(self,parent):
        self.parent=parent
        Frame.__init__(self,parent)
        self.initUI()
    def initUI(self):
        """Creating content in main window"""
        self.centeredWindow()
        self.setUserLvl()
        #self.parent.overrideredirect(True) #prevent moving the window
        self.parent.title("MainMenu") 
        self.pack   
       
        #variables
        self.valueUserLvl=IntVar()
        self.valueUserLvl.set(MainMenu.userLvl)

        self.setUserName=StringVar()
        self.setUserName.set(MainMenu.userName)

        self.addInfo=IntVar()
        self.addInfo.set(MainMenu.addScore)

        self.subInfo=IntVar()
        self.subInfo.set(MainMenu.subScore)

        self.multiInfo=IntVar()
        self.multiInfo.set(MainMenu.multiScore)

        self.devInfo=IntVar()
        self.devInfo.set(MainMenu.devScore)
        
        #Frames
        buttonFrame=Frame(self.parent,background="#DAFF75",borderwidth=2)
        buttonFrame.pack(side="left")
        buttonFrame.config(width=50,height=600)

        self.logFrame=Frame(self.parent,background="#4DA6FF",borderwidth=2)
        self.logFrame.pack(fill="both", expand=True, padx=(0,10),pady=10)# padding Frame one(right) side

        #buttons
        self.plus=Button(buttonFrame,text="Додавання",font="Times 25",command=self.addition)
        self.plus.config(width=10)
        self.plus.pack(padx=10, pady=10)

        self.minus=Button(buttonFrame,text="Віднімання",font="Times 25",command=self.subtraction)
        self.minus.config(width=10)
        self.minus.pack(padx=10, pady=10)

        self.multiply=Button(buttonFrame,text="Множення",font="Times 25",command=self.multiplycation)
        self.multiply.config(width=10)
        self.multiply.pack(padx=10, pady=10)

        self.devide=Button(buttonFrame,text="Ділення",font="Times 25",command=self.devision)
        self.devide.config(width=10)
        self.devide.pack(padx=10, pady=10)

        self.logOut=Button(self.logFrame,text='Вихід',font="Times 15",command=self.goLoginPage)
        self.logOut.pack(side='top',anchor=NE,padx=10,pady=(10,0))

        self.logText=Text(self.logFrame,font="Times 15",fg="red")
        self.logText.insert(INSERT,"Історія помилок:\n")
        self.logText.config(state=DISABLED,width=300, height=300)
        self.logText.pack(padx=20,pady=(100,0))
        
        #Labels
        self.score_label=Label(self.parent,background="#DAFF75",foreground="green", text="Рівень:", borderwidth=2,font="Times 20")
        self.score_label.pack()
        self.score_label.place(x=55,y=70)

        self.score_value=Label(self.parent,background="#DAFF75",foreground="green", textvariable=self.valueUserLvl, borderwidth=2,font="Times 20")
        self.score_value.pack()
        self.score_value.place(x=135,y=70)
    
        self.userName_label=Label(self.parent,background="#DAFF75",foreground="blue", textvariable=self.setUserName, borderwidth=2,font="Times 30")
        self.userName_label.pack()
        self.userName_label.place(x=60,y=25)

        self.addScore_label=Label(self.parent,width=10,background="#DAFF75",foreground="green", text="Додавання:", borderwidth=2,font="Times 18",anchor='w')
        self.addScore_label.pack()
        self.addScore_label.place(x=235,y=20)

        self.add_value=Label(self.parent,width=4,background="#DAFF75",foreground="green", textvariable=self.addInfo, borderwidth=2,font="Times 18",anchor='w')
        self.add_value.pack()
        self.add_value.place(x=370,y=20)
    
        self.subScore_label=Label(self.parent,width=10,background="#DAFF75",foreground="green", text="Віднімання:", borderwidth=2,font="Times 18",anchor='w')
        self.subScore_label.pack()
        self.subScore_label.place(x=235,y=50)

        self.sub_value=Label(self.parent,width=4,background="#DAFF75",foreground="green", textvariable=self.subInfo, borderwidth=2,font="Times 18",anchor='w')
        self.sub_value.pack()
        self.sub_value.place(x=370,y=50)

        self.multiScore_label=Label(self.parent,width=10,background="#DAFF75",foreground="green", text="Множення:", borderwidth=2,font="Times 18",anchor='w')
        self.multiScore_label.pack()
        self.multiScore_label.place(x=235,y=80)

        self.multi_value=Label(self.parent,width=4,background="#DAFF75",foreground="green", textvariable=self.multiInfo, borderwidth=2,font="Times 18",anchor='w')
        self.multi_value.pack()
        self.multi_value.place(x=370,y=80)

        self.devScore_label=Label(self.parent,width=10,background="#DAFF75",foreground="green", text="Ділення:", borderwidth=2,font="Times 18",anchor='w')
        self.devScore_label.pack()
        self.devScore_label.place(x=235,y=110)

        self.dev_value=Label(self.parent,width=4,background="#DAFF75",foreground="green", textvariable=self.devInfo, borderwidth=2,font="Times 18",anchor='w')
        self.dev_value.pack()
        self.dev_value.place(x=370,y=110)
    
    def goLoginPage(self):
        LoginWindow.catchUser=0
        self.parent.destroy()
        
        login_window=Tk()
        self.appLogin=LoginWindow(login_window)
        login_window.mainloop()
    
    def setUserLvl(self):
        MainMenu.addScore=MainMenu.scoreDict['addScore']# here assign val from dict to class variable
        MainMenu.subScore=MainMenu.scoreDict['subScore']
        MainMenu.multiScore=MainMenu.scoreDict['multiScore']
        MainMenu.devScore=MainMenu.scoreDict['devScore']
        self.minValueDict=min(MainMenu.scoreDict.items(),key=lambda x: x[1])
        print('This is a minimal value in dict: ',self.minValueDict[1])
        if self.minValueDict[1]<200:
            MainMenu.userLvl=1
            print('User lvl is :',MainMenu.userLvl)
        if 200<=self.minValueDict[1]<300:
            MainMenu.userLvl=2
            print('User lvl is :',MainMenu.userLvl)
        if 300<=self.minValueDict[1]<400:
            MainMenu.userLvl=3
            print('User lvl is :',MainMenu.userLvl)
        if 400<=self.minValueDict[1]<500:
            MainMenu.userLvl=4
            print('User lvl is :',MainMenu.userLvl)
        if 500<=self.minValueDict[1]<600:
            MainMenu.userLvl=5
            print('User lvl is :',MainMenu.userLvl)

    def centeredWindow(self):
        """Put app window in the center os screen"""
        window_width=800
        window_height=600
        screen_width=self.parent.winfo_screenwidth()
        screen_height=self.parent.winfo_screenheight()
        x_coordinate = (screen_width/2)-(window_width/2)
        y_coordinate = (screen_height/2-(window_height/2))

        self.parent.geometry("%dx%d+%d+%d" % (window_width,window_height,x_coordinate,y_coordinate))
        self.parent.configure(background="#DAFF75")
    
    
    def addition(self):
        """Creating window with Addition"""
        self.addition_training = AdditionWindow()

    def subtraction(self):
        """Creating window with Subtraction"""
        self.subtract_training = SubtractionWindow()

    def multiplycation(self):
        """Creating window with Multiplication"""
        self.multiply_training = MultiplycationWindow()
    
    def devision(self):
        """Creating window with Devision"""
        self.devide_training = DevisionWindow()    

class AdditionWindow():
    userLogined=0
    currentUser=''
    currentPassword=''

    def __init__(self):
        #variables
        self.top=Toplevel()
        self.top.title("Addition Training")
        #top.overrideredirect(True)
        window_width=800
        window_height=600
        screen_width=self.top.winfo_screenwidth()
        screen_height=self.top.winfo_screenheight()
        x_coordinate = (screen_width/2)-(window_width/2)
        y_coordinate = (screen_height/2-(window_height/2))

        self.top.geometry("%dx%d+%d+%d" % (window_width,window_height,x_coordinate,y_coordinate))
        self.top.configure(background="#DAFF75")
        
        self.a=IntVar()
        self.b=IntVar()
        self.sumAB=IntVar()
        self.countAdd=IntVar()
        self.entryS=IntVar()
        
        self.countAdd.set(MainMenu.addScore)
        
        if MainMenu.userLvl==1:
            self.a.set(random.randrange(1,10))
            self.b.set(random.randrange(1,10))
 
        elif MainMenu.userLvl==2:
            self.a.set(random.randrange(1,20))
            self.b.set(random.randrange(1,20))
 
        elif MainMenu.userLvl==3:
            self.a.set(random.randrange(1,30))
            self.b.set(random.randrange(1,30))
 
        elif MainMenu.userLvl==4:
            self.a.set(random.randrange(1,40))
            self.b.set(random.randrange(1,40))

        elif MainMenu.userLvl==5:
            self.a.set(random.randrange(1,50))
            self.b.set(random.randrange(1,50))
            
        self.sumAB.set(self.a.get()+self.b.get())
        
        #Frames
        self.numbersFrame=Frame(self.top)
        self.numbersFrame.pack()
        self.numbersFrame.place(x=150,y=250)
        
        #Labels
        self.textAction=Label(self.top,background="#DAFF75", text="Обчислити приклад:",foreground="#004DE6",font="Times 35")
        self.textAction.pack()
        self.textAction.place(x=180,y=160)

        self.aElem=Label(self.numbersFrame,background="#DAFF75", borderwidth=2,textvariable=self.a,font="Times 70")
        self.aElem.pack(side="left")


        self.plusElem=Label(self.numbersFrame,bg="#DAFF75", borderwidth=2,text="+",font="Times 70")
        self.plusElem.pack(side="left")


        self.bElem=Label(self.numbersFrame,background="#DAFF75", borderwidth=2,textvariable=self.b,font="Times 70")
        self.bElem.pack(side="left")


        self.equalElem=Label(self.numbersFrame,bg="#DAFF75", borderwidth=2,text="=",font="Times 70")
        self.equalElem.pack(side="left")

        self.sumEntry=Entry(self.top,background="#FFFFCC",font="Times 70",textvariable=self.entryS)
        self.sumEntry.delete(0, 'end')
        self.sumEntry.bind("<Return>", self.addFunc)
        self.sumEntry.pack(side="right")
        self.sumEntry.place(x=470,y=251)
        self.sumEntry.config(width=4)

        self.score_label=Label(self.top,background="#DAFF75", foreground="#E60000", text="Бали:", borderwidth=2,font="Times 30")
        self.score_label.pack()
        self.score_label.place(x=10,y=30)

        self.score_value=Label(self.top,background="#DAFF75",foreground="#E60000", textvariable=self.countAdd, borderwidth=2,font="Times 30")
        self.score_value.pack()
        self.score_value.place(x=110,y=30)

        self.backButton=Button(self.top,text="Назад",font="Times 20",command=self.backButtonFunc)
        self.backButton.pack(padx=10, pady=10)
        self.backButton.place(x=10,y=535)
    
    def addFunc(self,*args):
        counter=1
        sumToCheck=self.entryS.get()
        sumValid=self.sumAB.get()
        print(int(sumToCheck))
        print(int(sumValid))
        if sumToCheck==sumValid:
            counter=self.countAdd.get()+1
            self.countAdd.set(counter)
            print("Right answer")
            self.sumEntry.delete(0, 'end') # clearing input field
        else:
            print("Wrong answer")
            counter=self.countAdd.get()-1
            self.countAdd.set(counter)
            self.sumEntry.delete(0, 'end') # clearing input field
            if counter<=0:
                self.countAdd.set(0)
        
        if MainMenu.userLvl==1:
            self.a.set(random.randrange(1,10))
            self.b.set(random.randrange(1,10))
 
        elif MainMenu.userLvl==2:
            self.a.set(random.randrange(1,20))
            self.b.set(random.randrange(1,20))
 
        elif MainMenu.userLvl==3:
            self.a.set(random.randrange(1,30))
            self.b.set(random.randrange(1,30))
 
        elif MainMenu.userLvl==4:
            self.a.set(random.randrange(1,40))
            self.b.set(random.randrange(1,40))

        elif MainMenu.userLvl==5:
            self.a.set(random.randrange(1,50))
            self.b.set(random.randrange(1,50))
        
        self.sumAB.set(self.a.get()+self.b.get())
    
    def backButtonFunc(self):
        """This function must sent total score of numbers addition4
             what was earned and go back to main menu"""
        
        if AdditionWindow.userLogined[0]==AdditionWindow.currentUser and AdditionWindow.userLogined[1]==AdditionWindow.currentPassword:
            self.conn=sqlite3.connect('D:\\readyProjects\\math\\MathUsers.db')
            with self.conn:    
                self.cur=self.conn.cursor()
                self.cur.execute('UPDATE MathUsersDB SET ScoreAdd = ? WHERE Login=? AND Password=?',(self.countAdd.get(),AdditionWindow.currentUser,AdditionWindow.currentPassword))
                self.conn.commit()
        
        # self.setUserLvl() 
        MainMenu.scoreDict['addScore']=self.countAdd.get()# updating value ADDITION in main menu
        MainMenu.setUserLvl(self)
        self.top.destroy()    

class SubtractionWindow():
    
    userLogined=0
    currentUser=''
    currentPassword=''
    
    def __init__(self):
        #variables
        # self.count=IntVar()
        # self.count.set(1)
        self.top=Toplevel()
        self.top.title("Subtraction Training")
        # top.overrideredirect(True)
        window_width=800
        window_height=600
        screen_width=self.top.winfo_screenwidth()
        screen_height=self.top.winfo_screenheight()
        x_coordinate = (screen_width/2)-(window_width/2)
        y_coordinate = (screen_height/2-(window_height/2))

        self.top.geometry("%dx%d+%d+%d" % (window_width,window_height,x_coordinate,y_coordinate))
        self.top.configure(background="#DAFF75")
        
        self.a=IntVar()
        self.b=IntVar()
        self.countSub=IntVar()
        self.c=IntVar()
        self.subAB=IntVar()
        self.entrySub=IntVar()
        
        self.countSub.set(MainMenu.subScore)
        
        if MainMenu.userLvl==1:
            self.a.set(random.randrange(1,10))
            self.b.set(random.randrange(1,10))

        elif MainMenu.userLvl==2:
            self.a.set(random.randrange(1,20))
            self.b.set(random.randrange(1,20))

        elif MainMenu.userLvl==3:
            self.a.set(random.randrange(1,30))
            self.b.set(random.randrange(1,30))
 
        elif MainMenu.userLvl==4:
            self.a.set(random.randrange(1,40))
            self.b.set(random.randrange(1,40))

        elif MainMenu.userLvl==5:
            self.a.set(random.randrange(1,50))
            self.b.set(random.randrange(1,50))
        

        #condition that changing a and places!
        if self.a.get()<self.b.get():
            self.c.set(self.a.get())
            self.a.set(self.b.get())
            self.b.set(self.c.get())
            print("Changing a and b places: ",self.a.get(),self.b.get())
            
        self.subAB.set(self.a.get()-self.b.get())

        #Frames
        self.numbersFrame=Frame(self.top)
        self.numbersFrame.pack()
        self.numbersFrame.place(x=150,y=250)
        
        #Labels
        self.textAction=Label(self.top,background="#DAFF75", text="Обчислити приклад:",foreground="#004DE6",font="Times 35")
        self.textAction.pack()
        self.textAction.place(x=180,y=160)

        self.aElem=Label(self.numbersFrame,background="#DAFF75", borderwidth=2,textvariable=self.a,font="Times 70")
        self.aElem.pack(side="left")


        self.minusElem=Label(self.numbersFrame,bg="#DAFF75", borderwidth=2,text="-",font="Times 70")
        self.minusElem.pack(side="left")


        self.bElem=Label(self.numbersFrame,background="#DAFF75", borderwidth=2,textvariable=self.b,font="Times 70")
        self.bElem.pack(side="left")


        self.equalElem=Label(self.numbersFrame,bg="#DAFF75", borderwidth=2,text="=",font="Times 70")
        self.equalElem.pack(side="left")

        self.subEntry=Entry(self.top,background="#FFFFCC",font="Times 70",textvariable=self.entrySub)
        self.subEntry.delete(0, 'end')
        self.subEntry.bind("<Return>", self.subFunc)
        self.subEntry.pack(side="right")
        self.subEntry.place(x=470,y=251)
        self.subEntry.config(width=4)

        self.score_label=Label(self.top,background="#DAFF75", foreground="#E60000", text="Бали:", borderwidth=2,font="Times 30")
        self.score_label.pack()
        self.score_label.place(x=10,y=30)

        self.score_value=Label(self.top,background="#DAFF75",foreground="#E60000", textvariable=self.countSub, borderwidth=2,font="Times 30")
        self.score_value.pack()
        self.score_value.place(x=110,y=30)

        self.backButton=Button(self.top,text="Назад",font="Times 20",command=self.backButtonFunc)
        self.backButton.pack(padx=10, pady=10)
        self.backButton.place(x=10,y=535)

    def subFunc(self,*args):
        counter=1
        subToCheck=self.entrySub.get()
        subValid=self.subAB.get()
        print(int(subToCheck))
        print(int(subValid))
        if subToCheck==subValid:
            counter=self.countSub.get()+1
            self.countSub.set(counter)
            print("Right answer")
            self.subEntry.delete(0, 'end') # clearing input field
        else:
            print("Wrong answer")
            counter=self.countSub.get()-1
            self.countSub.set(counter)
            self.subEntry.delete(0, 'end') # clearing input field
            if counter<=0:
                self.countSub.set(0)
        
        if MainMenu.userLvl==1:
            self.a.set(random.randrange(1,10))
            self.b.set(random.randrange(1,10))

        elif MainMenu.userLvl==2:
            self.a.set(random.randrange(1,20))
            self.b.set(random.randrange(1,20))

        elif MainMenu.userLvl==3:
            self.a.set(random.randrange(1,30))
            self.b.set(random.randrange(1,30))
 
        elif MainMenu.userLvl==4:
            self.a.set(random.randrange(1,40))
            self.b.set(random.randrange(1,40))

        elif MainMenu.userLvl==5:
            self.a.set(random.randrange(1,50))
            self.b.set(random.randrange(1,50))

        #condition that changing a and b places!
        if self.a.get()<self.b.get():
            self.c.set(self.a.get())
            self.a.set(self.b.get())
            self.b.set(self.c.get())
            print("Changing a and b places: ",self.a.get(),self.b.get())
        
        self.subAB.set(self.a.get()-self.b.get())
    
    def backButtonFunc(self):
        """This function must sent total score of numbers addition4
             what was earned and go back to main menu"""
        print(SubtractionWindow.userLogined)
        print(SubtractionWindow.currentUser)
        print(SubtractionWindow.currentPassword)
        
        if SubtractionWindow.userLogined[0]==SubtractionWindow.currentUser and SubtractionWindow.userLogined[1]==SubtractionWindow.currentPassword:
            self.conn=sqlite3.connect('D:\\readyProjects\\math\\MathUsers.db')
            with self.conn:    
                self.cur=self.conn.cursor()
                self.cur.execute('UPDATE MathUsersDB SET ScoreSub = ? WHERE Login=? AND Password=?',(self.countSub.get(),SubtractionWindow.currentUser,SubtractionWindow.currentPassword))
                self.conn.commit()
        
        MainMenu.subScore=self.countSub.get()# updating value SUBTRACTION in main menu
        self.top.destroy()        

class MultiplycationWindow():
    
    userLogined=0
    currentUser=''
    currentPassword=''

    def __init__(self):
        #variables
        # self.count=IntVar()
        # self.count.set(1)
        self.top=Toplevel()
        self.top.title("Multiplication Training")
        # top.overrideredirect(True)
        window_width=800
        window_height=600
        screen_width=self.top.winfo_screenwidth()
        screen_height=self.top.winfo_screenheight()
        x_coordinate = (screen_width/2)-(window_width/2)
        y_coordinate = (screen_height/2-(window_height/2))

        self.top.geometry("%dx%d+%d+%d" % (window_width,window_height,x_coordinate,y_coordinate))
        self.top.configure(background="#DAFF75")
        
        self.a=IntVar()
        self.b=IntVar()
        self.multiAB=IntVar()
        self.countMulti=IntVar()
        self.entryMulti=IntVar()
        
        self.countMulti.set(MainMenu.multiScore)
        
        if MainMenu.userLvl==1:
            self.a.set(random.randrange(1,6))
            self.b.set(random.randrange(1,6))

        elif MainMenu.userLvl==2:
            self.a.set(random.randrange(1,11))
            self.b.set(random.randrange(1,11))

        elif MainMenu.userLvl==3:
            self.a.set(random.randrange(1,16))
            self.b.set(random.randrange(1,16))
 
        elif MainMenu.userLvl==4:
            self.a.set(random.randrange(1,21))
            self.b.set(random.randrange(1,21))

        elif MainMenu.userLvl==5:
            self.a.set(random.randrange(1,26))
            self.b.set(random.randrange(1,26))

        self.multiAB.set(self.a.get()*self.b.get())

        #Frames
        self.numbersFrame=Frame(self.top)
        self.numbersFrame.pack()
        self.numbersFrame.place(x=150,y=250)
        
        #Labels
        self.textAction=Label(self.top,background="#DAFF75", text="Обчислити приклад:",foreground="#004DE6",font="Times 35")
        self.textAction.pack()
        self.textAction.place(x=180,y=160)

        self.aElem=Label(self.numbersFrame,background="#DAFF75", borderwidth=2,textvariable=self.a,font="Times 70")
        self.aElem.pack(side="left")


        self.plusElem=Label(self.numbersFrame,bg="#DAFF75", borderwidth=2,text="*",font="Times 70")
        self.plusElem.pack(side="left")


        self.bElem=Label(self.numbersFrame,background="#DAFF75", borderwidth=2,textvariable=self.b,font="Times 70")
        self.bElem.pack(side="left")


        self.equalElem=Label(self.numbersFrame,bg="#DAFF75", borderwidth=2,text="=",font="Times 70")
        self.equalElem.pack(side="left")

        self.multiEntry=Entry(self.top,background="#FFFFCC",font="Times 70",textvariable=self.entryMulti)
        self.multiEntry.delete(0, 'end')
        self.multiEntry.bind("<Return>", self.multiFunc)
        self.multiEntry.pack(side="right")
        self.multiEntry.place(x=470,y=251)
        self.multiEntry.config(width=4)

        self.score_label=Label(self.top,background="#DAFF75", foreground="#E60000", text="Бали:", borderwidth=2,font="Times 30")
        self.score_label.pack()
        self.score_label.place(x=10,y=30)

        self.score_value=Label(self.top,background="#DAFF75",foreground="#E60000", textvariable=self.countMulti, borderwidth=2,font="Times 30")
        self.score_value.pack()
        self.score_value.place(x=110,y=30)

        self.backButton=Button(self.top,text="Назад",font="Times 20",command=self.backButtonFunc)
        self.backButton.pack(padx=10, pady=10)
        self.backButton.place(x=10,y=535)

    def multiFunc(self,*args):
        counter=1
        multiToCheck=self.entryMulti.get()
        multiValid=self.multiAB.get()
        print(int(multiToCheck))
        print(int(multiValid))
        if multiToCheck==multiValid:
            counter=self.countMulti.get()+1
            self.countMulti.set(counter)
            print("Right answer")
            self.multiEntry.delete(0, 'end') # clearing input field
        else:
            print("Wrong answer")
            counter=self.countMulti.get()-1
            self.countMulti.set(counter)
            self.multiEntry.delete(0, 'end') # clearing input field
            if counter<=0:
                self.countMulti.set(0)
        if MainMenu.userLvl==1:
            self.a.set(random.randrange(1,6))
            self.b.set(random.randrange(1,6))

        elif MainMenu.userLvl==2:
            self.a.set(random.randrange(1,11))
            self.b.set(random.randrange(1,11))

        elif MainMenu.userLvl==3:
            self.a.set(random.randrange(1,16))
            self.b.set(random.randrange(1,16))
 
        elif MainMenu.userLvl==4:
            self.a.set(random.randrange(1,21))
            self.b.set(random.randrange(1,21))

        elif MainMenu.userLvl==5:
            self.a.set(random.randrange(1,26))
            self.b.set(random.randrange(1,26))
        
        self.multiAB.set(self.a.get()*self.b.get())
    
    def backButtonFunc(self):
        """This function must sent total score of numbers addition4
             what was earned and go back to main menu"""
        print(MultiplycationWindow.userLogined)
        print(MultiplycationWindow.currentUser)
        print(MultiplycationWindow.currentPassword)
        
        if MultiplycationWindow.userLogined[0]==MultiplycationWindow.currentUser and MultiplycationWindow.userLogined[1]==MultiplycationWindow.currentPassword:
            self.conn=sqlite3.connect('D:\\readyProjects\\math\\MathUsers.db')
            with self.conn:    
                self.cur=self.conn.cursor()
                self.cur.execute('UPDATE MathUsersDB SET ScoreMulti = ? WHERE Login=? AND Password=?',(self.countMulti.get(),MultiplycationWindow.currentUser,MultiplycationWindow.currentPassword))
                self.conn.commit()
        
        MainMenu.multiScore=self.countMulti.get()# updating value SUBTRACTION in main menu
        self.top.destroy()      

class DevisionWindow():
    
    userLogined=0
    currentUser=''
    currentPassword=''
    
    def __init__(self):
        #variables
        self.top=Toplevel()
        self.top.title("Devision Training")
        window_width=800
        window_height=600
        screen_width=self.top.winfo_screenwidth()
        screen_height=self.top.winfo_screenheight()
        x_coordinate = (screen_width/2)-(window_width/2)
        y_coordinate = (screen_height/2-(window_height/2))

        self.top.geometry("%dx%d+%d+%d" % (window_width,window_height,x_coordinate,y_coordinate))
        self.top.configure(background="#DAFF75")
        

        self.b=IntVar()
        self.a=IntVar()
        self.devAB=IntVar()
        self.countDev=IntVar()
        self.entryDev=IntVar()
        
        self.countDev.set(MainMenu.devScore)
        
        if MainMenu.userLvl==1:
            self.b.set(random.randrange(1,6))
            self.a.set(random.randrange(1,6)*self.b.get())

        elif MainMenu.userLvl==2:
            self.b.set(random.randrange(1,11))
            self.a.set(random.randrange(1,11)*self.b.get())

        elif MainMenu.userLvl==3:
            self.b.set(random.randrange(1,16))
            self.a.set(random.randrange(1,16)*self.b.get())
 
        elif MainMenu.userLvl==4:
            self.b.set(random.randrange(1,21))
            self.a.set(random.randrange(1,21)*self.b.get())

        elif MainMenu.userLvl==5:
            self.b.set(random.randrange(1,26))
            self.a.set(random.randrange(1,26)*self.b.get()) 

        self.devAB.set(self.a.get()/self.b.get())

        #Frames
        self.numbersFrame=Frame(self.top)
        self.numbersFrame.pack()
        self.numbersFrame.place(x=150,y=250)
        
        #Labels
        self.textAction=Label(self.top,background="#DAFF75", text="Обчислити приклад:",foreground="#004DE6",font="Times 35")
        self.textAction.pack()
        self.textAction.place(x=180,y=160)

        self.aElem=Label(self.numbersFrame,background="#DAFF75", borderwidth=2,textvariable=self.a,font="Times 70")
        self.aElem.pack(side="left")


        self.plusElem=Label(self.numbersFrame,bg="#DAFF75", borderwidth=2,text=":",font="Times 70")
        self.plusElem.pack(side="left")


        self.bElem=Label(self.numbersFrame,background="#DAFF75", borderwidth=2,textvariable=self.b,font="Times 70")
        self.bElem.pack(side="left")


        self.equalElem=Label(self.numbersFrame,bg="#DAFF75", borderwidth=2,text="=",font="Times 70")
        self.equalElem.pack(side="left")

        self.devEntry=Entry(self.top,background="#FFFFCC",font="Times 70",textvariable=self.entryDev)
        self.devEntry.delete(0, 'end')
        self.devEntry.bind("<Return>", self.devFunc) # bind button enter to Entry widget
        self.devEntry.pack(side="right")
        self.devEntry.place(x=470,y=251)
        self.devEntry.config(width=4)

        self.score_label=Label(self.top,background="#DAFF75", foreground="#E60000", text="Бали:", borderwidth=2,font="Times 30")
        self.score_label.pack()
        self.score_label.place(x=10,y=30)

        self.score_value=Label(self.top,background="#DAFF75",foreground="#E60000", textvariable=self.countDev, borderwidth=2,font="Times 30")
        self.score_value.pack()
        self.score_value.place(x=110,y=30)

        self.backButton=Button(self.top,text="Назад",font="Times 20",command=self.backButtonFunc)
        self.backButton.pack(padx=10, pady=10)
        self.backButton.place(x=10,y=535)

    def devFunc(self,*args):
        counter=1
        devToCheck=self.entryDev.get()
        devValid=self.devAB.get()
        print(int(devToCheck))
        print(int(devValid))
        if devToCheck==devValid:
            counter=self.countDev.get()+1
            self.countDev.set(counter)
            print("Right answer")
            self.devEntry.delete(0, 'end') # clearing input field
        else:
            print("Wrong answer")
            counter=self.countDev.get()-1
            self.countDev.set(counter)
            self.devEntry.delete(0, 'end') # clearing input field
            if counter<=0:
                self.countDev.set(0)

        if MainMenu.userLvl==1:
            self.b.set(random.randrange(1,6))
            self.a.set(random.randrange(1,6)*self.b.get())

        elif MainMenu.userLvl==2:
            self.b.set(random.randrange(1,11))
            self.a.set(random.randrange(1,11)*self.b.get())

        elif MainMenu.userLvl==3:
            self.b.set(random.randrange(1,16))
            self.a.set(random.randrange(1,16)*self.b.get())
 
        elif MainMenu.userLvl==4:
            self.b.set(random.randrange(1,21))
            self.a.set(random.randrange(1,21)*self.b.get())

        elif MainMenu.userLvl==5:
            self.b.set(random.randrange(1,26))
            self.a.set(random.randrange(1,26)*self.b.get())
        
        self.devAB.set(self.a.get()/self.b.get())

    def backButtonFunc(self):
        """This function must sent total score of numbers addition4
             what was earned and go back to main menu"""
        
        if DevisionWindow.userLogined[0]==DevisionWindow.currentUser and DevisionWindow.userLogined[1]==DevisionWindow.currentPassword:
            self.conn=sqlite3.connect('D:\\readyProjects\\math\\MathUsers.db')
            with self.conn:    
                self.cur=self.conn.cursor()
                self.cur.execute('UPDATE MathUsersDB SET ScoreDev = ? WHERE Login=? AND Password=?',(self.countDev.get(),DevisionWindow.currentUser,DevisionWindow.currentPassword))
                self.conn.commit()
        
        print(DevisionWindow.userLogined)
        print(DevisionWindow.currentUser)
        print(DevisionWindow.currentPassword)

        MainMenu.devScore=self.countDev.get()# updating value SUBTRACTION in main menu
        self.top.destroy()      

login_window=Tk()
appLogin=LoginWindow(login_window)
login_window.mainloop()

