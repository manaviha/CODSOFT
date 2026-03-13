import random
from tkinter import *
user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    user_label.config(text="You chose: " + user_choice)
    computer_label.config(text="Computer chose: " + computer_choice)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score}  Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score → You: 0  Computer: 0")
    result_label.config(text="")
    user_label.config(text="")
    computer_label.config(text="")
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
title = Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title.pack(pady=10)
instruction = Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))
instruction.pack()
frame = Frame(root)
frame.pack(pady=15)
Button(frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
Button(frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
Button(frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)
user_label = Label(root, text="", font=("Arial", 12))
user_label.pack()
computer_label = Label(root, text="", font=("Arial", 12))
computer_label.pack()
result_label = Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)
score_label = Label(root, text="Score → You: 0  Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)
Button(root, text="Reset Game", command=reset_game).pack(pady=10)
root.mainloop()