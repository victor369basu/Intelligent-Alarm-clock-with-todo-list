from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from time import strftime
import datetime
import pygame.mixer
from time import sleep
from threading import Thread, Timer
import calendar
import pyowm
import dill
from PIL import Image, ImageTk
import win32com.client
from win32com.client import Dispatch
import os
#from sys import exit
#print('125')
time_1 = ''
Alarm_1 = ''
m_1 =''
Alarm_2 = ''
m_2 =''
Alarm_3 = ''
m_3 =''
Alarm_4 = ''
m_4 =''
Alarm_5 = ''
m_5 = ''
Alarm_6 = ''
m_6 =''
Alarm_7 = ''
m_7 =''
Alarm_8 = ''
m_8 =''
Alarm_9 = ''
m_9 =''
Alarm_10 = ''
m_10 = ''
Todo_Al_1 = ''
Todo_M1 = ''
Todo_Al_2 = ''
Todo_M2 = ''
Todo_Al_3 = ''
Todo_M3 = ''
Todo_Al_4 = ''
Todo_M4 = ''
Todo_Al_5 = ''
Todo_M5 = ''
Todo_Al_6 = ''
Todo_M6 = ''
Todo_Al_7 = ''
Todo_M7 = ''
Todo_Al_8 = ''
Todo_M8 = ''
Todo_Al_9 = ''
Todo_M9 = ''
Todo_Al_10 = ''
Todo_M10 = ''
Todo_Al_11 = ''
Todo_M11 = ''
Todo_Al_12 = ''
Todo_M12 = ''
date_ = ''
with open('Alarm_time.plk', 'rb')as z1:
    try:
        Alarm_1 = dill.load(z1)
    except:
        pass
if (Alarm_1 == ''):
    count_a = 0
count_b = 0
count_c = 0
x = 0
Z_Play = 1
Z_Play_todo = 1
Z_play_check=0
Z_play_todo_check=0
To_do_m = 0
loop = 0
check_loop = 0
root = Tk()
root.title('BURN')
root.minsize(height = 688,width = 1346)
root.maxsize(height = 758,width = 1386)
root.configure(background= 'black')
root.attributes('-alpha',0.698)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #root.destroy()
        #os.system("start /B start cmd.exe @cmd /k python Alarm_NEW.py")
        Wm.iconify(root)

def reset():
    os.remove(os.getcwd()+'\\Alarm_count.plk')
    os.remove(os.getcwd()+'\\Alarm_time.plk')
    os.remove(os.getcwd()+'\\Weather_ALARM.plk')
    os.remove(os.getcwd()+'\\Alarm_time_mess.plk')
    os.remove(os.getcwd()+'\\Alarm_todo_count.plk')
    os.remove(os.getcwd()+'\\Alarm_todo_mess.plk')
    os.remove(os.getcwd()+'\\Alarm_todo_time.plk')
    os.remove(os.getcwd()+'\\Alarm_todo_tone.plk')
    os.remove(os.getcwd()+'\\Alarm_tone.plk')

    f0 = open(os.getcwd()+'\\Alarm_count.plk','w+')
    f0.close()
    f1 = open(os.getcwd()+'\\Alarm_time.plk', 'w+')
    f1.close()
    f2 = open(os.getcwd()+'\\Weather_ALARM.plk', 'w+')
    f2.close()
    f3 = open(os.getcwd()+'\\Alarm_time_mess.plk', 'w+')
    f3.close()
    f4 = open(os.getcwd()+'\\Alarm_todo_count.plk', 'w+')
    f4.close()
    f5 = open(os.getcwd()+'\\Alarm_todo_mess.plk', 'w+')
    f5.close()
    f6 = open(os.getcwd()+'\\Alarm_todo_time.plk', 'w+')
    f6.close()
    f7 = open(os.getcwd()+'\\Alarm_todo_tone.plk', 'w+')
    f7.close()
    f8 = open(os.getcwd()+'\\Alarm_tone.plk', 'w+')
    f8.close()
    #python = sys.executable
    #print(python)
    #os.execv(python,['python'] + sys.argv)
    root.destroy()
    os.system("start /B start cmd.exe @cmd /k python Alarm_NEW.py")

def set_Startup():
    try:
        objShell = win32com.client.Dispatch("WScript.Shell")
        startupFlder = objShell.SpecialFolders("Startup")
        path = os.path.join(startupFlder, "Alarm_NEW.lnk")

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = os.getcwd()+'\\Alarm_NEW.exe'
        shortcut.WorkingDirectory = os.getcwd()+"\\"
        shortcut.IconLocation = os.getcwd()+'\\Alarm_NEW.exe'

        shortcut.Save()
    except:
        pass

def open_tones():
    global Z_Play, Z_Play_todo, Z_play_check, Z_play_todo_check
    try:
        with open('Alarm_todo_tone.plk', 'rb') as s11:
            Z_play_check = dill.load(s11)
            Z_Play_todo = dill.load(s11)
    except:
        pass
    try:
        with open('Alarm_tone.plk', 'rb') as s1:
            Z_play_check = dill.load(s1)
            Z_Play = dill.load(s1)
    except:
        pass
def Alarm_M():
    def call_Alarm_M():
        global Alarm_1
        global Alarm_2
        global Alarm_3
        global Alarm_4
        global Alarm_5
        global Alarm_6
        global Alarm_7
        global Alarm_8
        global Alarm_9
        global Alarm_10
        global m_1
        global m_2
        global m_3
        global m_4
        global m_5
        global m_6
        global m_7
        global m_8
        global m_9
        global m_10
        global count_a
        with open('Alarm_count.plk', 'wb')as z9:
            dill.dump(count_a, z9)
        with open('Alarm_time.plk', 'wb')as z12:
            dill.dump(Alarm_1, z12)
            dill.dump(Alarm_2, z12)
            dill.dump(Alarm_3, z12)
            dill.dump(Alarm_4, z12)
            dill.dump(Alarm_5, z12)
            dill.dump(Alarm_6, z12)
            dill.dump(Alarm_7, z12)
            dill.dump(Alarm_8, z12)
            dill.dump(Alarm_9, z12)
            dill.dump(Alarm_10, z12)
        with open('Alarm_time_mess.plk', 'wb')as z22:
            dill.dump(m_1, z22)
            dill.dump(m_2, z22)
            dill.dump(m_3, z22)
            dill.dump(m_4, z22)
            dill.dump(m_5, z22)
            dill.dump(m_6, z22)
            dill.dump(m_7, z22)
            dill.dump(m_8, z22)
            dill.dump(m_9, z22)
            dill.dump(m_10, z22)
        Alarm_M()

    global Alarm_1, Alarm_2, Alarm_3, Alarm_4, Alarm_5, Alarm_6, Alarm_7, Alarm_8, Alarm_9, Alarm_10
    global m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9, m_10
    global count_a
    global loop
    cover = Label(root,bg= 'black', height = 50, width = 80)
    cover.pack()
    cover.place( x = 920,y = 70)
    i=0
    #count_Present = 0
    #count_Present = count_Present + 1
    with open('Alarm_time.plk', 'rb') as zz:
        try:
            Alarm_1 = dill.load(zz)
        except:
            pass
        try:
            Alarm_2 = dill.load(zz)
        except:
            pass
        try:
            Alarm_3 = dill.load(zz)
        except:
            pass
        try:
            Alarm_4 = dill.load(zz)
        except:
            pass
        try:
            Alarm_5 = dill.load(zz)
        except:
            pass
        try:
            Alarm_6 = dill.load(zz)
        except:
            pass
        try:
            Alarm_7 = dill.load(zz)
        except:
            pass
        try:
            Alarm_8 = dill.load(zz)
        except:
            pass
        try:
            Alarm_9 = dill.load(zz)
        except:
            pass
        try:
            Alarm_10 = dill.load(zz)
        except:
            pass
    with open('Alarm_time_mess.plk', 'rb')as zp2:
        try:
            m_1 = dill.load(zp2)
        except:
            pass
        try:
            m_2 = dill.load(zp2)
        except:
            pass
        try:
            m_3 = dill.load(zp2)
        except:
            pass
        try:
            m_4 = dill.load(zp2)
        except:
            pass
        try:
            m_5 = dill.load(zp2)
        except:
            pass
        try:
            m_6 = dill.load(zp2)
        except:
            pass
        try:
            m_7 = dill.load(zp2)
        except:
            pass
        try:
            m_8 = dill.load(zp2)
        except:
            pass
        try:
            m_9 = dill.load(zp2)
        except:
            pass
        try:
            m_10 = dill.load(zp2)
        except:
            pass
    with open('Alarm_count.plk', 'rb')as z:
        try:
            count_a = dill.load(z)
        except:
            pass
    if(Alarm_1 != ''):
        Al_C_1 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_1[:5]+" "+Alarm_1[8:]+' ',relief='raised', borderwidth=7)
        Al_C_1.pack()
        Al_C_1.place( x = 920,y = 90 + i)
        print(Al_C_1.cget("text"))
        i = i + 50
        #count_Present = count_Present + 1
    if(loop == 1):
        Alarm_1 = Alarm_2[:]
        Alarm_2 = Alarm_3[:]
        Alarm_3 = Alarm_4[:]
        Alarm_4 = Alarm_5[:]
        Alarm_5 = Alarm_6[:]
        Alarm_6 = Alarm_7[:]
        Alarm_7 = Alarm_8[:]
        Alarm_8 = Alarm_9[:]
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_1 = m_2[:]
        m_2 = m_3[:]
        m_3 = m_4[:]
        m_4 = m_5[:]
        m_5 = m_6[:]
        m_6 = m_7[:]
        m_7 = m_8[:]
        m_8 = m_9[:]
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if (Alarm_2 != ''):
        Al_C_2 = Label(root, font=('ms serif', 25), fg='blue', bg='white',text=Alarm_2[:5] + " " + Alarm_2[8:] + ' ', relief='raised', borderwidth=7)
        Al_C_2.pack()
        Al_C_2.place(x=920, y=90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if(loop == 3):
        Alarm_2 = Alarm_3[:]
        Alarm_3 = Alarm_4[:]
        Alarm_4 = Alarm_5[:]
        Alarm_5 = Alarm_6[:]
        Alarm_6 = Alarm_7[:]
        Alarm_7 = Alarm_8[:]
        Alarm_8 = Alarm_9[:]
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_2 = m_3[:]
        m_3 = m_4[:]
        m_4 = m_5[:]
        m_5 = m_6[:]
        m_6 = m_7[:]
        m_7 = m_8[:]
        m_8 = m_9[:]
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if (Alarm_3 !=''):
        Al_C_3 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_3[:5]+" "+Alarm_3[8:]+' ',relief='raised', borderwidth=7)
        Al_C_3.pack()
        Al_C_3.place( x = 920,y = 90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if(loop == 5):
        Alarm_3 = Alarm_4[:]
        Alarm_4 = Alarm_5[:]
        Alarm_5 = Alarm_6[:]
        Alarm_6 = Alarm_7[:]
        Alarm_7 = Alarm_8[:]
        Alarm_8 = Alarm_9[:]
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_3 = m_4[:]
        m_4 = m_5[:]
        m_5 = m_6[:]
        m_6 = m_7[:]
        m_7 = m_8[:]
        m_8 = m_9[:]
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if(Alarm_4 !=''):
        Al_C_4 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_4[:5]+" "+Alarm_4[8:]+' ',relief='raised', borderwidth=7)
        Al_C_4.pack()
        Al_C_4.place( x = 920,y = 90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if(loop == 7):
        Alarm_4 = Alarm_5[:]
        Alarm_5 = Alarm_6[:]
        Alarm_6 = Alarm_7[:]
        Alarm_7 = Alarm_8[:]
        Alarm_8 = Alarm_9[:]
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_4 = m_5[:]
        m_5 = m_6[:]
        m_6 = m_7[:]
        m_7 = m_8[:]
        m_8 = m_9[:]
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if(Alarm_5 !=''):
        Al_C_5 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_5[:5]+" "+Alarm_5[8:]+' ',relief='raised', borderwidth=7)
        Al_C_5.pack()
        Al_C_5.place( x = 920,y = 90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if (loop == 9):
        Alarm_5 = Alarm_6[:]
        Alarm_6 = Alarm_7[:]
        Alarm_7 = Alarm_8[:]
        Alarm_8 = Alarm_9[:]
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_5 = m_6[:]
        m_6 = m_7[:]
        m_7 = m_8[:]
        m_8 = m_9[:]
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if (Alarm_6 !=''):
        Al_C_6 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_6[:5]+" "+Alarm_6[8:]+' ',relief='raised', borderwidth=7)
        Al_C_6.pack()
        Al_C_6.place( x = 920,y = 90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if (loop == 11):
        Alarm_6 = Alarm_7[:]
        Alarm_7 = Alarm_8[:]
        Alarm_8 = Alarm_9[:]
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_6 = m_7[:]
        m_7 = m_8[:]
        m_8 = m_9[:]
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if(Alarm_7 !=''):
        Al_C_7 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_7[:5]+" "+Alarm_7[8:]+' ',relief='raised', borderwidth=7)
        Al_C_7.pack()
        Al_C_7.place( x = 920,y = 90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if (loop == 13):
        Alarm_7 = Alarm_8[:]
        Alarm_8 = Alarm_9[:]
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_7 = m_8[:]
        m_8 = m_9[:]
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if(Alarm_8 !=''):
        Al_C_8 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_8[:5]+" "+Alarm_8[8:]+' ',relief='raised', borderwidth=7)
        Al_C_8.pack()
        Al_C_8.place( x = 920,y = 90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if (loop == 15):
        Alarm_8 = Alarm_9[:]
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_8 = m_9[:]
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if(Alarm_9 !=''):
        Al_C_9 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_9[:5]+" "+Alarm_9[8:]+' ',relief='raised', borderwidth=7)
        Al_C_9.pack()
        Al_C_9.place( x = 920,y = 90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if (loop == 17):
        Alarm_9 = Alarm_10[:]
        Alarm_10 = ''
        m_9 = m_10[:]
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    if(Alarm_10 !=''):
        Al_C_10 = Label(root, font=('ms serif', 25), fg='blue', bg='white', text=Alarm_10[:5]+" "+Alarm_10[8:]+' ',relief='raised', borderwidth=7)
        Al_C_10.pack()
        Al_C_10.place( x = 920,y = 90 + i)
        i = i + 50
        #count_Present = count_Present + 1
    if (loop == 19):
        Alarm_10 = ''
        m_10 = ''
        count_a = count_a - 1
        loop = 0
        call_Alarm_M()
    with open('Alarm_count.plk', 'wb')as z9:
        dill.dump(count_a, z9)
    with open('Alarm_time.plk', 'wb')as z12:
        dill.dump(Alarm_1, z12)
        dill.dump(Alarm_2, z12)
        dill.dump(Alarm_3, z12)
        dill.dump(Alarm_4, z12)
        dill.dump(Alarm_5, z12)
        dill.dump(Alarm_6, z12)
        dill.dump(Alarm_7, z12)
        dill.dump(Alarm_8, z12)
        dill.dump(Alarm_9, z12)
        dill.dump(Alarm_10, z12)
    with open('Alarm_time_mess.plk', 'wb')as z22:
        dill.dump(m_1, z22)
        dill.dump(m_2, z22)
        dill.dump(m_3, z22)
        dill.dump(m_4, z22)
        dill.dump(m_5, z22)
        dill.dump(m_6, z22)
        dill.dump(m_7, z22)
        dill.dump(m_8, z22)
        dill.dump(m_9, z22)
        dill.dump(m_10, z22)

def Ring_TO_do(to_do_t):
    global Todo_Al_1, Todo_M1, Todo_Al_2, Todo_M2, Todo_Al_3, Todo_M3, Todo_Al_4, Todo_M4, Todo_Al_5,Todo_M5, Todo_Al_6,Todo_M6,Todo_Al_7,Todo_M7
    global Todo_Al_8, Todo_M8, Todo_Al_9, Todo_M9, Todo_Al_10, Todo_M10, Todo_Al_11, Todo_M11, Todo_Al_12, Todo_M12
    def on_closing_todo():
        if (pygame.mixer.get_init()):
            pygame.mixer.music.stop()
    Todo_ = Toplevel(root)
    Todo_.title("TODO-LIST-ALARM")
    Todo_.configure(background = 'black')
    #Todo_.attributes("-toolwindow", 10)
    Todo_ring = to_do_t
    def over_todo():
        pygame.mixer.music.stop()
        Todo_.destroy()
    ring_prio = Label(Todo_, font=('ms serif', 30), text=' PRIORITY ', fg='dodgerblue', bg='black', relief='raised', borderwidth=2)
    ring_prio.pack()
    Arrow = Label(Todo_, font=('ms serif', 30), text=u'\u2193', fg='magenta', bg='black')
    Arrow.pack()
    #ring_prio.place(x= 20 , y=50)
    def play_todo():
        global Z_Play_todo
        pygame.mixer.init()
        if (Z_Play_todo==1):
            pygame.mixer.music.load(open(os.getcwd()+"\Loud_Alarm_Clock_Buzzer-Muk1984-493547174.wav", "rb"))
        if (Z_Play_todo==2):
            pygame.mixer.music.load(open(os.getcwd()+"\Rooster Crow-SoundBible.com-1802551702.wav", "rb"))
        if (Z_Play_todo==3):
            pygame.mixer.music.load(open(os.getcwd()+"\Pager Beeps-SoundBible.com-260751720.wav", "rb"))
        if (Z_Play_todo==4):
            pygame.mixer.music.load(open(os.getcwd()+"\Analog-watch-alarm_daniel_simon.wav", "rb"))
        if (Z_Play_todo==5):
            pygame.mixer.music.load(open(os.getcwd()+"\submarine-diving-alarm-daniel_simon.wav", "rb"))
        if (Z_Play_todo==6):
            pygame.mixer.music.load(open(os.getcwd()+"\old-fashioned-door-bell-daniel_simon.wav", "rb"))
        if (Z_Play_todo==7):
            pygame.mixer.music.load(open(os.getcwd()+"\Railroad_crossing_bell_Brylon_Terry-1551570865.wav", "rb"))
        if (Z_Play_todo==8):
            pygame.mixer.music.load(open(os.getcwd()+"\Tornado Siren-SoundBible.com-897026957.wav", "rb"))
        if (Z_Play_todo==9):
            pygame.mixer.music.load(open(os.getcwd()+"\Police Siren 3-SoundBible.com-553177907.wav", "rb"))
        if (Z_Play_todo==10):
            pygame.mixer.music.load(open(os.getcwd()+"\church-chime-daniel_simon.wav", "rb"))
        if (Z_Play_todo==11):
            with open('Alarm_todo_tone.plk', 'rb') as s11:
                Z_play_check = dill.load(s11)
                Z_Play_todo = dill.load(s11)
                file_path_todo = dill.load(s11)
            pygame.mixer.music.load(open(file_path_todo[0], "rb"))
        pygame.mixer.music.play(-1)
        while (pygame.mixer.music.get_busy() == True):
            sleep(23)
    with open('Alarm_todo_mess.plk', 'rb')as zm:
        Todo_M1 = dill.load(zm)
        Todo_M2 = dill.load(zm)
        Todo_M3 = dill.load(zm)
        Todo_M4 = dill.load(zm)
        Todo_M5 = dill.load(zm)
        Todo_M6 = dill.load(zm)
        Todo_M7 = dill.load(zm)
        Todo_M8 = dill.load(zm)
        Todo_M9 = dill.load(zm)
        Todo_M10 = dill.load(zm)
        Todo_M11 = dill.load(zm)
        Todo_M12 = dill.load(zm)

    if(Todo_ring == Todo_Al_1[:23]):
        def blink():
            current_color = t1.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t1.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target= play_todo)
        thread_todo_play.start()
        t1 = Label(Todo_, font=('impact', 30), text= " "+Todo_Al_1[27: ]+" ", fg='red', bg='black', relief='raised', borderwidth=2)
        t1.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised', borderwidth=2)
        ring_M.pack()
        to1 = StringVar()
        l1 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to1, relief='raised', borderwidth=7,width = 500)
        to1.set(Todo_M1)
        if (Todo_M1 == ''):
            to1.set(' WORKING TIME ')
        l1.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove', borderwidth=5,command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_2[:23]):
        def blink():
            current_color = t2.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t2.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t2 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_2[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t2.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to2 = StringVar()
        l2 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to2, relief='raised',borderwidth=7, width=500)
        to2.set(Todo_M2)
        if (Todo_M2 == ''):
            to2.set(' WORKING TIME ')
        l2.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_3[:23]):
        def blink():
            current_color = t3.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t3.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t3 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_3[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t3.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to3 = StringVar()
        l3 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to3, relief='raised',borderwidth=7, width=500)
        to3.set(Todo_M3)
        if (Todo_M3 == ''):
            to3.set(' WORKING TIME ')
        l3.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_4[:23]):
        def blink():
            current_color = t4.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t4.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t4 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_4[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t4.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to4 = StringVar()
        l4 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to4, relief='raised',borderwidth=7, width=500)
        to4.set(Todo_M4)
        if (Todo_M4 == ''):
            to4.set(' WORKING TIME ')
        l4.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_5[:23]):
        def blink():
            current_color = t5.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t5.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t5 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_5[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t5.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to5 = StringVar()
        l5 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to5, relief='raised',borderwidth=7, width=500)
        to5.set(Todo_M5)
        if (Todo_M5 == ''):
            to5.set(' WORKING TIME ')
        l5.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_6[:23]):
        def blink():
            current_color = t6.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t6.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t6 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_6[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t6.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to6 = StringVar()
        l6 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to6, relief='raised',borderwidth=7, width=500)
        to6.set(Todo_M6)
        if (Todo_M6 == ''):
            to6.set(' WORKING TIME ')
        l6.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_7[:23]):
        def blink():
            current_color = t7.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t7.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t7 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_7[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t7.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to7 = StringVar()
        l7 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to7, relief='raised',borderwidth=7, width=500)
        to7.set(Todo_M7)
        if (Todo_M7 == ''):
            to7.set(' WORKING TIME ')
        l7.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_8[:23]):
        def blink():
            current_color = t8.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t8.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t8 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_8[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t8.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to8 = StringVar()
        l8 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to8, relief='raised',borderwidth=7, width=500)
        to8.set(Todo_M8)
        if (Todo_M8 == ''):
            to8.set(' WORKING TIME ')
        l8.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_9[:23]):
        def blink():
            current_color = t9.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t9.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t9 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_9[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t9.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to9 = StringVar()
        l9 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to9, relief='raised',borderwidth=7, width=500)
        to9.set(Todo_M9)
        if (Todo_M9 == ''):
            to9.set(' WORKING TIME ')
        l9.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_10[:23]):
        def blink():
            current_color = t10.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t10.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t10 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_10[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t10.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to10 = StringVar()
        l10 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to10, relief='raised',borderwidth=7, width=500)
        to10.set(Todo_M10)
        if (Todo_M10 == ''):
            to10.set(' WORKING TIME ')
        l10.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_11[:23]):
        def blink():
            current_color = t11.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t11.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t11 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_11[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t11.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to11 = StringVar()
        l11 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to11, relief='raised',borderwidth=7, width=500)
        to11.set(Todo_M11)
        if (Todo_M11 == ''):
            to11.set(' WORKING TIME ')
        l11.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")
    if (Todo_ring == Todo_Al_12[:23]):
        def blink():
            current_color = t12.cget("foreground")
            next_color = "red" if current_color == "yellow" else "yellow"
            t12.config(foreground=next_color)
            Todo_.after(1000, blink)
        thread_todo_play = Thread(target=play_todo)
        thread_todo_play.start()
        t12 = Label(Todo_, font=('impact', 30), text=" " + Todo_Al_12[27:] + " ", fg='red', bg='black', relief='raised',borderwidth=2)
        t12.pack()
        blink()
        ring_M = Label(Todo_, font=('impact', 30), text=' MESSAGE . . . . ', fg='silver', bg='black', relief='raised',borderwidth=2)
        ring_M.pack()
        to12 = StringVar()
        l12 = Message(Todo_, font=('Comic Sans MS', 20), fg='chartreuse', bg='black', textvariable=to12, relief='raised',borderwidth=7, width=500)
        to12.set(Todo_M12)
        if (Todo_M12 == ''):
            to12.set(' WORKING TIME ')
        l12.pack()
        oK = Button(Todo_, font=('', 20), fg='maroon', bg='lavenderblush', text='  GOT IT  ', relief='groove',borderwidth=5, command=over_todo)
        oK.pack()
        print("WAke UP")

    Todo_.protocol("WM_DELETE_WINDOW", on_closing_todo)

