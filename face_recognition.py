import cv2
import numpy as np
import dlib
from math import hypot

cap = cv2.VideoCapture(0)

board = np.zeros((400,400),np.uint8)
board[:] = 255

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Python3 6/shape_predictor_68_face_landmarks.dat")

#keyboard settings
FaceBoard = np.zeros((350,350,3),np.uint8)

first_column_no=[0, 7, 14, 21, 28, 35]
second_column_no=[1, 8, 15, 22, 29, 36]
third_column_no=[2, 9, 16, 23, 30, 37]
fourth_column_no=[3, 10, 17, 24, 31, 38]
fifth_column_no=[4, 11, 18, 25, 32, 39]
sixth_column_no=[5, 12, 19, 26, 33, 40]
seventh_column_no=[6,13,20,27,34,41]

keyset= {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5:"F",6:"@",
         7:"G", 8:"H", 9:"I", 10:"J", 11:"K",12:"L", 13:"+",
         14:"M", 15:"N", 16:"O", 17:"P",18:"Q", 19:"R", 20:"*",
         21:"S", 22:"T", 23:"U",24:"V", 25:"W", 26:"X", 27:";",
         28:"Y", 29:"Z",30:"1", 31:"2", 32:"3", 33:"/", 34:"-",
         35:"4",36:"5", 37:"6", 38:"7", 39:"8", 40:"9", 41:"0",
         42:"9", 43:"0", 44:"@", 45:"<", 46:"*", 47:"+", 48:":5"
         }
def letter(letter_index,text,letter_light):

    x=0
    y=0

    #first line
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 50
        y = 0
    elif letter_index == 2:
        x = 100
        y = 0
    elif letter_index == 3:
        x = 150
        y = 0
    elif letter_index == 4:
        x = 200
        y = 0
    elif letter_index == 5:
        x = 250
        y = 0
    elif letter_index == 6:
        x = 300
        y = 0

    #second line
    elif letter_index == 7:
        x = 0
        y = 50
    elif letter_index == 8:
        x = 50
        y = 50
    elif letter_index == 9:
        x = 100
        y = 50
    elif letter_index == 10:
        x = 150
        y = 50
    elif letter_index == 11:
        x = 200
        y = 50
    elif letter_index == 12:
        x = 250
        y = 50
    elif letter_index == 13:
        x = 300
        y = 50


    #thirdline
    elif letter_index == 14:
        x = 0
        y = 100
    elif letter_index == 15:
        x = 50
        y = 100
    elif letter_index == 16:
        x = 100
        y = 100
    elif letter_index == 17:
        x = 150
        y = 100
    elif letter_index == 18:
        x = 200
        y = 100
    elif letter_index == 19:
        x = 250
        y = 100
    elif letter_index == 20:
        x = 300
        y = 100

    #third line
    elif letter_index == 21:
        x = 0
        y = 150
    elif letter_index == 22:
        x = 50
        y = 150
    elif letter_index == 23:
        x = 100
        y = 150
    elif letter_index == 24:
        x = 150
        y = 150
    elif letter_index == 25:
        x = 200
        y = 150
    elif letter_index == 26:
        x = 250
        y = 150
    elif letter_index == 27:
        x = 300
        y = 150


    #fourth line
    elif letter_index == 28:
        x = 0
        y = 200
    elif letter_index == 29:
        x = 50
        y = 200
    elif letter_index == 30:
        x = 100
        y = 200
    elif letter_index == 31:
        x = 150
        y = 200
    elif letter_index == 32:
        x = 200
        y = 200
    elif letter_index == 33:
        x = 250
        y = 200
    elif letter_index == 34:
        x = 300
        y = 200

    #fifth line
    elif letter_index == 35:
        x = 0
        y = 250
    elif letter_index == 36:
        x = 50
        y = 250
    elif letter_index == 37:
        x = 100
        y = 250
    elif letter_index == 38:
        x = 150
        y = 250
    elif letter_index == 39:
        x = 200
        y = 250
    elif letter_index == 40:
        x = 250
        y = 250
    elif letter_index == 41:
        x = 300
        y = 250

    #sixth line
    elif letter_index == 42:
        x = 0
        y = 300
    elif letter_index == 43:
        x = 50
        y = 300
    elif letter_index == 44:
        x = 100
        y = 300
    elif letter_index == 45:
        x = 150
        y = 300
    elif letter_index == 46:
        x = 200
        y = 300
    elif letter_index == 47:
        x = 250
        y = 300
    elif letter_index == 48:
        x = 300
        y = 300





    #Icon settings
    width=50
    height=50
    th=2
    if letter_light is True:
       cv2.rectangle(FaceBoard,(x+th,y+th),(x+width-th,y+height-th),(255,255,255),-1)
    else:
       cv2.rectangle(FaceBoard, (x + th, y + th), (x + width - th, y + height - th), (255, 255, 255), th)
    #Textsettings
    font=cv2.FONT_HERSHEY_DUPLEX
    font_scale=1
    font_th=1
    text_size=cv2.getTextSize(text,font,font_scale,font_th)[0]
    width_text,height_text=text_size[0],text_size[1]
    text_x=int((width-width_text)/2)+x
    text_y=int((height+height_text)/2)+y
    cv2.putText(FaceBoard,text,(text_x,text_y),font,font_scale,(0,0,255),font_th)
