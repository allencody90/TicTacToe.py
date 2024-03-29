import random
import time


def board():
    print('   |   |')
    row1 = (' ' + space1 + ' | ' + space2 + ' | ' + space3)
    print(row1)
    print('   |   |')
    print('-----------')
    print('   |   |')
    row2 = (' ' + space4 + ' | ' + space5 + ' | ' + space6)
    print(row2)
    print('   |   |')
    print('-----------')
    print('   |   |')
    row3 = (' ' + space7 + ' | ' + space8 + ' |  ' + space9)
    print(row3)
    print('   |   |') #This is the Tic-Tac-Toe Board 

space1 = ' '
space2 = ' '
space3 = ' '
space4 = ' '
space5 = ' '
space6 = ' '
space7 = ' '
space8 = ' '
space9 = ' ' #these are blank spaces that fill up the board until the player, or computer, assigns them a different value.


spaced1 = 0
spaced2 = 0
spaced3 = 0
spaced4 = 0
spaced5 = 0
spaced6 = 0
spaced7 = 0
spaced8 = 0
spaced9 = 0 #these are to see whether or not a space on the board has been filled in with a letter.



player = ''
computer = '' #these are blanks variables until the player decides which letter he or she wants to be, subsequently setting the computer letter as well.



one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
six = '6'
seven = '7'
eight = '8'
nine = '9' #these are the available slots left on the board. Further down the code we see that if the player of the computer has used a space, the number is replaced with a blank.

gameisover = False #this helps tell if the game has ended or not



move = random.randint(1,2)
if move == 1:
    firstmove = 'player'
else:
    firstmove = 'computer' #this tells who will go first

def ComputerAI(): #setting up the Computer AI
    global space1
    global space2
    global space3
    global space4
    global space5
    global space6
    global space7
    global space8
    global space9

    global firstmove

    global spaced1
    global spaced2
    global spaced3
    global spaced4
    global spaced5
    global spaced6
    global spaced7
    global spaced8
    global spaced9 #all these 'globals' tell the program that the changes made to the variables in this definition will be global changes, not local ones. example: "X" in def OK(): might equal '1', but "X" outsid the def OK(): might equal '2'. If we put in the 'global' it tells the computer that the 'local' "X" inside the def OK(): will change the 'global' "X" outside the def OK():
    
    
    
    computermove = random.randint(1,9) #tells the computer to choose between 1-9 numbers, or basically the nine spaces on the board.



    

    



    
    
    if computermove == 1:
           if spaced1 == 0: 
            if computer == 'X':
                space1 = 'X'
                spaced1 = 1
                firstmove = 'player' #this sets up the 'back and forth' between the player and the computer. because we keep recalling 'firstmove' to see whos turn it is until the board is full or somebody has won.
            else:
                space1 = 'O'
                spaced1 = 1
                firstmove = 'player'
           else:
               ComputerAI() #if the move is already taken it tells the computer to repeat itself until it finds one that is not taken.
               
    elif computermove == 2:
           if spaced2 == 0: 
            if computer == 'X':
                space2 = 'X'
                spaced2 = 1
                firstmove = 'player'
            else:
                space2 = 'O'
                spaced2 = 1
                firstmove = 'player'
           else:
               ComputerAI()
               
    elif computermove == 3:
           if spaced3 == 0: 
            if computer == 'X':
                space3 = 'X'
                spaced3 = 1
                firstmove = 'player'
            else:
                space3 = 'O'
                spaced3 = 1
                firstmove = 'player'
           else:
               ComputerAI()
               
    elif computermove == 4:
           if spaced4 == 0: 
            if computer == 'X':
                space4 = 'X'
                spaced4 = 1
                firstmove = 'player'
            else:
                space4 = 'O'
                spaced4 = 1
                firstmove = 'player'
           else:
               ComputerAI()
               
    elif computermove == 5:
           if spaced5 == 0: 
            if computer == 'X':
                space5 = 'X'
                spaced5 = 1
                firstmove = 'player'
            else:
                space5 = 'O'
                spaced5 = 1
                firstmove = 'player'
           else:
               ComputerAI()
    elif computermove == 6:
           if spaced6 == 0: 
            if computer == 'X':
                space6 = 'X'
                spaced6 = 1
                firstmove = 'player'
            else:
                space6 = 'O'
                spaced6 = 1
                firstmove = 'player'
           else:
               ComputerAI()
               
    elif computermove == 7:
           if spaced7 == 0: 
            if computer == 'X':
                space7 = 'X'
                spaced7 = 1
                firstmove = 'player'
            else:
                space7 = 'O'
                spaced7 = 1
                firstmove = 'player'
           else:
               ComputerAI()
               
    elif computermove == 8:
           if spaced8 == 0: 
            if computer == 'X':
                space8 = 'X'
                spaced8 = 1
                firstmove = 'player'
            else:
                space8 = 'O'
                spaced8 = 1
                firstmove = 'player'
           else:
               ComputerAI()
               
    elif computermove == 9:
           if spaced9 == 0: 
            if computer == 'X':
                space9 = 'X'
                spaced9 = 1
                firstmove = 'player'
            else:
                space9 = 'O'
                spaced9 = 1
                firstmove = 'player'
           else:
               ComputerAI()
               

