'''
Description: Program that simulates a music player by reading what button was pressed and how many times to modify a playlist
Programmer: Bruno S.M.
Date: July 22, 2025
Version: 1.0
'''

PlayL=['A','B','C','D','E']     #Creating the default playlist
btns_clicked=0          #Defining the number of button presses as a constant

while True:
    b=input("Enter button number and press count(e.g., 1 3): ")     #Get button pressed
    if len(b)!=3:       #Check if input contains 3 characters
        print("Invalid input. Please enter two integers.")   #Display input error
        continue
    else:
        if not (b[0].isdigit() and b[1].isspace() and b[2].isdigit()):      #Check if there are 2 integers and a space
            print("Invalid input. Please enter two integers.")   #Display input error
            continue        
    
    if b[0]=='1':       #Check for every possible button
        if btns_clicked>=5:     #Check if buttons have already been pressed 5 times to disregard this
            print("Already clicked 5 buttons")
            continue
        else:
            for i in range(int(b[2])):   #Repeat as many times as button was pressed
                PlayL.append(PlayL[0])  #Insert first song at the end
                del(PlayL[0])           #Erase it from the beginning
                btns_clicked+=1     #Add button press
    elif b[0]=='2':
        for i in range(int(b[2])):
            PlayL.insert(0,PlayL[-1])   #Reverse of button 1, insert at beginning erase from end
            del(PlayL[-1])
            btns_clicked+=1 
    elif b[0]=='3':
        for i in range(int(b[2])):
            PlayL.insert(0,PlayL[1])    #Insert second song behind first
            del(PlayL[2])               #Remove the original second song
            btns_clicked+=1 
    elif b[0]=='5':
        for i in range(int(b[2])):
            temp=[]     #Defining an empty list to add the songs into
            for j in range(5):      #Repeat 5 times since that's the length of the playlist
                temp.append(PlayL[4-j])     #Add songs from end to start to a temporary list
            PlayL=temp              #Make the playlist equal to the temporary list
            btns_clicked+=1 
    elif b[0]=='6':
        for i in range(int(b[2])):
            PlayL.insert(0,PlayL[1])    #Same procces as button 2, insert and remove 2nd and 4th songs
            del(PlayL[2])
            PlayL.insert(2,PlayL[3])    
            del(PlayL[4])
            btns_clicked+=1     
    elif b[0]=='7':
        print("Final playlist: {}, {}, {}, {}, {}".format(PlayL[0],PlayL[1],PlayL[2],PlayL[3],PlayL[4]))   #Display resulting playlist
        break       #End loop, thus terminating the program
    else:       #All integers not between 1-7 (and 4) considered input errors
        print("Invalid input. Only buttons 1,2,3,5,6,7 work")   #Display input error
    print("Current playlist: {}, {}, {}, {}, {}".format(PlayL[0],PlayL[1],PlayL[2],PlayL[3],PlayL[4]))

