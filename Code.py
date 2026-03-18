import tkinter as tk
from tkinter import messagebox, simpledialog
import random
WinningSCORE=0 

Names=[
    "It's TTTIIIIMMMEEE!!!!✨","Banana","Cat","HAHAHAHHA","Tree","HO HO HO!","TRALALALALALALALA",
    "DUN DUN DUUUUNNNN!!!!!","Hat","GOOSE","Random","THaannnnnnnnnnkkkkkkkksssssss",
    "THIS IS UR NAME","CHA! CHA! CHA!","NO!","Skateboard","BEST NAME EVER RIGHT",
    "?????REALLY?????","WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA","DUNKIN DONUTS"
]

Player1=""
Player2=""

def Introduction():
    global WinningSCORE, Player1, Player2
    Player1=random.choice(Names)
    Player2=random.choice(Names)
    while Player1==Player2:
        Player2=random.choice(Names)

    Thisisthefirstplayer1=simpledialog.askstring("Welcome to Tic Tac ToEs","I cordially invite you to represent your name!")
    if not Thisisthefirstplayer1:
        Thisisthefirstplayer1=simpledialog.askstring("EROOORRRR!!!!!!!","YOU HAVE TO ENTER A NAME")
    else:
        messagebox.showinfo(f"{Thisisthefirstplayer1}",f"THat dosen't really matter! You're nickname is {Player1}")

    SECOND=simpledialog.askstring("Welcome to Tic Tac ToEs","I cordially invite you to represent your name!")
    if not SECOND:
        SECOND=simpledialog.askstring("EROOORRRR!!!!!!!","YOU HAVE TO ENTER A NAME")
    else:
        messagebox.showinfo(f"{SECOND}",f"THat dosen't really matter! You're nickname is {Player2}")

    Max_Games1=simpledialog.askinteger(f"MaXimum Games!!","How many games would you like to play against your opponent?")
    Max_Games2=simpledialog.askinteger(f"MaXimum Games!!","How many games would YOU like to play against your opponent?")
    BestOF=(Max_Games1+Max_Games2)//2

    while not BestOF or BestOF<=0:
        Max_Games1=simpledialog.askinteger("Retry!!","I ALREADY ASKED YOU ONCE!!!! NOW DONT MAKE ME ASK YOU AGAIN!!!!!")
        Max_Games2=simpledialog.askinteger("Retry!!","ANSWER!!! AAAAHHHHHH! THIS INSTANT!!!!")
        BestOF=(Max_Games1+Max_Games2)//2

    WinningSCORE=(BestOF//2)+1

    messagebox.showinfo("INSTRUCTIONS",f"The total number of rounds will be {BestOF}\n First to reach {WinningSCORE} Wins Is THe Tic Tac Toe Champion!!")
    messagebox.showinfo("NEW ALERT🚨⚠️","wINNER EARNS $100,000,000,000,000,000,000!!!! THIS IS TOTALLY NOT A SCAM🙃")
Introduction()
Board=[""]*9
Player="X"
Score={"X":0,"O":0}
Round_over=False

def check_winner():
    Win_Combinations=[
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (2,4,6),(0,4,8)
    ]
    for A,B,C in Win_Combinations:
        if Board[A]==Board[B]==Board[C]!="" :
            return Board[A]
    if "" not in Board:
        return "draw"
    return None

def reset_game():
    global Board,Player,Round_over, Score
    Board=[""]*9
    Round_over=False
    Player="X"
    for i in Buttons:
        i.config(text="")

def new_game(): 
    global Score 
    Score={"X":0,"O":0}
    Score_label.config(text=f"x:{Score["X"]}         O:{Score["O"]}")
    Introduction()

def on_click(i):
    global Player,Round_over, WinningSCORE, Player1, Player2 
    if Board[i]=="" and not Round_over:
        Board[i]=Player
        Buttons[i].config(text=Player)
        result=check_winner()
        if result:
            Round_over=True

            if result=="draw":
                messagebox.showinfo("Tic Tac Toe","IT IS A DRAW😀😀😀😀👏")
            else:
                if result=="X":
                    winner=f"X ({Player1})"
                else:
                    winner=f"O({Player2})"

                messagebox.showinfo("Winner",f"The Winner is {winner}!!!")
                Score[result]+=1

                if Score[result]>=WinningSCORE:
                    messagebox.showinfo("Champion",f"{winner} is the CHAMPION!!!")
                    reset_game()
                    return
            Score_label.config(text=f"x:{Score["X"]}         O:{Score["O"]}")

            reset_game()
            return

        if Player=="X":
            Player="O"
        else:
            Player="X"

root=tk.Tk()
root.resizable(True,True)
root.title("Tic TAC Toe!")
root.config(bg="#e2f5f6")

Buttons=[]
for i in range(9):
    b=tk.Button(root,text="",font=("Broadway",15),width=23,height=8,command=lambda i=i:on_click(i))
    b.grid(row=i//3,column=i%3)
    Buttons.append(b)
Score_label=tk.Label(root, text="X:0         O:0", font=("Broadway", 15), width=13, height=3) 
Score_label.grid(row=3, column=1)

New_button=tk.Button(root,text="NEW Game",font=("Algerian",15),width=19,height=6,command=new_game)
New_button.grid(row=1,column=4)

Reset_button=tk.Button(root,text="RESET Game",font=("Algerian",15),width=19,height=4,command=reset_game)
Reset_button.grid(row=7,column=1)

root.mainloop()

