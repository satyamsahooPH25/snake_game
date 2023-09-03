import pygame as pi
import cv2 as cv
import numpy as np
import random
from cvzone.HandTrackingModule import HandDetector
import time
detector = HandDetector(detectionCon=0.8,maxHands=1)
frameheight=1280
framewidth=1280
cap = cv.VideoCapture(0)
cap.set(3,frameheight)
cap.set(4,frameheight)
def empty(a):
    pass
import random
clock=pi.time.Clock()
pi.init()
sc=pi.display.set_mode((1280,720))
head=[0,0];
X=0;Y=0;
rx=random.randint(0,1280)
ry=random.randint(0,720)
r=[rx,ry]
food=pi.image.load(r"C:\Users\satya\Downloads\apple (1).png")
rect=food.get_rect()
rectnew=pi.Rect(head[0],head[1],50,50)
right=pi.Rect(1180,150,100,400)
left=pi.Rect(0,150,100,400)
up=pi.Rect(420,0,400,100)
down=pi.Rect(420,620,400,100)
starttime=time.time()
Total=48
score=-10
fps=30
while True:
    remaintime=time.time()-starttime
    remaintime=Total-int(remaintime)
    if remaintime>45 and remaintime<48:
            sc.fill((255,255,255))
            font=pi.font.Font(None,250)
            text=font.render('Snake.io!',True,(250,50,50))
            sc.blit(text,(240,260))
    elif remaintime<=45 and remaintime>1:
    
        rectnew.x=head[0]-24
        rectnew.y=head[1]-24
        pi.draw.rect(sc,(255,0,0),rectnew)
        pi.draw.rect(sc,(255,0,0),rect)
        success,img=cap.read()
        img=cv.flip(img,1)
        hands,img = detector.findHands(img,flipType=False)
        img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        img=np.rot90(img)
        frame=pi.surfarray.make_surface(img);
        frame = pi.transform.flip(frame,True,False)
        sc.blit(frame,(0,0))
        pi.draw.rect(sc,(255,0,0),right,10,30)
        pi.draw.rect(sc,(0,255,0),left,10,30)
        pi.draw.rect(sc,(255,255,255),up,10,30)
        pi.draw.rect(sc,(0,0,255),down,10,30)
        sc.blit(food,rect)
    #print(ballset)
    #print(prev[0])
        snake=pi.draw.circle(sc,(255,255,0),head,24);
        prev=head.copy()
        if pi.Rect.colliderect(rect,rectnew):
            r.clear();
            score+=10
            rect.x=random.randint(0,1000)
            rect.y=random.randint(0,600)
        pi.display.flip()
        if hands:
        
            hand=hands[0]
            #print(hand)
            x, y,z=hand['lmList'][8]
            if up.collidepoint(x, y):
                Y=-10.4;X=0
            elif down.collidepoint(x, y):
                Y=10.4;X=0
            elif left.collidepoint(x, y):
                X=-10.4;Y=0
            elif right.collidepoint(x, y):
                X=10.4;Y=0

        if head[0]>1280:head[0]=0;
        if head[0]<0:head[0]=1280;
        if head[1]>720:head[1]=0;
        if head[1]<0:head[1]=720;
        head[0]+=X;
        head[1]+=Y;
        font=pi.font.Font(None,50)
        textScore=font.render(f'score:{score}',True,(250,50,50))
        sc.blit(textScore,(35,35))
        texttime=font.render(f'Time:{remaintime}',True,(250,50,50))
        sc.blit(texttime,(1000,35))
           
    elif remaintime<=1:
        sc.fill((255,255,255))
        font=pi.font.Font(None,150)
        textScore=font.render(f'score:{score}',True,(250,50,50))
        sc.blit(textScore,(450,410))
        font=pi.font.Font(None,250)
        text=font.render('TimeUP!',True,(250,50,50))
        sc.blit(text,(330,260))
    for event in pi.event.get():
        if event.type== pi.QUIT:
             start=False
             pi.quit()
    
    pi.display.update()
    clock.tick(fps)
    
    