def playermove(): #sets up the players turn

     global space1
     global space2
     global space3
     global space4
     global space5
     global space6
     global space7
     global space8
     global space9 

     global firstmove

     global spaced1
     global spaced2
     global spaced3
     global spaced4
     global spaced5
     global spaced6
     global spaced7
     global spaced8
     global spaced9

     global running
     print('Where do you want to place your move?')



        
     print(one, two, three, four, five, six, seven, eight, nine) #possible moves at the time.
     print()
     
     if player == 'O':
         print('O:') 
     else:
         print('X:') #tells player which letter they chose.
     
     where = input() #asks player where he or she would like to put there letter.
     if where == '1':
       if spaced1 == 0:
           
        if player == 'X':
            space1 = 'X'
            spaced1 = 1
            firstmove = 'computer' #This sets the "back and forth" gameplay by letting 'firstmove', which probly should have just been called move, change from computer to player.

        else:
            space1 = 'O'
            spaced1 = 1
            firstmove = 'computer'
       else:
           print('That space is already taken.') #if space is already full it repeats the code until the player chooses an empty space.
           print()

     elif where == '2':
       if spaced2 == 0: 
        if player == 'X':
            space2 = 'X'
            spaced2 = 1
            firstmove = 'computer' 
        

        else:
            space2 = 'O'
            spaced2 = 1
            firstmove = 'computer'
       else:
           print('That space is already taken.')
           print()     

     elif where == '3':
       if spaced3 == 0: 
        if player == 'X':
            space3 = 'X'
            spaced3 = 1
            firstmove = 'computer'

        else:
            space3 = 'O'
            spaced3 = 1
            firstmove = 'computer'
       else:
           print('That space is already taken.')
           print() 

     elif where == '4':
       if spaced4 == 0: 
        if player == 'X':
            space4 = 'X'
            spaced4 = 1
            firstmove = 'computer'

        else:
            space4 = 'O'
            spaced4 = 1
            firstmove = 'computer'
       else:
           print('That space is already taken.')
           print()

     elif where == '5':
       if spaced5 == 0: 
        if player == 'X':
            space5 = 'X'
            spaced5 = 1
            firstmove = 'computer'

        else:
            space5 = 'O'
            spaced5 = 1
            firstmove = 'computer'

       else:
           print('That space is already taken.')
           print() 

     elif where == '6':
       if spaced6 == 0: 
        if player == 'X':
            space6 = 'X'
            spaced6 = 1
            firstmove = 'computer'

        else:
            space6 = 'O'
            spaced6 = 1
            firstmove = 'computer'
       else:
           print('That space is already taken.')
           print() 

     elif where == '7':
       if spaced7 == 0: 
        if player == 'X':
            space7 = 'X'
            spaced7 = 1
            firstmove = 'computer'

        else:
            space7 = 'O'
            spaced7 = 1
            firstmove = 'computer'
       else:
           print('That space is already taken.')
           print() 

     elif where == '8':
       if spaced8 == 0: 
        if player == 'X':
            space8 = 'X'
            spaced8 = 1
            firstmove = 'computer'

        else:
            space8 = 'O'
            spaced8 = 1
            firstmove = 'computer'
       else:
           print('That space is already taken.')
           print() 

     elif where == '9':
       if spaced9 == 0: 
        if player == 'X':
            space9 = 'X'
            spaced9 = 1
            firstmove = 'computer'

        else:
            space9 = 'O'
            spaced9 = 1
            firstmove = 'computer'
       else:
           print('That space is already taken.')
           print() 
            
     elif where == 'quit':
        running = 0 #this was just useful for me as I wrote the code because every time the code messed up and I clicked on the 'X' at the top-right of the computer screen, it kicked me out of the whole script, not just the IDLE. Pretty damn annoying actually.
        
     else:
        print('You must decide between the spaces:')
        print(one, two, three, four, five, six, seven, eight, nine) #if player doesn't choose between the numbers 1-9, this reminder will show up.

