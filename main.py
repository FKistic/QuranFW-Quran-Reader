from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os,sys,threading,pickle,time,webbrowser,shutil,subprocess,getpass


read_only_index=1
dir_path= os.path.dirname(os.path.realpath(__file__)) #to take File path`
Img_List=[]
l=[]
class Gui(Tk):
    def __init__(self):
        super().__init__()
        # HomeScreen
        global remove_list
        remove_list=[]
        self.geometry("504x704")
        self.wm_attributes("-topmost", 1)
        self.title("Al - Quran for Windows")
        self.resizable(False,False)
        self.iconbitmap(f"{dir_path}\\Icon\\bg.ico")
        
        # #Menu
        # main_menu=Menu(self,background="grey")
        # sub_menu1=Menu(main_menu,tearoff=0)
        # sub_menu1.add_command(label="Exit",command=self.destroy)
        # main_menu.add_cascade(label="Files",menu=sub_menu1)
        # sub_menu2=Menu(main_menu)
        # main_menu.add_command(label="Help")
        # self.config(menu=main_menu)

        # #Status bar
        # statusbar=Label(text="Running",justify=LEFT,anchor="w",relief=FLAT)
        # statusbar.pack(side=BOTTOM,fill=X)

        #bgpic
        bgpic = Image.open(f"{dir_path}\\Icon\\bg1.png")
        tkpic = ImageTk.PhotoImage(bgpic)
        label = Label(self, image=tkpic)
        label.image = tkpic  # Save reference to image
        label.pack(fill=BOTH)
        remove_list.append(label)

        # Read Quran button
        readbuttonimage=Image.open(f"{dir_path}\\Icon\\button.png")
        readbuttonimage = readbuttonimage.resize((100,100), Image.ANTIALIAS)
        buttonimage = ImageTk.PhotoImage(readbuttonimage)
        readbutton= Button(self,bg="#117b89",image=buttonimage,borderwidth=1,activebackground="#218a9b",relief=RIDGE,command = Functions.ReadOnly)
        read_lable=Label(text="Read Al-Quran",font="Sublime 8 bold",bg="#0c6877",fg="white")
        read_lable.place(x=80,y=400)
        readbutton.image = buttonimage
        readbutton.place(x=70,y=290)
        # Read and listen Quran
        read_and_listenbuttonimage=Image.open(f"{dir_path}\\Icon\\button2.png")
        read_and_listenbuttonimage = read_and_listenbuttonimage.resize((70,70), Image.ANTIALIAS)
        read_and_listenbuttonimage = ImageTk.PhotoImage(read_and_listenbuttonimage)
        read_and_listenbutton=Button(self,bg="#168491",image=read_and_listenbuttonimage,borderwidth=1,activebackground="#0f6e80",relief=GROOVE,command=Functions.Read_and_listen)
        read_and_listen_label=Label(text="Read & Listen\nAl-Quran",font="Sublime 7 bold",bg="#107a88",fg="white")
        read_and_listen_label.place(x=353,y=265)
        read_and_listenbutton.image = read_and_listenbuttonimage
        read_and_listenbutton.place(x=350,y=200)
        # Salah Notifier
        Salah_Notifer_image=Image.open(f"{dir_path}\\Icon\\notifier.png")
        Salah_Notifer_image = Salah_Notifer_image.resize((70,70), Image.ANTIALIAS)
        Salah_Notifer_image = ImageTk.PhotoImage(Salah_Notifer_image)
        Salah_Notifer_button=Button(self,bg="#0d314b",image=Salah_Notifer_image,borderwidth=1,activebackground="#11536d",relief=GROOVE,command=Functions.SalahNotifier)
        Salah_Notifier_label=Label(text="Salah Notifier",font="Sublime 7 bold",bg="#0d314b",fg="white")
        Salah_Notifier_label.place(x=355,y=525)
        Salah_Notifer_button.image = Salah_Notifer_image
        Salah_Notifer_button.place(x=350,y=450)
        remove_list.append(Salah_Notifier_label)
        remove_list.append(read_and_listen_label)
        remove_list.append(read_lable)
        remove_list.append(read_and_listenbutton)
        remove_list.append(readbutton)
        remove_list.append(Salah_Notifer_button)

