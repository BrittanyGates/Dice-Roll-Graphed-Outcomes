#!/usr/bin/python3
"""This module contains the Dice class and its methods."""
from console import console, notification
from custom_sided_dice import custom_same_sided_dice, custom_different_sided_dice
from dice_graph import create_same_sided_dice_graph
from text_display_tools import clear_screen, sleep_print
import sys


class Dice:
    def __init__(self, number_of_sides=0):
        """Information about the Dice class.
        :param number_of_sides: The number of sides on the die.
        """
        self.number_of_sides = number_of_sides

    def roll_two_same_sided_dice(self) -> None:
        """Allows the user to roll two custom same-sided dice.
        :return: None
        """
        console.print("Enter 0 to exit without rolling dice.", justify="center")
        console.print()
        console.print("Choose dice to roll:", justify="center")
        console.print()
        console.print("1 - 2 x D4 (Four-Sided Dice)", justify="center")
        console.print("2 - 2 x D6 (Sox-Sided Dice)", justify="center")
        console.print("3 - 2 x D8 (Eight-Sided Dice)", justify="center")
        console.print("4 - 2 x D10 (Ten-Sided Dice)", justify="center")
        console.print("5 - 2 x D12 (Twelve-Sided Dice)", justify="center")
        console.print("6 - 2 x D20 (Twenty-Sided Dice)", justify="center")
        console.print("7 - 2 x Custom-Sided Dice", justify="center")
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
            dice.roll_two_same_sided_dice()
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
                    create_same_sided_dice_graph(self.number_of_sides)
                case 2:
                    self.number_of_sides = 6
                    create_same_sided_dice_graph(self.number_of_sides)
                case 3:
                    self.number_of_sides = 8
                    create_same_sided_dice_graph(self.number_of_sides)
                case 4:
                    self.number_of_sides = 10
                    create_same_sided_dice_graph(self.number_of_sides)
                case 5:
                    self.number_of_sides = 12
                    create_same_sided_dice_graph(self.number_of_sides)
                case 6:
                    self.number_of_sides = 20
                    create_same_sided_dice_graph(self.number_of_sides)
                case 7:
                    custom_same_sided_dice()
                case _:
                    console.print()
                    console.print("!! Enter a number from 0 to 7 !!", style=notification, justify="center")
                    console.print()
                    console.print(" -- The menu will reappear in a few seconds -- ", style=notification, justify="center")
                    sleep_print()
                    clear_screen()
                    dice.roll_two_same_sided_dice()

    def roll_two_different_sided_dice(self) -> int | None:
        """Allows the user to choose multiple dice to roll, or create custom-sided dice.
        :return: None.
        """
        custom_different_sided_dice()


# Create the dice instances
dice = Dice()
