# Snake_with_handtracking

## Perequisites:

- Python 3.8 or higher

For windows users:
[get python from here](https://www.python.org/downloads/)  
>add both python and pip to path  

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
#terminal commands that work in windows powershell
pip install opencv-python
pip install cvzone
pip install mediapipe
pip install pygame
```

## How we made it


The handtraking module:
Adaugare modul: -hand_tracking
		-mainEx.py - exemplu de folosire

Dependete(pentru functionare are nevoie de urmatoarele librarii):
	-opencv-python
	-cvzone
	-mediapipe
	-time(Update 1)

Functionalitati:

Contine clasa CvHand cu:
-metoda current_hand_side() care returneaza:
	-o litera din: {w, s, a, d}
	-frame-ul se imparte in 4 triunghiuri \/ , fiecare triunghi corespunzand unei parti: 
					       /\
		Up -> w
		Down -> s
		Left -> a
		Right -> d
	
	-daca nu se gaseste o mana in frame, se returneaza partea anterioara in care era mana 

-variablia flip se poate seta pe True pentru a face mirror frame-urilor(stanga devine dreapta si vice versa),
 folositor pentru unele camere.
 Recomand implementarea unei optiuni pentru a putea face flip frame-urilor

-functia release_capture() care trebuie apelata la sfarsitul programului, sau dupa ce nu mai avem nevoie de
 functionalitatea clasei CvHand

note:
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
  








