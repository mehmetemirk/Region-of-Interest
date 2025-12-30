import cv2

cam = cv2.VideoCapture(0)
 
check, rec = cam.read()

height = rec.shape[0]
width = rec.shape[1] 
x1, y1, x2, y2 = int(width/2 +100) , int(height/2 +100) , int(width/2 -100) , int(height/2 -100)
pt1 = x1, y1
pt2 = x2, y2

while True:

    check, rec = cam.read()

    if not check:
        print("görüntü alınamadı")
        break 


    roi = rec[y2:y1, x2:x1]
    
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    bgr_gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    rec[y2:y1, x2:x1] = bgr_gray


    cv2.rectangle(rec,pt1,pt2, (255,50,50),1 )
    cv2.imshow("kamera", rec )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
