import requests
import csv

# Set the OneFS API endpoint and credentials
onefs_endpoint = "https://isilon.example.com:8080"
onefs_username = "username"
onefs_password = "password"

# Set the system capacity API endpoint
system_capacity_endpoint = f"{onefs_endpoint}/platform/1/storagepool"

# Set the headers for the system capacity request
system_capacity_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Send a GET request to retrieve the system capacity with the credentials and headers
system_capacity_response = requests.get(system_capacity_endpoint, auth=(onefs_username, onefs_password), headers=system_capacity_headers)

# Check if the request was successful
if system_capacity_response.status_code == 200:
    # Get the system capacity from the response JSON
    system_capacity = system_capacity_response.json()

    # Extract the usage, available space, and total capacity
    usage_bytes = int(system_capacity["cluster"]["logical_capacity"]["used_bytes"])
    available_bytes = int(system_capacity["cluster"]["logical_capacity"]["free_bytes"])
    total_bytes = int(system_capacity["cluster"]["logical_capacity"]["total_bytes"])

    # Convert the usage, available space, and total capacity to human-readable units
    usage = "{:.2f} GB".format(usage_bytes / (1024 ** 3))
    available = "{:.2f} GB".format(available_bytes / (1024 ** 3))
    total = "{:.2f} GB".format(total_bytes / (1024 ** 3))

    # Write the usage, available space, and total capacity to a CSV file
    with open("isilon_capacity.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Usage", "Available", "Total"])
        csvwriter.writerow([usage, available, total])

    print("Isilon capacity information exported to 'isilon_capacity.csv'.")
else:
    # Print an error message if the system capacity request was not successful
    print("Failed to retrieve system capacity.")
