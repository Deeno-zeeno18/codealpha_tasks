"""
CALCULATING STOCKS PRICES
"""
def check_the_stocks():
    no_of_stocks1 = input("Enter number of stock type you would want to buy: ")
    while  not no_of_stocks1.isdigit() or int(no_of_stocks1) < 0:
        print("Please enter a valid number")
        no_of_stocks1 = input("Enter number of stock type you would want to buy: ")
    no_of_stocks = int(no_of_stocks1)
    return no_of_stocks


no_stocks = check_the_stocks()
"""
ASKING THE USER FOR THE STOCKS NAMES AND QUANTITY
"""
def ask_for_stocks():
    your_stocks_dict = {}
    for x in range(no_stocks):
        stock_name = input("Enter stock name in conventional abbreviation:").strip()
        while not stock_name.isalpha():
            print(f"Please enter a valid stock name")
            stock_name = input("Enter stock name in conventional abbreviation:").strip()

        stock_quantity1 =  input("Enter your stock quantity:")
        while not stock_quantity1.isdigit() or int(stock_quantity1) < 0:
            print("Please enter a valid number")
            stock_quantity1 = input("Enter your stock quantity: ")
        stock_quantity = int(stock_quantity1)
        your_stocks_dict[stock_name.upper()] = your_stocks_dict.get(stock_name.upper(), 0) + stock_quantity

    return your_stocks_dict

"""
DEFINING THE STOCK PRICES
"""
def define_the_stock_price():
    defined_stocks_dict = {
    "NVIDIA" : {"NVDA": 220.00}, "APPLE INC." : {"AAPL": 337.00}, "MICROSOFT CORPORATION" : {"MSFT": 495.00}, "GOOGLE" : {"GOOGL": 338.00},
    "META PLATFORMS INC." : {"META": 774.00}, "AMAZON.COM INC." : {"AMZN": 249.00}, "TESLA, INC." : {"TSLA": 363.00}, "NETFLIX, INC" : {"NFLX": 710.20}
                          }
    return defined_stocks_dict


"""
CALCULATING THE TOTAL INVESTMENT VALUE
"""
def calculate_the_total_investment():
    your_stocks_dict = ask_for_stocks()
    defined_stocks_dict = define_the_stock_price()
    investment_dict = {}
    for key in your_stocks_dict.keys():
        is_the_value_there = False
        for val in defined_stocks_dict.values():
            if key in val.keys():
                stock_name = key
                total_stock_value = your_stocks_dict[key] * val[key]
                investment_dict[stock_name] = total_stock_value
                is_the_value_there = True
                break

        if not is_the_value_there:
            print(f"Warning: '{key}' not recognized, skipping.")
    return investment_dict


invest_dict = calculate_the_total_investment()

"""
CALCULATING THE VALUE OF THE INVESTMENT
"""
def calculate_the_value():
    return sum(invest_dict.values())


total_investment_value = calculate_the_value()
print(total_investment_value)
"""
SAVING RESULT IN A TXT FILE
"""
numero = 0
with open("INVESTMENT.TXT", "w") as investment_file:
    investment_file.write(f"-------------TOTAL INVESTMENT VALUE PER STOCK TYPE-----------------")
    investment_file.write("\n")
    investment_file.write(f"STOCK NAMES----------------------- TOTAL INVESTMENT VALUE")
    investment_file.write("\n")
    for keys, vals in invest_dict.items():
        investment_file.write(f"{numero + 1}.{keys}-----------------${vals:.2f}\n")
        numero += 1

    investment_file.write(f"----------THE TOTAL INVESTMENT IS: {total_investment_value:.2f}\n")


