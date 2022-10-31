def set_tax_rate():
  state = input("Enter the abbreviation for your state:\n")
  tax_dict = {
    "NJ": 0.06625,
    "DE": 0.00,
    "OR": 0.00,
  }
  tax_rate = tax_dict[state]
  return tax_rate


def get_items():
  items = []
  prices = []
  while True:
    item_name = input("What item are you buying?")
    price = float(input("What is the price of the item?"))
    buy_more = input("Are you buying another item?\nEnter y or n.").lower()
    items.append(item_name)
    prices.append(price)
    if buy_more == "y":
      continue
    else:
      break
  return items, prices


def calculate_tax(prices, tax_rate):
  sales_tax_amounts = []
  total = 0
  for price in prices:
    sales_tax = price * tax_rate
    sales_tax_amounts.append(sales_tax)
    total = total + price + sales_tax
  return total, sales_tax_amounts


def receipt():
  for i in range(0, len(item_names)):
    print(f"You purchased {item_names[i]}")
    print(f"Its price was ${prices[i]}")
    print(f"You paid ${sales_tax_amounts[i]:.2f} in sales tax.")
  print(f"The total cost is ${total:.2f}")


item_names, prices = get_items()
tax_rate = set_tax_rate()
total, sales_tax_amounts = calculate_tax(prices, tax_rate)
receipt()
