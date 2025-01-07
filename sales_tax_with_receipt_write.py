import os

def clear():
  os.system("clear")

def welcome():
  print("=" * 20)
  print("SALES TAX CALCULATOR")
  print("      and")
  print("RECEIPT MAKER")
  print("=" * 20)
  print()
  input("Press Enter to Begin")
  clear()

def get_state():
  print("Enter the two-letter abbreviation of the state where")
  state = input("you are making the purchase: ").upper()
  return state

def set_tax_rate(state):
  tax_rates = {
    "AL": 0.04,
    "AK": 0.00,
    "AZ": 0.056,
    "AR": 0.065,
    "CA": 0.0725,
    "CO": 0.029,
    "CT": 0.0635,
    "DE": 0.00,
    "FL": 0.06,
    "GA": 0.04,
    "HI": 0.04,
    "ID": 0.06,
    
  }
  tax_rate = tax_rates[state]
  return tax_rate

def get_num_of_items():
  num_of_items = int(input("Enter the number of items you wish to purchase: "))
  clear()
  return num_of_items

def get_item_name(counter):
  item_name = input(f"Enter the name of item {counter + 1}: ").title()
  clear()
  return item_name

def get_item_cost(counter):
  item_cost = float(input(f"Enter the cost of the item {counter + 1}: $"))
  clear()
  return item_cost

def calculate_sales_tax(item_cost, tax_rate):
  sales_tax = item_cost * tax_rate
  return sales_tax

def calculate_total_cost(item_cost, sales_tax):
  total_cost = item_cost + sales_tax
  return total_cost

def get_items(tax_rate):
  item_costs = []
  item_names = []
  tax_amounts = []
  item_totals = []

  num_items = get_num_of_items()
  for i in range(num_items):
      # Get item names and append them to the list
      item_name = get_item_name(i)
      item_names.append(item_name)

      # Get item costs and append to the list
      item_cost = get_item_cost(i)
      item_costs.append(item_cost)

      # Calculate sales tax amounts and append to the list
      tax_amount = calculate_sales_tax(item_cost, tax_rate)
      tax_amounts.append(tax_amount)

      # Calculate total price and append to the list
      total = calculate_total_cost(item_cost, tax_amount)
      item_totals.append(total)

  return num_items, item_names, item_costs, tax_amounts, item_totals

def get_totals(item_costs, tax_amounts):
  return sum(item_costs), sum(tax_amounts)

def display_receipt(num_items, item_names, item_costs, tax_amounts, item_totals, total_cost, total_tax):
  print("\nRECEIPT:")
  print("=" * 20)
  for i in range(num_items):
      item_name = item_names[i]
      item_cost = item_costs[i]
      tax_amount = tax_amounts[i]
      total = item_totals[i]

      print(f"Item: {item_name}")
      print(f"Price: ${item_cost:.2f}")
      print(f"Sales Tax Amount: ${tax_amount:.2f}")
      print(f"Total Cost: ${total:.2f}")
      print("-" * 20)

  print()
  print(f"Total Sales Tax: ${total_tax:.2f}")
  print(f"Total Cost: ${total_tax + total_cost:.2f}")

def write_receipt(num_items, item_names, item_costs, tax_amounts, item_totals, total_cost, total_tax):
  with open("receipt.txt", "w") as f:
    print("\nRECEIPT:", file=f)
    print("=" * 20, file=f)
    for i in range(num_items):
        item_name = item_names[i]
        item_cost = item_costs[i]
        tax_amount = tax_amounts[i]
        total = item_totals[i]
    
        print(f"Item: {item_name}", file=f)
        print(f"Price: ${item_cost:.2f}", file=f)
        print(f"Sales Tax Amount: ${tax_amount:.2f}", file=f)
        print(f"Total Cost: ${total:.2f}", file=f)
        print("-" * 20, file=f)
    
    print(file=f)
    print(f"Total Sales Tax: ${total_tax:.2f}", file=f)
    print(f"Total Cost: ${total_tax + total_cost:.2f}", file=f)
  

def run():
  welcome()
  state = get_state()
  tax_rate = set_tax_rate(state)
  num_items, item_names, item_costs, tax_amounts, item_totals = get_items(tax_rate)
  total_cost, total_tax = get_totals(item_costs, tax_amounts)
  display_receipt(num_items, item_names, item_costs, tax_amounts, item_totals, total_cost, total_tax)
  write_receipt(num_items, item_names, item_costs, tax_amounts, item_totals, total_cost, total_tax)

if __name__ == "__main__":
  run()
