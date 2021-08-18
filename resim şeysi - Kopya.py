import cv2, time ,pandas
from datetime import datetime
back=None
mlist=[None,None]
time=[]
df=pandas.DataFrame(columns=["Start","End"])
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    motion=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if back is None:
        back=gray
        continue
    diff_frame=cv2.absdiff(back,gray)
    thresh_frame=cv2.threshold(diff_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    cnts,_=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour)<10000:
            continue
        motion=1
        (x,y,v,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+v,y+h),(0,255,0),3)
        
    mlist.append(motion)
    mlist=mlist[-2:]
    if mlist[-1]==1 and mlist[-2]==0:
        time.append(datetime.now())
    if mlist[-1]==0 and mlist[-2]==1:
        time.append(datetime.now())
    cv2.imshow("Gri görüntü",gray)
    cv2.imshow("aradaki fark ",diff_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("renkli görüntü",frame)
    key=cv2.waitKey(1)
    if key ==ord("q"):
        if motion ==1:
            time.append(datetime.now())
        break
for i in range(0,len(time),2):
    df=df.append({"Start":time[1],"End":time[i+1]},ignore_index=True)
df.to_csv("Time_of_movements.csv")
video.releade()
cv2.destroyAllWindows()
    
    
    