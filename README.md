

---

# SubdomainFinder

## Overview

**SubdomainFinder** is a subdomain scanner designed to find and log subdomains of a target domain. It leverages multi-threading to speed up the scanning process and ensures graceful handling of interruptions.

## Features

- **Concurrent Requests**: Utilizes `ThreadPoolExecutor` to perform multiple requests simultaneously, enhancing the efficiency of the scanning process.
- **Graceful Shutdown**: Handles `Ctrl+C` interrupts to stop scanning and shut down resources cleanly.
- **Logging**: Saves discovered subdomains to a file (`found_subdomains.txt`) and prevents re-checking of already discovered subdomains.
- **Error Handling**: Suppresses error messages and manages exceptions during execution.

## How It Works

1. **Load Existing Subdomains**:
   - Reads the `found_subdomains.txt` file to retrieve any previously discovered subdomains.
   - If the file is absent, it initializes with an empty set.

2. **Subdomain Checking**:
   - Iterates through a list of subdomains (from `subDomainlist.txt`), constructs the full URL, and checks its availability.
   - If a subdomain resolves successfully, it is printed and added to `found_subdomains.txt`.

3. **Handling Interrupts**:
   - Uses signal handling to detect `Ctrl+C` interrupts, setting a shutdown event to notify threads to stop.
   - Waits for all threads to complete before exiting the program.

4. **Resource Cleanup**:
   - Ensures that the `ThreadPoolExecutor` is properly shut down and resources are released.
   - Provides feedback to the user indicating the completion of the subdomain scan and that the program has closed.

## Usage

1. **Setup**:
   - Ensure Python is installed on your system.
   - Install the required libraries using: `pip install requests`.

2. **Configuration**:
   - Modify the `target_url` variable in the script to the domain you want to scan.
   - Update the `wordlist_file` variable with the path to your subdomain list file.

3. **Running the Script**:
   - Execute the script using: `python subDomainFinder.py`.
   - Press `Ctrl+C` to interrupt the scan. The script will handle the shutdown process and exit gracefully.

### Example

```bash
python subDomainFinder.py
```

**Note**: The script will create and update `found_subdomains.txt` with each discovered subdomain. Ensure you have the necessary write permissions for this file.



---

