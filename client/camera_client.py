#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Product     : Raspberry PiCar-B
# File name   : camera_test.py
# Description : testing the webcam in tkinter
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : Thomas Fojan
# Date        : 2019/11/10
import tkinter as tk
import cv2
from PIL import Image, ImageTk

width, height = 100, 75
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()
