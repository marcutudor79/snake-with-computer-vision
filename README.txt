Adougare modul: -hand_tracking
		-mainEx.py - exemplu de folosire

Dependete(pentru functionare are nevoie de urmatoarele librarii):
	-opencv-python
	-cvzone
	-mediapipe

Functionalitati:

Contine clasa CvHand cu:
-metoda current_hand_side() care returneaza:
	-o litera din: {w, s, a, d}
	-frame-ul se imparte in 4 triunghiuri  \/ , fiecare triunghi corespunzand unei parti: 
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