def tie(): #lets us know if the game is a tie.
    
    global running
    global gameisover
    
    if spaced1 == 1:
        if spaced2 == 1:
            if spaced3 == 1:
                if spaced4 == 1:
                    if spaced5 == 1:
                        if spaced6 == 1:
                            if spaced7 == 1:
                                if spaced8 == 1:
                                    if spaced9 == 1:
                                       if gameisover != True: #basically says that if no one has won and the board is full, it is a tie.
                                           
                                        print('UH-OH. IT IS A TIE!')
                                        print()
                                        running = 0
                                        
                                           
                            
def gameWon(): #lets us know if someone has one.
    global running
    global gameisover

    # (1,2,3) (1,5,9) (1,4,7)........The rest of this code is basically a computers way of saying 'O' across at the top or 'X' diagonally.
    # You would not believe the pain in the ass this code was until I realized that in order for it to work I had to assign 'if' statements to each possible win, and not 'elif' statements.
    
    if space1 == 'O':
        if space2 == 'O':

        
                
                
            if space3 == 'O':
                if player == 'O':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                     
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
    if space1 == 'O':
                    
        if space5 == 'O':
            if space9 == 'O':
                if player == 'O':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True

    if space1 == 'O':
                    
        if space4 == 'O':
            if space7 == 'O':
                if player == 'O':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
                    
    
          

    
    # (3,6,9) (3,2,1) (3,5,7)      
    if space3 == 'O':
        if space6 == 'O':
            if space9 == 'O':
                if player == 'O':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
    


    if space3 == 'O':

        if space5 == 'O':
            if space7 == 'O':
                if player == 'O':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
                
           

                    
    if space7 == 'O':
        if space8 == 'O':
            if space9 == 'O':
                if player == 'O':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True

    if space2 == 'O':
        if space5 == 'O':
            if space8 == 'O':
                if player == 'O':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
         

                
    
        
   
         
    if space4 == 'O':
        if space5 == 'O':
            if space6 == 'O':
                if player == 'O':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
                
                
    #######################
    #######################
    #######################
    #######################

    #this is just a 'break' I added to seperate my 'O' wins from my 'X' wins

                    
    # (1,2,3) (1,5,9) (1,4,7)
    if space1 == 'X':
        if space2 == 'X':

        
                
                
            if space3 == 'X':
                if player == 'X':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
    if space1 == 'X':
                    
        if space5 == 'X':
            if space9 == 'X':
                if player == 'X':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
    if space1 == 'X':
                    
        if space4 == 'X':
            if space7 == 'X':
                if player == 'X':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
                    
    
          

    
    # (3,6,9) (3,2,1) (3,5,7)      
    if space3 == 'X':
        if space6 == 'X':
            if space9 == 'X':
                if player == 'X':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
    

    if space3 == 'X':

        if space5 == 'X':
            if space7 == 'X':
                if player == 'X':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
                
           

                    
    if space7 == 'X':
        if space8 == 'X':
            if space9 == 'X':
                if player == 'X':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True

    if space2 == 'X':
        if space5 == 'X':
            if space8 == 'X':
                if player == 'X':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True
         

                
    
        
   
         
    if space4 == 'X':
        if space5 == 'X':
            if space6 == 'X':
                if player == 'X':
                    print('CONGRATULATIONS! YOU HAVE WON!!!')
                    print()
                    running = 0
                    gameisover = True
                    board()
                    
                    

                else:
                    print('UH-OH. THE COMPUTER HAS WON!')
                    print()
                    running = 0
                    gameisover = True


                    
    



            
