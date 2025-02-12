#!/usr/bin/env python3
"""Dice Roll Graphed Outcomes
Creator: Brittany Gates (https://github.com/brittbot-bgates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: A CLI application allowing users to roll different sided die or dice, and display the counts of each number in
graph format. Use the output for common and rare numbers to use in a game or application.
"""
from console import console, notification
from die import Die
from dice import Dice
from text_display_tools import clear_screen, sleep_print
import sys

die = Die()
dice = Dice()


def main_menu() -> None:
    """Displays the main menu.
    :return: None
    """
    clear_screen()
    console.print()
    console.print("Dice Roll Graphed Outcomes", justify="center")
    console.print()
    console.print("Roll a die or dice to see the count of each roll as a graph.", justify="center")
    console.print()
    console.print("The program rolls each die 1000 times.", justify="center")
    console.print()
    console.print("0 - Exit Program", justify="center")
    console.print("1 - Roll One Die", justify="center")
    console.print("2 - Roll Two, Same-Sided Dice", justify="center")
    console.print("3 - Roll Two, Different-Sided Dice", justify="center")
    console.print()
    try:
        menu_choice: int = int(input("Enter your choice here: "))
    except ValueError:
        console.print()
        console.print("!! This menu only accepts numbers !!", style=notification, justify="center")
        console.print()
        console.print("-- The menu will reappear in a few seconds --", style=notification, justify="center")
        sleep_print()
        clear_screen()
        main_menu()
    except (EOFError, KeyboardInterrupt):
        console.print()
        console.print()
        console.print(" -- Interrupt signal received --", style=notification, justify="center")
        console.print()
    else:
        if menu_choice == 0:
            console.print()
            console.print("!! You exited the program !!", style=notification, justify="center")
            console.print()
            sys.exit()
        elif menu_choice == 1:
            clear_screen()
            die.roll_one_die()
        elif menu_choice == 2:
            clear_screen()
            dice.roll_two_same_sided_dice()
        elif menu_choice == 3:
            clear_screen()
            dice.roll_two_different_sided_dice()
        else:
            console.print()
            console.print("!! Enter either 0, 1, 2 or 3 !!", style=notification, justify="center")
            console.print()
            console.print(" -- The menu will reappear in a few seconds -- ", style=notification, justify="center")
            sleep_print()
            clear_screen()
            main_menu()


if __name__ == '__main__':
    main_menu()
