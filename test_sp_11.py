import os
import cv2
import RPi.GPIO as GPIO
import geocoder
from threading import Thread
from multiprocessing import Process
from time import time
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

r=GPIO.PWM(21,50)
r.start(0)
sleep(2)
r.ChangeDutyCycle(3)
sleep(2)

p=GPIO.PWM(13,50)
p.start(0)
sleep(2)
p.ChangeDutyCycle(3)
sleep(2)

q=GPIO.PWM(5,50)
q.start(0)
sleep(2)
q.ChangeDutyCycle(3)
sleep(2)

s=GPIO.PWM(27,50)
s.start(0)
sleep(2)
s.ChangeDutyCycle(3)
sleep(2)

i,j,k,l=3,3,3,3


def up(i,j,k,l):

    maximum=max(i,j,k,l)
    if maximum>10:
        maximum=10
    while not i==j==k==l:
        if i>maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i -= 0.01
        if j>maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j -= 0.01
        if k>maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k -= 0.01
        if l>maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l -= 0.01
        if i<maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i += 0.01
        if j<maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j += 0.01
        if k<maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k += 0.01
        if l<maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l += 0.01
        i,j,k,l=round(i,2),round(j,2),round(k,2),round(l,2)

    i,j,k,l =round(i*2)/2,round(j*2)/2,round(k*2)/2,round(l*2)/2
    w,x,y,z=i,j,k,l

    if w>=10 or x>=10 or y>=10 or z>=10:
        print("max speed")

    else:
        while w<i+0.5 and x<j+0.5 and y<k+0.5 and z<l+0.5:
            
            p.ChangeDutyCycle(w)
            sleep(0.05)
            w += 0.01

            q.ChangeDutyCycle(x)
            sleep(0.05)
            x += 0.01

            r.ChangeDutyCycle(y)
            sleep(0.05)
            y += 0.01

            s.ChangeDutyCycle(z)
            sleep(0.05)
            z += 0.01

    i,j,k,l=round (w*2)/2, round (x*2)/2, round (y*2)/2, round (z*2)/2

    return i,j,k,l

def down(i,j,k,l):
    
    maximum=max(i,j,k,l)
    if maximum>10:
        maximum=10
    while not i==j==k==l:
        if i>maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i -= 0.01
        if j>maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j -= 0.01
        if k>maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k -= 0.01
        if l>maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l -= 0.01
        if i<maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i += 0.01
        if j<maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j += 0.01
        if k<maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k += 0.01
        if l<maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l += 0.01
        i,j,k,l=round(i,2),round(j,2),round(k,2),round(l,2)

    i,j,k,l =round(i*2)/2,round(j*2)/2,round(k*2)/2,round(l*2)/2
    w,x,y,z=i,j,k,l

    if w<=3 or x<=3 or y<=3 or z<=3:
        print("lowest speed")

    else:
        while w>i-0.5 and x>j-0.5 and y>k-0.5 and z>l-0.5:
            
            p.ChangeDutyCycle(w)
            sleep(0.05)
            w -= 0.01

            q.ChangeDutyCycle(x)
            sleep(0.05)
            x -= 0.01

            r.ChangeDutyCycle(y)
            sleep(0.05)
            y -= 0.01

            s.ChangeDutyCycle(z)
            sleep(0.05)
            z -= 0.01

    i,j,k,l=round (w*2)/2, round (x*2)/2, round (y*2)/2, round (z*2)/2

    return i,j,k,l

def forward(i,j,k,l):
    
    maximum=max(i,j,k,l)
    if maximum>10:
        maximum=10
    while not i==j==k==l:
        if i>maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i -= 0.01
        if j>maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j -= 0.01
        if k>maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k -= 0.01
        if l>maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l -= 0.01
        if i<maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i += 0.01
        if j<maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j += 0.01
        if k<maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k += 0.01
        if l<maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l += 0.01
        i,j,k,l=round(i,2),round(j,2),round(k,2),round(l,2)

    i,j,k,l =round(i*2)/2,round(j*2)/2,round(k*2)/2,round(l*2)/2
    w,x,y,z=i,j,k,l

    while w<i+0.5 and x<j+0.5 and y>k-0.5 and z>l-0.5:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w += 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x += 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y -= 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z -= 0.01
    w,x,y,z=round(w,1),round(x,1),round(y,1),round(z,1)
    while w>i-0.5 and x>j-0.5 and y<k+0.5 and z<l+0.5:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w -= 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x -= 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y += 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z += 0.01
    
    i,j,k,l=round (w*2)/2, round (x*2)/2, round (y*2)/2, round (z*2)/2

    return i,j,k,l

