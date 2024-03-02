from tkinter import *
import tkinter.font as font
import random

player_score=0
comp_score=0
options=[("rock",0),("paper",1),("scissor",2)]

def player_choice(player_input):
    global player_score,comp_score

    comp_input=get_comp_choice()
    player_choice_label.config(text="Your Selected :"+player_input[0])
    comp_choice_label.config(text="Computer Selected :"+comp_input[0])

    if(player_input==comp_input):
        winner_label.config(text="Tie")
    elif((player_input[1]-comp_input[1])%3==1):
        player_score+=1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text="your score: "+str(player_score))
    else:
        comp_score+=1 
        winner_label.config(text="Computer Won!!!")
        comp_score_label.config(text='Your Score :'+str(comp_score))

def get_comp_choice():
    return random.choice(options)
               
game_window=Tk()
game_window.title("ROCK PAPER SCISSOR GAME")

app_font=font.Font(size=13)

#display game title
game_title=Label(text='Rock Paper Scissor',font=font.Font(size=20),fg="red")
game_title.pack()

winner_label=Label(text="Let's Start the Game...",fg='green',font=font.Font(size=13),pady=8)
winner_label.pack()

input_frame=Frame(game_window)
input_frame.pack()


#displaying player option
player_option=Label(input_frame,text="Your Option : ",font=app_font,fg='blue')
player_option.grid(row=2,column=1,padx=8,pady=8)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 2, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'yellow', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 2, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 2, column = 3, padx = 8, pady = 5)

#Displaying Score and players choise
score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'blue')
score_label.grid(row = 3, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected :--', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score :-', font = app_font)
player_score_label.grid(row = 3, column = 3, pady = 5)

comp_choice_label = Label(input_frame, text = 'Computer Selected :--', font = app_font, fg = 'black')
comp_choice_label.grid(row = 4, column = 1, pady = 5)

comp_score_label = Label(input_frame, text = 'Computer Score :-', font = app_font, fg = 'black')
comp_score_label.grid(row = 4, column = 3,  pady = 5)

game_window.geometry('800x400')
game_window.mainloop()