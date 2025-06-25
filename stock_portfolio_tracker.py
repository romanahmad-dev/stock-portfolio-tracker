
import pandas as pd
import requests
import matplotlib.pyplot as plt

import requests

# Insert your Alpha Vantage API Key here
API_KEY = ''

# Initialize the Portfolio
portfolio = {}

# Function to add a stock to the portfolio
def add_stock(ticker, shares, purchase_price):
    portfolio[ticker] = {"shares": shares, "purchase_price": purchase_price}
    print(f"{shares} shares of {ticker} added at ${purchase_price} each.")

# Function to remove a stock from the portfolio
def remove_stock(ticker):
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"{ticker} removed from portfolio.")
    else:
        print(f"{ticker} not found in portfolio.")

# Function to view the portfolio
def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.")
    else:
        print("\nCurrent Portfolio:")
        for ticker, data in portfolio.items():
            print(f"{ticker}: {data['shares']} shares at ${data['purchase_price']} each")
        print()

# Function to get real-time stock price from Alpha Vantage API
def get_stock_price(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    try:
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        latest_price = float(data["Time Series (1min)"][last_refreshed]["4. close"])
        return latest_price
    except KeyError:
        print(f"Error retrieving data for {ticker}.")
        return None

# Function to track the portfolio with real-time prices
def track_portfolio():
    total_value = 0.0
    print("\nTracking Portfolio Performance:")
    for ticker, info in portfolio.items():
        current_price = get_stock_price(ticker)
        if current_price:
            value = current_price * info['shares']
            purchase_value = info['purchase_price'] * info['shares']
            profit_loss = value - purchase_value
            total_value += value

            print(f"{ticker}: Current Price = ${current_price}, Total Value = ${value:.2f}, Profit/Loss = ${profit_loss:.2f}")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Menu function to interact with the user
def menu():
    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Portfolio (with real-time prices)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter stock ticker (symbol): ").upper()
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price: "))
            add_stock(ticker, shares, purchase_price)

        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ").upper()
            remove_stock(ticker)

        elif choice == '3':
            view_portfolio()

        elif choice == '4':
            track_portfolio()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu function
menu()



import requests

# Insert your Alpha Vantage API Key here
API_KEY = ''

# Initialize the Portfolio with pre-defined stocks
portfolio = {
    'MSFT': {'shares': 10, 'purchase_price': 300.00},
    'AMZN': {'shares': 5, 'purchase_price': 1500.00},
    'TSLA': {'shares': 3, 'purchase_price': 700.00},
    'GOOGL': {'shares': 4, 'purchase_price': 2800.00},
    'META': {'shares': 6, 'purchase_price': 350.00},
    'NVDA': {'shares': 2, 'purchase_price': 600.00},
    'JNJ': {'shares': 8, 'purchase_price': 150.00},
    'KO': {'shares': 20, 'purchase_price': 55.00},
    'PG': {'shares': 15, 'purchase_price': 140.00},
    'NFLX': {'shares': 7, 'purchase_price': 500.00}
}

# Function to add a stock to the portfolio
def add_stock(ticker, shares, purchase_price):
    portfolio[ticker] = {"shares": shares, "purchase_price": purchase_price}
    print(f"{shares} shares of {ticker} added at ${purchase_price} each.")

# Function to remove a stock from the portfolio
def remove_stock(ticker):
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"{ticker} removed from portfolio.")
    else:
        print(f"{ticker} not found in portfolio.")

# Function to view the portfolio
def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.")
    else:
        print("\nCurrent Portfolio:")
        for ticker, data in portfolio.items():
            print(f"{ticker}: {data['shares']} shares at ${data['purchase_price']} each")
        print()