def left(i,j,k,l):
    
    maximum=max(i,j,k,l)
    if maximum>10:
        maximum=10
    while not i==j==k==l:
        if i>maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i -= 0.01
        if j>maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j -= 0.01
        if k>maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k -= 0.01
        if l>maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l -= 0.01
        if i<maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i += 0.01
        if j<maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j += 0.01
        if k<maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k += 0.01
        if l<maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l += 0.01
        i,j,k,l=round(i,2),round(j,2),round(k,2),round(l,2)

    i,j,k,l =round(i*2)/2,round(j*2)/2,round(k*2)/2,round(l*2)/2
    w,x,y,z=i,j,k,l

    while w<i+0.5 and x>j-0.5 and y>k-0.5 and z<l+0.5:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w += 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x -= 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y -= 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z += 0.01
    w,x,y,z=round(w,1),round(x,1),round(y,1),round(z,1)

    while w>i-0.5 and x<j+0.5 and y<k+0.5 and z>l-0.5:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w -= 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x += 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y += 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z -= 0.01
    
    i,j,k,l=round (w*2)/2, round (x*2)/2, round (y*2)/2, round (z*2)/2

    return i,j,k,l

def backward(i,j,k,l):
    
    maximum=max(i,j,k,l)
    if maximum>10:
        maximum=10
    while not i==j==k==l:
        if i>maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i -= 0.01
        if j>maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j -= 0.01
        if k>maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k -= 0.01
        if l>maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l -= 0.01
        if i<maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i += 0.01
        if j<maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j += 0.01
        if k<maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k += 0.01
        if l<maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l += 0.01
        i,j,k,l=round(i,2),round(j,2),round(k,2),round(l,2)

    i,j,k,l =round(i*2)/2,round(j*2)/2,round(k*2)/2,round(l*2)/2
    w,x,y,z=i,j,k,l

    while w>i-0.5 and x>j-0.5 and y<k+0.5 and z<l+0.5:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w -= 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x -= 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y += 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z += 0.01
    w,x,y,z=round(w,1),round(x,1),round(y,1),round(z,1)

    while w<i+0.5 and x<j+0.5 and y>k-0.5 and z>l-0.5:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w += 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x += 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y -= 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z -= 0.01
    
    i,j,k,l=round (w*2)/2, round (x*2)/2, round (y*2)/2, round (z*2)/2

    return i,j,k,l

def right(i,j,k,l):
    
    maximum=max(i,j,k,l)
    if maximum>10:
        maximum=10
    while not i==j==k==l:
        if i>maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i -= 0.01
        if j>maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j -= 0.01
        if k>maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k -= 0.01
        if l>maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l -= 0.01
        if i<maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i += 0.01
        if j<maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j += 0.01
        if k<maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k += 0.01
        if l<maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l += 0.01
        i,j,k,l=round(i,2),round(j,2),round(k,2),round(l,2)

    i,j,k,l =round(i*2)/2,round(j*2)/2,round(k*2)/2,round(l*2)/2
    w,x,y,z=i,j,k,l

    while w>i-0.5 and x<j+0.5 and y<k+0.5 and z>l-0.5:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w -= 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x += 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y += 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z -= 0.01
    w,x,y,z=round(w,1),round(x,1),round(y,1),round(z,1)

    while w<i+0.5 and x>j-0.5 and y>k-0.5 and z<l+0.5:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w += 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x -= 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y -= 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z += 0.01
    
    i,j,k,l=round (w*2)/2, round (x*2)/2, round (y*2)/2, round (z*2)/2

    return i,j,k,l


def right_yaw(i,j,k,l):
    
    w,x,y,z=i,j,k,l

    if i>10 or j<=3 or k>10 or l<=3:
        print("highest right yaw speed.")
    else:
        while w<i+0.5 and x>j-0.5 and y<k+0.5 and z>l-0.5:
            
            p.ChangeDutyCycle(w)
            sleep(0.05)
            w += 0.01

            q.ChangeDutyCycle(x)
            sleep(0.05)
            x -= 0.01

            r.ChangeDutyCycle(y)
            sleep(0.05)
            y += 0.01

            s.ChangeDutyCycle(z)
            sleep(0.05)
            z -= 0.01

    i,j,k,l=round (w*2)/2, round (x*2)/2, round (y*2)/2, round (z*2)/2

    return i,j,k,l

