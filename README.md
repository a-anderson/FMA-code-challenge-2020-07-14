# FMA Coding Challenge - Tic Tac Toe
**Author: Ashley Anderson**\
**Submit By: 14th July 2020**

## Task
The assigned challenge was to create a CLI based Tic Tac Toe game in python. The game must accept input from two players, who play as either "X" or "O". The players take turns to enter the coordinates of their symbol on the board, and play until either there is a winner or the game has finished. The first player always plays with "X".


## How To Run
### Setup
The code for this game uses f-strings and therefore requires Python 3.6+ to run. I developed and tested on Python 3.8.2, but the results of Travis testing suggest that the code should be executable on Python versions 3.6+.

The Tic Tac Toe code uses only the contents of the base Python library, and will run without the need for installing any third party Python libraries. However, if you would like to run the tests you will need to install the `pytest`, `flake8`, and `mypy` libraries. This can be done by:

```
pip install -r requirements.txt
```

I suggest that this command is run within a virtual environment to avoid any conflicts that you have in your main system. I used `virtualenv`, for which the installation instructions can be found here: https://virtualenv.pypa.io/en/stable/installation.html .

### How to Run Tic Tac Toe

From within the FMA-code-challenge folder run the following command:

```
python3 tictactoe.py
```

and follow the prompts.

### How To Run the Tests

If you decided to install `pytest`, the tests can be run by running the following commands from within the FMA-code-challenge folder:

```
pytest tests.py
```

An optional `-v` command can be added to the end of the call for a deeper explanation of the tests as they are being tested. Also note that the final three tests for `test_play()` will take a little longer to complete, which is caused by the time delay (`time.sleep()`) before transitioning from the acceptance/rejection of player input. 

Pythonic (PEP8) styling can be checked using the `flake8` library. To check styling for both the tictactoe.py and tests.py files run the following command:

```
flake8 tictactoe.py tests.py --max-line-length=100
```

Note that I have specified the maximum line length to 100 characters, rather than the conventional 80 characters. 

To type-check this project run:

```
mypy tictactoe.py
```

## Discussion
### My Approach:
### Game 
**Using Base Python** \
I chose to use libraries that are available in base python for this game. This served firstly to reduce the setup time to get everything up and running.

**Functional Approach** \
Python is a multi-paradigm programming language, allowing for the use of both object oriented and functional programming (I am less familiar with procedural and imperative programming, but python allows for these paradigms as well). I chose to use a mostly functional approach to build the tic tac toe game, which is the paradigm that I am most comfortable with. 

**Using Hash Functions for Information Storage** \
Wherever I could I chose to use sets and dictionaries for data that stored multiple pieces of information, and that I called on frequently. This allowed for `if x in y` and `dict[key]` searches to be completed in O(1) time, rather than O(n) time for lists or tuples. With so few options for tic tac toe, this probably wouldn't make much difference in practical terms. However, I have found that it makes a huge difference in analysis run time for very large data sets (which I have used in bioinformatics analysis).

Sets also have the added benefit of allowing for easy identification of the number of unique values contained within an iterable, which I used to identify if win conditions were met in the game.

**Game Board** \
I chose a game board display that I thought was both aesthetically pleasing and easy to understand (at least for a CLI based game). I chose to display the coordinates next to the game board to make the required input easier for the user to understand. In tables, coordinates are usually presented as (\<row\>, \<column\>), where row numbers move top-down and column numbers move left to right, each starting at number 1. However, mathematical co-ordinates usually start with (x,y) = (0,0) in the bottom left corner, and increase moving left (x-axis) and up (y-axis). To remove any ambiguity for the user, I included a simple guide directly adjacent to the current board.

The co-ordinates are placed inside parentheses to clearly separate one co-ordinate from another. In the event that a user thinks that using parentheses is necessary (or simply copy-pastes), I use regex to remove any parentheses and trailing white space before assessing the validity of the user input. 

**Time Delays** \
I used a small time delay after the user input was accepted or rejected. This was to allow players time enough to read the result of their input. I found that not having a delay made the game jerky and difficult to follow. I included a time delay on the round divider ("====") which acts both to draw the player's attention to the result of their output, and shows that the game is still running and hasn't stalled - much like a game loading bar.

**Would You Like to Play Again?** \
Although this was not a part of the submission guidelines, I included the option to play again for two reasons:
1. It makes it much easier for the user to manually test a set of different conditions without needing to call the file over and over again.
2. Every (simple) computer game that I have played (and finished) gives players the option to play again. It didn't feel right not include that option.

### Testing
Python has a range of testing suites, and among the most popular are `unittest` and `pytest`. One advantage of unittest is that it included in the base Python library, and therefore requires no extra installation. However, I personally find the structure of unittest test classes much more difficult to understand, and much slower to set up compared to `pytest`. As mentioned above, I am much more comfortable setting up scripts in a functional format, and `pytest` allowed me to do just that. 

`pytest` also has a lot of extra functionality that allows for multiple tests to be condensed into one, for greater understandability for anyone reading the test script. I explain a bit more about one particularly useful `pytest` feature in the "What I Learned" section a bit further down.

### Code Styling
I used `flake8` to check that I was following the PEP8 style guidelines, which I tried to adhere to as much as possible. As can be seen in the `flake8` command above, I have changed the line length to 100 characters rather than the conventional 80 character limit. This was simply due to the fact that I find 100 a bit easier to work with, particularly when using long strings (for printing the board).

I also used type-hinting in all of the tic tac toe functions. Coming from a data analysis background, I have found it extremely useful to catch any mistakes in the data that I'm passing through to further analysis which makes debugging these problems much easier.

### Continuous Integration
I used Travis for automated testing. For a project so small as this it is probably not necessary to have done this, however, I included it for three reasons:
1. To ensure that the code ran on multiple versions of python.
2. To allow any interested parties to see that all tests pass without needing to test everything for themselves.
3. To catch any mistakes that I have made in the event that I forget to test the code before I commit it to the repository.  

### What I Learned
Although I have used `pytest` for small projects before, I have never used it to test standard output or for mocking user input. I used the `pytest` documentation to find the appropriate tools for the job. This lead me to `capsys` and subsequently to the `pytest.mark.paramaterize` decorator. This made it much easier to test multiple outputs for a single function. This allowed four separate tests to be condensed down to one, making to test code much easier to understand rather than just having many similarly named test functions stacked on top of one another. 

This is also the first time I have set up multiple script lines in Travis. Although this was extremely simple, I still found it a valuable lesson and will be able to apply multiple automated test commands going forward.

### Possible Improvements
I think there are a few improvements that could be made to the game, many of which involve a better user experience. Despite the time delays and round dividers for better clarity, I think the game is still a bit jerky and not as easy to follow as it could be. One possible solution would be to use colored highlighting which can be done using the `curses` python library. This would make the active player, game board, and player feedback easier to see. However, I'm not sure how this would effect testing for the printed output. This is something I could explore further in my own time.

Ultimately I think that using a GUI would be a much better overall experience for the user. However, given that we were explicitly asked *not* to write a GUI I left the game with a simple command line interface. 