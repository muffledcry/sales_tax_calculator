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

def calculate_sales_tax(item_cost):
  sales_tax = item_cost * 0.06625
  return sales_tax

def calculate_total_cost(item_cost, sales_tax):
  total_cost = item_cost + sales_tax
  return total_cost

def get_items():
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
      tax_amount = calculate_sales_tax(item_cost)
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
  

def run():
  welcome()
  num_items, item_names, item_costs, tax_amounts, item_totals = get_items()
  total_cost, total_tax = get_totals(item_costs, tax_amounts)
  display_receipt(num_items, item_names, item_costs, tax_amounts, item_totals, total_cost, total_tax)

if __name__ == "__main__":
  run()
