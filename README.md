# Snake_with_handtracking


## Summary: 

We want to **bring back an old game**, the snake game, **by implementing new innovative ways** to move the snake with **augmented computer vision.**
  
![image](https://user-images.githubusercontent.com/62753923/147962344-9e2ce3a8-53e2-48b3-b6fd-f00d7b9f7d90.png)  

The name of the window is a joke related to the fact that maybe in the "Metaverse", people will be able to move snakes with their hands

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

Install with **pip**:
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
After installing all the perequisites you should be able to run the game using:
```
python snake.py
```  
or
```
python3 snake.py
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

> The module was written and tested using PyCharm Community Edition 2021.3 with Python 3.10.1  

**Common warning for Windows:**

>[ WARN:0] global C:\...\opencv-python\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (438)  
`anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback  

---
Updates and realeases:  

**Update 1:**  
- Suggestive renaming of the variables 
- Added a function fps_counter(), which returns the framerate of the processed camera feed
- Camera feed resolution was set to 640x480 in order to increase performance   

**Update 2:**
- Camera feed resolution was set to 1280x720 in order to easen the control of the snake
- Added a function which returns the camera feed

## The game:
Dependencies:
- pygame  

This game was written using python using the pygame module  
It is the oldschool snake game in which the player needs to increase the length of the snake by eating apples up to a certain length  

---
## Our view:  

We wanted to bring this game back to life by changing the way you move the snake  
In this game, the player needs to eat 10 apples in order to win, but the snake will move only using the handtracking module

**You cannot use the keyboard to move the snake**  

Updated and releases:  

**Update 1:**  
- Added a lose window
- Adjusted the snake's speed

**Update 2:**
- Added another block for the snake's head
- Merged the game with handtracking_module

**Update 3:**
- Fixed the fps problem that makes the snake move faster
- The of the game is based on the speed of the computer

**Update 4:**
- Made the snake's body the same color as the head





