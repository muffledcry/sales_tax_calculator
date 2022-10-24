


def set_tax_rate():
  state = input("Enter the abbreviation for your state:\n")
  tax_dict = {"NJ":0.066, 
              "DE":0.00,
              "OR":0.00,
             }
  tax_rate = tax_dict[state]
  return tax_rate

def get_item():
  item_name = input("What item are you buying?")
  price = float(input("What is the price of the item?"))
  return item_name, price

def calculate_tax(price, tax_rate):
  global tax_rate
  sales_tax = price * tax_rate
  total = price + sales_tax
  return total, sales_tax