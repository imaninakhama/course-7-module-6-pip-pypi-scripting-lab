from datetime import datetime
import os

def generate_log(data):

    if not isinstance(data, list):
        raise ValueError("data must be a list")


    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for item in data:
            file.write(f"{item}\n")

    print(f"Log written to {filename}")

    return filename