#!/usr/bin/python3
"""This module creates the graph from the results of the die roll."""
from console import console, graph_creation
from text_display_tools import sleep_print
import plotly.express as px
import random


def create_die_graph(number_of_sides: int):
    # Roll the die and store the results in a list
    results = []
    for rolls in range(1000):
        result = random.randint(1, number_of_sides)
        results.append(result)

    # Analyze the results
    result_count = []
    possible_results = range(1, number_of_sides + 1)
    for value in possible_results:
        frequency = results.count(value)
        result_count.append(frequency)

    # Create the graph to display the results
    title = f"Results Of Rolling One D{number_of_sides} Die 1000 Times"
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
