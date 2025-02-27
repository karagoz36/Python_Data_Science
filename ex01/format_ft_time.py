# format_ft_time.py

import time
import datetime

# Get the current Unix timestamp
current_time = time.time()

# Format the current date as "Oct 21 2022"
formatted_date = datetime.datetime.now().strftime("%b %d %Y")

# Print the results with scientific notation
print(f"Seconds since January 1, 1970: {current_time:.4f} or {current_time:.2e} in scientific notation")
print(formatted_date)
