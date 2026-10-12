# Personal Mini-Toolkit - PLP Python Week 8 Final Project

## What it does
This is Nasro's personal mini-toolkit - a menu-driven Python program with 4 handy tools:
1. **To-Do List Manager** - add, view, remove tasks (uses a live-changing list)
2. **Number Guessing Game** - guess 1-50 with hints
3. **Simple Calculator** - +, -, *, / with friendly messages
4. **Countdown Timer** - countdown with loop

## How to run it
python toolkit.py

## Files
- toolkit_plan.txt - blueprint plan before coding
- toolkit.py - main program
- screenshots/ - screenshots of menu and each tool

## Concepts Covered
- Loop: main while True menu, while loop in guessing game, for loop in countdown
- List: tasks = [] that grows/shrinks with append() and pop()
- Conditional: if/elif/else for menu routing
- F-strings: all messages use f""

## Reflection
The hardest part was planning the menu loop to return after each tool without exiting, I first made it quit after one tool. The bug that took longest was the to-do remove - I forgot to check if list is empty and got IndexError, so I added empty checks and try/except. With one more week I would add file saving for to-do list so tasks persist, add a 5th tool like password generator, and add colors to make menu more beautiful.