# Function to get real-time stock price from Alpha Vantage API
def get_stock_price(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    try:
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        latest_price = float(data["Time Series (1min)"][last_refreshed]["4. close"])
        return latest_price
    except KeyError:
        print(f"Error retrieving data for {ticker}.")
        return None

# Function to track the portfolio with real-time prices
def track_portfolio():
    total_value = 0.0
    print("\nTracking Portfolio Performance:")
    for ticker, info in portfolio.items():
        current_price = get_stock_price(ticker)
        if current_price:
            value = current_price * info['shares']
            purchase_value = info['purchase_price'] * info['shares']
            profit_loss = value - purchase_value
            total_value += value

            print(f"{ticker}: Current Price = ${current_price}, Total Value = ${value:.2f}, Profit/Loss = ${profit_loss:.2f}")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Menu function to interact with the user
def menu():
    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Portfolio (with real-time prices)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter stock ticker (symbol): ").upper()
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price: "))
            add_stock(ticker, shares, purchase_price)

        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ").upper()
            remove_stock(ticker)

        elif choice == '3':
            view_portfolio()

        elif choice == '4':
            track_portfolio()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu function
menu()

!pip install seaborn

pip install gradio yfinance matplotlib

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Insert your Alpha Vantage API Key here
API_KEY = ''

# Initialize the Portfolio
portfolio = {}

# Function to add a stock to the portfolio
def add_stock(ticker, shares, purchase_price):
    portfolio[ticker] = {"shares": shares, "purchase_price": purchase_price}
    print(f"{shares} shares of {ticker} added at ${purchase_price} each.")

# Function to remove a stock from the portfolio
def remove_stock(ticker):
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"{ticker} removed from portfolio.")
    else:
        print(f"{ticker} not found in portfolio.")

# Function to view the portfolio
def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.")
    else:
        print("\nCurrent Portfolio:")
        for ticker, data in portfolio.items():
            print(f"{ticker}: {data['shares']} shares at ${data['purchase_price']} each")
        print()

# Function to get real-time stock price from Alpha Vantage API
def get_stock_price(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    try:
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        latest_price = float(data["Time Series (1min)"][last_refreshed]["4. close"])
        return latest_price
    except KeyError:
        print(f"Error retrieving data for {ticker}.")
        return None

# Function to track the portfolio with real-time prices
def track_portfolio():
    total_value = 0.0
    print("\nTracking Portfolio Performance:")
    for ticker, info in portfolio.items():
        current_price = get_stock_price(ticker)
        if current_price:
            value = current_price * info['shares']
            purchase_value = info['purchase_price'] * info['shares']
            profit_loss = value - purchase_value
            total_value += value

            print(f"{ticker}: Current Price = ${current_price}, Total Value = ${value:.2f}, Profit/Loss = ${profit_loss:.2f}")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Function to plot real-time stock price
def plot_stock_prices(stock_data, ticker):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=stock_data, x='Timestamp', y='Price', marker='o')
    plt.title(f'Real-Time Stock Prices for {ticker}')
    plt.xlabel('Timestamp')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

# Function to fetch and plot stock price over time
def visualize_stock(ticker):
    stock_data = []

    # Fetch price data multiple times to build a time series
    for _ in range(5):  # Change the range for more data points
        current_price = get_stock_price(ticker)
        if current_price is not None:
            timestamp = pd.Timestamp.now()
            stock_data.append({'Timestamp': timestamp, 'Price': current_price})

    if stock_data:
        df = pd.DataFrame(stock_data)
        plot_stock_prices(df, ticker)

# Menu function to interact with the user
def menu():
    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Portfolio (with real-time prices)")
        print("5. Visualize Stock Price")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter stock ticker (symbol): ").upper()
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price: "))
            add_stock(ticker, shares, purchase_price)

        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ").upper()
            remove_stock(ticker)

        elif choice == '3':
            view_portfolio()

        elif choice == '4':
            track_portfolio()

        elif choice == '5':
            ticker = input("Enter stock ticker to visualize: ").upper()
            visualize_stock(ticker)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu function
menu()

import gradio as gr
import matplotlib.pyplot as plt
import yfinance as yf

# ===========================
# 🧠 Backend Functions
# ===========================

portfolio = {}

def add_stock(symbol, shares, price):
    if symbol in portfolio:
        portfolio[symbol]["shares"] += int(shares)
        portfolio[symbol]["price"] = float(price)
    else:
        portfolio[symbol] = {"shares": int(shares), "price": float(price)}
    return f"{shares} shares of {symbol} added at ${price} each."

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        return f"{symbol} removed from portfolio."
    else:
        return f"{symbol} not found in portfolio."

