# Snake_with_handtracking

## Perequisites:

- Python 3.8 or higher

For windows users:
[get python from here](https://www.python.org/downloads/)  
**!!add both python and pip to path**  

For **debian based linux distros** users:
```
sudo apt update
sudo apt upgrade
sudo apt install python3.8
```

installed with **pip**:
- opencv-python
- cvzone
- mediapipe
- pygame
```
pip install opencv-python
pip install cvzone
pip install mediapipe
pip install pygame
```

## How we made it


## The handtraking module:  

Dependencies:    
- opencv-python  
- cvzone  
- mediapipe  
- time (Update 1)  

Features:

Uses CvHand in order to implement:  
-method current_hand_side() which returns:
- a letter from: {w, s, a, d}  
- detects your hand through your camera which will be split in four triangles, each triangle corresponding to:   

![Untitled](https://user-images.githubusercontent.com/62753923/147959491-8d8ead72-5c2b-489e-9222-755f2515bdb9.png)

UP -> w  
DOWN -> s  
LEFT -> a  
RIGHT -> d  
	
- if no hand is detected, this method returns the previous returned value

- the flip variable can be set to True in order to mirror the frames captured via your camera (left becomes right and right becomes left)

- method **release_capture()** which must be called when the program ends or when we no longer need CvHand

> notes:
Modulul a fost scris si testat in PyCharm Community Edition 2021.3 cu Python 3.10.1
Au fost folosite cele mai noi versiuni ale tuturor librariilor
Warning comun pentru Windows:
[ WARN:0] global D:\a\opencv-python\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (438)
`anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback

Update 1:
-Redenumire mai sugestiva a unor variabile
-Adaugare functie fps_counter() care returneaza framerate-ul de procesare al videoclipului
-Setare rezolutie video la 640x480 pentru perfomanta 

+ Am adugat snake_w_handtracking-base.py pentru testare clasa CvHand cu un joc
	-frame-ul setat dinamic (+20 fps - optim)
	-pentru performanta optima modulul necesita o camera de cel putin 60 fps si o rezolutie de cel putin 640x480
	-daca va conectati cu telefonul ca webcam setati variabila flip a instantei din CvHand cu True
	 ex my_hand.flip = True
  