class Functions(Gui):
    def ReadOnly():
        global jump_var
        jump_var=IntVar()
        len_list=len(remove_list)
        try:
            for lable in remove_list:lable.destroy()
        except Exception as e:
            print(e)
        a_root.geometry("150x40+200+30")
        def close():
            a_root.destroy()
        def close_hover(e):
            info_var.set('"Icon by: Vector Market from www.flaticon.com"')
        def close_hover_leave(e):
            info_var.set('')
        a_root.overrideredirect(True) # turns off title bar, geometry
        def addition():
            global read_only_index
            read_only_index+=1
            if read_only_index>604:
                read_only_index=604
                messagebox.showerror("Error!","No further pages.")
            driver.get(fr"{dir_path}\Files\Read\{read_only_index}.png")
            var.set(read_only_index)
            jump_entry.update()
        def subtraction():
            global read_only_index
            read_only_index-=1
            if read_only_index<=1:
                read_only_index=1
            driver.get(fr"{dir_path}\Files\Read\{read_only_index}.png")
            var.set(read_only_index)
            jump_entry.update()
        def jump(e):
            global read_only_index
            a=jump_entry.get()
            try:
                if a=="":
                     messagebox.showerror("Error!","Please Enter an Integer from 1 to 604!")
                if int(a)>604:
                    a=604
                    read_only_index=a
                    messagebox.showerror("Error!","No further pages.")
                if int(a)<1:
                    a=1
            except Exception as e:
                print(e)
            read_only_index=int(a)
            driver.get(fr"{dir_path}\Files\Read\{a}.png")
            var.set(a)
            jump_entry.update()
        def surah_name():
            surahlist = ["1. al-Fātihah",
                    "2. al-Baqarah",
                    "3. Āl-ʿImrān",
                    "4. an-Nisāʾ",
                    "5. al-Māʾidah",
                    "6. al-Anʿām",
                    "7. al-Aʿrāf",
                    "8. al-Anfāl",
                    "9. at-Taubah",
                    "10. Yūnus",
                    "11. Hūd",
                    "12. Yūsuf",
                    "13. ar-Raʿd",
                    "14. Ibrāhīm",
                    "15. al-Ḥijr",
                    "16. an-Naḥl",
                    "17. al-Isrā'",
                    "18. al-Kahf",
                    "19. Maryam",
                    "20. Ṭā-Hā",
                    "21. al-Anbiyāʾ",
                    "22. al-Ḥajj",
                    "23. al-Muʾminūn",
                    "24. an-Nūr",
                    "25. al-Furqān",
                    "26. ash-Shuʿarā",
                    "27. an-Naml",
                    "28. al-Qaṣaṣ",
                    "29. al-ʿAnkabūt",
                    "30. ar-Rūm",
                    "31. Luqmān",
                    "32. as-Sajdah",
                    "33. al-Aḥzāb",
                    "34. Sabaʾ",
                    "35. Fāṭir",
                    "36. Yā-Sīn",
                    "37. as-Ṣāffāt",
                    "38. Ṣād",
                    "39. az-Zumar",
                    "40. Ghāfir",
                    "41. Fuṣṣilat",
                    "42. ash-Shūrā",
                    "43. az-Zukhruf",
                    "44. ad-Dukhān",
                    "45. al-Jāthiyah",
                    "46. al-Aḥqāf",
                    "47. Muḥammad",
                    "48. al-Fatḥ",
                    "49. al-Ḥujurāt",
                    "50. Qāf",
                    "51. adh-Dhāriyāt",
                    "52. at-Ṭūr",
                    "53. an-Najm",
                    "54. al-Qamar",
                    "55. ar-Raḥmān",
                    "56. al-Wāqiʿah",
                    "57. al-Ḥadīd",
                    "58. al-Mujādilah",
                    "59. al-Ḥashr",
                    "60. al-Mumtaḥanah",
                    "61. as-Ṣaff",
                    "62. al-Jumuʿah",
                    "63. al-Munāfiqūn",
                    "64. at-Taghābun",
                    "65. at-Ṭalāq",
                    "66. at-Taḥrīm",
                    "67. al-Mulk",
                    "68. al-Qalam",
                    "69. al-Ḥāqqah",
                    "70. al-Maʿārij",
                    "71. Nūḥ",
                    "72. al-Jinn",
                    "73. al-Muzzammil",
                    "74. al-Muddaththir",
                    "75. al-Qiyāmah",
                    "76. al-Insān",
                    "77. al-Mursalāt",
                    "78. an-Nabaʾ",
                    "79. an-Nāziʿāt",
                    "80. ʿAbasa",
                    "81. at-Takwīr",
                    "82. al-Infiṭār",
                    "83. al-Muṭaffifīn",
                    "84. al-Inshiqāq",
                    "85. al-Burūj",
                    "86. at-Ṭāriq",
                    "87. al-Aʿlā",
                    "88. al-Ghāshiyah",
                    "89. al-Fajr",
                    "90. al-Balad",
                    "91. ash-Shams",
                    "92. al-Layl",
                    "93. ad-Ḍuḥā",
                    "94. ash-Sharḥ"
                    "95. at-Tīn",
                    "96. al-ʿAlaq",
                    "97. al-Qadr",
                    "98. al-Bayyinah",
                    "99. az-Zalzalah",
                    "100. al-ʿĀdiyāt",
                    "101. al-Qāriʿah",
                    "102. at-Takāthur",
                    "103. al-ʿAsr",
                    "104. al-Humazah",
                    "105. al-Fīl",
                    "106. Quraysh",
                    "107. al-Māʿūn",
                    "108. al-Kawthar",
                    "109. al-Kāfirūn",
                    "110. an-Naṣr",
                    "111. al-Masad",
                    "112. al-Ikhlāṣ",
                    "113. al-Falaq",
                    "114. an-Nās"]
            surah_list=Listbox()
            for i in range(len(surahlist)):
                surah_list.insert(END,surahlist[i])
            surah_list.place(x=272,y=15)
            surah_list.index(10)
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument(fr"--app={dir_path}\Files\Read\{read_only_index}.png")
        driver = webdriver.Chrome(r'{dir_path}\chromedriver.exe',options=chrome_options)
        driver.maximize_window()

        var=StringVar()


        close_img = Image.open(f"{dir_path}\\Icon\\close.png")
        close_img = close_img.resize((10,10), Image.ANTIALIAS)
        close_img = ImageTk.PhotoImage(close_img)
        close_button=Button(image=close_img,command=close,borderwidth=0)
        close_button.image=close_img
        close_button.bind("<Enter>", close_hover)
        close_button.bind("<Leave>", close_hover_leave)
        close_button.place(x=137,y=0)

        left = Image.open(f"{dir_path}\\Icon\\left.png")
        left = left.resize((25,25), Image.ANTIALIAS)
        left_img = ImageTk.PhotoImage(left)
        l.append(left_img)


        left_button=Button(image=l[0],borderwidth=0,activebackground="white",command=addition)
        left_button.image= l[0]
        left_button.place(x=15,y=9)
        remove_list.append(left_button)


        right = Image.open(f"{dir_path}\\Icon\\right.png")
        right = right.resize((25,25), Image.ANTIALIAS)
        right_img = ImageTk.PhotoImage(right)
        l.append(right_img)


        right_button=Button(image=l[1],borderwidth=0,activebackground="white",command=subtraction)
        right_button.image= l[1]
        right_button.place(x=100,y=9)
        remove_list.append(right_button)


        jump_entry=Entry(bg="#efefef",width=5,font="Sublime 15 bold",fg="Black",justify=CENTER,textvariable=var,borderwidth=0)
        jump_entry.place(x=40,y=9)
        jump_entry.bind("<Return>",jump)
        remove_list.append(jump_entry)
        var.set(read_only_index)


        surah_var=StringVar()
        surah_select=Button(textvariable=surah_var,command=surah_name)
        surah_var.set("")
        surah_select.place(x=400,y=10)




        info_var=StringVar()
        info=Label(textvariable=info_var,font="sublime 5 italic")
        info.pack(side=BOTTOM,anchor="e")


        driver.get(fr"{dir_path}\Files\Read\{read_only_index}.png")
    def Read_and_listen():
        messagebox.showinfo("Work in Process!", "Inshallah you will get this opption by next month")
    def SalahNotifier():
        len_list=len(remove_list)
        try:
            for lable in remove_list[1:len_list]:lable.destroy()
        except Exception as e:
            print(e)
        # root = Tk()
        # p1 = PhotoImage(file = "icon\\bg.png")
        # root.iconphoto(False,p1)
        #Logic
        def logic():
            if mode_value.get()==1:
                mode=1
                with open(f"{dir_path}\\Data\\mode.dat",'wb') as modes:
                    pickle.dump(mode,modes)
            if mode_value.get()==2:
                mode=2
                with open(f"{dir_path}\\Data\\mode.dat",'wb') as modes:
                    pickle.dump(mode,modes)
            if mode_value.get()==3:
                mode=3
                with open(f"{dir_path}\\Data\\mode.dat",'wb') as modes:
                    pickle.dump(mode,modes)
            if mode_value.get()==4:
                mode=4
                with open(f"{dir_path}\\Data\\mode.dat",'wb') as modes:
                    pickle.dump(mode,modes)
            a="questions",messagebox.askquestion("Submitted", "Confirm?\nDo You want to quit?")
            if a[1]=="yes":
                with open(f"{dir_path}\\Data\\mode.dat",'rb') as modes:
                    a=pickle.load(modes)
                    print(a)
                webbrowser.open(dir_path+"\\mode_selector.pyw")
        def home_func():
                webbrowser.open(f"{dir_path}\\main.pyw")
                a_root.destroy()
        def Change_Salah_Time():
            len_list=len(remove_list)
            try:
                for lable in remove_list[1:len_list]:lable.destroy()
            except Exception as e:
                print(e)
            #Salah timing 
            # img2=ImageTk.PhotoImage(Image.open("icon\\bg.png"))
            # p1 = PhotoImage(file = "icon\\bg.png")
            # root2.iconphoto(False,p1)
            # Label(root2,image=img2).pack()

            def Submit():
                l1=[f'{Fajr1.get()}:{Fajr2.get()}:{Fajr3.get()},{Duhar1.get()}:{Duhar2.get()}:{Duhar3.get()},{Asr1.get()}:{Asr2.get()}:{Asr3.get()},{Magrib1.get()}:{Magrib2.get()}:{Magrib3.get()},{Isha1.get()}:{Isha2.get()}:{Isha3.get()}']
                with open("SalahTimes.dat",'wb') as salahtime:
                    pickle.dump(l1,salahtime)
                home_func()
            
            Label(text="Change Prayer Time",bg="#06324b",foreground="white",font="Defalt 25 bold").place(x=70,y=5)
            Label(text='''Fajr :''',font="Times 20 italic underline",bg="#0e7885",fg="white").place(x=5,y=250)
            Label(text='''Duhar :''',font="Times 20 italic underline",bg="#0e7885",fg="white").place(x=5,y=300)
            Label(text='''Asr :''',font="Times 20 italic underline",bg="#0e7885",fg="white").place(x=5,y=350)
            Label(text='''Magrib :''',font="Times 20 italic underline",bg="#0e7885",fg="white").place(x=5,y=400)
            Label(text='''Isha :''',font="Times 20 italic underline",bg="#0e7885",fg="white").place(x=5,y=450)

            Fajr1=StringVar()
            Fajr2=StringVar()
            Fajr3=StringVar()

            Duhar1=StringVar()
            Duhar2=StringVar()
            Duhar3=StringVar()

            Asr1=StringVar()
            Asr2=StringVar()
            Asr3=StringVar()

            Magrib1=StringVar()
            Magrib2=StringVar()
            Magrib3=StringVar()

            Isha1=StringVar()
            Isha2=StringVar()
            Isha3=StringVar()

            hourEntry1= Entry(width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Fajr1,fg="White")
            hourEntry1.place(x=120,y=250)
            
            minuteEntry1= Entry( width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Fajr2,fg="White")
            minuteEntry1.place(x=190,y=250)
            
            secondEntry1= Entry(width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Fajr3,fg="White")
            secondEntry1.place(x=260,y=250)

            hourEntry2= Entry(width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Duhar1,fg="White")
            hourEntry2.place(x=120,y=300)
            
            minuteEntry2= Entry( width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Duhar2,fg="White")
            minuteEntry2.place(x=190,y=300)
            
            secondEntry2= Entry( width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Duhar3,fg="White")
            secondEntry2.place(x=260,y=300)

            hourEntry3= Entry(width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Asr1,fg="White")
            hourEntry3.place(x=120,y=350)
            
            minuteEntry3= Entry( width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Asr2,fg="White")
            minuteEntry3.place(x=190,y=350)
            
            secondEntry3= Entry( width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Asr3,fg="White")
            secondEntry3.place(x=260,y=350)

            hourEntry4= Entry(width=int(2.5), font=("Arial",20,""),bg="#0e7885",textvariable=Magrib1,fg="White")
            hourEntry4.place(x=120,y=400)
            
            minuteEntry4= Entry( width=int(2.5), font=("Arial",20,""),bg="#0e7885",
                            textvariable=Magrib2,fg="White")
            minuteEntry4.place(x=190,y=400)
            
            secondEntry4= Entry( width=int(2.5), font=("Arial",20,""),bg="#0e7885",
                            textvariable=Magrib3,fg="White")
            secondEntry4.place(x=260,y=400)

            hourEntry5= Entry(width=int(2.5), font=("Arial",20,""),bg="#0e7885",
                            textvariable=Isha1,fg="White")
            hourEntry5.place(x=120,y=450)
            
            minuteEntry5= Entry( width=int(2.5), font=("Arial",20,""),bg="#0e7885",
                            textvariable=Isha2,fg="White")
            minuteEntry5.place(x=190,y=450)
            
            secondEntry5= Entry( width=int(2.5), font=("Arial",20,""),textvariable=Isha3,fg="White",bg="#0e7885")
            secondEntry5.place(x=260,y=450)

            Fajr1.set("04")
            Fajr2.set("40")
            Fajr3.set("00")

            Duhar1.set("12")
            Duhar2.set("20")
            Duhar3.set("00")

            Asr1.set("17")
            Asr2.set("16")
            Asr3.set("00")

            Magrib1.set("19")
            Magrib2.set("17")
            Magrib3.set("00")

            Isha1.set("20")
            Isha2.set("40")
            Isha3.set("00")
            Button(text="Submit",bg="#06324b",fg="white",padx=30,pady=20,command=Submit).place(x=90,y=500)
        #BG Images

        # img2=ImageTk.PhotoImage(Image.open("icon\\bg.png"))
        # Label(root,image=img2).pack()
                                               
        #Values

        mode_value=IntVar()


        #Labels


        a=Label(text='''This program is made to notify you about salah timings''',font="Times 12 italic underline",bg="#0e7885",fg="white")
        a.place(x=5,y=290)
        remove_list.append(a)
        b=Label(text='''Different modes available this programs are:''',font="Times 12 italic underline",bg="#0e7885",fg="white")
        b.place(x=5,y=320)
        remove_list.append(b)
        c=Label(text='''1. Easy mode - ONLY NOTIFICATIONS AND ALERTS.''',font="Times 12 italic underline",bg="#0e7885",fg="white")
        c.place(x=40,y=350)
        remove_list.append(c)
        d=Label(text='''2. Mediam mode - FULL SCREEN NOTIFICATION With End Button''',font="Times 12 italic underline",bg="#0e7885",fg="white")
        d.place(x=40,y=380)
        remove_list.append(d)
        e=Label(text='''3. Hard mode - FULL screen notification no end Button.''',font="Times 12 italic underline",bg="#0e7885",fg="white")
        e.place(x=40,y=410)
        remove_list.append(e)
        f=Label(text='''4. Extream mode - WILL SHUTDOWN YOUR PC AT AZAN TIME.''',font="Times 12 italic underline",bg="#0e7885",fg="white")
        f.place(x=40,y=440)
        remove_list.append(f)

        # CheckBoxes

        mode=Radiobutton(bg="#0e7885",variable=mode_value,value=1)
        mode.place(x=10,y=350)
        remove_list.append(mode)
        mode=Radiobutton(bg="#0e7885",variable=mode_value,value=2)
        mode.place(x=10,y=380)
        remove_list.append(mode)
        mode=Radiobutton(bg="#0e7885",variable=mode_value,value=3)
        mode.place(x=10,y=410)
        remove_list.append(mode)
        mode=Radiobutton(bg="#0e7885",variable=mode_value,value=4)
        mode.place(x=10,y=440)
        remove_list.append(mode)

        #Button
        submit=Button(text="Submit",command=logic,padx=10,bg="#0e7885",fg="white")
        submit.place(x=50,y=470)
        remove_list.append(submit)
        change_call=Button(text="Change Salah time",padx=5,bg="#0e7885",fg="white",command=Change_Salah_Time)
        change_call.place(x=380,y=10)
        remove_list.append(change_call)
        Home_Img = Image.open(f"{dir_path}\\Icon\\home-button.png")
        Home_Img = Home_Img.resize((30,30), Image.ANTIALIAS)
        Home_Img = ImageTk.PhotoImage(Home_Img)
        Home_Button=Button(bg="#06324b",image=Home_Img,borderwidth=1,activebackground="#0f6e80",relief=GROOVE,command=home_func)
        Home_Button.image = Home_Img
        Home_Button.place(x=5,y=5)

    #From here starts the mode sections

    def easy():
        with open(f"{dir_path}\\Data\\TimeNow.dat",'rb') as t:
            agft=pickle.load(t)
        print(agft)
        #Importing Modules
        from plyer import notification
        from playsound import playsound
        from tkinter import messagebox
        username=getpass.getuser()#to take username
        #Reading Salah time
        with open(f"{dir_path}\\Data\\SalahTimes.dat",'rb') as salahtime:
            salahtimes=pickle.load(salahtime)
        salahtimes=str(salahtimes)
        salahtimes=salahtimes.replace("[","")
        salahtimes=salahtimes.replace("]","")
        salahtimes=salahtimes.replace("'","")
        salahtimes=salahtimes.split(",")
        
        #Files load
        fajr_audio=dir_path+"\\Audio\\fajr.mp3"
        audio_mp3=dir_path+"\\Audio\\azan.mp3"
        appicon=dir_path+"\\Icon\\bg.ico"

        print("Its the time for Fajr")
        playsound(fajr_audio,False)#uses playsound moldule
        notification.notify(title="Its the time for Fajr",#uses plyer module
        
        message='''QURAN 2:110,
        "And establish prayer and give zakah, and whatever good you put forward for yourselves 
        You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
        app_icon= appicon,
        timeout=120,
        toast=False)
        with open(f"{dir_path}\\Data\\TimeNow.dat",'rb') as timenow1:
            b=pickle.load(timenow1)

        if b==(salahtimes[0]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Fajr")
            playsound(fajr_audio,False)#uses playsound moldule
            notification.notify(title="Its the time for Fajr",#uses plyer module
            
            message='''QURAN 2:110,
        "And establish prayer and give zakah, and whatever good you put forward for yourselves 
        You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
            app_icon= appicon,
            timeout=120,
            toast=False)
            
        if b==(salahtimes[1]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Duhar")
            playsound(audio_mp3,False)
            notification.notify(title="Its the time for Duhar",
            message='''QURAN 2:110,
        "And establish prayer and give zakah, and whatever good you put forward for yourselves 
        You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
            app_icon= appicon,
            timeout=120,
            toast=False)
            
        if b==(salahtimes[2]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Asr")
            playsound(audio_mp3,False)
            notification.notify(title="Its the time for Asr",
            message='''QURAN 2:110,
        "And establish prayer and give zakah, and whatever good you put forward for yourselves 
        You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
            app_icon= appicon,
            timeout=120,
            toast=False)
            
        if b==(salahtimes[3]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Magrib")
            playsound(audio_mp3,False)
            notification.notify(title="Its the time for Magrib",
            message='''QURAN 2:110,
        "And establish prayer and give zakah, and whatever good you put forward for yourselves 
        You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
            app_icon= appicon,
            timeout=120,
            toast=False)
            
        if b==(salahtimes[4]):  #YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Isha")
            playsound(audio_mp3,False)
            notification.notify(title="Its the time for Isha",
            app_name="Come to Succes",
            message='''QURAN 2:110,
        "And establish prayer and give zakah, and whatever good you put forward for yourselves 
        You will find it with Allah. Indeed, Allah of what you do, is Seeing."''',
            app_icon= appicon,
            timeout=120,
            toast=False)
            
        webbrowser.open(dir_path+"mode_selector.pyw")
    
    def mediam():
        #Importing Modules
        

        def pic():
            import time
            salah=Tk()
            salah.title("Come To Success")
            screen_width = salah.winfo_screenwidth()
            screen_height = salah.winfo_screenheight()
            salah.resizable(False,False)
            mycolor = '#d3d3d3'
            salah.configure(background=mycolor)
            salah.attributes("-fullscreen", True)
            salah.wm_attributes("-topmost", 1)
            img2=Image.open("Icon\\pic.png")
            image1 = img2.resize((screen_width, screen_height), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image1)
            Label(salah,image=img).pack()
            hour=StringVar()
            minute=StringVar()
            second=StringVar()
            hour.set("00")
            minute.set("15")
            second.set("00")
            def disable_event():
                pass
            salah.protocol("WM_DELETE_WINDOW", disable_event)

            Button(text="Click here to quit",command=salah.destroy,padx=10,pady=10,bg="#f4f5f0", font="defalt 20 bold italic").place(x=150,y=350)
            Label(salah,text="Its time for Prayer",width=30, font="Arial 20 bold italic").place(x=10,y=200)
            Label(salah,width=45,text="Please go and Pray dont delay",bg="#f4f5f0", font="Arial 20 bold italic").place(x=10,y=250)
            hourEntry= Entry(salah, width=2, font="Arial 80",bg="#f4f5f0",textvariable=hour)
            hourEntry.place(x=450,y=300)
            minuteEntry= Entry(salah, width=2, font="Arial 80",bg="#f4f5f0",textvariable=minute)
            minuteEntry.place(x=600,y=300)
            
            secondEntry= Entry(salah, width=2, font="Arial 80",fg="White",bg="#3b2e1e",textvariable=second)
            secondEntry.place(x=750,y=300)

            
            try:
                # the input provided by the user is
                # stored in here :temp
                temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
            except:
                print("Please input the right value")
            while temp >-1:
                # divmod(firstvalue = temp//60, secondvalue = temp%60)
                mins,secs = divmod(temp,60)

                # Converting the input entered in mins or secs to hours,
                # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                # 50min: 0sec)
                hours=0
                if mins >60:
                    
                    # divmod(firstvalue = temp//60, secondvalue
                    # = temp%60)
                    hours, mins = divmod(mins, 60)
                
                # using format () method to store the value up to
                # two decimal places
                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                # updating the GUI window after decrementing the
                # temp value every time
                salah.update()
                time.sleep(1)

                # when temp value = 0; then a messagebox pop's up
                # with a message:"Time's up"
                if (temp == 0):
                    time.sleep(2)
                    salah.destroy()
                
                # after every one sec the value of temp will be decremented
                # by one
                temp -= 1
            salah.mainloop()

        username=getpass.getuser()#to take username

        #Reading Salah time
        with open(f"{dir_path}\\Data\\SalahTimes.dat",'rb') as salahtime:
            salahtimes=pickle.load(salahtime)
        salahtimes=str(salahtimes)
        salahtimes=salahtimes.replace("[","")
        salahtimes=salahtimes.replace("]","")
        salahtimes=salahtimes.replace("'","")
        salahtimes=salahtimes.split(",")

        #Files load
        fajr_audio=dir_path+"\\Audio\\fajr.mp3"
        audio_mp3=dir_path+"\\Audio\\azan.mp3"
        appicon=dir_path+"\\Icon\\icon.ico"

        with open(f"{dir_path}\\Data\\TimeNow.dat",'rb') as timenow1:
            b=pickle.load(timenow1)

        if b==(salahtimes[0]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            playsound(audio_mp3,False)
            try:
                pic()
            except Exception as e:
                print(e)
            
        if b==(salahtimes[1]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            playsound(audio_mp3,False)
            try:
                pic()
            except Exception as e:
                print(e)
            
        if b==(salahtimes[2]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            playsound(audio_mp3,False)
            try:
                pic()
            except Exception as e:
                print(e)
            
        if b==(salahtimes[3]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            playsound(audio_mp3,False)
            try:
                pic()
            except Exception as e:
                print(e)
            
        if b==(salahtimes[4]):  #YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            playsound(audio_mp3,False)
            try:
                pic()
            except Exception as e:
                print(e)
                
        webbrowser.open(dir_path+"\\mode_selector.pyw")

    def hard():
        import time as t
        a=getpass.getuser()
        def pic():
            import time
            salah=Tk()
            salah.title("Come To Success")
            screen_width = salah.winfo_screenwidth()
            screen_height = salah.winfo_screenheight()
            salah.geometry("1330x800")
            salah.resizable(False,False)
            mycolor = '#d3d3d3'
            salah.configure(background=mycolor)
            salah.attributes("-fullscreen", True)
            salah.wm_attributes("-topmost", 1)
            img2=Image.open("Icon\\pic.png")
            image1 = img2.resize((screen_width, screen_height), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image1)
            Label(salah,image=img).pack()
            hour=StringVar()
            minute=StringVar()
            second=StringVar()
            hour.set("00")
            minute.set("15")
            second.set("00")
            def disable_event():
                pass
            salah.protocol("WM_DELETE_WINDOW", disable_event)

            Label(salah,width=40,text="Its time for Prayer", font=("defalt",20,"")).place(x=450,y=10)
            Label(salah,width=45,text="Please go and Pray dont delay",bg="#f4f5f0", font=("defalt",20,"",)).place(x=1,y=200)
            hourEntry= Entry(salah, width=2, font=("Arial",80,""),bg="#f4f5f0",
                            textvariable=hour)
            hourEntry.place(x=450,y=300)
            
            minuteEntry= Entry(salah, width=2, font=("Arial",80,""),bg="#f4f5f0",
                            textvariable=minute)
            minuteEntry.place(x=600,y=300)
            
            secondEntry= Entry(salah, width=2, font=("Arial",80,""),fg="White",bg="#3b2e1e",
                            textvariable=second)
            secondEntry.place(x=750,y=300)
            try:
                # the input provided by the user is
                # stored in here :temp
                temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
            except:
                print("Please input the right value")
            while temp >-1:
                
                # divmod(firstvalue = temp//60, secondvalue = temp%60)
                mins,secs = divmod(temp,60)

                # Converting the input entered in mins or secs to hours,
                # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                # 50min: 0sec)
                hours=0
                if mins >60:
                    
                    # divmod(firstvalue = temp//60, secondvalue
                    # = temp%60)
                    hours, mins = divmod(mins, 60)
                
                # using format () method to store the value up to
                # two decimal places
                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                # updating the GUI window after decrementing the
                # temp value every time
                salah.update()
                time.sleep(1)

                # when temp value = 0; then a messagebox pop's up
                # with a message:"Time's up"
                if (temp == 0):
                    time.sleep(2)
                    salah.destroy()
                
                # after every one sec the value of temp will be decremented
                # by one
                temp -= 1
            salah.mainloop()

        a=getpass.getuser()
        username=getpass.getuser()#to take username

        #Reading Salah time
        with open(f"{dir_path}\\Data\\SalahTimes.dat",'rb') as salahtime:
            salahtimes=pickle.load(salahtime)
        salahtimes=str(salahtimes)
        salahtimes=salahtimes.replace("[","")
        salahtimes=salahtimes.replace("]","")
        salahtimes=salahtimes.replace("'","")
        salahtimes=salahtimes.split(",")

        #Files load
        fajr_audio=dir_path+"\\Audio\\fajr.mp3"
        audio_mp3=dir_path+"\\Audio\\azan.mp3"
        appicon=dir_path+"\\Icon\\icon.ico"

        with open(f"{dir_path}\\Modes\\TimeNow.dat") as timenow1:
            b=timenow1.load()

        if b==(salahtimes[0]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Fajr")
            playsound(fajr_audio,False)
            try: 
                pic()
            except Exception as e:
                print(e)

        if b==(salahtimes[1]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Duhar")
            playsound(audio_mp3,False)
            try: 
                pic()
            except Exception as e:
                print(e)
        if b==(salahtimes[2]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Asr")
            playsound(audio_mp3,False)
            try: 
                pic()
            except Exception as e:
                print(e)

        if b==(salahtimes[3]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Magrib")
            playsound(audio_mp3,False)
            try: 
                pic()
            except Exception as e:
                print(e)
        if b==(salahtimes[4]):  #YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Isha")
            playsound(audio_mp3,False)
            try: 
                pic()
            except Exception as e:
                print(e)
        webbrowser.open(dir_path+"\\mode_selector.pyw")
    
    def extream():
        def pic():
            salah=Tk()
            salah.title("Come To Success")
            screen_width = salah.winfo_screenwidth()
            screen_height = salah.winfo_screenheight()
            salah.geometry("1330x800")
            salah.resizable(False,False)
            mycolor = '#d3d3d3'
            salah.configure(background=mycolor)
            # salah.attributes("-fullscreen", True)
            img2=Image.open("Icon\\pic.png")
            image1 = img2.resize((screen_width, screen_height), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image1)
            Label(salah,image=img).pack()
            hour=StringVar()
            minute=StringVar()
            second=StringVar()
            hour.set("00")
            minute.set("05")
            second.set("00")
            def disable_event():
                pass
            salah.protocol("WM_DELETE_WINDOW", disable_event)
            # Use of Entry class to take input from the user
            Label(salah,width=40,text="You have 5 minutes to save your work!", font=("defalt",20,"")).place(x=450,y=10)
            Label(salah,width=45,text="Note: You cannot close this,\n                         So minimize this window and save your work.",bg="#f4f5f0", font=("defalt",20,"",)).place(x=1,y=200)
            hourEntry= Entry(salah, width=2, font=("Arial",80,""),bg="#f4f5f0",
                            textvariable=hour)
            hourEntry.place(x=450,y=300)
            
            minuteEntry= Entry(salah, width=2, font=("Arial",80,""),bg="#f4f5f0",
                            textvariable=minute)
            minuteEntry.place(x=600,y=300)
            
            secondEntry= Entry(salah, width=2, font=("Arial",80,""),fg="White",bg="#3b2e1e",
                            textvariable=second)
            secondEntry.place(x=750,y=300)
            try:
                # the input provided by the user is
                # stored in here :temp
                temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
            except:
                print("Please input the right value")
            while temp >-1:
                
                # divmod(firstvalue = temp//60, secondvalue = temp%60)
                mins,secs = divmod(temp,60)

                # Converting the input entered in mins or secs to hours,
                # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                # 50min: 0sec)
                hours=0
                if mins >60:
                    
                    # divmod(firstvalue = temp//60, secondvalue
                    # = temp%60)
                    hours, mins = divmod(mins, 60)
                
                # using format () method to store the value up to
                # two decimal places
                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                # updating the GUI window after decrementing the
                # temp value every time
                salah.update()
                time.sleep(1)

                # when temp value = 0; then a messagebox pop's up
                # with a message:"Time's up"
                if (temp == 0):
                    time.sleep(2)
                    salah.destroy()
                
                # after every one sec the value of temp will be decremented
                # by one
                temp -= 1
            
            # button widget
            salah.mainloop()
        a=getpass.getuser()
        dir_path = os.path.dirname(os.path.realpath(__file__)) #to take File path
        username=getpass.getuser()#to take username


        #Reading Salah time
        with open(f"{dir_path}\\Data\\SalahTimes.dat",'rb') as salahtime:
            salahtimes=pickle.load(salahtime)
        salahtimes=str(salahtimes)
        salahtimes=salahtimes.replace("[","")
        salahtimes=salahtimes.replace("]","")
        salahtimes=salahtimes.replace("'","")
        salahtimes=salahtimes.split(",")

        pic()
        os.system("shutdown /s /t 1")
        #Files load
        fajr_audio=dir_path+"\\Audio\\fajr.mp3"
        audio_mp3=dir_path+"\\Audio\\azan.mp3"
        appicon=dir_path+"\\Icon\\icon.ico"
        with open(f"{dir_path}\\Modes\\TimeNow.dat") as timenow1:
            b=timenow1.load()

        if b==(salahtimes[0]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Fajr")
            playsound(fajr_audio,False)
            pic()
            os.system("shutdown /s /t 1")
            
        if b==(salahtimes[1]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Duhar")
            playsound(audio_mp3,False)
            pic()
            os.system("shutdown /s /t 1")
            
        if b==(salahtimes[2]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Asr")
            playsound("audio.mp3",False)

            pic()
            os.system("shutdown /s /t 1")
            
        if b==(salahtimes[3]):#YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Magrib")
            playsound(audio_mp3,False)
            pic()
            os.system("shutdown /s /t 1")
            
        if b==(salahtimes[4]):  #YOU CAN CHANGE ACCORDING TO YOUR PLACES 
            print(b,"Its the time for Isha")
            playsound(audio_mp3,False)
            pic()
            os.system("shutdown /s /t 1")
            
        webbrowser.open(dir_path+"\\mode_selector.pyw")
if __name__=='__main__':
    a_root=Gui()
    a_root.mainloop()
