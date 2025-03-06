import random

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def update_price(self):
        change_percent = random.uniform(-5, 5)  # Simulating random market fluctuation (-5% to +5%)
        self.price *= (1 + change_percent / 100)
        self.price = round(self.price, 2)

class Portfolio:
    def __init__(self):
        self.balance = 10000  # Starting balance
        self.holdings = {}
    
    def buy_stock(self, stock, quantity):
        total_cost = stock.price * quantity
        if total_cost <= self.balance:
            self.balance -= total_cost
            self.holdings[stock.name] = self.holdings.get(stock.name, 0) + quantity
            print(f"Bought {quantity} shares of {stock.name} at ${stock.price} each.")
        else:
            print("Insufficient funds!")
    
    def sell_stock(self, stock, quantity):
        if stock.name in self.holdings and self.holdings[stock.name] >= quantity:
            self.balance += stock.price * quantity
            self.holdings[stock.name] -= quantity
            print(f"Sold {quantity} shares of {stock.name} at ${stock.price} each.")
            if self.holdings[stock.name] == 0:
                del self.holdings[stock.name]
        else:
            print("Not enough shares to sell!")
    
    def show_portfolio(self):
        print("\nPortfolio:")
        print(f"Balance: ${self.balance:.2f}")
        for stock, quantity in self.holdings.items():
            print(f"{stock}: {quantity} shares")
        print()

# Simulation
def main():
    stocks = [Stock("AAPL", 150), Stock("GOOGL", 2800), Stock("TSLA", 700)]
    portfolio = Portfolio()
    
    while True:
        print("\nStock Market:")
        for stock in stocks:
            stock.update_price()
            print(f"{stock.name}: ${stock.price}")
        
        print("\nOptions:")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            stock_name = input("Enter stock name (AAPL/GOOGL/TSLA): ").upper()
            quantity = int(input("Enter quantity: "))
            stock = next((s for s in stocks if s.name == stock_name), None)
            if stock:
                portfolio.buy_stock(stock, quantity)
            else:
                print("Invalid stock name!")
        
        elif choice == "2":
            stock_name = input("Enter stock name (AAPL/GOOGL/TSLA): ").upper()
            quantity = int(input("Enter quantity: "))
            stock = next((s for s in stocks if s.name == stock_name), None)
            if stock:
                portfolio.sell_stock(stock, quantity)
            else:
                print("Invalid stock name!")
        
        elif choice == "3":
            portfolio.show_portfolio()
        
        elif choice == "4":
            print("Exiting simulator...")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