def Ring(t):
    global Alarm_1, Alarm_2, Alarm_3, Alarm_4, Alarm_5, Alarm_6, Alarm_7, Alarm_8, Alarm_9, Alarm_10
    global loop
    Time_o = t
    def close_alarm():
        if (pygame.mixer.get_init()):
            pygame.mixer.music.stop()
    date = {'M':'Mon','T':'Tue','W':'Wed','Th':'Thu','F':'Fri','S':'Sat','Su':'Sun'}
    if (Time_o == Alarm_1[:10]):
        if((Alarm_1[13:] == strftime('%a, %d %b')) or (Alarm_1[13:] == strftime('%a, %d %b %Y'))):
            loop = 1
        else:
            toy = Alarm_1[13:].split()
            for dd in toy:
                if (date[dd] == strftime('%a')):
                    flag = 0
                    break
                else :
                    flag = 1
            if (flag == 1):
                return
            loop = 2
    if (Time_o == Alarm_2[:10]):
        if((Alarm_2[13:] == strftime('%a, %d %b')) or (Alarm_2[13:] == strftime('%a, %d %b %Y'))):
            loop = 3
        else:
            toy1 = Alarm_2[13:].split()
            for dd1 in toy1:
                if (date[dd1] == strftime('%a')):
                    flag1 = 0
                    break
                else:
                    flag1 = 1
            if (flag1 == 1):
                return
            loop = 4
    if (Time_o == Alarm_3[:10]):
        if((Alarm_3[13:] == strftime('%a, %d %b')) or (Alarm_3[13:] == strftime('%a, %d %b %Y'))):
            loop = 5
        else:
            toy2 = Alarm_3[13:].split()
            for dd2 in toy2:
                if (date[dd2] == strftime('%a')):
                    flag2 = 0
                    break
                else:
                    flag2 = 1
            if (flag2 == 1):
                return
            loop = 6
    if (Time_o == Alarm_4[:10]):
        if((Alarm_4[13:] == strftime('%a, %d %b')) or (Alarm_4[13:] == strftime('%a, %d %b %Y'))):
            loop = 7
        else:
            toy3 = Alarm_4[13:].split()
            for dd3 in toy3:
                if (date[dd3] == strftime('%a')):
                    flag3 = 0
                    break
                else:
                    flag3 = 1
            if (flag3 == 1):
                return
            loop = 8
    if (Time_o == Alarm_5[:10]):
        if((Alarm_5[13:] == strftime('%a, %d %b')) or (Alarm_5[13:] == strftime('%a, %d %b %Y'))):
            loop = 9
        else:
            toy4 = Alarm_5[13:].split()
            for dd4 in toy4:
                if (date[dd4] == strftime('%a')):
                    flag4 = 0
                    break
                else:
                    flag4 = 1
            if (flag4 == 1):
                return
            loop = 10
    if (Time_o == Alarm_6[:10]):
        if((Alarm_6[13:] == strftime('%a, %d %b')) or (Alarm_6[13:] == strftime('%a, %d %b %Y'))):
            loop = 11
        else:
            toy5 = Alarm_6[13:].split()
            for dd5 in toy5:
                if (date[dd5] == strftime('%a')):
                    flag5 = 0
                    break
                else:
                    flag5 = 1
            if (flag5 == 1):
                return
            loop = 12
    if (Time_o == Alarm_7[:10]):
        if((Alarm_7[13:] == strftime('%a, %d %b')) or (Alarm_7[13:] == strftime('%a, %d %b %Y'))):
            loop = 13
        else:
            toy6 = Alarm_7[13:].split()
            for dd6 in toy6:
                if (date[dd6] == strftime('%a')):
                    flag6 = 0
                    break
                else:
                    flag6 = 1
            if (flag6 == 1):
                return
            loop = 14
    if (Time_o == Alarm_8[:10]):
        if((Alarm_8[13:] == strftime('%a, %d %b')) or (Alarm_8[13:] == strftime('%a, %d %b %Y'))):
            loop = 15
        else:
            toy7 = Alarm_8[13:].split()
            for dd7 in toy7:
                if (date[dd7] == strftime('%a')):
                    flag7 = 0
                    break
                else:
                    flag7 = 1
            if (flag7 == 1):
                return
            loop = 16
    if (Time_o == Alarm_9[:10]):
        if((Alarm_9[13:] == strftime('%a, %d %b')) or (Alarm_9[13:] == strftime('%a, %d %b %Y'))):
            loop = 17
        else:
            toy8 = Alarm_9[13:].split()
            for dd8 in toy8:
                if (date[dd8] == strftime('%a')):
                    flag8 = 0
                    break
                else:
                    flag8 = 1
            if (flag8 == 1):
                return
            loop = 18
    if (Time_o == Alarm_10[:10]):
        if((Alarm_10[13:] == strftime('%a, %d %b')) or (Alarm_10[13:] == strftime('%a, %d %b %Y'))):
            loop = 19
        else:
            toy9 = Alarm_10[13:].split()
            for dd9 in toy9:
                if (date[dd9] == strftime('%a')):
                    flag9 = 0
                    break
                else:
                    flag9 = 1
            if (flag9 == 1):
                return
            loop = 20
    T_a = Toplevel(root)
    T_a.title("ALARM TIME")
    T_a.configure(background = 'silver')
    def over():
        global loop
        pygame.mixer.music.stop()
        T_a.destroy()
        if (loop %2 != 0):
            Alarm_M()
    def play_():
        global Z_Play
        pygame.mixer.init()
        if (Z_Play==1):
            pygame.mixer.music.load(open(os.getcwd()+"\Loud_Alarm_Clock_Buzzer-Muk1984-493547174.wav", "rb"))
        if (Z_Play==2):
            pygame.mixer.music.load(open(os.getcwd()+"\Rooster Crow-SoundBible.com-1802551702.wav", "rb"))
        if (Z_Play==3):
            pygame.mixer.music.load(open(os.getcwd()+"\Pager Beeps-SoundBible.com-260751720.wav", "rb"))
        if (Z_Play==4):
            pygame.mixer.music.load(open(os.getcwd()+"\Analog-watch-alarm_daniel_simon.wav", "rb"))
        if (Z_Play==5):
            pygame.mixer.music.load(open(os.getcwd()+"\submarine-diving-alarm-daniel_simon.wav", "rb"))
        if (Z_Play==6):
            pygame.mixer.music.load(open(os.getcwd()+"\old-fashioned-door-bell-daniel_simon.wav", "rb"))
        if (Z_Play==7):
            pygame.mixer.music.load(open(os.getcwd()+"\Railroad_crossing_bell_Brylon_Terry-1551570865.wav", "rb"))
        if (Z_Play==8):
            pygame.mixer.music.load(open(os.getcwd()+"\Tornado Siren-SoundBible.com-897026957.wav", "rb"))
        if (Z_Play==9):
            pygame.mixer.music.load(open(os.getcwd()+"\Police Siren 3-SoundBible.com-553177907.wav", "rb"))
        if (Z_Play==10):
            pygame.mixer.music.load(open(os.getcwd()+"\church-chime-daniel_simon.wav", "rb"))
        if (Z_Play==11):
            with open('Alarm_tone.plk', 'rb') as s1:
                Z_play_check = dill.load(s1)
                Z_Play = dill.load(s1)
                file_path = dill.load(s1)
            pygame.mixer.music.load(open(file_path[0], "rb"))
        pygame.mixer.music.play(-1)
        while (pygame.mixer.music.get_busy() == True):
            sleep(23)
    with open('Alarm_time_mess.plk', 'rb')as z2:
        m_1 = dill.load(z2)
        m_2 = dill.load(z2)
        m_3 = dill.load(z2)
        m_4 = dill.load(z2)
        m_5 = dill.load(z2)
        m_6 = dill.load(z2)
        m_7 = dill.load(z2)
        m_8 = dill.load(z2)
        m_9 = dill.load(z2)
        m_10 = dill.load(z2)
    if ( Time_o == Alarm_1[:10] ):
        Time_o = 'a'
        play_thread = Thread(target= play_)
        play_thread.start()
        q1 = StringVar()
        l1 = Message(T_a,font = ('impact',40),fg='silver' , bg='black', textvariable = q1,relief='raised', borderwidth=7)
        q1.set(m_1)
        l1.pack()
        g1 = Button(T_a,font = ('',20),fg = 'yellow', bg = 'black',text = '  GOT IT  ',relief = 'raised', borderwidth=5,command = over)
        g1.pack()
    if ( Time_o == Alarm_2[:10] ):
        Time_o = 'b'
        play_thread = Thread(target=play_)
        play_thread.start()
        q2 = StringVar()
        l2 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable = q2, relief='raised', borderwidth=7)
        q2.set(m_2)
        l2.pack()
        g2 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g2.pack()
    if ( Time_o == Alarm_3[:10] ):
        Time_o = 'c'
        play_thread = Thread(target=play_)
        play_thread.start()
        q3 = StringVar()
        l3 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable=q3, relief='raised', borderwidth=7)
        q3.set(m_3)
        l3.pack()
        g3 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g3.pack()
    if ( Time_o == Alarm_4[:10] ):
        Time_o = 'd'
        play_thread = Thread(target=play_)
        play_thread.start()
        q4 = StringVar()
        l4 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable=q4, relief='raised', borderwidth=7)
        q4.set(m_4)
        l4.pack()
        g4 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g4.pack()
    if ( Time_o == Alarm_5[:10]):
        Time_o = 'e'
        play_thread = Thread(target=play_)
        play_thread.start()
        q5 = StringVar()
        l5 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable=q5, relief='raised', borderwidth=7)
        q5.set(m_5)
        l5.pack()
        g5 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g5.pack()
    if ( Time_o == Alarm_6[:10] ):
        Time_o = 'f'
        play_thread = Thread(target=play_)
        play_thread.start()
        q6 = StringVar()
        l6 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable=q6, relief='raised', borderwidth=7)
        q6.set(m_6)
        l6.pack()
        g6 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g6.pack()
    if ( Time_o == Alarm_7[:10]):
        Time_o = 'g'
        play_thread = Thread(target=play_)
        play_thread.start()
        q7 = StringVar()
        l7 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable=q7, relief='raised', borderwidth=7)
        q7.set(m_7)
        l7.pack()
        g7 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g7.pack()
    if ( Time_o == Alarm_8[:10] ):
        Time_o = 'h'
        play_thread = Thread(target=play_)
        play_thread.start()
        q8 = StringVar()
        l8 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable=q8, relief='raised', borderwidth=7)
        q8.set(m_8)
        l8.pack()
        g8 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g8.pack()
    if ( Time_o == Alarm_9[:10] ):
        Time_o = 'i'
        play_thread = Thread(target=play_)
        play_thread.start()
        q9 = StringVar()
        l9 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable=q9, relief='raised', borderwidth=7)
        q9.set(m_9)
        l9.pack()
        g9 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g9.pack()
    if ( Time_o == Alarm_10[:10] ):
        Time_o = 'j'
        play_thread = Thread(target=play_)
        play_thread.start()
        q10 = StringVar()
        l10 = Message(T_a, font=('impact', 40), fg='silver', bg='black', textvariable=q10, relief='raised', borderwidth=7)
        q10.set(m_10)
        l10.pack()
        g10 = Button(T_a, font=('', 20), fg='yellow', bg='black', text='  GOT IT  ', relief='raised', borderwidth=5,command=over)
        g10.pack()

    T_a.protocol("WM_DELETE_WINDOW", close_alarm)

