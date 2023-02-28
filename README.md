# Isilon-Capacity-Report

The script uses the requests library to send a GET request to the OneFS API endpoint to retrieve the system capacity information. The usage, available space, and total capacity are then extracted from the response JSON and converted to human-readable units. Finally, the capacity information is exported to a CSV file.

Before running the script, you must configure the following variables in the isilon_capacity.py file:

onefs_endpoint: The OneFS API endpoint URL for your Isilon cluster.
onefs_username: The username for your Isilon cluster.
onefs_password: The password for your Isilon cluster.
