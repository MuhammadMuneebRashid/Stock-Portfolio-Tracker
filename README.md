# 📈 Stock Portfolio Tracker

A simple and beginner-friendly **Python Stock Portfolio Tracker** that allows users to select stocks, enter quantities, calculate their investment, and generate a portfolio summary.

This project is designed to demonstrate fundamental Python programming concepts such as **dictionaries, loops, conditional statements, user input, calculations, and file handling**.

## 🚀 Features

* 📊 Displays available stocks and their prices
* 🔎 Allows users to enter stock symbols
* 🔢 Accepts the quantity of shares
* 💰 Calculates the investment for each stock
* 📈 Maintains the total portfolio investment
* 📝 Generates a portfolio summary
* 💾 Saves the portfolio summary to `Portfolio.txt`
* ⚠️ Handles invalid stock symbols

## 🛠️ Technologies Used

* **Python 3**
* Dictionaries
* `for` and `while` loops
* Conditional statements
* User input
* File handling
* Basic arithmetic operations

## 📋 Available Stocks

The project currently includes the following stocks:

| Stock | Price |
| ----- | ----: |
| AAPL  |  $180 |
| TSLA  |  $250 |
| MSFT  |  $420 |
| GOOGL |  $140 |

> Stock prices are predefined sample values for demonstration purposes and are not live market prices.

## ⚙️ How It Works

1. The program displays the available stocks and their prices.
2. The user enters a stock symbol.
3. The user enters the desired quantity.
4. The program calculates the investment:

```text
Investment = Stock Price × Quantity
```

5. The investment is added to the total portfolio value.
6. The user can continue adding stocks.
7. Entering `done` ends the input process.
8. The final portfolio summary is saved in `Portfolio.txt`.

## 💻 Example

```text
=== STOCK PORTFOLIO TRACKER ===
Available Stocks
AAPL - $180
TSLA - $250
MSFT - $420
GOOGL - $140

Enter the stock name (or 'done' to finish): AAPL
Enter the quantity: 5

AAPL x 5 = $900
=== PORTFOLIO SUMMARY ===
Total Investment: $900
Portfolio saved in Portfolio.txt
```

## 📁 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio.py
├── Portfolio.txt
└── README.md
```

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Stock-Portfolio-Tracker
```

### 3. Run the Python Program

```bash
python stock_portfolio.py
```

## 🎯 Learning Objectives

This project helps beginners understand:

* How Python dictionaries store data
* How to use loops for repeated user interaction
* How conditional statements control program flow
* How to perform calculations using user input
* How to validate user-provided stock symbols
* How to write data into a text file
* How to build a simple command-line application

## 🔮 Future Improvements

Possible improvements for future versions include:

* Fetching real-time stock prices using an API
* Supporting more stocks
* Adding buy/sell transactions
* Tracking individual holdings
* Calculating profit and loss
* Adding input validation for quantities
* Creating a graphical user interface
* Exporting portfolio data to CSV or Excel

## 📌 Disclaimer

This project is created for **educational and demonstration purposes**. The stock prices used in the program are static sample values and should not be considered real-time market data or financial advice.

## 📌 About This Project

This project is part of my journey of learning and building with **Python and AI Automation**. While working on AI automation workflows, I am also strengthening my Python programming skills by developing practical projects like this Stock Portfolio Tracker.

This project focuses on applying core Python concepts such as dictionaries, loops, conditional statements, user input, calculations, and file handling in a simple real-world application.
<img width="1920" height="1080" alt="stocker tracker" src="https://github.com/user-attachments/assets/b64e7bf6-1558-4b4b-a4a3-290e49e9f7e8" />



https://github.com/user-attachments/assets/0bab37f3-ef33-494f-b732-e3426c8a5de9


More advanced portfolio tracking features may be added in future versions.
