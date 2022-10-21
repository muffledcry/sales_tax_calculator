#We need to know the sales tax rate
def set_tax_rate():
  #To Do:
  #1. Add all 50 states + Puerto Rico
  #2. Grab the tax rate from the dictionary using its abbreviation.
  #3. Return that tax rate for use elsewhere in our code.
  state = input("Enter the abbreviation for your state:\n")
  tax_dict = {"NJ":0.066, 
              "DE":0.00,
              "OR":0.00,
             }

#We need to get the price of the item
def get_item():
  item_name = input("What item are you buying?")
  price = float(input("What is the price of the item?"))
  return item_name, price

