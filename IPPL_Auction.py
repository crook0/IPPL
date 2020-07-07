import numpy as np 
import csv
from tkinter import *
from PIL import ImageTk,Image
import cv2 as cv
import urllib.request
import io
import requests
import webbrowser

deleted = None

i = 0

new = 0

def openweb(url):
	webbrowser.open(url,new=new)


root = Tk()  
canvas = Canvas(root, width = 700, height = 700)  
canvas.pack()  

current = []

new_file = "Round2.csv"

with open("Final_pool.csv",'r') as pool:
	file = csv.reader(pool)
	for row in file:
		current.append(row)


def write():

	with open("Final_pool.csv","w") as file:
		csvwriter = csv.writer(file)
		csvwriter.writerows(current)


def unsold():
	global current,deleted

	with open(new_file,'a') as pool:
		csvwriter = csv.writer(pool)
		csvwriter.writerow(deleted)



def display():
	global i,Btn,deleted

	canvas.delete("all")


	row = current[0]


	deleted = current.pop(0)

	write()

	name = row[1]
	role = row[5]
	basePrice = row[7]
	photo_url = row[8]

	img = ImageTk.PhotoImage(Image.open("ippl.jpeg"))  
	canvas.create_image(450, 10, anchor=NW, image=img) 

	img2 = ImageTk.PhotoImage(Image.open("iiit.jpeg"))  
	canvas.create_image(20, 10, anchor=NW, image=img2) 


	text = "Name: " + str(name)
	canvas.create_text(350,300,font = ("Helvetica",40) , text = text,anchor="center",fill="blue")

	text2 = "Base Price: " + str(basePrice)
	canvas.create_text(350,400,font = ("Helvetica",40) , text = text2,anchor="center",fill="red")

	text3 = "Role: " + str(role)
	canvas.create_text(350,500,font = ("Helvetica",40) , text = text3,anchor="center",fill="green")

	Btn = Button(canvas, text = "Open Image",command=openweb(photo_url))


	i+=1

	root.mainloop()


button = Button(root,text = "Move to Next Player" , command=display)
button.pack()

button2 = Button(root , text = "Player goes Unsold" , command = unsold)
button2.pack()

if __name__ == '__main__':
	display()