def weather():
    wthr = Toplevel(root)
    wthr.title('WEATHER')
    wthr.configure(background = 'floralwhite')
    wthr.minsize(height=388, width=846)
    wthr.maxsize(height=758, width=1386)
    wtr = StringVar()
    wtr_1 = StringVar()
    wtr_2 = StringVar()
    def done():
        tempp ={'City':wtr.get().title(),'State':wtr_1.get().title(),'Country':wtr_2.get().title()}
        with open('Weather_ALARM.plk','wb')as ww:
            dill.dump(tempp,ww)
        wthr.destroy()
        with open('Weather_ALARM.plk', 'rb')as ww:
            try:
                weat = dill.load(ww)
                if ((weat['City'] == 'Siliguri')or(weat['City'] == 'Shiliguri')):
                    weat['City'] = 'Jalpaiguri'
                owm = pyowm.OWM('9aa222a1f36c220d515108dd905ba698')
                dest = weat['City'] + ", " + weat['State'] + ", " + weat['Country']
                observation = owm.weather_at_place(dest)
                w = observation.get_weather()
                weatherr = 'Temperature -> ' + str(w.get_temperature('celsius')['temp']) + ' ' + u'\u2103' + ', ' + w.get_detailed_status() + '\n' + 'Wind speed -> ' + str(w.get_wind()['speed']) + ' m/s' + "  " + 'Humidity -> ' + str(w.get_humidity()) + " %"
                pos = Label(root, font=('ms serif', 25), text=dest, fg="dodgerblue", bg='black')
                pos.pack()
                pos.place(x=186, y=489)
                pos_weather = Label(root, font=('ms serif', 25), text=weatherr, fg="lavenderblush", bg='black')
                pos_weather.pack()
                pos_weather.place(x=120, y=555)
                def weather_Update():
                    Timer(7200, weather_Update).start()
                    observation_7 = owm.weather_at_place(dest)
                    w_7 = observation_7.get_weather()
                    print('cc')
                    weatherr_7 = 'Temperature -> ' + str(w_7.get_temperature('celsius')['temp']) + ' ' + u'\u2103' + ', ' + w_7.get_detailed_status() + '\n' + 'Wind speed -> ' + str(w_7.get_wind()['speed']) + ' m/s' + "  " + 'Humidity -> ' + str(w_7.get_humidity()) + " %"
                    pos.config(text=dest)
                    pos_weather.config(text=weatherr_7)
                weather_Update()
            except:
                def weather_destroy():
                    Weather.destroy()
                Weather = Button(root, relief=RAISED, font=('ms serif', 25), fg='navy', bg='lime', borderwidth=10,text='SET WEATHER', command= lambda :[weather_destroy(),weather()])
                Weather.pack()
                Weather.place(x=300, y=500)
                pass

    wtr_ = Label(wthr, font=('impact', 30), text=' Enter the your current location ', fg='black', bg='lavenderblush', relief='raised',borderwidth=5)
    wtr_.pack()
    wtr_city = Label(wthr, font=('impact', 30), text=' CITY ', fg='maroon', bg='lavenderblush', relief='raised',borderwidth=2)
    wtr_city.pack()
    wtr_city.place( x = 60,y=80)
    wtr_city_entry = Entry(wthr, textvariable=wtr, font=('ms serif', 30), bg='yellow', fg='darkblue')
    wtr_city_entry.pack()
    wtr_city_entry.place(x=240, y=80)
    wtr_state = Label(wthr, font=('impact', 30), text=' STATE ', fg='maroon', bg='lavenderblush', relief='raised',borderwidth=2)
    wtr_state.pack()
    wtr_state.place(x=60, y=150)
    wtr_state_entry = Entry(wthr, textvariable=wtr_1, font=('ms serif', 30), bg='yellow', fg='darkblue')
    wtr_state_entry.pack()
    wtr_state_entry.place(x=240, y=155)
    wtr_country = Label(wthr, font=('impact', 30), text=' COUNTRY ', fg='maroon', bg='lavenderblush', relief='raised',borderwidth=2)
    wtr_country.pack()
    wtr_country.place(x=60, y=230)
    wtr_country_entry = Entry(wthr, textvariable=wtr_2, font=('ms serif', 30), bg='yellow', fg='darkblue')
    wtr_country_entry.pack()
    wtr_country_entry.place(x=240, y=235)

    done = Button(wthr,relief = RAISED, font = ('impact',25),fg = 'crimson' , bg = 'greenyellow',borderwidth = 7, text = '  DONE  ',command = done)
    done.pack()
    done.place( x = 340, y =295)

def Load_todo():
    global Todo_Al_1
    global Todo_M1
    global Todo_Al_2
    global Todo_M2
    global Todo_Al_3
    global Todo_M3
    global Todo_Al_4
    global Todo_M4
    global Todo_Al_5
    global Todo_M5
    global Todo_Al_6
    global Todo_M6
    global Todo_Al_7
    global Todo_M7
    global Todo_Al_8
    global Todo_M8
    global Todo_Al_9
    global Todo_M9
    global Todo_Al_10
    global Todo_M10
    global Todo_Al_11
    global Todo_M11
    global Todo_Al_12
    global Todo_M12
    with open('Alarm_todo_time.plk', 'rb') as tt:
        try:
            Todo_Al_1 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_2 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_3 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_4 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_5 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_6 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_7 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_8 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_9 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_10 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_11 = dill.load(tt)
        except:
            pass
        try:
            Todo_Al_12 = dill.load(tt)
        except:
            pass
    with open('Alarm_todo_mess.plk','rb') as tm:
        try:
            Todo_M1 = dill.load(tm)
        except:
            pass
        try:
            Todo_M2 = dill.load(tm)
        except:
            pass
        try:
            Todo_M3 = dill.load(tm)
        except:
            pass
        try:
            Todo_M4 = dill.load(tm)
        except:
            pass
        try:
            Todo_M5 = dill.load(tm)
        except:
            pass
        try:
            Todo_M6 = dill.load(tm)
        except:
            pass
        try:
            Todo_M7 = dill.load(tm)
        except:
            pass
        try:
            Todo_M8 = dill.load(tm)
        except:
            pass
        try:
            Todo_M9 = dill.load(tm)
        except:
            pass
        try:
            Todo_M10 = dill.load(tm)
        except:
            pass
        try:
            Todo_M11 = dill.load(tm)
        except:
            pass
        try:
            Todo_M12 = dill.load(tm)
        except:
            pass

def Load_tones():
    global Z_play_check
    global Z_Play
    try:
        with open('Alarm_tone.plk','rb') as s1:
            Z_play_check = dill.load(s1)
            Z_Play = dill.load(s1)
            print(Z_play_check, Z_Play)
    except:
        pass

def Load_tone_todo():
    global Z_Play_todo
    global Z_play_todo_check
    try:
        with open('Alarm_todo_tone.plk','rb') as it:
            Z_play_todo_check = dill.load(it)
            Z_Play_todo = dill.load(it)
    except:
        pass

