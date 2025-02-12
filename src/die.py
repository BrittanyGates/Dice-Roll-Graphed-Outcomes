#!/usr/bin/python3
"""This module contains the Die class and its methods."""
from console import console, notification
from custom_sided_die import custom_sided_die
from die_graph import create_die_graph
from text_display_tools import clear_screen, sleep_print
import sys


class Die:
    def __init__(self, number_of_sides=0):
        """Information about the Die class.
        :param number_of_sides: The number of sides on the die.
        """
        self.number_of_sides = number_of_sides

    def roll_one_die(self) -> None:
        """Allows the user to choose the die to roll, or create a custom-sided die.
        :return: None
        """
        console.print("Enter 0 to exit without rolling a die.", justify="center")
        console.print()
        console.print("Choose a die to roll:", justify="center")
        console.print()
        console.print("1 - D4 (Four-Sided Die)", justify="center")
        console.print("2 - D6 (Sox-Sided Die)", justify="center")
        console.print("3 - D8 (Eight-Sided Die)", justify="center")
        console.print("4 - D10 (Ten-Sided Die)", justify="center")
        console.print("5 - D12 (Twelve-Sided Die)", justify="center")
        console.print("6 - D20 (Twenty-Sided Die)", justify="center")
        console.print("7 - Custom-Sided Die", justify="center")
        console.print()

        try:
            user_choice = int(input("Enter your choice here: "))
        except ValueError:
            console.print()
            console.print("!! Incorrect input !!", style=notification, justify="center")
            console.print()
            console.print("-- The menu will reappear in a few seconds --", style=notification, justify="center")
            sleep_print()
            clear_screen()
            die.roll_one_die()
        except (EOFError, KeyboardInterrupt):
            console.print()
            console.print()
            console.print(" -- Interrupt signal received --", style=notification, justify="center")
            console.print()
        else:
            match user_choice:
                case 0:
                    console.print()
                    console.print("!! You exited the program !!", style=notification, justify="center")
                    console.print()
                    sys.exit()
                case 1:
                    self.number_of_sides = 4
                    create_die_graph(self.number_of_sides)
                case 2:
                    self.number_of_sides = 6
                    create_die_graph(self.number_of_sides)
                case 3:
                    self.number_of_sides = 8
                    create_die_graph(self.number_of_sides)
                case 4:
                    self.number_of_sides = 10
                    create_die_graph(self.number_of_sides)
                case 5:
                    self.number_of_sides = 12
                    create_die_graph(self.number_of_sides)
                case 6:
                    self.number_of_sides = 20
                    create_die_graph(self.number_of_sides)
                case 7:
                    custom_sided_die()
                case _:
                    console.print()
                    console.print("!! Enter a number from 0 to 7 !!", style=notification, justify="center")
                    console.print()
                    console.print(" -- The menu will reappear in a few seconds -- ", style=notification, justify="center")
                    sleep_print()
                    clear_screen()
                    die.roll_one_die()


# Create the die instance
die = Die()
