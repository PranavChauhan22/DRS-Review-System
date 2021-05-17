import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import imutils
import threading
import time
stream=cv2.VideoCapture("MyDRS.mp4")
def play(speed):
    print(f"The speed is {speed}")
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,anchor=tkinter.NW,image=frame)
def pending(decision):
    frame=cv2.cvtColor(cv2.imread("DecisionPending.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    canvas.image=frame
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0,0,anchor=tkinter.NW,image=frame)

    time.sleep(3)
    frame=cv2.cvtColor(cv2.imread("IPL-Logo.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    canvas.image=frame
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0,0,anchor=tkinter.NW,image=frame)

    time.sleep(3)
    if decision == 'out':
        decisionImg = "OUT.png"
    else:
        decisionImg = "NOTOUT.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,anchor=tkinter.NW, image=frame)
def Out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("Player is OUT!")
def NotOut():
    thread=threading.Thread(target=pending,args=("notout",))
    thread.daemon=1
    thread.start()
    print("Player is NOT OUT!")



SET_WIDTH=368
SET_HEIGHT=550
window=tkinter.Tk()
cvimg=cv2.cvtColor(cv2.imread("head.png"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
# frame=imutils.resize(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cvimg))
image_on_canvas=canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas.pack()
bt1=tkinter.Button(window,text="<<Previous Fast",command=partial(play,-25))
bt1.pack(ipadx=10,ipady=3,padx=10,pady=8)
bt2=tkinter.Button(window,text="<<Previous Slow",command=partial(play,-2))
bt2.pack(ipadx=10,ipady=3,padx=10,pady=8)
bt3=tkinter.Button(window,text="Forward Fast>>",command=partial(play,10))
bt3.pack(ipadx=10,ipady=3,padx=10,pady=8)
bt4=tkinter.Button(window,text="Forward Slow>>",command=partial(play,2))
bt4.pack(ipadx=10,ipady=3,padx=10,pady=8)
bt5=tkinter.Button(window,text="Give OUT!",command=Out)
bt5.pack(ipadx=10,ipady=3,padx=10,pady=8)
bt6=tkinter.Button(window,text="Give NOT OUT!",command=NotOut)
bt6.pack(ipadx=10,ipady=3,padx=10,pady=8)
window.mainloop()