def Set_todo():
    todo = Toplevel(root)
    todo.title('TO DO LIST')
    todo.minsize(height=688, width=1346)
    todo.maxsize(height=758, width=1386)
    todo.configure(background='lavenderblush')
    todo.attributes('-alpha', 0.8)

    def close_todo():
        global count_b
        global count_c
        if (pygame.mixer.get_init()):
            pygame.mixer.music.stop()
        if (count_b >= 46):
            count_b = count_b - 46
            count_c = count_c - 1
        with open('Alarm_todo_count.plk', 'wb') as cc:
            dill.dump(count_b, cc)
            dill.dump(count_c, cc)
        todo.destroy()
    title_TO_DO = Label(todo,font = ('impact',30),text= ' TO-DO LIST ',fg = 'black' , bg = 'lavenderblush',relief = 'raised',borderwidth = 5 )
    title_TO_DO.pack()
    title_TO_DO.place(x = 565,y = 20)

    Leb_Year = Label(todo, font=('impact', 20), text=' YEAR ', fg='black', bg='snow', relief='raised', borderwidth=2)
    Leb_Year.pack()
    Leb_Year.place(x=50, y=100)

    Leb_Month = Label(todo, font=('impact', 20), text=' MONTH ', fg='black', bg='snow', relief='raised', borderwidth=2)
    Leb_Month.pack()
    Leb_Month.place(x=175, y=100)

    Leb_Day = Label(todo, font=('impact', 20), text=' DAY ', fg='black', bg='snow', relief='raised', borderwidth=2)
    Leb_Day.pack()
    Leb_Day.place(x=300, y=100)

    leb_h = Label(todo, font=('impact', 20), text=' HOUR ', fg='black', bg='snow', relief='raised', borderwidth=2)
    leb_h.pack()
    leb_h.place(x=500, y=100)

    leb_m = Label(todo, font=('impact', 20), text=' MINUTES ', fg='black', bg='snow', relief='raised', borderwidth=2)
    leb_m.pack()
    leb_m.place(x=600, y=100)

    leb_Pri = Label(todo, font=('impact', 20), text=' PRIORITY ', fg='black', bg='snow', relief='raised', borderwidth=2)
    leb_Pri.pack()
    leb_Pri.place(x=800, y=100)

    Leb_message = Label(todo, font=('impact', 20), text=' NOTE / MESSAGE ', bg='snow', fg='black')
    Leb_message.pack()
    Leb_message.place(x=1000, y=100)

    def Add_Task():
        global Todo_Al_1, Todo_M1, Todo_Al_2, Todo_M2, Todo_Al_3, Todo_M3, Todo_Al_4, Todo_M4, Todo_Al_5, Todo_M5
        global Todo_Al_6, Todo_M6, Todo_Al_7, Todo_M7, Todo_Al_8, Todo_M8, Todo_Al_9, Todo_M9, Todo_Al_10, Todo_M10, Todo_Al_11, Todo_M11, Todo_Al_12, Todo_M12
        global count_b
        global count_c
        def Prepared_Todo():
            global Todo_Al_1, Todo_M1, Todo_Al_2, Todo_M2, Todo_Al_3, Todo_M3, Todo_Al_4, Todo_M4, Todo_Al_5, Todo_M5
            global Todo_Al_6, Todo_M6, Todo_Al_7, Todo_M7, Todo_Al_8, Todo_M8, Todo_Al_9, Todo_M9, Todo_Al_10, Todo_M10, Todo_Al_11, Todo_M11, Todo_Al_12, Todo_M12
            d = 50
            m = 20
            pre_todo = Toplevel(root)
            pre_todo.title('PREPARED TO DO LIST')
            pre_todo.minsize(height=688, width=1346)
            pre_todo.maxsize(height=758, width=1386)
            pre_todo.configure(background='lightgoldenrodyellow')
            #pre_todo.attributes('-alpha', 0.8)
            def dest_pre():
                pre_todo.destroy()

            title_TO_DO = Label(pre_todo, font=('impact', 30), text=' TO-DO LIST ', fg='chartreuse', bg='black',relief='raised', borderwidth=5)
            title_TO_DO.pack()
            title_TO_DO.place(x=565, y=20-10)

            Leb_date = Label(pre_todo, font=('impact', 20), text=' DATE (YYYY/MM/DD)', fg='black', bg='yellow', relief='raised',borderwidth=2)
            Leb_date.pack()
            Leb_date.place(x=20, y=90-m-5)

            Leb_time = Label(pre_todo, font=('impact', 20), text='  TIME  ', fg='black', bg='yellow',relief='raised', borderwidth=2)
            Leb_time.pack()
            Leb_time.place(x=430, y=90-m-5)

            Leb_prio = Label(pre_todo, font=('impact', 20), text=' PRIORITY ', fg='black', bg='yellow', relief='raised',borderwidth=2)
            Leb_prio.pack()
            Leb_prio.place(x=790, y=90-m-5)

            Leb_show = Label(pre_todo, font=('impact', 20), text=' MESSAGE ', fg='black', bg='yellow', relief='raised',borderwidth=2)
            Leb_show.pack()
            Leb_show.place(x=1000, y=90-m-5)

            Pre_add_task = Button(pre_todo, relief=GROOVE, font=(7), fg='black', bg='silver', borderwidth=8,text=' ADD TASK ', command=lambda: [dest_pre(),Set_todo()])
            Pre_add_task.pack()
            Pre_add_task.place(x=998, y=20-5)

            if (Todo_Al_1 != ''):
                Todo_1 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_1[:17]+" "+Todo_Al_1[20:], fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_1.pack()
                Todo_1.place(x = 20,y =130-m)

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M1[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M1)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x = 1000, y=130-m)

            if (Todo_Al_2 != ''):
                Todo_2 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_2[:17]+" "+Todo_Al_2[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_2.pack()
                Todo_2.place(x = 20,y =130-m + d)

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M2[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M2)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x = 1000, y=130-m + d)

            if (Todo_Al_3 != ''):
                Todo_33 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_3[:17]+" "+Todo_Al_3[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_33.pack()
                Todo_33.place(x = 20,y =130 - m + (d*2))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M3[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M3)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x = 1000, y=130 - m + (d*2))

            if (Todo_Al_4 != ''):
                Todo_44 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_4[:17]+" "+Todo_Al_4[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_44.pack()
                Todo_44.place(x = 20,y =130 - m + (d*3))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M4[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M4)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x = 1000, y=130 - m + (d*3))

            if (Todo_Al_5 != ''):
                Todo_55 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_5[:17]+" "+Todo_Al_5[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_55.pack()
                Todo_55.place(x = 20,y =130 - m + (d*4))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M5[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M5)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x = 1000, y=130 - m + (d*4))

            if (Todo_Al_6 != ''):
                Todo_66 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_6[:17]+" "+Todo_Al_6[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_66.pack()
                Todo_66.place(x = 20,y =130 - m + (d*5))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M6[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M6)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x = 1000, y=130 - m + (d*5))

            if (Todo_Al_7 != ''):
                Todo_77 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_7[:17]+" "+Todo_Al_7[20:] + " ", fg='mediumblue',bg='floralwhite', relief='raised', borderwidth=2)
                Todo_77.pack()
                Todo_77.place(x=20, y=130 - m + (d * 6))

                Mess_pre_todo = Menubutton(pre_todo, text=Todo_M7[0:10] + " .... ", relief='raised',font=('Comic Sans MS', 16), fg='mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M7)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x=1000, y=130 -m + (d * 6))

            if (Todo_Al_8 != ''):
                Todo_88 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_8[:17]+" "+Todo_Al_8[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_88.pack()
                Todo_88.place(x = 20,y =130 - m + (d*7))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M8[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M8)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x=1000, y=130 - m + (d * 7))

            if (Todo_Al_9 != ''):
                Todo_99 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_9[:17]+" "+Todo_Al_9[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_99.pack()
                Todo_99.place(x = 20,y =130 - m + (d*8))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M9[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M9)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x=1000, y=130 - m + (d * 8))

            if (Todo_Al_10 != ''):
                Todo_10 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_10[:17]+" "+Todo_Al_10[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_10.pack()
                Todo_10.place(x = 20,y =130 - m + (d*9))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M10[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M10)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x=1000, y=130 - m + (d * 9))

            if (Todo_Al_11 != ''):
                Todo_111 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_11[:17]+" "+Todo_Al_11[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_111.pack()
                Todo_111.place(x = 20,y =130 - m + (d*10))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M11[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M11)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x=1000, y=130 - m + (d * 10))

            if (Todo_Al_12 != ''):
                Todo_112 = Label(pre_todo, font=('Comic Sans MS', 20), text = " "+Todo_Al_12[:17]+" "+Todo_Al_12[20:]+" ", fg='mediumblue', bg='floralwhite',relief='raised', borderwidth=2)
                Todo_112.pack()
                Todo_112.place(x = 20,y =130 - m + (d*11))

                Mess_pre_todo = Menubutton(pre_todo, text= Todo_M12[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg = 'mediumblue')
                Mess_pre_todo.grid()
                mayoVar = IntVar()
                Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
                Mess_pre_todo["menu"] = Mess_pre_todo.menu
                Mess_pre_todo.menu.add_command(label=Todo_M12)
                Mess_pre_todo.pack()
                Mess_pre_todo.place(x=1000, y=130 - m + (d * 11))

        m_todo = StringVar()
        var_month = StringVar(todo)
        var_day = StringVar(todo)
        button_add_task.destroy()
        var_month.set(strftime('%m'))
        var_day.set(strftime('%d'))
        try:
            with open('Alarm_todo_count.plk', 'rb') as c5:
                count_b = dill.load(c5)
                count_c = dill.load(c5)
        except:
            pass
        if (count_b != 552):
            def update_day():
                year = int(Todo_year.get().zfill(2))
                month = int(Todo_month.get().zfill(2))
                maxday = calendar.monthrange(year, month)[1]
                Todo_day.config(to=maxday)

            Todo_year = Spinbox(todo, font=('impact', 20), fg='darkblue', bg='aliceblue', from_=int(strftime('%Y')),to=12 + int(strftime('%Y')), width=5, justify=CENTER, relief=GROOVE)
            Todo_year.pack()
            Todo_year.place(x=50, y=152 + count_b)

            todo_M = Spinbox(todo)
            Todo_month = Spinbox(todo, font=('impact', 20), fg='darkblue', bg='aliceblue', from_=1, to=12, width=3,textvariable=var_month, justify=CENTER, relief=GROOVE, command=update_day)
            Todo_month.pack()
            Todo_month.place(x=175, y=152 + count_b)

            todo_D = Spinbox(todo)
            Todo_day = Spinbox(todo, font=('impact', 20), fg='darkblue', bg='aliceblue', from_=1, to=31, width=3,textvariable=var_day, justify=CENTER, relief=GROOVE)
            Todo_day.pack()
            Todo_day.place(x=300, y=152 + count_b)

            Todo_H = Spinbox(todo)
            Todo_HRS = Spinbox(todo, font=('impact', 20), fg='darkblue', bg='aliceblue', from_=1, to=12, width=3,justify=CENTER, relief=GROOVE)
            Todo_HRS.pack()
            Todo_HRS.place(x=505, y=152 + count_b)

            Todo_M = Spinbox(todo)
            Todo_MIN = Spinbox(todo, font=('impact', 20), fg='darkblue', bg='aliceblue', from_=0, to=59, width=3,justify=CENTER, relief=GROOVE)
            Todo_MIN.pack()
            Todo_MIN.place(x=620, y=152 + count_b)

            AM_PM = Spinbox(todo, font=('impact', 20), fg='darkblue', bg='aliceblue', values=(' AM ', ' PM '), width=3,justify=CENTER, relief=GROOVE)
            AM_PM.pack()
            AM_PM.place(x=720, y=152 + count_b)

            Todo_P = Spinbox(todo)
            Todo_Pri = Spinbox(todo, font=('impact', 20), fg='darkblue', bg='aliceblue',values=('LOW', 'MEDIUM', 'HIGH'), width=7, justify=CENTER, relief=GROOVE)
            Todo_Pri.pack()
            Todo_Pri.place(x=800, y=152 + count_b)

            Todo_mess = Entry(todo, textvariable=m_todo, font=('Comic Sans MS', 20), bg='antiquewhite', fg='darkblue')
            Todo_mess.pack()
            Todo_mess.place(x=1000, y=152 + count_b)

            def sett():
                global x
                global Z_play_todo_check
                x = 1
                if(pygame.mixer.get_init()):
                    pygame.mixer.music.stop()

            def store_todo():
                global x
                global Todo_Al_1, Todo_M1, Todo_Al_2, Todo_M2, Todo_Al_3, Todo_M3, Todo_Al_4, Todo_M4, Todo_Al_5, Todo_M5
                global Todo_Al_6, Todo_M6, Todo_Al_7, Todo_M7, Todo_Al_8, Todo_M8, Todo_Al_9, Todo_M9, Todo_Al_10, Todo_M10, Todo_Al_11, Todo_M11, Todo_Al_12, Todo_M12
                global count_b
                global count_c
                global To_do_m

                T_Y = Todo_year.get()
                T_M = Todo_month.get().zfill(2)
                T_D = Todo_day.get().zfill(2)
                T_hrs = Todo_HRS.get().zfill(2)
                T_min = Todo_MIN.get().zfill(2)
                T_AP = AM_PM.get()
                T_pri = Todo_Pri.get()
                T_ME = m_todo.get()
                try:
                    with open('Alarm_todo_count.plk', 'rb')as ck:
                        count_b = dill.load(ck)
                        count_c = dill.load(ck)
                except:
                    pass
                if (count_c == 1):
                    Todo_Al_1 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+ T_AP + " \t\t" + T_pri
                    Todo_M1 = T_ME
                    b01 = "Date -> "+T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 1",b01+ "\n"+Todo_M1):
                        Todo_Al_1 = ''
                        Todo_M1 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state = "disabled")
                        Todo_month.configure(state = "disabled")
                        Todo_day.configure(state = "disabled")
                        Todo_HRS.configure(state = "disabled")
                        Todo_MIN.configure(state = "disabled")
                        AM_PM.configure(state = "disabled")
                        Todo_Pri.configure(state = "disabled")
                        Todo_mess.configure(state = "disabled")
                    print('3')
                    if x==1:
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_1)
                        print(Todo_M1)
                        x = 0
                    print(Todo_Al_1)
                    print(Todo_M1)
                if (count_c == 2):
                    Todo_Al_2 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min + ":00"+ T_AP + " \t\t" + T_pri
                    Todo_M2 = T_ME
                    b02 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 2", b02 + "\n" + Todo_M2):
                        Todo_Al_2 = ''
                        Todo_M2 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_2)
                        print(Todo_M2)
                        x = 0
                    print(Todo_Al_2)
                    print(Todo_M2)
                if (count_c == 3):
                    Todo_Al_3 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+ T_AP + " \t\t" + T_pri
                    Todo_M3 = T_ME
                    b03 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 3", b03 + "\n" + Todo_M3):
                        Todo_Al_3 = ''
                        Todo_M3 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_3)
                        print(Todo_M3)
                        x = 0
                    print(Todo_Al_3)
                    print(Todo_M3)
                if (count_c == 4):
                    Todo_Al_4 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+ T_AP + " \t\t" + T_pri
                    Todo_M4 = T_ME
                    b04 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 4", b04 + "\n" + Todo_M4):
                        Todo_Al_4 = ''
                        Todo_M4 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_4)
                        print(Todo_M4)
                        x = 0
                    print(Todo_Al_4)
                    print(Todo_M4)
                if (count_c == 5):
                    Todo_Al_5 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+ T_AP + " \t\t" + T_pri
                    Todo_M5 = T_ME
                    b05 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 5", b05 + "\n" + Todo_M5):
                        Todo_Al_5 = ''
                        Todo_M5 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_5)
                        print(Todo_M5)
                        x = 0
                    print(Todo_Al_5)
                    print(Todo_M5)
                if (count_c == 6):
                    Todo_Al_6 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+ T_AP + " \t\t" + T_pri
                    Todo_M6 = T_ME
                    b06 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 6", b06 + "\n" + Todo_M6):
                        Todo_Al_6 = ''
                        Todo_M6 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_6)
                        print(Todo_M6)
                        x = 0
                    print(Todo_Al_6)
                    print(Todo_M6)
                if (count_c == 7):
                    Todo_Al_7 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+ T_AP + " \t\t" + T_pri
                    Todo_M7 = T_ME
                    b07 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 7", b07 + "\n" + Todo_M7):
                        Todo_Al_7 = ''
                        Todo_M7 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_7)
                        print(Todo_M7)
                        x = 0
                    print(Todo_Al_7)
                    print(Todo_M7)
                if (count_c == 8):
                    Todo_Al_8 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+ T_AP + " \t\t" + T_pri
                    Todo_M8 = T_ME
                    b08 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 8", b08 + "\n" + Todo_M8):
                        Todo_Al_8 = ''
                        Todo_M8 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_8)
                        print(Todo_M8)
                        x = 0
                    print(Todo_Al_8)
                    print(Todo_M8)
                if (count_c == 9):
                    Todo_Al_9 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min + ":00"+ T_AP + " \t\t" + T_pri
                    Todo_M9 = T_ME
                    b09 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 9", b09 + "\n" + Todo_M9):
                        Todo_Al_9 = ''
                        Todo_M9 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_9)
                        print(Todo_M9)
                        x = 0
                    print(Todo_Al_9)
                    print(Todo_M9)
                if (count_c == 10):
                    Todo_Al_10 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min + ":00"+ T_AP + " \t\t" + T_pri
                    Todo_M10 = T_ME
                    b10 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 10", b10 + "\n" + Todo_M10):
                        Todo_Al_10 = ''
                        Todo_M10 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_10)
                        print(Todo_M10)
                        x = 0
                    print(Todo_Al_10)
                    print(Todo_M10)
                if (count_c == 11):
                    Todo_Al_11 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+ T_AP + " \t\t" + T_pri
                    Todo_M11 = T_ME
                    b11 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 11", b11 + "\n" + Todo_M11):
                        Todo_Al_11 = ''
                        Todo_M11 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_11)
                        print(Todo_M11)
                        x = 0
                    print(Todo_Al_11)
                    print(Todo_M11)
                if (count_c == 12):
                    Todo_Al_12 = T_Y + "/" + T_M + "/" + T_D + "\t\t" + T_hrs + ":" + T_min +":00"+T_AP + " \t\t" + T_pri
                    Todo_M12 = T_ME
                    b12 = "Date -> " + T_Y + "/" + T_M + "/" + T_D + " Time -> " + T_hrs + ":" + T_min + T_AP + " Priority -> " + T_pri
                    if not messagebox.askokcancel("Checkpoint - 12", b12 + "\n" + Todo_M12):
                        Todo_Al_12 = ''
                        Todo_M12 = ''
                        count_c = count_c - 1
                        count_b = count_b - 46
                        with open('Alarm_todo_count.plk', 'wb') as cc:
                            dill.dump(count_b, cc)
                            dill.dump(count_c, cc)
                        Todo_year.destroy()
                        Todo_month.destroy()
                        Todo_day.destroy()
                        Todo_HRS.destroy()
                        Todo_MIN.destroy()
                        AM_PM.destroy()
                        Todo_Pri.destroy()
                        Todo_mess.destroy()
                        print(count_c, count_b)
                        return
                    else:
                        Todo_year.configure(state="disabled")
                        Todo_month.configure(state="disabled")
                        Todo_day.configure(state="disabled")
                        Todo_HRS.configure(state="disabled")
                        Todo_MIN.configure(state="disabled")
                        AM_PM.configure(state="disabled")
                        Todo_Pri.configure(state="disabled")
                        Todo_mess.configure(state="disabled")
                    if (x==1):
                        todo.destroy()
                        if (To_do_m != 1):
                            try:
                                To_do.destroy()
                            except:
                                pass
                        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8,command = Prepared_Todo)
                        To_do_set.pack()
                        To_do_set.place(x= 100, y=65)
                        print(Todo_Al_12)
                        print(Todo_M12)
                        x = 0
                    print(Todo_Al_12)
                    print(Todo_M12)
                with open('Alarm_todo_time.plk', 'wb')as t:
                    dill.dump(Todo_Al_1, t)
                    dill.dump(Todo_Al_2, t)
                    dill.dump(Todo_Al_3, t)
                    dill.dump(Todo_Al_4, t)
                    dill.dump(Todo_Al_5, t)
                    dill.dump(Todo_Al_6, t)
                    dill.dump(Todo_Al_7, t)
                    dill.dump(Todo_Al_8, t)
                    dill.dump(Todo_Al_9, t)
                    dill.dump(Todo_Al_10, t)
                    dill.dump(Todo_Al_11, t)
                    dill.dump(Todo_Al_12, t)
                with open('Alarm_todo_mess.plk','wb')as t1:
                    dill.dump(Todo_M1, t1)
                    dill.dump(Todo_M2, t1)
                    dill.dump(Todo_M3, t1)
                    dill.dump(Todo_M4, t1)
                    dill.dump(Todo_M5, t1)
                    dill.dump(Todo_M6, t1)
                    dill.dump(Todo_M7, t1)
                    dill.dump(Todo_M8, t1)
                    dill.dump(Todo_M9, t1)
                    dill.dump(Todo_M10, t1)
                    dill.dump(Todo_M11, t1)
                    dill.dump(Todo_M12, t1)

            button_add_task_1 = Button(todo, relief=GROOVE, font=(7), fg='orange', bg='maroon', borderwidth=8,text=' ADD TASK ', command=lambda: [store_todo(), Add_Task()])
            button_add_task_1.pack()
            button_add_task_1.place(x=366, y=27)

            button_set = Button(todo, relief=GROOVE, font=("impact 16 italic"), fg='lightgreen', bg='darkgreen',borderwidth=8, text='  SET  ', command=lambda: [sett(),store_todo()])
            button_set.pack()
            button_set.place(x=998, y=20)

            count_b = count_b + 46
            count_c = count_c + 1
            with open('Alarm_todo_count.plk','wb') as cc:
                dill.dump(count_b, cc)
                dill.dump(count_c, cc)

    Tone_todo = Label(todo, font=('impact', 15), text=' SELECT ALARM TONE ', bg='black', fg='whitesmoke')
    Tone_todo.pack()
    Tone_todo.place(x=68, y=15)
    def change11():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 1
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Loud_Alarm_Clock_Buzzer-Muk1984-493547174.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- LOUD BUZZER --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change22():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 2
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Rooster Crow-SoundBible.com-1802551702.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- ROOSTER CROW --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change33():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 3
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Pager Beeps-SoundBible.com-260751720.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- PAGER BEEPS --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change44():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 4
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Analog-watch-alarm_daniel_simon.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- DIGITAL BEEPS --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change55():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 5
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\submarine-diving-alarm-daniel_simon.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- SUBMARINE DIVING --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change66():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 6
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\old-fashioned-door-bell-daniel_simon.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- DOOR BELL --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change77():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 7
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Railroad_crossing_bell_Brylon_Terry-1551570865.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- RAIL ROAD CROSSING --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change88():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 8
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Tornado Siren-SoundBible.com-897026957.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- TORNADO SIREN --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change99():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 9
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Police Siren 3-SoundBible.com-553177907.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- POLICE SIREN --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change200():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 10
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\church-chime-daniel_simon.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure( text = " --- CHURCH BELL --- ")
        with open('Alarm_todo_tone.plk','wb') as so:
            dill.dump(Z_play_todo_check,so)
            dill.dump(Z_Play_todo,so)
    def change211():
        global Z_Play_todo
        global Z_play_todo_check
        Z_play_todo_check = 1
        Z_Play_todo = 11
        file_path_todo = filedialog.askopenfilenames(filetypes=(("WAV files", "*.wav"), ("MP3 files", "*.mp3")))
        head1, tail1 = os.path.split(file_path_todo[0])
        pygame.mixer.init()
        pygame.mixer.music.load(open(file_path_todo[0], "rb"))
        pygame.mixer.music.play(1)
        set_Tone_todo.configure(text=" --- " + tail1[:10] + " --- ")
        with open('Alarm_todo_tone.plk', 'wb') as so:
            dill.dump(Z_play_todo_check, so)
            dill.dump(Z_Play_todo, so)
            dill.dump(file_path_todo, so)

    set_Tone_todo = Menubutton(todo, text=' ---LOUD BUZZER--- ', relief='raised', font=('MS Sans Serif', 16), bg='black', fg='whitesmoke')
    set_Tone_todo.grid()
    mayoVar = IntVar()
    set_Tone_todo.menu = Menu(set_Tone_todo, tearoff=0)
    set_Tone_todo["menu"] = set_Tone_todo.menu
    global Z_Play_todo
    global Z_play_todo_check
    Load_tone_todo()
    if( Z_play_todo_check == 1):
        if (Z_Play_todo == 1):
            set_Tone_todo.configure( text = " --- LOUD BUZZER --- ")
        if (Z_Play_todo == 2):
            set_Tone_todo.configure( text = " --- ROOSTER CROW --- ")
        if (Z_Play_todo == 3):
            set_Tone_todo.configure( text = " --- PAGER BEEPS --- ")
        if (Z_Play_todo == 4):
            set_Tone_todo.configure( text = " --- DIGITAL BEEPS --- ")
        if (Z_Play_todo == 5):
            set_Tone_todo.configure( text = " --- SUBMARINE DIVING --- ")
        if (Z_Play_todo == 6):
            set_Tone_todo.configure( text = " --- DOOR BELL --- ")
        if (Z_Play_todo == 7):
            set_Tone_todo.configure( text = " --- RAIL ROAD CROSSING --- ")
        if (Z_Play_todo == 8):
            set_Tone_todo.configure( text = " --- TORNADO SIREN --- ")
        if (Z_Play_todo == 9):
            set_Tone_todo.configure( text = " --- POLICE SIREN --- ")
        if (Z_Play_todo == 10):
            set_Tone_todo.configure( text = " --- CHURCH BELL --- ")
        if (Z_Play_todo == 11):
            with open('Alarm_todo_tone.plk', 'rb') as s1:
                Z_play_todo_check = dill.load(s1)
                Z_Play_todo = dill.load(s1)
                file_path_todo = dill.load(s1)
            head1, tail1 = os.path.split(file_path_todo[0])
            set_Tone_todo.configure(text=" --- " + tail1[:10] + " --- ")

    set_Tone_todo.menu.add_command(label=' Loud buzzer ',command =change11)
    set_Tone_todo.menu.add_command(label=' Rooster Crow ',command =change22)
    set_Tone_todo.menu.add_command(label=' Pager Beeps ',command =change33)
    set_Tone_todo.menu.add_command(label=' Digital Beeps ',command =change44)
    set_Tone_todo.menu.add_command(label=' Submarine Diving ',command =change55)
    set_Tone_todo.menu.add_command(label=' Door Bell ',command =change66)
    set_Tone_todo.menu.add_command(label=' Rail road Crossing ',command =change77)
    set_Tone_todo.menu.add_command(label=' Tornado Siren ',command =change88)
    set_Tone_todo.menu.add_command(label=' Police Siren ',command =change99)
    set_Tone_todo.menu.add_command(label=' Church  Bell ',command =change200)
    set_Tone_todo.menu.add_command(label='Select your song.', command=change211)
    set_Tone_todo.pack()
    set_Tone_todo.place(x=50, y=50)

    button_add_task = Button(todo,relief = GROOVE, font = (7),fg = 'orange' , bg = 'maroon',borderwidth = 8, text = ' ADD TASK ',command =Add_Task)
    button_add_task.pack()
    button_add_task.place( x= 366,y = 27)
    todo.protocol("WM_DELETE_WINDOW",close_todo)

