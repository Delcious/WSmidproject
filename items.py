import json
def read_orders():
  
def process_items():
  
def main():
  orders = read_orders('example_orders.json')
  items = process_items(orders)
  with open('items.json', 'w') as f:
        json.dump(items, f)
if __name__ =="__main__":
  main()
