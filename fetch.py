import yaml
import requests
import time
import sys
import threading
from collections import defaultdict

class Fetch:
    def __init__(self, yaml_path):
        # Loads the configuration
        self.endpoints = self.load_yaml(yaml_path)
        # Initialize a Dictionary to store 2 Keys. Each will be initialized with 0
        # This will track number of succeseful 'up' and 'total'
        self.availability_counts = defaultdict(lambda: {'up': 0, 'total': 0})
        self.stop_event = threading.Event()

    def load_yaml(self, yaml_path):
        # Load the YAML configuration file. (Make sure the yaml file is declared correctly!!) EX: /this/is/my/path.yaml
        # If YAML is in same directory as this script you can declare it like this ./test.yaml
        with open(yaml_path, 'r') as file:
            return yaml.safe_load(file)
    

    def Looping_Health_Check(self):
        # Run health checks in 15 second intervals until stopped
        while not self.stop_event.is_set():
            for endpoint in self.endpoints:
                self.request(endpoint)
            self.log_availability()
            time.sleep(15)

    def request(self, endpoint):
        url = endpoint['url']
        method = endpoint.get('method', 'GET').upper()
        headers = endpoint.get('headers', {})
        body = endpoint.get('body', None)

        # Pulls the domain to keep track
        domain = self.get_domain(url)
        self.availability_counts[domain]['total'] += 1

        try:
            # Send the Request from the request prep above
            response = requests.request(method, url, headers=headers, json=body)
            latency = response.elapsed.total_seconds() * 1000  # <---Convert to milliseconds

            # Determine if the endpoint is UP or DOWN
            if 200 <= response.status_code < 300 and latency < 500:
                self.availability_counts[domain]['up'] += 1
                print(f"{endpoint['name']}:\n  Returns: UP  \n  status: {response.status_code}  \n  latency: {latency:.2f} ms")
            else:
                print(f"{endpoint['name']}:\n  Returns: DOWN  \n  status: {response.status_code}  \n  latency: {latency:.2f} ms")
        except Exception as e:
            # Catches any exceptions and will print the error
            print(f"Error with '{endpoint['name']}' Request Error: {e}")

    def log_availability(self):
        # Calculate and log the availability percentage for each domain
        # This print adds line to de clutter the output
        print()
        for domain, counts in self.availability_counts.items():
            if counts['total'] > 0:
                percentage = round(100 * counts['up'] / counts['total'])
                print(f"{domain} has {percentage}% availability")
        # This print adds line to de clutter the output       
        print()
                

    def get_domain(self, url):
        # Extract the domain from the URL
        return url.split("//")[-1].split("/")[0]
    
    def run(self):
        # Notifies user status of program in console
        try:
            print("\nLooping through endoint health checks...\nTo stop press CTRL+C\n----------------------------------------")
            self.Looping_Health_Check()
        except KeyboardInterrupt:
            print("\n----------------------------------------\nStopping health checks...")
            self.stop_event.set()

def main():
    # verifies number of arguments needed for program to work.
    if len(sys.argv) != 2:
        print("Usage: python health_checker.py <file_path_for_yaml_file>")
        sys.exit(1)
    config_path = sys.argv[1]
    checker = Fetch(config_path)
    checker.run()


if __name__ == "__main__":
    main()