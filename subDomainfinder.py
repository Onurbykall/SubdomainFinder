import requests
import signal
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import io
import time

# Global variables
executor = None
shutdown_event = threading.Event()

# File used for storing found subdomains
found_subdomains_file = "found_subdomains.txt"

# Function to load existing subdomains from the file
def load_existing_subdomains():
    try:
        # Attempt to read the file and return a set of existing subdomains
        with open(found_subdomains_file, "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        # If the file does not exist, return an empty set
        return set()

# Signal handler for graceful shutdown
def signal_handler(signum, frame):
    print("\nReceived Ctrl+C. Exiting...")
    shutdown_event.set()  # Set the event to signal threads to stop
    cleanup_and_exit()  # Call the cleanup function to exit the program

# Function to perform HTTP GET requests
def request(url):
    try:
        # Attempt to perform a GET request with a timeout of 5 seconds
        return requests.get("http://" + url, timeout=5)
    except requests.exceptions.RequestException:
        # Return None if there is any request exception
        return None

# Function to check a subdomain
def check_subdomain(word, existing_subdomains):
    # If the shutdown event is set, exit the function
    if shutdown_event.is_set():
        return

    # Form the subdomain URL to check
    test_url = word + "." + target_url
    # Skip if the subdomain is already in the existing list
    if test_url in existing_subdomains:
        return

    # Make a request to the subdomain
    response = request(test_url)
    if response:
        # If a response is received, print and log the subdomain
        print(f"Found Subdomain --> {test_url}")
        with open(found_subdomains_file, "a") as log_file:
            log_file.write(f"{test_url}\n")

# Function to clean up resources and exit the program
def cleanup_and_exit():
    global executor
    if executor:
        print("Shutting down executor... Please wait for 5 seconds.")
        shutdown_event.set()  # Set the shutdown event to signal threads to stop
        executor.shutdown(wait=True)  # Wait for all threads to complete
    # Print the exit message
    print("Saved. Program closed.")
    sys.exit(0)  # Exit the program immediately

if __name__ == "__main__":
    # Set up the signal handler for graceful shutdown on Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    target_url = "google.com"  # The target domain to check
    wordlist_file = "subDomainlist.txt"  # The file containing the subdomain list

    # Redirect stderr to suppress error messages
    original_stderr = sys.stderr
    sys.stderr = io.StringIO()

    # Load existing subdomains from the file
    existing_subdomains = load_existing_subdomains()

    try:
        # Read the wordlist file and prepare the list of subdomains to check
        with open(wordlist_file, "r") as list_file:
            words = [line.strip() for line in list_file]

        # Create a ThreadPoolExecutor for concurrent subdomain checks
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(check_subdomain, word, existing_subdomains) for word in words]
            # Iterate over completed futures
            for future in as_completed(futures):
                if shutdown_event.is_set():
                    break  # Exit the loop if shutdown signal is received
                try:
                    future.result()  # Retrieve the result of each future
                except Exception as e:
                    # Print any exceptions that occur during execution
                    print(f"An error occurred: {e}")

    except KeyboardInterrupt:
        # Handle the case where Ctrl+C is pressed
        cleanup_and_exit()
    finally:
        # Ensure the executor is shut down properly
        if executor:
            executor.shutdown(wait=True)
        # Print the final message
        print("Saved. Program closed.")
        # Restore the original stderr
        sys.stderr = original_stderr
