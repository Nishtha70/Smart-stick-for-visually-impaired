# Smart-stick-for-visually-impaired

Sensors used:
1. Ultrasonic Sensor (HC-SR04)
2. Accelerometer (ADXL250)
3. Logitech web camera
4. Neo 6M GPS Module
5. Button

Output Through:
1. Buzzer
2. SMS sent to relative/friend using Twilio
3. Earphones

Working
1. Ultrasonic sensor keeps track of the distance between the object and the blind person.
2. If the distance is less than 100cm, the object name (identified through a pre-trained OpenCV model) and object distance (calculated using an ultrasonic sensor) are provided to the blind man as audio output from the earphones(done using python pyttsx3 library). This helps to avoid the collision of blind man with objects while walking and ensure his safety. The code of opencv implementation of identifying objects through OpenCV and working of the camera is in the qq.py folder.
3. In case, the blind man drops the stick or meets an accident, the buzzer starts producing a sound. The code logic is: accelerometer keeps check of the orientation of the stick. As soon as its orientation is detected as falling, the buzzer starts. Along with a buzzer, a message is sent to the blind man's relative or friend about the person being in an emergency containing the person's location (latitude and longitude values obtained using a GPS module). The message is sent using The Twilio Python Helper Library which acts as an interface between Twilio API and Python program to deliver the sms. In case, the blind person is safe and only the stick slipped from his hand, sound from the buzzer module will also help the blind person to locate the stick. The blind person, if safe, could press the button on the stick. The pressing button would again send a message to the relative/friend that the person is safe, only the stick has accidentally slipped from his hand, and help is not really needed. 

Code Files:
1. ultrasonic.py: main execution file, contains working of ultrasonic sensor and imports other files to meet the required functionality of the device.
2. executable.py: controls working of camera and implementation of opencv for object detection
3. orientation.py: controls working of the accelerometer and conditional statement on when buzzer should ring.
4. buzzerf.py: controls working of buzzer and control of button and sending sms through twilio.
5. gps.py: contains code to read latitude and longitude values from the gps module.