def start(): #lets the player choose a letter.
    
    global player
    global computer
    global spaced1
    global spaced2
    global spaced3
    global spaced4
    global spaced5
    global spaced6
    global spaced7
    global spaced8
    global spaced9
    global numbers
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    
    
        
    
    print('Which letter do you want to be? "X" or "O"')
    which = input().upper() #gets input from the player. also, the upper() means that if the player types in a 'x' (lowercase 'x'), the code will recognize it as a 'X' (capital 'X')
    
    if which == 'X': 
        player = 'X'
        computer = 'O' #if player chooses 'X', computer is 'O'
        
    elif which == 'O':
        player = 'O'
        computer = 'X' #if player chooses 'O', computer is 'X'
    else:
        print('You must pick between "X" or "O"')
        start()
        print()
        print() #if 'which' wasn't "X" or "O" this tells it to repeat itself until the player chooses correctly.

print('Hello & Welcome To Cody Allens Tic Tac Toe')
print('Beware of the computer!!')
print('')
print()
print() #sets up the introduction



start() #runs the def start()
running = 1 #sets up the 'while' loop




print()
board()

while running == 1: #the 'while' loop
  
    if spaced1 == 1:
        one = ''
    if spaced2 == 1:
        two = ''
    if spaced3 == 1:
        three = ''
    if spaced4 == 1:
        four = ''
    if spaced5 == 1:
        five = ''
    if spaced6 == 1:
        six = ''
    if spaced7 == 1:
        seven = ''
    if spaced8 == 1:
        eight = ''
    if spaced9 == 1:
        nine = '' #this adds blank spaces to the possible lists of move whenever the player or computer has used a space on the board. Lets you know what spaces are left.
        
    
    
    
    
    if firstmove == 'player': #if 'firstmove' is  equal to 'player', then it is the players turn. And after the player has made an appropriate move, it makes 'firstmove' equal 'computer'. So then, it is the computers turn.
        playermove() #runs the def playermove()
        board()
        
        
        print()
        print()
        gameWon() #checks to see if anyone has won
        tie() #checks to see if it is a tie
        

    elif firstmove == 'computer':
        
        
        #START OF AREA: if you were to erase this function you would erase from the START OF AREA: to the END OF AREA.        
        print('IT IS THE COMPUTERS TURN')
        print('...')
        time.sleep(.7)
        print('...')
        time.sleep(1)
    
        print('THE COMPUTER IS THINKING...')
        randomtime = random.randint(1,2)
        time.sleep(randomtime) #this is just a little set-up to give the computer AI more depth and the game more feel, or some kinda bs. Without it the computer chooses a response is less than a second. If you don't like it just erase it. It won't mess up the game.
        #END OF AREA: stop erasing here.


        
        ComputerAI()
        board() #prints out the board so the player can see where the computer has moved
        print()
        print()
        print()
        print()
        gameWon() 
        tie()

        #code will run until someone wins, it is a tie, or if the player types in 'quit'.
        


        


     

            
            
                
           

            

    
