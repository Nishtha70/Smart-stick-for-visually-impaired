import cv2
import pyttsx3
import time


def start(distance):
        #Import the Open-CV extra functionalities
        classNames = []
        classFile = "/home/pi/Downloads/Object_Detection_Files/coco.names"
        with open(classFile,"rt") as f:
                classNames = f.read().rstrip("\n").split("\n")
        configPath = "/home/pi/Downloads/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        weightsPath = "/home/pi/Downloads/Object_Detection_Files/frozen_inference_graph.pb"
        net = cv2.dnn_DetectionModel(weightsPath,configPath)
        net.setInputSize(320,320)
        net.setInputScale(1.0/ 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        print("working")
#Below determines the size of the live feed window that will be displayed on the Raspberry Pi OS
        cap = cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)
        #cap.set(10,70)
        x = "ab"
        n=1
#Below is the never ending loop that determines what will happen when an object is identified.    
        while n==1:
            success, img = cap.read()
            thres = 0.45
            nms = 0.2
            objects = []
            classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
         #Below has been commented out, if you want to print each sighting of an object to the console you can uncomment below
            #print(classIds,bbox)
            if len(objects) == 0: objects = classNames
            objectInfo =[]
            if len(classIds) != 0:
                for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                    className = classNames[classId - 1]
                    if className in objects:
                        objectInfo.append(className)
                        if (True):
                            cv2.rectangle(img,box,color=(0,255,0),thickness=2)

                            cv2.putText(img,classNames[classId-1].upper(),(box[0]-10,box[1]-30),
                                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                            cv2.putText(img,str(round(confidence*100,2)),(box[0]-200,box[1]-30),
                                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                            engine = pyttsx3.init()
                            engine.say(classNames[classId-1]) 
                            engine.say(distance, "cm") 
                            engine.runAndWait()
                            n=0
                        
#Below provides a huge amount of controll. the 0.45 number is the threshold number, the 0.2 number is the nms number)
        #result, objectInfo = getObjects(img,0.45,0.2)
        #print(objectInfo)
            cv2.imshow("Output",img)
            cv2.waitKey(1)
            time.sleep(1)  
