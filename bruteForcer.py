import requests
from urllib3.exceptions import InsecureRequestWarning
import argparse

# supress insecure warning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# deal with arguments
parser = argparse.ArgumentParser(description="brute force testing script\n")
parser.add_argument("target", help="target")
parser.add_argument("file", help="file")

# parse arguments
args = parser.parse_args()

# variables
urlTarget = "https://"+args.target
filePath = args.file
sessionVal = "session="

# update ports as necessary
proxies = {
	"http": "http://127.0.0.1:8080",
	"https": "http://127.0.0.1:8080"
}

session = requests.Session()
# session.proxies.update(proxies)

try:
    with open(filePath, 'r') as file:
        for line in file:
            response = session.get(urlTarget + line, cookies={"Cookie":sessionVal}, proxies=proxies, verify=False)
            print(f"Status code: {response.status_code}")
            print(f"Url requested: {urlTarget}{line}")

except FileNotFoundError:
    print(f"Error: File '{filePath}' not found.")

except Exception as e:
    print(f"Error: {e}")

print("done")
