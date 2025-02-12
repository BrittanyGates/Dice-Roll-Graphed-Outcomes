#!/usr/bin/python3
"""This module creates the graph from the results of the dice roll."""
from console import console, graph_creation
from text_display_tools import sleep_print
import plotly.express as px
import random


def create_same_sided_dice_graph(number_of_sides: int) -> None:
    """Rolls the same-sided dice and store the results in a list.
    :param number_of_sides: The number of sides on the dice.
    :return: None
    """
    results = []
    for rolls in range(1000):
        result = random.randint(1, number_of_sides) + random.randint(1, number_of_sides)
        results.append(result)

    # Analyze the results
    result_count = []
    max_result = number_of_sides + number_of_sides
    possible_results = range(2, max_result + 1)
    for value in possible_results:
        frequency = results.count(value)
        result_count.append(frequency)

    # Create the graph to display the results
    title = f"Results Of Rolling Two D{number_of_sides} Dice 1000 Times"
    labels = {
        "x": "Result",
        "y": "Total Count Of Each Result",
        "color": "Result",
    }

    console.print()
    console.print("Generating the graph to display your web browser.", style=graph_creation, justify="center")
    console.print()
    sleep_print()
    console.print("Graph generated. Please check your web browser.", style=graph_creation, justify="center")
    console.print()

    fig = px.bar(x=possible_results, y=result_count, title=title, labels=labels, text_auto=True, color=possible_results,
                 color_continuous_scale="Brwnyl")
    fig.update_layout(title_font_size=24, xaxis_title_font_size=18, yaxis_title_font_size=18, xaxis=dict(
        tickmode="linear",
        tick0=0,
        dtick=1,
    ))
    fig.show()


def create_different_sided_dice_graph(first_number_of_sides: int, second_number_of_sides: int):
    """Rolls the different-sided dice and store the results in a list.
    :param first_number_of_sides: The number of sides on the first die.
    :param second_number_of_sides: The number of sides on the second die.
    :return:
    """
    results = []
    for rolls in range(1000):
        result = random.randint(1, first_number_of_sides) + random.randint(1, second_number_of_sides)
        results.append(result)

    # Analyze the results
    result_count = []
    max_result = first_number_of_sides + second_number_of_sides
    possible_results = range(2, max_result + 1)
    for value in possible_results:
        frequency = results.count(value)
        result_count.append(frequency)

    # Create the graph to display the results
    title = f"Results Of Rolling One D{first_number_of_sides} Die and One D{second_number_of_sides} Die 1000 Times"
    labels = {
        "x": "Result",
        "y": "Total Count Of Each Result",
        "color": "Result",
    }

    console.print()
    console.print("Generating the graph to display your web browser.", style=graph_creation, justify="center")
    console.print()
    sleep_print()
    console.print("Graph generated. Please check your web browser.", style=graph_creation, justify="center")
    console.print()

    fig = px.bar(x=possible_results, y=result_count, title=title, labels=labels, text_auto=True, color=possible_results,
                 color_continuous_scale="Brwnyl")
    fig.update_layout(title_font_size=24, xaxis_title_font_size=18, yaxis_title_font_size=18, xaxis=dict(
        tickmode="linear",
        tick0=0,
        dtick=1,
    ))
    fig.show()
