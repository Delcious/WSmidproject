import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='?', default='example_orders.json')
args = parser.parse_args()

customer = {}
with open('customers.json','w') as f:
    json.dump(customer,f)