def view_portfolio():
    if not portfolio:
        return "Portfolio is empty."
    output = "Current Portfolio:\n"
    for symbol, info in portfolio.items():
        output += f"{symbol}: {info['shares']} shares at ${info['price']} each\n"
    return output

def track_portfolio():
    if not portfolio:
        return "Portfolio is empty."
    output = "Real-time Portfolio Tracking:\n"
    total_value = 0
    for symbol, info in portfolio.items():
        data = yf.Ticker(symbol)
        live_price = data.info.get("regularMarketPrice", "N/A")
        value = info['shares'] * (live_price if isinstance(live_price, (int, float)) else 0)
        total_value += value
        output += f"{symbol}: {info['shares']} shares × ${live_price} = ${value:.2f}\n"
    output += f"\nTotal Portfolio Value: ${total_value:.2f}"
    return output

# ===========================
# 📉 Visualize Stock Price
# ===========================
def visualize_stock(symbol):
    try:
        data = yf.download(symbol, period="1mo", interval="1d")  # 1-month daily prices
        if data.empty:
            return "Invalid symbol or no data available.", None

        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data['Close'], label='Close Price')
        plt.title(f"{symbol} Stock Price (Last 1 Month)")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.grid(True)
        plt.legend()
        return "", plt.gcf()

    except Exception as e:
        return f"Error: {str(e)}", None

# ===========================
# 🎨 Gradio Frontend UI
# ===========================
with gr.Blocks() as demo:
    gr.Markdown("## 📈 Stock Portfolio Tracker")

    with gr.Tab("➕ Add Stock"):
        symbol = gr.Textbox(label="Stock Symbol (e.g., AAPL)")
        shares = gr.Number(label="Number of Shares", precision=0)
        price = gr.Number(label="Price per Share ($)")
        add_btn = gr.Button("Add")
        add_output = gr.Textbox(label="Status")
        add_btn.click(add_stock, inputs=[symbol, shares, price], outputs=add_output)

    with gr.Tab("➖ Remove Stock"):
        rm_symbol = gr.Textbox(label="Stock Symbol to Remove")
        rm_btn = gr.Button("Remove")
        rm_output = gr.Textbox(label="Status")
        rm_btn.click(remove_stock, inputs=rm_symbol, outputs=rm_output)

    with gr.Tab("📂 View Portfolio"):
        view_btn = gr.Button("View Portfolio")
        view_output = gr.Textbox(label="Portfolio Details", lines=10)
        view_btn.click(view_portfolio, outputs=view_output)

    with gr.Tab("📊 Track Portfolio (Real-time)"):
        track_btn = gr.Button("Track")
        track_output = gr.Textbox(label="Live Tracking", lines=10)
        track_btn.click(track_portfolio, outputs=track_output)

    with gr.Tab("📉 Visualize Stock Price"):
        vis_symbol = gr.Textbox(label="Enter Stock Symbol to Visualize (e.g., AAPL)")
        vis_btn = gr.Button("Visualize")
        vis_status = gr.Textbox(label="Message", interactive=False)
        vis_plot = gr.Plot(label="Stock Price Chart")
        vis_btn.click(visualize_stock, inputs=vis_symbol, outputs=[vis_status, vis_plot])

demo.launch()

"""# **Top Global Companies and Their Tickers:**
Apple Inc. - AAPL



Alphabet Inc. (Google) - GOOGL

Microsoft Corporation - MSFT

Amazon.com, Inc. - AMZN

Tesla Inc. - TSLA

NVIDIA Corporation - NVDA

Meta Platforms Inc. (formerly Facebook) - META

Taiwan Semiconductor Manufacturing Company - TSM

Visa Inc. - V

Johnson & Johnson - JNJ

Berkshire Hathaway Inc. - BRK.B

Walmart Inc. - WMT

Procter & Gamble Co. - PG

UnitedHealth Group - UNH

Coca-Cola Company - KO

Pfizer Inc. - PFE

Intel Corporation - INTC

Adobe Inc. - ADBE

Exxon Mobil Corporation - XOM

Chevron Corporation - CVX




"""
