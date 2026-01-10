import cv2

cam = cv2.VideoCapture(0)

check, rec = cam.read()

if not check:
    print("kamera başlatılamadı")
    exit()

def bos():
    pass

cv2.namedWindow("HSV_Pencere")
cv2.resizeWindow("HSV_Pencere",700,230)

cv2.createTrackbar("H_min", "HSV_Pencere", 0, 179, bos)
cv2.createTrackbar("H_max", "HSV_Pencere", 179, 179, bos)
cv2.createTrackbar("S_min", "HSV_Pencere", 0, 255, bos)
cv2.createTrackbar("S_max", "HSV_Pencere", 255, 255, bos)
cv2.createTrackbar("V_min", "HSV_Pencere", 0, 255, bos)
cv2.createTrackbar("V_max", "HSV_Pencere", 255, 255, bos)

while True:

    check, rec = cam.read()

    rec = cv2.resize(rec, (640,480))

    hsv_rec = cv2.cvtColor(rec,cv2.COLOR_BGR2HSV )

    h_min = cv2.getTrackbarPos("H_min", "HSV_Pencere")
    h_max = cv2.getTrackbarPos("H_max", "HSV_Pencere")
    s_min = cv2.getTrackbarPos("S_min", "HSV_Pencere")
    s_max = cv2.getTrackbarPos("S_max", "HSV_Pencere")
    v_min = cv2.getTrackbarPos("V_min", "HSV_Pencere")
    v_max = cv2.getTrackbarPos("V_max", "HSV_Pencere")

    min_sinir = (h_min, s_min, v_min)
    max_sinir = (h_max, s_max, v_max)

    filtreli = cv2.inRange(hsv_rec, min_sinir, max_sinir)

    cv2.imshow("kayit", rec)
    cv2.imshow("filtreli", filtreli)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break



cam.release()

cv2.destroyAllWindows()
