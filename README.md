# F1-Strategy-Generator
This Python application for F1 race strategy planning features a modular design and leverages dictionaries for circuit data. It dynamically calculates the average speed required to match the fastest lap and provides data-driven recommendations. A comprehensive test suite using `pytest` ensures functionality.
## Features

  * **Circuit Selection:** The program prompts the user to choose from a list of predefined F1 circuits, including Monaco, Silverstone, Belgium, and Spain.
  * **Strategy Planning:** Users can select between 'Aggressive', 'Conservative', and 'Balanced' strategies.
  * **Performance Calculation:** The application calculates the average speed required to match the fastest lap time for the chosen circuit.
  * **Strategy Recommendation:** The program provides a recommendation for the number of pit stops and the specific tire compounds to use based on the selected strategy.
  * **Input Validation:** The program validates user input to ensure a valid circuit and strategy are selected.

## How to Run

### Prerequisites

  * Python 3.x
  * `pip` (Python's package installer)

### Installation

1.  First, clone the repository to your local machine.
2.  Install the required dependencies using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### Execution

Run the program from your terminal using the following command:

```bash
python project.py
```

You will then be prompted to choose a circuit and a strategy.

## Running Tests

The project includes a test suite to ensure the functionality of its core components. The tests are written using the `pytest` framework.

To run the tests, use the following command in your terminal:

```bash
pytest
```

This will run all test functions located in `test_project.py`.
