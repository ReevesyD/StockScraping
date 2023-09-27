import requests
import json
import configparser

# Create a ConfigParser instance
config = configparser.ConfigParser()

# Read the config file
config.read('config.ini')

# Access Alpha Vantage settings
alpha_vantage_section = config['AlphaVantage']

base_url = alpha_vantage_section['base_url']
function = alpha_vantage_section['function']
symbol = alpha_vantage_section['symbol']
api_key = alpha_vantage_section['api_key']
output_size = alpha_vantage_section['output_size']

# Construct the API URL using config settings
api_url = f"{base_url}?function={function}&symbol={symbol}&outputsize={output_size}&apikey={api_key}"

r = requests.get(api_url)
data = r.json()

print(data)

# Serializing json
json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
output_file_name = f"{symbol}_{function}.json"
with open(output_file_name, "w") as outfile:
    outfile.write(json_object)
