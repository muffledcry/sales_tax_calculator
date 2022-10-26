def set_tax_rate():
  state = input("Enter the abbreviation for your state:\n")
  tax_dict = {"NJ":0.06625, 
              "DE":0.00,
              "OR":0.00,
             }
  tax_rate = tax_dict[state]
  return tax_rate

def get_item():
  items = []
  prices = []
  while True:
    item_name = input("What item are you buying?")
    price = float(input("What is the price of the item?"))
    buy_more = input("Are you buying another item?")
    items.append(item_name)
    prices.append(price)
    if buy_more == "y":
      continue
    else:
      break
  return items, prices

def calculate_tax(price, tax_rate):
  sales_tax = price * tax_rate
  total = price + sales_tax
  return total, sales_tax

def receipt():
  print(f"You purchased {item_name}")
  print(f"Its price was ${price}")
  print(f"You paid ${sales_tax:.2f} in sales tax.")
  print(f"The total cost is ${total:.2f}")

item_name, price = get_item()
tax_rate = set_tax_rate()
total, sales_tax = calculate_tax(price, tax_rate)
receipt()