def left_yaw(i,j,k,l):
    
    w,x,y,z=i,j,k,l

    if i<=3 or j>10 or k<=3 or l>10:
        print("highest left yaw speed.")
    else:
        while w>i-0.5 and x<j+0.5 and y>k-0.5 and z<l+0.5:
            
            p.ChangeDutyCycle(w)
            sleep(0.05)
            w -= 0.01

            q.ChangeDutyCycle(x)
            sleep(0.05)
            x += 0.01

            r.ChangeDutyCycle(y)
            sleep(0.05)
            y -= 0.01

            s.ChangeDutyCycle(z)
            sleep(0.05)
            z += 0.01

    i,j,k,l=round (w*2)/2, round (x*2)/2, round (y*2)/2, round (z*2)/2

    return i,j,k,l
def landing(i,j,k,l):

    maximum=max(i,j,k,l)
    if maximum>10:
        maximum=10
    while not i==j==k==l:
        if i>maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i -= 0.01
        if j>maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j -= 0.01
        if k>maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k -= 0.01
        if l>maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l -= 0.01
        if i<maximum:
            p.ChangeDutyCycle(i)
            sleep(0.05)
            i += 0.01
        if j<maximum:
            p.ChangeDutyCycle(j)
            sleep(0.05)
            j += 0.01
        if k<maximum:
            p.ChangeDutyCycle(k)
            sleep(0.05)
            k += 0.01
        if l<maximum:
            p.ChangeDutyCycle(l)
            sleep(0.05)
            l += 0.01
        i,j,k,l=round(i,2),round(j,2),round(k,2),round(l,2)

    i,j,k,l =round(i*2)/2,round(j*2)/2,round(k*2)/2,round(l*2)/2
    w,x,y,z=i,j,k,l

    while w>3 or x>3 or y>3 or z>3:
        
        p.ChangeDutyCycle(w)
        sleep(0.05)
        w -= 0.01

        q.ChangeDutyCycle(x)
        sleep(0.05)
        x -= 0.01

        r.ChangeDutyCycle(y)
        sleep(0.05)
        y -= 0.01

        s.ChangeDutyCycle(z)
        sleep(0.05)
        z -= 0.01

#---------Semi Main Code---------

def shutdown():
    p.stop()
    q.stop()
    r.stop()
    s.stop()
    GPIO.cleanup()

def video():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        
        cv2.imshow("preview", frame)
        cv2.moveWindow("preview",0,0)
        rval, frame = vc.read()
        frame = cv2.flip (frame,0)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            shutdown()
            break
            
    vc.release()
    cv2.destroyWindow("preview")

def inp():
    global start_t, choice
    choice=None
    start_t=time()
    choice=input("F/G/H/I/J/K/L/M/N : ").capitalize()

def tim(*ijkl):
    ijkl=list(ijkl)
    i=ijkl[0]
    j=ijkl[1]
    k=ijkl[2]
    l=ijkl[3]
    sec=8
    passed = time()-start_t
    if passed>sec and choice==None:
        print("Please enter input within 8 seconds. Now landing....")
        landing(i,j,k,l)
        os._exit(1)

#---------Main Code---------

need=input("please enter input according to your need-\npress 1 for free style\npress 2 for navigation\npress 3 for preset path\n")
if need==1:
    v=Process(target=video, name='video')
    v.start()

    while True:
        t1= Thread(target=inp)
        t1.start()
        sleep(9)
        t2=Thread(target=tim, args=(i,j,k,l))
        t2.start()
        
        if choice=='F':
            pass

        elif choice=='G':
            i,j,k,l=down(i,j,k,l)

        elif choice== 'H':
            i,j,k,l=up(i,j,k,l)

        elif choice=='I':
            i,j,k,l=forward(i,j,k,l)

        elif choice=='J':
            i,j,k,l=left(i,j,k,l)

        elif choice=='K':
            i,j,k,l=backward(i,j,k,l)

        elif choice =='L':
            i,j,k,l=right(i,j,k,l)

        elif choice=='M':
            i,j,k,l=right_yaw(i,j,k,l)

        elif choice=='N':
            i,j,k,l=left_yaw(i,j,k,l)
            
        else:
            landing(i,j,k,l)
            shutdown()
            break

    if v.is_alive():
        v.terminate()

elif need==2:
    des=input("please input destination latitude and longitude:")
    des= des.strip()
    if(des.find(',')):
        des_lat=des.split(',')[0]
        des_lat=float(des_lat)
        des_lng=des.split(',')[1]
        des_lng=des_lng.strip()
        des_lng=float(des_lng)
    else:
        des_lat=des.split(' ')[0]
        des_lat=float(des_lat)
        des_lng=des.split(' ')[1]
        des_lng=des_lng.strip()
        des_lng=float(des_lng)

    current= geocoder.ip('me')
    current_lat, current_lng =current.latlng
    v=Process(target=video, name='video')
    v.start()
    