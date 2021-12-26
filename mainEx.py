# Example for using CvHand class:

import hand_tracking as ht
# Initialize

my_hand = ht.CvHand()
# Flip image - depending on camera => my_hand.flip = True
# Test1
for i in range(50):
    print("Next move(Test 1):")
    print(my_hand.current_hand_side())

my_hand2 = ht.CvHand()
# Test2
for i in range(100):
    print("Next move(Test 2):")
    print(my_hand2.current_hand_side())

#Release capture device at the end of the program
ht.release_capture()
