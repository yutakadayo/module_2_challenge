# Loan Qualifier Functions

This function will search through list of loans to match your needs and financial status.

---

## Technologies

**Programming language**

`python 3.7 or later`

**libraries used in the functions**

`csv` and `pathlib` to read and write loan data.

`questionary` and `fire` to interact with the functions in CLI.

`sys` to exit from the application.

---

## Installation Guide

- Please install required libraries by tying following command in your terminal.

`pip install fire`

`pip install questionary`

---

## Usage

1. Download or clone the [app.py](app.py), [data](data/), and [qualifier](qualifier/) in a same directory.

2. Use terminal to navigate the directory you saved all the data.

3. Type `python app.py` in your terminal to run the functions
   - If the system puts you `NoConsoleScreenBufferError`, then type `winpty python app.py`

4. When the function asks you to enter a file path, type `data/daily_rate_sheet.csv`

5. Enter your personal information as directed by the functions.

6. You'll see results in printed messages, then the function will ask you to save list of qualifying loans

7. If you wish to save new list, type `y` to continue
   - Otherwise, type `n` to exit the functions

8. Enter new file path to save the list of qualifying loans.
   - For example: `data/qualifying_loans.csv`

9. New list is saved in the directory you specified.

---

## Contributors

Yu Takahashi
Email: yu.taka.070202@outlook.com

---

## License

Contact Yu Takahashi via the Email address above