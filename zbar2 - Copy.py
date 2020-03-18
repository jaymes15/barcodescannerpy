import cv2;
import numpy as np;
import pyzbar.pyzbar as pyzbar;
'''
#get qrcode image
img = cv2.imread("C:/Users/TOMI/Downloads/barcodeImage.png");

decodedObjects = pyzbar.decode(img);
print(decodedObjects);
for obj in decodedObjects:
    print("Data:", obj.data);


#show qrcode image
cv2.imshow("image", img);
cv2.waitKey(0);

'''

cap = cv2.VideoCapture(0);
font = cv2.FONT_HERSHEY_PLAIN;
while True:
    _, frame =cap.read();

    decodedObjects = pyzbar.decode(frame);
    for obj in decodedObjects:
        print("Data:", obj.data);
        cv2.putText(frame, str(obj.data), (50, 50), font, 3, (255, 0, 0), 3)

    
    cv2.imshow("Frame", frame);

    key = cv2.waitKey(1);
    if key == 27:
        break
        
