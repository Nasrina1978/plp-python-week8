"""
Personal Mini-Toolkit - Final Project PLP Python Week 8
Author: Nasro (Nasrina1978)
Description: Menu-driven program with 4 useful tools
"""

import random
import time

# This list is shared across the program for Tool 1 - it changes while running
tasks = []

# Tool 1: To-Do List Manager - uses LIST that changes, LOOP, CONDITIONAL, F-STRING
def todo_manager():
    """Manages a to-do list that user can add, view, remove tasks from."""
    print("\n--- To-Do List Manager ---")
    while True:
        print("\nTo-Do Options:")
        print("a) Add task")
        print("b) View tasks")
        print("c) Remove task")
        print("d) Back to main menu")
        choice = input("Choose (a/b/c/d): ").lower().strip()

        if choice == 'a':
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: '{task}' - You now have {len(tasks)} task(s).")
            else:
                print("Task cannot be empty!")
        elif choice == 'b':
            if not tasks:
                print("Your to-do list is empty! Add something first.")
            else:
                print("\nYour Tasks:")
                for i, t in enumerate(tasks, start=1):
                    print(f"  {i}. {t}")
        elif choice == 'c':
            if not tasks:
                print("Nothing to remove, list is empty.")
            else:
                for i, t in enumerate(tasks, start=1):
                    print(f"  {i}. {t}")
                try:
                    num = int(input("Enter number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        print(f"Removed: '{removed}'")
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == 'd':
            print("Returning to main menu...")
            break
        else:
            print("Invalid option! Please choose a, b, c, or d.")

# Tool 2: Number Guessing Game - uses LOOP and CONDITIONAL
def guessing_game():
    """Number guessing game 1-50 with hints - demonstrates loops and conditionals."""
    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 50!")
    target = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < target:
                print(f"Too low! Try higher. (Attempt {attempts})")
            elif guess > target:
                print(f"Too high! Try lower. (Attempt {attempts})")
            else:
                print(f"Correct! The number was {target}. You got it in {attempts} tries!")
                break
        except ValueError:
            print("Please enter a valid number!")

# Tool 3: Simple Calculator - uses CONDITIONAL and F-STRING
def calculator():
    """Simple calculator for +, -, *, / with friendly output."""
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif op == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif op == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif op == '/':
            if num2 == 0:
                print("Oops! Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print(f"Unknown operator '{op}'. Please use +, -, *, or /")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Tool 4: Countdown Timer - uses LOOP
def countdown_timer():
    """Counts down from user-given seconds to 0."""
    print("\n--- Countdown Timer ---")
    try:
        seconds = int(input("Enter seconds to countdown: "))
        if seconds <= 0:
            print("Please enter a positive number!")
            return
        if seconds > 30:
            print("Let's keep it 30 seconds max for demo, counting 30...")
            seconds = 30

        print(f"Starting countdown from {seconds}...")
        for i in range(seconds, 0, -1):
            print(f"  {i}...")
            time.sleep(0.5)
        print("Time's up! Ding ding ding!")
    except ValueError:
        print("Please enter a valid whole number!")

# Main Menu Loop - handles menu, routing with if/elif/else, and invalid choices
def main():
    print("========================================")
    print("  WELCOME TO NASRO'S MINI-TOOLKIT")
    print("========================================")
    print("Your personal toolkit with 4 handy tools!")

    while True:
        print("\n----------------------------------------")
        print("MAIN MENU")
        print("----------------------------------------")
        print("1. To-Do List Manager")
        print("2. Number Guessing Game")
        print("3. Simple Calculator")
        print("4. Countdown Timer")
        print("5. Quit")
        print("----------------------------------------")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            todo_manager()
        elif choice == '2':
            guessing_game()
        elif choice == '3':
            calculator()
        elif choice == '4':
            countdown_timer()
        elif choice == '5':
            print("\nThanks for using Abdul's Mini-Toolkit! Goodbye!")
            break
        else:
            # Graceful handling of invalid choice - program does NOT crash
            print(f"\nOops! '{choice}' is not a valid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()