def Prepared_Todo_2():
    global Todo_Al_1, Todo_M1,Todo_Al_2, Todo_M2, Todo_Al_3, Todo_M3, Todo_Al_4, Todo_M4, Todo_Al_5, Todo_M5
    global Todo_Al_6, Todo_M6, Todo_Al_7, Todo_M7, Todo_Al_8, Todo_M8, Todo_Al_9, Todo_M9, Todo_Al_10, Todo_M10, Todo_Al_11, Todo_M11, Todo_Al_12, Todo_M12
    d = 50
    m = 20
    pre_todo = Toplevel(root)
    pre_todo.title('PREPARED TO DO LIST')
    pre_todo.minsize(height=688, width=1346)
    pre_todo.maxsize(height=758, width=1386)
    pre_todo.configure(background='lightgoldenrodyellow')

    # pre_todo.attributes('-alpha', 0.8)
    def dest_pre():
        pre_todo.destroy()

    title_TO_DO = Label(pre_todo, font=('impact', 30), text=' TO-DO LIST ', fg='chartreuse', bg='black',relief='raised', borderwidth=5)
    title_TO_DO.pack()
    title_TO_DO.place(x=565, y=20 - 10)

    Leb_date = Label(pre_todo, font=('impact', 20), text=' DATE (YYYY/MM/DD)', fg='black', bg='yellow', relief='raised',borderwidth=2)
    Leb_date.pack()
    Leb_date.place(x=20, y=90 - m - 5)

    Leb_time = Label(pre_todo, font=('impact', 20), text='  TIME  ', fg='black', bg='yellow', relief='raised',borderwidth=2)
    Leb_time.pack()
    Leb_time.place(x=430, y=90 - m - 5)

    Leb_prio = Label(pre_todo, font=('impact', 20), text=' PRIORITY ', fg='black', bg='yellow', relief='raised',borderwidth=2)
    Leb_prio.pack()
    Leb_prio.place(x=790, y=90 - m - 5)

    Leb_show = Label(pre_todo, font=('impact', 20), text=' MESSAGE ', fg='black', bg='yellow', relief='raised',borderwidth=2)
    Leb_show.pack()
    Leb_show.place(x=1000, y=90 - m - 5)

    Pre_add_task = Button(pre_todo, relief=GROOVE, font=(7), fg='black', bg='silver', borderwidth=8, text=' ADD TASK ',command=lambda: [dest_pre(), Set_todo()])
    Pre_add_task.pack()
    Pre_add_task.place(x=998, y=20 - 5)

    Load_todo()

    if (Todo_Al_1 != ''):
        Todo_1 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_1[:17] + " " + Todo_Al_1[20:],fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_1.pack()
        Todo_1.place(x=20, y=130 - m)

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M1[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M1)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m)

    if (Todo_Al_2 != ''):
        Todo_2 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_2[:17] + " " + Todo_Al_2[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_2.pack()
        Todo_2.place(x=20, y=130 - m + d)

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M2[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M2)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + d)

    if (Todo_Al_3 != ''):
        Todo_33 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_3[:17] + " " + Todo_Al_3[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_33.pack()
        Todo_33.place(x=20, y=130 - m + (d * 2))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M3[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M3)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 2))

    if (Todo_Al_4 != ''):
        Todo_44 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_4[:17] + " " + Todo_Al_4[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_44.pack()
        Todo_44.place(x=20, y=130 - m + (d * 3))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M4[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M4)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 3))

    if (Todo_Al_5 != ''):
        Todo_55 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_5[:17] + " " + Todo_Al_5[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_55.pack()
        Todo_55.place(x=20, y=130 - m + (d * 4))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M5[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M5)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 4))

    if (Todo_Al_6 != ''):
        Todo_66 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_6[:17] + " " + Todo_Al_6[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_66.pack()
        Todo_66.place(x=20, y=130 - m + (d * 5))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M6[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M6)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 5))

    if (Todo_Al_7 != ''):
        Todo_77 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_7[:17] + " " + Todo_Al_7[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_77.pack()
        Todo_77.place(x=20, y=130 - m + (d * 6))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M7[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M7)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 6))

    if (Todo_Al_8 != ''):
        Todo_88 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_8[:17] + " " + Todo_Al_8[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_88.pack()
        Todo_88.place(x=20, y=130 - m + (d * 7))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M8[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M8)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 7))

    if (Todo_Al_9 != ''):
        Todo_99 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_9[:17] + " " + Todo_Al_9[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_99.pack()
        Todo_99.place(x=20, y=130 - m + (d * 8))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M9[0:10] + " .... ", relief='raised', font=('Comic Sans MS', 16),fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M9)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 8))

    if (Todo_Al_10 != ''):
        Todo_10 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_10[:17] + " " + Todo_Al_10[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_10.pack()
        Todo_10.place(x=20, y=130 - m + (d * 9))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M10[0:10] + " .... ", relief='raised',font=('Comic Sans MS', 16), fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M10)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 9))

    if (Todo_Al_11 != ''):
        Todo_111 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_11[:17] + " " + Todo_Al_11[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_111.pack()
        Todo_111.place(x=20, y=130 - m + (d * 10))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M11[0:10] + " .... ", relief='raised',font=('Comic Sans MS', 16), fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M11)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 10))

    if (Todo_Al_12 != ''):
        Todo_112 = Label(pre_todo, font=('Comic Sans MS', 20), text=" " + Todo_Al_12[:17] + " " + Todo_Al_12[20:] + " ",fg='mediumblue', bg='floralwhite', relief='raised', borderwidth=2)
        Todo_112.pack()
        Todo_112.place(x=20, y=130 - m + (d * 11))

        Mess_pre_todo = Menubutton(pre_todo, text=Todo_M12[0:10] + " .... ", relief='raised',font=('Comic Sans MS', 16), fg='mediumblue')
        Mess_pre_todo.grid()
        mayoVar = IntVar()
        Mess_pre_todo.menu = Menu(Mess_pre_todo, tearoff=0)
        Mess_pre_todo["menu"] = Mess_pre_todo.menu
        Mess_pre_todo.menu.add_command(label=Todo_M12)
        Mess_pre_todo.pack()
        Mess_pre_todo.place(x=1000, y=130 - m + (d * 11))

