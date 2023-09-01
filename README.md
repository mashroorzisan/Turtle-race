# Turtle Race

Welcome to the Turtle Race Python repository! This is a simple yet entertaining turtle racing game where four colorful turtles race against each other, and you can place bets on the winner. Here's how to play:

## How to Play

1. Clone this repository to your local machine or download the code files.

2. Make sure you have Python and the Turtle graphics library installed on your system.

3. Open the `turtle_race.py` file in your Python IDE or text editor.

4. Run the `turtle_race.py` script.

5. A window will appear, displaying the turtle race track, and you'll be prompted to enter your bet. Choose a color from the available options: 'red', 'green', 'blue', or 'yellow'.

6. Once you've placed your bet, the turtles will start racing towards the finishing line, with their progress randomized.

7. The race will continue until one of the turtles crosses the finishing line. If your chosen turtle wins, you'll receive a congratulatory message. If not, you'll be informed of the winning turtle's color.

8. Close the window when you're done playing.

## Game Mechanics

- The race track includes a distinctive finishing line, and each turtle has its own unique color.

- The turtles move forward a random distance in each step, simulating a random race.

- You can choose a turtle color to bet on. If your chosen turtle wins, you win the race.

- The game will inform you of the race's outcome, whether you win or lose.

## Code Structure

Here's an overview of the code's structure:

- `turtle_race.py`: The main Python script that runs the turtle race game.

- `draw_finishing_line()`: Function to draw the finishing line on the race track.

- `generate_turtles()`: Function to create and position the four racing turtles.

- `race()`: The main race function that controls the race and determines the winner.

## Requirements

To run this game, you need Python and the Turtle graphics library. You can install the Turtle graphics library using the following command:

```bash
pip install PythonTurtle
