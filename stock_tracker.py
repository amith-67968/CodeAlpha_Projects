stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))

        value = stock_prices[stock] * quantity
        total_investment += value

        print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

    else:
        print("Stock not found!")

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ${total_investment}")

with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

print("Portfolio saved to 'portfolio_summary.txt'")