def Enter_Time():
    select = Toplevel(root)
    select.title('SET ALARM')
    select.minsize(height=688, width=1346)
    select.maxsize(height=758, width=1386)
    select.configure(background='black')
    select.attributes('-alpha', 0.8)
    var = StringVar()
    m_a = StringVar()
    mo = IntVar()
    tu = IntVar()
    we = IntVar()
    th = IntVar()
    fr = IntVar()
    sa = IntVar()
    su = IntVar()
    def Datee():
        import calendar
        import tkinter as Tkinter
        import tkinter.font as tkFont
        from tkinter import ttk

        def get_calendar(locale, fwday):
            # instantiate proper calendar class
            if locale is None:
                return calendar.TextCalendar(fwday)
            else:
                return calendar.LocaleTextCalendar(fwday, locale)

        class Calendar(ttk.Frame):
            # XXX ToDo: cget and configure

            datetime = calendar.datetime.datetime
            timedelta = calendar.datetime.timedelta

            def __init__(self, master=None, **kw):
                """
                WIDGET-SPECIFIC OPTIONS

                    locale, firstweekday, year, month, selectbackground,
                    selectforeground
                """
                # remove custom options from kw before initializating ttk.Frame
                fwday = kw.pop('firstweekday', calendar.MONDAY)
                year = kw.pop('year', self.datetime.now().year)
                month = kw.pop('month', self.datetime.now().month)
                locale = kw.pop('locale', None)
                sel_bg = kw.pop('selectbackground', 'yellow')
                sel_fg = kw.pop('selectforeground', 'blue')

                self._date = self.datetime(year, month, 1)
                self._selection = None  # no date selected

                ttk.Frame.__init__(self, master, **kw)

                self._cal = get_calendar(locale, fwday)

                self.__setup_styles()  # creates custom styles
                self.__place_widgets()  # pack/grid used widgets
                self.__config_calendar()  # adjust calendar columns and setup tags
                # configure a canvas, and proper bindings, for selecting dates
                self.__setup_selection(sel_bg, sel_fg)

                # store items ids, used for insertion later
                self._items = [self._calendar.insert('', 'end', values='')for _ in range(6)]
                # insert dates in the currently empty calendar
                self._build_calendar()

                # set the minimal size for the widget
                #self._calendar.bind('<Map>', self.__minsize)

            def __setitem__(self, item, value):
                if item in ('year', 'month'):
                    raise AttributeError("attribute '%s' is not writeable" % item)
                elif item == 'selectbackground':
                    self._canvas['background'] = value
                elif item == 'selectforeground':
                    self._canvas.itemconfigure(self._canvas.text, item=value)
                else:
                    ttk.Frame.__setitem__(self, item, value)

            def __getitem__(self, item):
                if item in ('year', 'month'):
                    return getattr(self._date, item)
                elif item == 'selectbackground':
                    return self._canvas['background']
                elif item == 'selectforeground':
                    return self._canvas.itemcget(self._canvas.text, 'fill')
                else:
                    r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)})
                    return r[item]

            def __setup_styles(self):
                # custom ttk styles
                style = ttk.Style(self.master)
                arrow_layout = lambda dir: (
                    [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
                )
                style.layout('L.TButton', arrow_layout('left'))
                style.layout('R.TButton', arrow_layout('right'))

            def __place_widgets(self):
                # header frame and its widgets
                hframe = ttk.Frame(self)
                lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
                rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
                self._header = ttk.Label(hframe, width=15, anchor='center')
                # the calendar
                self._calendar = ttk.Treeview(self,show='', selectmode='none', height=7)

                # pack the widgets
                hframe.pack(in_=self, side='top', pady=4, anchor='center')
                lbtn.grid(in_=hframe)
                self._header.grid(in_=hframe, column=1, row=0, padx=12)
                rbtn.grid(in_=hframe, column=2, row=0)
                self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

            def __config_calendar(self):
                cols = self._cal.formatweekheader(3).split()
                self._calendar['columns'] = cols
                self._calendar.tag_configure('header', background='grey90')
                self._calendar.insert('', 'end', values=cols, tag='header')
                # adjust its columns width
                font = tkFont.Font()
                maxwidth = max(font.measure(col) for col in cols)
                for col in cols:
                    self._calendar.column(col, width=maxwidth, minwidth=maxwidth,anchor='e')

            def __setup_selection(self, sel_bg, sel_fg):
                self._font = tkFont.Font()
                self._canvas = canvas = Tkinter.Canvas(self._calendar,background=sel_bg, borderwidth=0, highlightthickness=0)
                canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

                canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
                self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
                self._calendar.bind('<ButtonPress-1>', self._pressed)

            #def __minsize(self, evt):
                #width, height = self._calendar.master.geometry().split('x')
                #height = height[:height.index('+')]
                #self._calendar.master.minsize(width, height)

            def _build_calendar(self):
                year, month = self._date.year, self._date.month

                # update header text (Month, YEAR)
                header = self._cal.formatmonthname(year, month, 0)
                self._header['text'] = header.title()

                # update calendar shown dates
                cal = self._cal.monthdayscalendar(year, month)
                for indx, item in enumerate(self._items):
                    week = cal[indx] if indx < len(cal) else []
                    fmt_week = [('%02d' % day) if day else '' for day in week]
                    self._calendar.item(item, values=fmt_week)

            def _show_selection(self, text, bbox):
                """Configure canvas for a new selection."""
                x, y, width, height = bbox

                textw = self._font.measure(text)

                canvas = self._canvas
                canvas.configure(width=width, height=height)
                canvas.coords(canvas.text, width - textw, height / 2 - 1)
                canvas.itemconfigure(canvas.text, text=text)
                canvas.place(in_=self._calendar, x=x, y=y)

            # Callbacks

            def _pressed(self, evt):
                """Clicked somewhere in the calendar."""
                x, y, widget = evt.x, evt.y, evt.widget
                item = widget.identify_row(y)
                column = widget.identify_column(x)

                if not column or not item in self._items:
                    # clicked in the weekdays row or just outside the columns
                    return

                item_values = widget.item(item)['values']
                if not len(item_values):  # row is empty for this month
                    return

                text = item_values[int(column[1]) - 1]
                if not text:  # date is empty
                    return

                bbox = widget.bbox(item, column)
                if not bbox:  # calendar not visible yet
                    return

                # update and then show selection
                text = '%02d' % text
                self._selection = (text, item, column)
                self._show_selection(text, bbox)

            def _prev_month(self):
                """Updated calendar to show the previous month."""
                self._canvas.place_forget()

                self._date = self._date - self.timedelta(days=1)
                self._date = self.datetime(self._date.year, self._date.month, 1)
                self._build_calendar()  # reconstuct calendar

            def _next_month(self):
                """Update calendar to show the next month."""
                self._canvas.place_forget()
                year, month = self._date.year, self._date.month
                self._date = self._date + self.timedelta(days=calendar.monthrange(year, month)[1] + 1)
                self._date = self.datetime(self._date.year, self._date.month, 1)
                self._build_calendar()  # reconstruct calendar
            # Properties
            @property
            def selection(self):
                """Return a datetime representing the current selected date."""
                if not self._selection:
                    return None

                year, month = self._date.year, self._date.month
                return self.datetime(year, month, int(self._selection[0]))

        def test():
            import sys
            dte = Toplevel(select)
            dte.title('Calendar')
            ttkcal = Calendar(dte,firstweekday=calendar.SUNDAY)
            ttkcal.pack(expand=1, fill='both')
            dte.update()

            def store_cal():
                global date_
                xe = ttkcal.selection
                try:
                    if (datetime.datetime.strptime(str(xe.year),"%Y") == datetime.datetime.strptime(strftime('%Y'),"%Y")):
                        date_ = xe.strftime('%a, %d %b')
                    if (datetime.datetime.strptime(str(xe.year),"%Y") < datetime.datetime.strptime(strftime('%Y'),"%Y")):
                        fdate = messagebox.showerror('ERROR','The applied date is invalid.')
                        dte.destroy()
                        Datee()
                    if (datetime.datetime.strptime(str(xe.year),"%Y") > datetime.datetime.strptime(strftime('%Y'),"%Y")):
                        date_= xe.strftime('%a, %d %b %Y')
                except:
                    date_ = ''
                    pass
                dte.destroy()
                print('x is: ', xe, date_)

            if 'win' not in sys.platform:
                style = ttk.Style()
                style.theme_use('clam')

            set_cal = Button(dte, relief=RAISED, font=('impact', 15), fg='lavenderblush', bg='red', borderwidth=5,text='   OK   ', command=store_cal)
            set_cal.pack()

        if __name__ == '__main__':
            test()

    def close_select():
        if (pygame.mixer.get_init()):
            pygame.mixer.music.stop()
        select.destroy()
    Enter_h = Label(select,font = ('impact',30),text= 'HOUR',fg = 'red' , bg = 'black',relief = 'raised',borderwidth = 5)
    Enter_h.pack()
    Enter_h.place(x = 500,y = 50)

    Enter_m = Label(select, font=('impact', 30), text='MINUTES', fg='red', bg='black', relief='raised',borderwidth = 5)
    Enter_m.pack()
    Enter_m.place(x=650, y=50)

    scroll_H = Spinbox(select)
    list_h = Spinbox(select,font = ('impact',30),fg = 'red' , bg= 'black', from_= 1 , to= 12,width= 3,justify= CENTER,relief= GROOVE)
    list_h.pack()
    list_h.place(x=500, y=150)

    scroll_M = Spinbox(select)
    list_m = Spinbox(select, font=('impact', 30), fg='red', bg= 'black', from_= 0, to= 60, width= 3, justify= CENTER,relief= GROOVE)
    list_m.pack()
    list_m.place(x=689, y=150)

    Date = Button(select, relief=RAISED, font=('impact', 15), bg='dodgerblue', fg='black', borderwidth=5, text='  DATE  ',command = Datee)
    Date.pack()
    Date.place( x= 350, y =250)

    def store():
        global Alarm_1, m_1, Alarm_2, m_2, Alarm_3, m_3, Alarm_4, m_4, Alarm_5, m_5, Alarm_6, m_6, Alarm_7, m_7, Alarm_8, m_8, Alarm_9, m_9, Alarm_10, m_10
        global count_a
        global Z_play_check
        global date_
        if (pygame.mixer.get_init()):
            pygame.mixer.music.stop()
        count_a = count_a + 1
        if (count_a == 1):
            repeat_1 = ''
            A_H = list_h.get().zfill(2)
            A_M = list_m.get().zfill(2)
            eve = var.get()
            mon_1 = mo.get()
            tue_1 = tu.get()
            wed_1 = we.get()
            thu_1 = th.get()
            fri_1 = fr.get()
            sat_1 = sa.get()
            sun_1 = su.get()
            if (mon_1>0):
                repeat_1 = repeat_1 + 'M '
            if (tue_1 > 0):
                repeat_1 = repeat_1 + 'T '
            if (wed_1 > 0):
                repeat_1 = repeat_1 + 'W '
            if (thu_1 > 0):
                repeat_1 = repeat_1 + 'Th '
            if (fri_1 > 0):
                repeat_1 = repeat_1 + 'F '
            if (sat_1 > 0):
                repeat_1 = repeat_1 + 'S '
            if (sun_1 > 0):
                repeat_1 = repeat_1 + 'Su '
            if ((mon_1==0)and(tue_1==0)and(wed_1==0)and(thu_1==0)and(fri_1==0)and(sat_1==0)and(sun_1==0)):
                if(date_ != ''):
                    repeat_1 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H + ":"+ A_M + eve
                    FMT = "%I:%M%p"
                    if(datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_1 = datetime.datetime.strftime(tomorrow,'%a, %d %b')
                    else:
                        repeat_1 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_1 = '  WAKE  UP   '
            else:
                m_1 = m_a.get()
            Alarm_1 = A_H + ":"+ A_M + ":00" + eve +" - "+ repeat_1
            a01 = A_H + ":"+ A_M + eve +" - "+ repeat_1
            if not messagebox.askokcancel("Alarm - 1",a01+"\n"+m_1):
                Alarm_1 = ''
                m_1 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_1)
            print(m_1)
        if (count_a == 2):
            repeat_2 = ''
            A_H_1 = list_h.get().zfill(2)
            A_M_1 = list_m.get().zfill(2)
            eve_1 = var.get()
            mon_2 = mo.get()
            tue_2 = tu.get()
            wed_2 = we.get()
            thu_2 = th.get()
            fri_2 = fr.get()
            sat_2 = sa.get()
            sun_2 = su.get()
            if (mon_2 > 0):
                repeat_2 = repeat_2 + 'M '
            if (tue_2 > 0):
                repeat_2 = repeat_2 + 'T '
            if (wed_2 > 0):
                repeat_2 = repeat_2 + 'W '
            if (thu_2 > 0):
                repeat_2 = repeat_2 + 'Th '
            if (fri_2 > 0):
                repeat_2 = repeat_2 + 'F '
            if (sat_2 > 0):
                repeat_2 = repeat_2 + 'S '
            if (sun_2 > 0):
                repeat_2 = repeat_2 + 'Su '
            if ((mon_2 == 0) and (tue_2 == 0) and (wed_2 == 0) and (thu_2 == 0) and (fri_2 == 0) and (sat_2 == 0) and (sun_2 == 0)):
                if (date_ != ''):
                    repeat_2 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_1 + ":" + A_M_1 + eve_1
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_2 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_2 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_2 = '  WAKE  UP   '
            else:
                m_2 = m_a.get()
            Alarm_2 = A_H_1 + ":" + A_M_1 + ":00" + eve_1 + " - "+ repeat_2
            a02 = A_H_1 + ":" + A_M_1 + eve_1 + " - " + repeat_2
            if not messagebox.askokcancel("Alarm - 2", a02 + "\n" + m_2):
                Alarm_2 = ''
                m_2 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_2)
            print(m_2)
        if (count_a == 3):
            repeat_3 = ''
            A_H_2 = list_h.get().zfill(2)
            A_M_2 = list_m.get().zfill(2)
            eve_2 = var.get()
            mon_3 = mo.get()
            tue_3 = tu.get()
            wed_3 = we.get()
            thu_3 = th.get()
            fri_3 = fr.get()
            sat_3 = sa.get()
            sun_3 = su.get()
            if (mon_3 > 0):
                repeat_3 = repeat_3 + 'M '
            if (tue_3 > 0):
                repeat_3 = repeat_3 + 'T '
            if (wed_3 > 0):
                repeat_3 = repeat_3 + 'W '
            if (thu_3 > 0):
                repeat_3 = repeat_3 + 'Th '
            if (fri_3 > 0):
                repeat_3 = repeat_3 + 'F '
            if (sat_3 > 0):
                repeat_3 = repeat_3 + 'S '
            if (sun_3 > 0):
                repeat_3 = repeat_3 + 'Su '
            if ((mon_3 == 0) and (tue_3 == 0) and (wed_3 == 0) and (thu_3 == 0) and (fri_3 == 0) and (sat_3 == 0) and (sun_3 == 0)):
                if (date_ != ''):
                    repeat_3 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_2 + ":" + A_M_2 + eve_2
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_3 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_3 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_3 = '  WAKE  UP   '
            else:
                m_3 = m_a.get()
            Alarm_3 = A_H_2 + ":" + A_M_2 + ":00" + eve_2 + " - "+ repeat_3
            a03 = A_H_2 + ":" + A_M_2 + eve_2 + " - " + repeat_3
            if not messagebox.askokcancel("Alarm - 3", a03 + "\n" + m_3):
                Alarm_3 = ''
                m_3 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_3)
            print(m_3)
        if (count_a == 4):
            repeat_4 = ''
            A_H_3 = list_h.get().zfill(2)
            A_M_3 = list_m.get().zfill(2)
            eve_3 = var.get()
            mon_4 = mo.get()
            tue_4 = tu.get()
            wed_4 = we.get()
            thu_4 = th.get()
            fri_4 = fr.get()
            sat_4 = sa.get()
            sun_4 = su.get()
            if (mon_4 > 0):
                repeat_4 = repeat_4 + 'M '
            if (tue_4 > 0):
                repeat_4 = repeat_4 + 'T '
            if (wed_4 > 0):
                repeat_4 = repeat_4 + 'W '
            if (thu_4 > 0):
                repeat_4 = repeat_4 + 'Th '
            if (fri_4 > 0):
                repeat_4 = repeat_4 + 'F '
            if (sat_4 > 0):
                repeat_4 = repeat_4 + 'S '
            if (sun_4 > 0):
                repeat_4 = repeat_4 + 'Su '
            if ((mon_4 == 0) and (tue_4 == 0) and (wed_4 == 0) and (thu_4 == 0) and (fri_4 == 0) and (sat_4 == 0) and (sun_4 == 0)):
                if (date_ != ''):
                    repeat_4 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_3 + ":" + A_M_3 + eve_3
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_4 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_4 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_4 = '  WAKE  UP   '
            else:
                m_4 = m_a.get()
            Alarm_4 = A_H_3 + ":" + A_M_3 + ":00" + eve_3 + " - "+ repeat_4
            a04 = A_H_3 + ":" + A_M_3 + eve_3 + " - " + repeat_4
            if not messagebox.askokcancel("Alarm - 4", a04 + "\n" + m_4):
                Alarm_4 = ''
                m_4 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_4)
            print(m_4)
        if (count_a == 5):
            repeat_5 = ''
            A_H_4 = list_h.get().zfill(2)
            A_M_4 = list_m.get().zfill(2)
            eve_4 = var.get()
            mon_5 = mo.get()
            tue_5 = tu.get()
            wed_5 = we.get()
            thu_5 = th.get()
            fri_5 = fr.get()
            sat_5 = sa.get()
            sun_5 = su.get()
            if (mon_5 > 0):
                repeat_5 = repeat_5 + 'M '
            if (tue_5 > 0):
                repeat_5 = repeat_5 + 'T '
            if (wed_5 > 0):
                repeat_5 = repeat_5 + 'W '
            if (thu_5 > 0):
                repeat_5 = repeat_5 + 'Th '
            if (fri_5 > 0):
                repeat_5 = repeat_5 + 'F '
            if (sat_5 > 0):
                repeat_5 = repeat_5 + 'S '
            if (sun_5 > 0):
                repeat_5 = repeat_5 + 'Su '
            if ((mon_5 == 0) and (tue_5 == 0) and (wed_5 == 0) and (thu_5 == 0) and (fri_5 == 0) and (sat_5 == 0) and (sun_5 == 0)):
                if (date_ != ''):
                    repeat_5 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_4 + ":" + A_M_4 + eve_4
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_5 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_5 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_5 = '  WAKE  UP   '
            else:
                m_5 = m_a.get()
            Alarm_5 = A_H_4 + ":" + A_M_4+ ":00" + eve_4 + " - "+ repeat_5
            a05 = A_H_4 + ":" + A_M_4 + eve_4 + " - " + repeat_5
            if not messagebox.askokcancel("Alarm - 5", a05 + "\n" + m_5):
                Alarm_5 = ''
                m_5 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_5)
            print(m_5)
        if (count_a == 6):
            repeat_6 = ''
            A_H_5 = list_h.get().zfill(2)
            A_M_5 = list_m.get().zfill(2)
            eve_5 = var.get()
            mon_6 = mo.get()
            tue_6 = tu.get()
            wed_6 = we.get()
            thu_6 = th.get()
            fri_6 = fr.get()
            sat_6 = sa.get()
            sun_6 = su.get()
            if (mon_6 > 0):
                repeat_6 = repeat_6 + 'M '
            if (tue_6 > 0):
                repeat_6 = repeat_6 + 'T '
            if (wed_6 > 0):
                repeat_6 = repeat_6 + 'W '
            if (thu_6 > 0):
                repeat_6 = repeat_6 + 'Th '
            if (fri_6 > 0):
                repeat_6 = repeat_6 + 'F '
            if (sat_6 > 0):
                repeat_6 = repeat_6 + 'S '
            if (sun_6 > 0):
                repeat_6 = repeat_6 + 'Su '
            if ((mon_6 == 0) and (tue_6 == 0) and (wed_6 == 0) and (thu_6 == 0) and (fri_6 == 0) and (sat_6 == 0) and (sun_6 == 0)):
                if (date_ != ''):
                    repeat_6 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_5 + ":" + A_M_5 + eve_5
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_6 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_6 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_6 = '  WAKE  UP   '
            else:
                m_6 = m_a.get()
            Alarm_6 = A_H_5 + ":" + A_M_5+ ":00" + eve_5 + " - "+ repeat_6
            a06 = A_H_5 + ":" + A_M_5 + eve_5 + " - " + repeat_6
            if not messagebox.askokcancel("Alarm - 6", a06 + "\n" + m_6):
                Alarm_6 = ''
                m_6 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_6)
            print(m_6)
        if (count_a == 7):
            repeat_7 = ''
            A_H_6 = list_h.get().zfill(2)
            A_M_6 = list_m.get().zfill(2)
            eve_6 = var.get()
            mon_7 = mo.get()
            tue_7 = tu.get()
            wed_7 = we.get()
            thu_7 = th.get()
            fri_7 = fr.get()
            sat_7 = sa.get()
            sun_7 = su.get()
            if (mon_7 > 0):
                repeat_7 = repeat_7 + 'M '
            if (tue_7 > 0):
                repeat_7 = repeat_7 + 'T '
            if (wed_7 > 0):
                repeat_7 = repeat_7 + 'W '
            if (thu_7 > 0):
                repeat_7 = repeat_7 + 'Th '
            if (fri_7 > 0):
                repeat_7 = repeat_7 + 'F '
            if (sat_7 > 0):
                repeat_7 = repeat_7 + 'S '
            if (sun_7 > 0):
                repeat_7 = repeat_7 + 'Su '
            if ((mon_7 == 0) and (tue_7 == 0) and (wed_7 == 0) and (thu_7 == 0) and (fri_7 == 0) and (sat_7 == 0) and (sun_7 == 0)):
                if (date_ != ''):
                    repeat_7 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_6 + ":" + A_M_6 + eve_6
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_7 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_7 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_7 = '  WAKE  UP   '
            else:
                m_7 = m_a.get()
            Alarm_7 = A_H_6 + ":" + A_M_6+ ":00" + eve_6 + " - "+ repeat_7
            a07 = A_H_6 + ":" + A_M_6 + eve_6 + " - " + repeat_7
            if not messagebox.askokcancel("Alarm - 7", a07 + "\n" + m_7):
                Alarm_7 = ''
                m_7 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_7)
            print(m_7)
        if (count_a == 8):
            repeat_8 = ''
            A_H_7 = list_h.get().zfill(2)
            A_M_7 = list_m.get().zfill(2)
            eve_7 = var.get()
            mon_8 = mo.get()
            tue_8 = tu.get()
            wed_8 = we.get()
            thu_8 = th.get()
            fri_8 = fr.get()
            sat_8 = sa.get()
            sun_8 = su.get()
            if (mon_8 > 0):
                repeat_8 = repeat_8 + 'M '
            if (tue_8 > 0):
                repeat_8 = repeat_8 + 'T '
            if (wed_8 > 0):
                repeat_8 = repeat_8 + 'W '
            if (thu_8 > 0):
                repeat_8 = repeat_8 + 'Th '
            if (fri_8 > 0):
                repeat_8 = repeat_8 + 'F '
            if (sat_8 > 0):
                repeat_8 = repeat_8 + 'S '
            if (sun_8 > 0):
                repeat_8 = repeat_8 + 'Su '
            if ((mon_8 == 0) and (tue_8 == 0) and (wed_8 == 0) and (thu_8 == 0) and (fri_8 == 0) and (sat_8 == 0) and (sun_8 == 0)):
                if (date_ != ''):
                    repeat_8 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_7 + ":" + A_M_7 + eve_7
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_8 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_8 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_8 = '  WAKE  UP   '
            else:
                m_8 = m_a.get()
            Alarm_8 = A_H_7 + ":" + A_M_7+ ":00" + eve_7 + " - "+ repeat_8
            a08 = A_H_7 + ":" + A_M_7 + eve_7 + " - " + repeat_8
            if not messagebox.askokcancel("Alarm - 8", a08 + "\n" + m_8):
                Alarm_8 = ''
                m_8 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_8)
            print(m_8)
        if (count_a == 9):
            repeat_9 = ''
            A_H_8 = list_h.get().zfill(2)
            A_M_8 = list_m.get().zfill(2)
            eve_8 = var.get()
            mon_9 = mo.get()
            tue_9 = tu.get()
            wed_9 = we.get()
            thu_9 = th.get()
            fri_9 = fr.get()
            sat_9 = sa.get()
            sun_9 = su.get()
            if (mon_9 > 0):
                repeat_9 = repeat_9 + 'M '
            if (tue_9 > 0):
                repeat_9 = repeat_9 + 'T '
            if (wed_9 > 0):
                repeat_9 = repeat_9 + 'W '
            if (thu_9 > 0):
                repeat_9 = repeat_9 + 'Th '
            if (fri_9 > 0):
                repeat_9 = repeat_9 + 'F '
            if (sat_9 > 0):
                repeat_9 = repeat_9 + 'S '
            if (sun_9 > 0):
                repeat_9 = repeat_9 + 'Su '
            if ((mon_9 == 0) and (tue_9 == 0) and (wed_9 == 0) and (thu_9 == 0) and (fri_9 == 0) and (sat_9 == 0) and (sun_9 == 0)):
                if (date_ != ''):
                    repeat_9 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_8 + ":" + A_M_8 + eve_8
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_9 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_9 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_9 = '  WAKE  UP   '
            else:
                m_9 = m_a.get()
            Alarm_9 = A_H_8 + ":" + A_M_8 + ":00" + eve_8 + " - "+ repeat_9
            a09 = A_H_8 + ":" + A_M_8 + eve_8 + " - " + repeat_9
            if not messagebox.askokcancel("Alarm - 9", a09 + "\n" + m_9):
                Alarm_9 = ''
                m_9 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_9)
            print(m_9)
        if (count_a == 10):
            repeat_10 = ''
            A_H_9 = list_h.get().zfill(2)
            A_M_9 = list_m.get().zfill(2)
            eve_9 = var.get()
            mon_10 = mo.get()
            tue_10 = tu.get()
            wed_10 = we.get()
            thu_10 = th.get()
            fri_10 = fr.get()
            sat_10 = sa.get()
            sun_10 = su.get()
            if (mon_10 > 0):
                repeat_10 = repeat_10 + 'M '
            if (tue_10 > 0):
                repeat_10 = repeat_10 + 'T '
            if (wed_10 > 0):
                repeat_10 = repeat_10 + 'W '
            if (thu_10 > 0):
                repeat_10 = repeat_10 + 'Th '
            if (fri_10 > 0):
                repeat_10 = repeat_10 + 'F '
            if (sat_10 > 0):
                repeat_10 = repeat_10 + 'S '
            if (sun_10 > 0):
                repeat_10 = repeat_10 + 'Su '
            if ((mon_10 == 0) and (tue_10 == 0) and (wed_10 == 0) and (thu_10 == 0) and (fri_10 == 0) and (sat_10 == 0) and (sun_10 == 0)):
                if (date_ != ''):
                    repeat_10 = date_
                if (date_ == ''):
                    today = datetime.datetime.today()
                    r1 = strftime('%I:%M%p')
                    r2 = A_H_9 + ":" + A_M_9 + eve_9
                    FMT = "%I:%M%p"
                    if (datetime.datetime.strptime(r1, FMT) > datetime.datetime.strptime(r2, FMT)):
                        tomorrow = today + datetime.timedelta(days=1)
                        repeat_10 = datetime.datetime.strftime(tomorrow, '%a, %d %b')
                    else:
                        repeat_10 = datetime.datetime.strftime(today, '%a, %d %b')
            if ((m_a.get()) == ''):
                m_10 = '  WAKE  UP   '
            else:
                m_10 = m_a.get()
            Alarm_10 = A_H_9 + ":" + A_M_9 + ":00" + eve_9 + " - "+ repeat_10
            a10 = A_H_9 + ":" + A_M_9 + eve_9 + " - " + repeat_10
            if not messagebox.askokcancel("Alarm - 10", a10 + "\n" + m_10):
                Alarm_10 = ''
                m_10 = ''
                count_a = count_a - 1
                with open('Alarm_count.plk', 'wb')as z:
                    dill.dump(count_a, z)
                with open('Alarm_time.plk', 'wb')as z1:
                    dill.dump(Alarm_1, z1)
                    dill.dump(Alarm_2, z1)
                    dill.dump(Alarm_3, z1)
                    dill.dump(Alarm_4, z1)
                    dill.dump(Alarm_5, z1)
                    dill.dump(Alarm_6, z1)
                    dill.dump(Alarm_7, z1)
                    dill.dump(Alarm_8, z1)
                    dill.dump(Alarm_9, z1)
                    dill.dump(Alarm_10, z1)
                with open('Alarm_time_mess.plk', 'wb')as z2:
                    dill.dump(m_1, z2)
                    dill.dump(m_2, z2)
                    dill.dump(m_3, z2)
                    dill.dump(m_4, z2)
                    dill.dump(m_5, z2)
                    dill.dump(m_6, z2)
                    dill.dump(m_7, z2)
                    dill.dump(m_8, z2)
                    dill.dump(m_9, z2)
                    dill.dump(m_10, z2)
                select.destroy()
                Enter_Time()
            date_ = ''
            print(Alarm_10)
            print(m_10)

        with open('Alarm_count.plk', 'wb')as z:
            dill.dump(count_a, z)
        with open('Alarm_time.plk', 'wb')as z1:
            dill.dump(Alarm_1, z1)
            dill.dump(Alarm_2, z1)
            dill.dump(Alarm_3, z1)
            dill.dump(Alarm_4, z1)
            dill.dump(Alarm_5, z1)
            dill.dump(Alarm_6, z1)
            dill.dump(Alarm_7, z1)
            dill.dump(Alarm_8, z1)
            dill.dump(Alarm_9, z1)
            dill.dump(Alarm_10, z1)
        with open('Alarm_time_mess.plk', 'wb')as z2:
            dill.dump(m_1, z2)
            dill.dump(m_2, z2)
            dill.dump(m_3, z2)
            dill.dump(m_4, z2)
            dill.dump(m_5, z2)
            dill.dump(m_6, z2)
            dill.dump(m_7, z2)
            dill.dump(m_8, z2)
            dill.dump(m_9, z2)
            dill.dump(m_10, z2)
        select.destroy()
        Alarm_M()
    def change1():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 1
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Loud_Alarm_Clock_Buzzer-Muk1984-493547174.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- LOUD BUZZER --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change2():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 2
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Rooster Crow-SoundBible.com-1802551702.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- ROOSTER CROW --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change3():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 3
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Pager Beeps-SoundBible.com-260751720.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- PAGER BEEPS --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change4():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 4
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Analog-watch-alarm_daniel_simon.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- DIGITAL BEEPS --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change5():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 5
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\submarine-diving-alarm-daniel_simon.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- SUBMARINE DIVING --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change6():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 6
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\old-fashioned-door-bell-daniel_simon.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- DOOR BELL --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change7():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 7
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Railroad_crossing_bell_Brylon_Terry-1551570865.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- RAIL ROAD CROSSING --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change8():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 8
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Tornado Siren-SoundBible.com-897026957.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- TORNADO SIREN --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change9():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 9
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\Police Siren 3-SoundBible.com-553177907.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- POLICE SIREN --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change10():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 10
        pygame.mixer.init()
        pygame.mixer.music.load(open(os.getcwd()+"\church-chime-daniel_simon.wav", "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure( text = " --- CHURCH BELL --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
    def change11():
        global Z_Play
        global Z_play_check
        Z_play_check = 1
        Z_Play = 11
        file_path = filedialog.askopenfilenames(filetypes=(("WAV files", "*.wav"),("MP3 files","*.mp3")))
        head,tail = os.path.split(file_path[0])
        pygame.mixer.init()
        pygame.mixer.music.load(open(file_path[0], "rb"))
        pygame.mixer.music.play(1)
        set_Tone.configure(text=" --- "+tail[:10]+" --- ")
        with open('Alarm_tone.plk','wb') as s1:
            dill.dump(Z_play_check,s1)
            dill.dump(Z_Play,s1)
            dill.dump(file_path,s1)

    Tone = Label(select,font=('impact', 26),text = ' SELECT ALARM TONE ' ,bg = 'black',fg = 'white')
    Tone.pack()
    Tone.place( x=900, y= 220)

    set_Tone = Menubutton(select, text = ' ---LOUD BUZZER--- ',relief = 'raised',font = ('MS Sans Serif',14),bg = 'red')
    set_Tone.grid()
    mayoVar = IntVar()
    set_Tone.menu = Menu(set_Tone, tearoff = 0)
    set_Tone["menu"] = set_Tone.menu
    global Z_Play
    global Z_play_check
    Load_tones()
    if (Z_play_check == 1):
        print(Z_Play,Z_play_check)
        if (Z_Play == 1):
            set_Tone.configure(text=" --- LOUD BUZZER --- ")
        if (Z_Play == 2):
            set_Tone.configure(text=" --- ROOSTER CROW --- ")
        if (Z_Play == 3):
            set_Tone.configure(text=" --- PAGER BEEPS --- ")
        if (Z_Play == 4):
            set_Tone.configure(text=" --- DIGITAL BEEPS --- ")
        if (Z_Play == 5):
            set_Tone.configure(text=" --- SUBMARINE DIVING --- ")
        if (Z_Play == 6):
            set_Tone.configure(text=" --- DOOR BELL --- ")
        if (Z_Play == 7):
            set_Tone.configure(text=" --- RAIL ROAD CROSSING --- ")
        if (Z_Play == 8):
            set_Tone.configure(text=" --- TORNADO SIREN --- ")
        if (Z_Play == 9):
            set_Tone.configure(text=" --- POLICE SIREN --- ")
        if (Z_Play == 10):
            set_Tone.configure(text=" --- CHURCH BELL --- ")
        if (Z_Play == 11):
            with open('Alarm_tone.plk', 'rb') as s1:
                Z_play_check = dill.load(s1)
                Z_Play = dill.load(s1)
                file_path = dill.load(s1)
            head, tail = os.path.split(file_path[0])
            set_Tone.configure(text=" --- " + tail[:10] + " --- ")

    set_Tone.menu.add_command(label= ' Loud buzzer ', command=change1)
    set_Tone.menu.add_command(label=' Rooster Crow ', command=change2)
    set_Tone.menu.add_command(label=' Pager Beeps ', command=change3)
    set_Tone.menu.add_command(label=' Digital Beeps ', command=change4)
    set_Tone.menu.add_command(label=' Submarine Diving ', command=change5)
    set_Tone.menu.add_command(label=' Door Bell ', command=change6)
    set_Tone.menu.add_command(label=' Rail road Crossing ', command=change7)
    set_Tone.menu.add_command(label=' Tornado Siren ', command=change8)
    set_Tone.menu.add_command(label=' Police Siren ', command=change9)
    set_Tone.menu.add_command(label=' Church  Bell ', command=change10)
    set_Tone.menu.add_command(label = 'Select your song.', command = change11)
    set_Tone.pack()
    set_Tone.place(x=925, y=280)

    r_AM = Radiobutton(select,variable = var,font=('impact', 30),text = 'AM',value = 'AM',bg = 'black',fg = 'red')
    r_AM.pack()
    r_AM.place( x = 625,y = 220)

    r_PM = Radiobutton(select,variable = var, font=('impact', 30), text='PM', value = 'PM', bg = 'black',fg = 'red')
    r_PM.pack()
    r_PM.place(x=625, y=420)

    message = Label(select ,font=('impact', 26),text = ' NOTE / MESSAGE ' ,bg = 'black',fg = 'white')
    message.pack()
    message.place( x = 100, y = 220-100)
    m_e = Entry(select,textvariable = m_a,font = ('bookman',20),bg = 'red',fg = 'white')
    m_e.pack()
    m_e.place(x = 114,y = 270-100)

    repeat = Label(select,font = ('ms serif', 30),text = ' REPEAT ', bg = 'black', fg = 'dodgerblue')
    repeat.pack()
    repeat.place(x = 100, y= 250)
    mon = Checkbutton(select,variable = mo,font=('impact', 20), text = 'MON',onvalue = 1, offvalue = 0,bg = 'black',fg = 'red' )
    mon.pack()
    mon.place(x = 100, y= 292)
    tue = Checkbutton(select, variable=tu, font=('impact', 20), text='TUE', onvalue= 2, offvalue=0, bg='black', fg='red')
    tue.pack()
    tue.place(x=100, y=292+50)
    wed = Checkbutton(select, variable=we, font=('impact', 20), text='WED', onvalue=3, offvalue=0, bg='black', fg='red')
    wed.pack()
    wed.place(x=100, y=292 + (50 * 2))
    thu = Checkbutton(select, variable=th, font=('impact', 20), text='THU', onvalue=4, offvalue=0, bg='black', fg='red')
    thu.pack()
    thu.place(x=100, y=292 + (50 * 3))
    fri = Checkbutton(select, variable=fr, font=('impact', 20), text='FRI', onvalue=5, offvalue=0, bg='black', fg='red')
    fri.pack()
    fri.place(x=100, y=292 + (50 * 4))
    sat = Checkbutton(select, variable=sa, font=('impact', 20), text='SAT', onvalue=6, offvalue=0, bg='black', fg='red')
    sat.pack()
    sat.place(x=100, y=292 + (50 * 5))
    sun = Checkbutton(select, variable=su, font=('impact', 20), text='SUN', onvalue=7, offvalue=0, bg='black', fg='red')
    sun.pack()
    sun.place(x=100, y=292 + (50 * 6))

    set =Button(select,relief = RAISED, font = ('impact',15),fg = 'black' , bg = 'red',borderwidth = 5, text = '   SET   ',command = store)
    set.pack()
    set.place(x = 625,y =520)
    r_AM.select()
    select.protocol("WM_DELETE_WINDOW", close_select)
    select.mainloop()

Clock = Label(root,font = ('impact',40),fg = "yellow", bg = 'black',text = strftime('[ %a ]   %d / %m (  %B  ) / %Y '))
Clock.place(x = 80 ,y = 400)

with open('Alarm_todo_time.plk', 'rb') as ccc:
    try:
        check_x = dill.load(ccc)
        To_do_m = 1
        To_do_set = Button(root, relief=GROOVE, font=('Comic Sans MS', 20), fg='black', bg='gold',text=' Prepared to-do list  ', borderwidth=8, command=Prepared_Todo_2)
        To_do_set.pack()
        To_do_set.place(x=100, y=65)
    except:
        To_do = Button(root,relief = GROOVE, font = ('Comic Sans MS',20),fg = 'black', bg = 'gold', text = '  To-Do list  ',borderwidth = 8,command = Set_todo)
        To_do.pack()
        To_do.place( x= 166, y=65)

Buttons = Button(root,relief = RAISED, font = ('fixedsys',20),fg = 'magenta' , bg = 'black',borderwidth = 10, text = 'SET ALARM', command = Enter_Time)
Buttons.pack()
Buttons.place( x = 600, y =65)

image = Image.open("151722817462417397.jpg")
photo = ImageTk.PhotoImage(image)
reset = Button(root,command = reset)
reset.config(image = photo,bg = 'black', borderwidth = 0)
reset.pack()
reset.place( x= 420, y=40)

Alarm_M()
Load_todo()
open_tones()
set_Startup()
Clock = Label(root,font = ('impact',100),fg = "chartreuse", bg = 'black')
Clock.pack()
Clock.place( x =80 , y = 200)

with open('Weather_ALARM.plk', 'rb')as ww:
    try:
        weat = dill.load(ww)
        if (weat['City'] == 'Siliguri'):
            weat['City'] = 'Jalpaiguri'
        dest = weat['City'] + ", " + weat['State'] + ", " + weat['Country']
        owm = pyowm.OWM('9aa222a1f36c220d515108dd905ba698')
        observation = owm.weather_at_place(dest)
        w = observation.get_weather()
        weatherr = 'Temperature -> '+str(w.get_temperature('celsius')['temp'])+' '+u'\u2103'+', '+w.get_detailed_status()+'\n'+'Wind speed -> '+str(w.get_wind()['speed'])+' m/s'+"  "+'Humidity -> '+str(w.get_humidity())+" %"
        pos = Label(root, font=('ms serif', 25), text=dest, fg="dodgerblue", bg='black')
        pos.pack()
        pos.place(x=186, y=489)
        pos_weather = Label(root,font = ('ms serif',25),text = weatherr,fg = "lavenderblush", bg = 'black')
        pos_weather.pack()
        pos_weather.place(x = 120,y = 555)
        def weather_Update():
            Timer(7200, weather_Update).start()
            observation_7 = owm.weather_at_place(dest)
            w_7 = observation_7.get_weather()
            weatherr_7 = 'Temperature -> ' + str(w_7.get_temperature('celsius')['temp']) + ' ' + u'\u2103' + ', ' + w_7.get_detailed_status() + '\n' + 'Wind speed -> ' + str(w_7.get_wind()['speed']) + ' m/s' + "  " + 'Humidity -> ' + str(w_7.get_humidity()) + " %"
            pos.config(text=dest)
            pos_weather.config(text=weatherr_7)
        weather_Update()
    except:
        def weather_destroy():
            Weather.destroy()
        Weather = Button(root, relief=RAISED, font=('ms serif', 25), fg='navy', bg='lime', borderwidth=10,text='SET WEATHER', command=lambda: [weather_destroy(),weather()])
        Weather.pack()
        Weather.place(x=300, y=500)
        pass

def Subject_time():
    global time_1
    global Alarm_1
    count_b = 0
    time_2 = strftime('%I : %M : %S %p')
    if (time_2 != time_1):
        time_1 = time_2
        Clock.config(text = time_2)
        t = strftime('%I:%M:%S%p')
        to_do_t = strftime('%Y/%m/%d\t\t%I:%M:%S %p')
        if ((t==Alarm_1[:10])or(t==Alarm_2[:10])or(t==Alarm_3[:10])or(t==Alarm_4[:10])or(t==Alarm_5[:10])or(t==Alarm_6[:10])or(t==Alarm_7[:10])or(t==Alarm_8[:10])or(t==Alarm_9[:10])or(t==Alarm_10[:10])) :
            Ring(t)
        if ((to_do_t==Todo_Al_1[:23])or(to_do_t==Todo_Al_2[:23])or(to_do_t==Todo_Al_3[:23])or(to_do_t==Todo_Al_4[:23])or(to_do_t==Todo_Al_5[:23])or(to_do_t==Todo_Al_6[:23])or(to_do_t==Todo_Al_7[:23])or(to_do_t==Todo_Al_8[:23])or(to_do_t==Todo_Al_9[:23])or(to_do_t==Todo_Al_10[:23])or(to_do_t==Todo_Al_11[:23])or(to_do_t==Todo_Al_12[:23])) :
            Ring_TO_do(to_do_t)
    Clock.after(200,Subject_time)

Subject_time()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()