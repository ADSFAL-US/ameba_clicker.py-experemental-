import tkinter as tk
from tkinter import Button, Entry, END,PhotoImage, Canvas
import pygame
from PIL import Image,ImageTk
import threading as thr
import time
import random as rnd
pygame.mixer.init()
root = tk.Tk()
ameba_lvl=0
coast0=1
coast1=100
clicks=0
do_tap=0
multy=1
lvl=1
scores=0
supercl=100
auto=1
vars = [ameba_lvl,coast0,coast1,clicks,do_tap,multy,lvl,scores,supercl,auto]
root.geometry("1000x1500")
basic_ameba=Image.open("./assets/ameba1.png")
ameba1 = Image.open("./assets/ameba2.png")
ameba2 = Image.open('./assets/ameba3.png')

resized_image= basic_ameba.resize((800,800))
basic_ameba= ImageTk.PhotoImage(resized_image)

resized_image1= ameba1.resize((800,800))
ameba1= ImageTk.PhotoImage(resized_image1)

resized_image2 = ameba2.resize((800,800))
ameba2= ImageTk.PhotoImage(resized_image2)

def save(data="",reset=False):
	try:
		a=open("./data/save.txt", "r")
		a.close()
	except:
		try:
			
			os.mkdir("./data")
		except:
			pass
		
		b=open("./data/save.txt", "x")
		b.write("tosave")
		b.close()		
	dataS = open("./data/save.txt", "a")
	dataS.write(str(data)+"\n")
	dataS.close()
	if reset == True:
		dataS = open("./data/save.txt", "w")
		dataS.write("tosave")
		dataS.close()



def load():
	bret = []
	a=open("./data/save.txt", "r")
	for o in range(0,9):
		b = a.readline()
		bret.append(b)
	return(bret)


			
		

def music():
		time.sleep(0.2)
		pygame.mixer.music.load("assets/music.mp3")
		pygame.mixer.music.play(loops=-1)
		pygame.mixer.music.set_volume(0.15)
		

def on_click():
	bg=pygame.mixer.Sound("assets/click.mp3")
	bg.play(loops=0)
	global clicks
	global lvl
	global scores
	global do_tap
	global supercl
	clicks=clicks+multy
	if rnd.randint(-100,100)>98:
		clicks=clicks+supercl
	
	if clicks / lvl >100:
		scores=scores+lvl
		clicks=clicks-lvl*100
		lvl=lvl+1
	do_tap=1
		
def usos():
	global do_tap
	global ameba
	while True:
		if do_tap == 1:
			pass


def upgrade_autoclick():
	global auto
	global clicks
	global scores
	global coast0
	if scores>=coast0:
		bg2=pygame.mixer.Sound("assets/lvlup.mp3")
		bg2.play(loops=0)
		scores=scores-coast0
		coast0=coast0*2
		auto = auto+1
	
def upgrade_click():
	global multy
	global scores
	global coast0
	if scores>=coast0:
		bg3=pygame.mixer.Sound("assets/lvlup.mp3")
		bg3.play(loops=0)
		scores=scores-coast0
		coast0=coast0*2
		multy=multy+1
	

amebalvl=0
def do_ameba():
	global scores
	global ameba
	global supercl
	global amebalvl
	global clicks
	global lvl
	global rebith
	global rebcoast
	if scores>=500 and amebalvl==1:
		bg1=pygame.mixer.Sound("assets/lvl.mp3")
		bg1.set_volume(10.0)
		bg1.play(loops=0)
		
		ameba.config(image=ameba2)
		scores=scores-500
		lvl=1
		supercl=supercl+500
		clicks=0
		amebalvl=2
		rebcoast = 1500
	if scores>=100 and amebalvl==0:
		bg1=pygame.mixer.Sound("assets/lvl.mp3")
		rebcoast = 500
		bg1.set_volume(10.0)
		bg1.play(loops=0)
		ameba.config(image=ameba1)
		scores=scores-100
		lvl=1
		supercl=supercl+100
		clicks=0
		amebalvl=1
	
		
			


main_cw=Canvas(root)
main_cw.pack(side="bottom")
main_cw.create_rectangle(0,0,2000,1500,fill="#51fc7f")

txt= Entry(main_cw,width=800)
txt.pack(side="bottom")

ameba = Button(main_cw, width=800, height=800, command=on_click,image=basic_ameba,)
ameba.pack(side="left",anchor="nw")

boost = Canvas(main_cw)
boost.pack(anchor="e",side="top")
boost.create_rectangle(0,0,1000,400,  fill="green")

boost1 = Canvas(main_cw)
boost1.pack(anchor="e",side="top")
boost1.create_rectangle(0,0,1000,400,  fill="red")



autoclick_upgrade = Button(boost, text="upgrade autoclick: "+str(coast0), command=upgrade_autoclick)
autoclick_upgrade.pack(side="top", anchor="s",pady=10,padx=5)

click_upgrade = Button(boost, text="upgrade click: "+str(coast0), command=upgrade_click)
click_upgrade.pack(side="top", anchor="s",pady=10,padx=5)

rebith = Button(boost1, text="upgrade ameba: "+str(coast1), command=do_ameba)
rebith.pack(side="top", anchor="s",pady=10,padx=5)
rebcoast = 100
def auto_thr():
	global ameba
	while True:
		time.sleep(0.5)
		if auto>1:
			bg1=pygame.mixer.Sound("assets/click.mp3")
			bg1.set_volume(0.3)
			bg1.play(loops=0)
		global clicks
		clicks=clicks+(auto-1)
		global autoclick_upgrade
		global click_upgrade
		global coast0
		global rebcoast
		rebith.config(text = "upgrade ameba: "+str(rebcoast))
		click_upgrade.config(text="upgrade click: "+str(coast0))
		autoclick_upgrade.config(text="upgrade autoclick: "+str(coast0))
		txt.delete(0,END)
		txt.insert(0, "clicks: "+str(clicks)+" lvl: "+str(lvl)+ " scores: "+ str(scores)+" click m/p: "+str(multy))

musica=thr.Thread(target=music)
auto_tthr=thr.Thread(target=auto_thr)
usiska = thr.Thread(target=usos)
auto_tthr.start()
usiska.start()
musica.start()

root.mainloop()