def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

font = cv2.FONT_HERSHEY_DUPLEX

def get_eyes_ratios(eye_points,facial_landmarks):

    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)

    centre_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    centre_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hori_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    vert_line = cv2.line(frame, centre_top, centre_bottom, (0, 255, 0), 2)

    vert_line_length = hypot((centre_top[0] - centre_bottom[0]), (centre_top[1] - centre_bottom[1]))
    hori_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))

    ratio = hori_line_length / vert_line_length
    return ratio

#counters
frames = 0
frames_count_columns = 0
frames_count_rows = 0
col_index=[]
col = 0
blink_indivijual_key = 0
blinking_frames = 0
text = ""
row = 0
col_select = False
is_blinked = False

while True:
    _,frame = cap.read()
    # frame = cv2.resize(frame,None, fx = 0.5 , fy = 0.5)
    FaceBoard[:] = (0,0,0)
    frames += 1
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # active_letter = keyset[letter_index]

    if col_select == True :
        frames_count_rows += 1

    else :
        frames_count_columns += 1

    if frames_count_columns == 10:
        col+=1
        if col==7:
            col=0
        frames_count_columns=0

    if frames_count_rows==10:
        row+=1
        if row==7:
            row=0
            col_select = False
        frames_count_rows = 0

    if col==0:
        col_index=first_column_no
    elif col ==1:
        col_index=second_column_no
    elif col==2:
        col_index=third_column_no
    elif col==3:
        col_index=fourth_column_no
    elif col==4:
        col_index=fifth_column_no
    elif col==5:
        col_index=sixth_column_no
    elif col==6:
        col_index=seventh_column_no

    if col_select == False:
        for i in range(0,42):
            if i in col_index:
               letter(i, keyset[i], True)

            else:
               letter(i, keyset[i], False)

    else:
        for i in range (0,42):
            if i == col_index[row]:
                letter(i, keyset[i], True)

            else:
                letter(i, keyset[i], False)




    faces = detector(gray)
    for face in faces:

        x,y=face.left(),face.top()
        x1,y1=face.right(),face.bottom()
        cv2.rectangle(frame, (x,y), (x1,y1),(0,255,0),2)

        landmarks = predictor(gray,face)

        #EYE BLINKING AND EYEBROW RAISING
        left_eye_ratio = get_eyes_ratios([36,37,38,39,40,41],landmarks)
        right_eye_ratio = get_eyes_ratios([42,43,44,45,46,47], landmarks)

        # print(left_eye_ratio)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        # print(blinking_ratio)
        if blinking_ratio > 4.1:
            cv2.putText(frame, "BLINKING", (50, 150), font, 1, (255, 0, 0), )
            blinking_frames += 1
            # frames -= 1
            if col_select == True:
                blink_indivijual_key+=1
                frames_count_rows-=1

            else:
                frames_count_columns-=1


        else:
            blinking_frames=0
            blink_indivijual_key=0

        if blinking_frames==10:
            col_select=True

        if blink_indivijual_key==10 and col_select==True:
            col_select=False
            text+=keyset[col_index[row]]
            blink_indivijual_key=0
            cv2.putText(board,text, (10,50), font, 1, 0, 1)
            row=0

    cv2.imshow("Frame", frame)
    cv2.imshow("FaceBoard",FaceBoard)
    cv2.imshow("Board",board)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
