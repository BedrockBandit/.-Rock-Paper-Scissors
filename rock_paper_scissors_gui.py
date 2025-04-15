import tkinter as tk
import random

# Choices and score
choices = ["Rock", "Paper", "Scissors"]
score = {"Wins": 0, "Losses": 0, "Draws": 0}

# Main game logic
def play(player_choice):
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        result = "Draw"
        score["Draws"] += 1
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        score["Wins"] += 1
    else:
        result = "You Lose!"
        score["Losses"] += 1

    # Update GUI
    result_label.config(
        text=f"You chose {player_choice}\nComputer chose {computer_choice}\n{result}"
    )
    score_label.config(
        text=f"Wins: {score['Wins']} | Losses: {score['Losses']} | Draws: {score['Draws']}"
    )

# Tkinter setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x300")

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), pady=20)
result_label.pack()

# Score label
score_label = tk.Label(root, text="Wins: 0 | Losses: 0 | Draws: 0", font=("Arial", 12))
score_label.pack()

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Buttons
tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Exit button
tk.Button(root, text="Exit", width=10, command=root.destroy).pack(pady=10)

# Start the app
root.mainloop()
