
# Basic Rock Paper Scissors Game
# Name: Timothy Moisio
# Date: 2/13/2026

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

# Implement this function to get and validate the user's choice.
def get_user_choice():
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	while True:
		user_input = console.input("[bold]Choose rock (1), paper (2), or scissors (3): [/bold]").strip().lower()
		if user_input in num_to_choice:
			user_choice = num_to_choice[user_input]
		else:
			user_choice = user_input
		if user_choice in choices:
			break
		else:
			console.print("[red]Invalid choice. Please try again.[/red]")
	return user_choice

#Implement this function to randomly select the computer's choice.
def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	computer_choice = random.choice(choices)
	console.print(f"[magenta]Computer chose: {computer_choice}[/magenta]")
	return computer_choice

#Implement this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	if user_choice == computer_choice:
		return "tie"
	elif (
		(user_choice == 'rock' and computer_choice == 'scissors') or
		(user_choice == 'paper' and computer_choice == 'rock') or
		(user_choice == 'scissors' and computer_choice == 'paper')
	):
		return 'user'
	else:
		return 'computer'

#Implement this function to print the round result with color.
def print_round_result(user_choice, computer_choice, winner):
	"""Print the choices and the winner of the round using rich colors."""
	print(f"User picked: {user_choice}\nComputer picked: {computer_choice}")
	match winner: # compares winner to the only 3 values it should be
		case "computer":
			console.print("[bold red]Computer wins this round![/bold red]")
		case "user":
			console.print("[bold green]You win this round![/bold green]")
		case "tie":
			console.print("[blue]It's a tie![/blue]")

#Implement the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		#Get user and computer choices
		user_input, computer_input = get_user_choice(), get_computer_choice()
		#Determine winner
		winner = determine_winner(user_input, computer_input)
		#Print round result
		print_round_result(user_input, computer_input, winner)
		match winner:
			case 'user':
				user_score += 1
			case 'computer':
				computer_score += 1
		#Update scores
		pass
	# Game summary
	console.print("\n[bold underline]Game Over![/bold underline]")
	console.print(f"[cyan]Your score: {user_score}[/cyan]")
	console.print(f"[magenta]Computer score: {computer_score}[/magenta]")
	# Announce overall winner
	if user_score > computer_score:
		console.print("[bold green]Congratulations, you win the game![/bold green]")
	elif user_score < computer_score:
		console.print("[bold red]Sorry, the computer wins the game.[/bold red]")
	else:
		console.print("[yellow]It's a tie game![/yellow]")
	pass

if __name__ == "__main__":
	main()
