#import the libraries
import tkinter 
import random 
  
#color list that will be appended to later
colours = ['Red','Blue','Yellow'] 

#varibles for the score, time, and level
score = 0
timeleft = 30
level = 1
  
#starts the game
def startGame(event): 
      
    if timeleft == 30: 
        countdown() 
          
    nextColor()

#changes the level and appends colors to the list
def levelChange():

    global score
    global level

    if score == 10:
        colours.append('Orange')
        colours.append('Purple')
        colours.append('Green')
        level += 1
        
    if score == 20:
        colours.append('White')
        colours.append('Black')
        colours.append('Gray')
        level += 1
    if score == 30:
        colours.append('Pink')
        colours.append('Brown')
        colours.append('Teal')
        level += 1

#function when a color changes
def nextColor(): 
  
    global score 
    global timeleft
    global level

    #if time hasn't run out...
    if timeleft > 0: 
        e.focus_set() 

        #and typed text is the same...
        if e.get().lower() == colours[1].lower(): 

            #add one to score
            score += 1

            #if score is less than 60 add three seconds
            if score < 60:
                timeleft += 3
            #if score is greater than or equal to 60 only add two
            else:
                timeleft += 2
            
            levelChange()

        #if the typed text is NOT the same, subtract two seconds and one point
        if e.get().lower() != colours[1].lower(): 

            if score > 0:
                score -= 1
                timeleft -= 2
            
        e.delete(0, tkinter.END) 

        #shuffle the colour list
        random.shuffle(colours) 

        #puts the color text on screen
        if score < 40:
            label.config(fg = str(colours[1]), text = str(colours[0]))
        else:
            label.config(fg = str(colours[1]), bg = str(colours[2]),
                         text = str(colours[0]))

        #shows score and level
        scoreLabel.config(text = "Score: " + str(score))
        levelLabel.config(text = "Level: " + str(level)) 

#counts down from 30
def countdown(): 
  
    global timeleft 
  
    if timeleft > 0: 

        timeleft -= 1
        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 

        timeLabel.after(1000, countdown) 

#makes tkinter screen
root = tkinter.Tk() 
  
root.title("colorSMASH") 

root.geometry("375x250") 

#gives instructions and makes text packs
instructions = tkinter.Label(root, text = "Type in the colour of the words,"
                             " not what the text says!", font=('Helvetica', 12)) 
instructions.pack()  

scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                      font=('Helvetica', 12)) 
scoreLabel.pack()

levelLabel = tkinter.Label(root, text = "", 
                                      font=('Helvetica', 12)) 
levelLabel.pack() 

timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12)) 
                
timeLabel.pack() 

label = tkinter.Label(root, font = ('Helvetica', 60)) 
label.pack() 

#if enter is pressed, start the game
e = tkinter.Entry(root) 
root.bind('<Return>', startGame) 
e.pack() 
e.focus_set() 

root.mainloop() 
