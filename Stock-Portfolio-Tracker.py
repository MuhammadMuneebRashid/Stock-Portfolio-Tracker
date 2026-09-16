stock_price= {
    "AAPL":180,
    "TSLA":250,
    "MSFT":420,
    "GOOGL":140
}
total_investment=0
print("=== STOCK PORTFOLIO TRACKER ===")
print("Available Stocks")
for stock,price in stock_price.items():
    print(f"{stock} - ${price}")
while True:
    stock_name=input("Enter the stock name (or 'done' to finish):").upper()
    if stock_name=="DONE":
        break
    if stock_name not in stock_price:
        print("Stock not found!")
        continue
    quantity=int(input("Enter the quantity:"))
    investment=stock_price[stock_name]*quantity
    total_investment+=investment
    print(f"{stock_name} x {quantity} = ${investment}")
    print("=== PORTFOLIO SUMMARY ===")
    print(f"Total Investment:${total_investment}")
    with open("Portfolio.txt","w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("------------------------------\n")
        f.write(f"Total Investment $ {total_investment}")
    print("Portfolio saved in Portfolio.txt")