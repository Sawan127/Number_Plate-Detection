# Project to detect the Number Plate from the videos and take the screenshot of the detected number plate.
import cv2

# Open the video file
cap = cv2.VideoCapture(r"E:\Opencv\Project 1\Videos\demo.mp4")

# Load the Haar Cascade for number plate detection
NumberPlateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Initialize a counter to save screenshots with unique names
count = 0

while True:
    ret, frame = cap.read()
    # Resize the frame
    frame = cv2.resize(frame, (640,480))
    if ret:
        print("Frame shape", frame.shape)
        
        # Convert the frame to grayscale
        frame_gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # cascade classifier to detect number plates
        number_plates = NumberPlateCascade.detectMultiScale(frame_gray, 1.1, 10)
        # Draw the bounding boxes around the detected number plates
        for (x, y, w, h) in number_plates:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Put the text on the top of the bounding box
            cv2.putText(frame, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Extract the region of interest (ROI) containing the number plate
            frameROI = frame[y:y+h, x:x+w]
        cv2.imshow("Frame ROI", frameROI)
        cv2.imshow("Output Video", frame)
        if cv2.waitKey(10) & 0xFF == ord('1'):
            # if user pressed 1 then region of the number plate will be clicked
            cv2.imwrite(r"E:\Opencv\Project 1\Number Plate Detection\Resources\Numberplate\NoPlate_"+str(count)+".jpg", frameROI)
            cv2.rectangle(frame, (0,200), (640,300), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, "Number Plate Saved", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Output Video", frame)
            cv2.waitKey(500)
            count += 1
        # break the loop if user pressed 'q'
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break