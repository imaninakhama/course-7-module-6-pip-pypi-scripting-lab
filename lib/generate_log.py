from datetime import datetime
import os

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

    """
    Generate a log file with timestamped filename.
    
    Args:
        data (list): List of log entries to write to file
    
    Returns:
        str: The filename that was created
    
    Raises:
        ValueError: If data is not a list
    """
    # Check if input is a list
    if not isinstance(data, list):
        raise ValueError("data must be a list")
    
    # Generate filename with pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # Write to file (works with empty lists too)
    with open(filename, 'w') as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    # Print confirmation message including filename
    print(f"Log written to {filename}")
    
    return filename
