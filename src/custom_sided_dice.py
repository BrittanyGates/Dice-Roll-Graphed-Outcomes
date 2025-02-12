#!/usr/bin/python3
"""This module contains the logic allowing the user to create two custom-sided dice."""
from console import console, notification
from dice_graph import create_same_sided_dice_graph, create_different_sided_dice_graph
from text_display_tools import clear_screen, sleep_print
import sys


def custom_same_sided_dice() -> None:
    """Allows the user to create two custom same-sided dice to roll.
    :return: None
    """
    clear_screen()
    console.print("Enter 0 to exit without creating dice.", justify="center")
    console.print()
    console.print("Create two custom same-sided dice from D2 (two sides) to D50 (fifty sides).", justify="center")
    console.print()
    try:
        user_custom_choice: int = int(input("Enter the number of sides for your custom dice here: "))
    except ValueError:
        console.print()
        console.print("!! Incorrect input !!", style=notification, justify="center")
        console.print()
        console.print("-- The menu will reappear in a few seconds --", style=notification, justify="center")
        sleep_print()
        clear_screen()
        custom_same_sided_dice()
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
            custom_same_sided_dice()
        else:
            number_of_sides = user_custom_choice
            create_same_sided_dice_graph(number_of_sides)


def custom_different_sided_dice() -> None:
    """Allows the user to create two custom different-sided dice to roll.
    :return: None
    """
    clear_screen()
    console.print("Enter 0 to exit without creating dice.", justify="center")
    console.print()
    console.print("Create two custom different-sided dice from D2 (two sides) to D50 (fifty sides).", justify="center")
    console.print()
    try:
        first_user_custom_choice: int = int(input("Enter the number of sides for your first custom dice here: "))
        second_user_custom_choice: int = int(input("Enter the number of sides for your second custom dice here: "))
    except ValueError:
        console.print()
        console.print("!! Incorrect input !!", style=notification, justify="center")
        console.print()
        console.print("-- The menu will reappear in a few seconds --", style=notification, justify="center")
        sleep_print()
        clear_screen()
        custom_different_sided_dice()
    except (EOFError, KeyboardInterrupt):
        console.print()
        console.print()
        console.print(" -- Interrupt signal received --", style=notification, justify="center")
        console.print()
    else:
        if first_user_custom_choice == 0 or second_user_custom_choice == 0:
            console.print()
            console.print("!! You exited the program !!", style=notification, justify="center")
            console.print()
            sys.exit()
        elif first_user_custom_choice < 2 or first_user_custom_choice > 50 or second_user_custom_choice < 2 or second_user_custom_choice > 50:
            console.print()
            console.print("!! Enter a number from 2 to 50 !!", style=notification, justify="center")
            console.print()
            console.print(" -- The menu will reappear in a few seconds -- ", style=notification, justify="center")
            sleep_print()
            clear_screen()
            custom_different_sided_dice()
        else:
            custom_die_one_number_of_sides = first_user_custom_choice
            custom_die_two_number_of_side = second_user_custom_choice
            create_different_sided_dice_graph(custom_die_one_number_of_sides, custom_die_two_number_of_side)
