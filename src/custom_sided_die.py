#!/usr/bin/python3
"""This module contains the logic allowing the user to create a custom-sided die."""
from console import console, notification
from die_graph import create_die_graph
from text_display_tools import clear_screen, sleep_print
import sys


def custom_sided_die() -> None:
    """Allows the user to create a custom-sided die to roll.
    :return: None
    """
    clear_screen()
    console.print("Enter 0 to exit without creating a die.", justify="center")
    console.print()
    console.print("Create one custom-sided die from D2 (two sides) to D50 (fifty sides).", justify="center")
    console.print()
    try:
        user_custom_choice: int = int(input("Enter the number of sides for your custom die here: "))
    except ValueError:
        console.print()
        console.print("!! Incorrect input !!", style=notification, justify="center")
        console.print()
        console.print("-- The menu will reappear in a few seconds --", style=notification, justify="center")
        sleep_print()
        clear_screen()
        custom_sided_die()
    except (EOFError, KeyboardInterrupt):
        console.print()
        console.print()
        console.print(" -- Interrupt signal received --", style=notification, justify="center")
        console.print()
    else:
        if user_custom_choice == 0:
            console.print()
            console.print("!! You exited the program !!", style=notification, justify="center")
            console.print()
            sys.exit()
        elif user_custom_choice < 2 or user_custom_choice > 50:
            console.print()
            console.print("!! Enter a number from 2 to 50 !!", style=notification, justify="center")
            console.print()
            console.print(" -- The menu will reappear in a few seconds -- ", style=notification, justify="center")
            sleep_print()
            clear_screen()
            custom_sided_die()
        else:
            number_of_sides = user_custom_choice
            create_die_graph(number_of_sides)
