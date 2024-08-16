# SubdomainFinder
SubdomainFinder
Subdomain Finder
Overview
This script is a simple subdomain scanner designed to find and log subdomains of a target domain. It utilizes multi-threading to speed up the scanning process and handles interruptions gracefully.

Features
Concurrent Requests: Uses ThreadPoolExecutor to perform multiple requests simultaneously, speeding up the scanning process.
Graceful Shutdown: Handles Ctrl+C interrupts to stop scanning and shut down resources properly.
Logging: Saves discovered subdomains to a file and avoids re-checking previously discovered subdomains.
Error Handling: Suppresses error messages and handles exceptions during execution.
How It Works
Load Existing Subdomains:

Reads the found_subdomains.txt file to load any previously discovered subdomains.
If the file does not exist, it starts with an empty set.
Subdomain Checking:

Iterates through a list of subdomains (from subDomainlist.txt), constructs the full URL, and checks if it resolves.
If a subdomain is found, it is printed and appended to the found_subdomains.txt file.
Handling Interrupts:

Uses signal handling to catch Ctrl+C interrupts, setting a shutdown event to signal threads to stop.
Waits for threads to finish before exiting the program.
Resource Cleanup:

Ensures that the ThreadPoolExecutor is properly shut down and resources are cleaned up.
Provides user feedback indicating that the subdomain scan is complete and the program has closed.
Usage
Setup:

Ensure you have Python installed.
Install the required libraries with pip install requests.
Configuration:

Modify the target_url variable to the domain you want to scan.
Update wordlist_file with the path to your subdomain list.
Running the Script:

Run the script using python arama.py.
Press Ctrl+C to interrupt the scan. The script will clean up and exit gracefully.
Example
bash
Kodu kopyala
python arama.py
Note: The script creates and updates found_subdomains.txt with each discovered subdomain. Make sure you have the necessary permissions to write to this file.
