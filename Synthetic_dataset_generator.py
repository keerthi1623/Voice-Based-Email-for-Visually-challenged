import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Create a Faker instance
fake = Faker()

# Number of rows in the dataset
num_rows = 100

# Initialize empty lists to store data
emails = []
times = []
titles = []
messages = []

# Generate synthetic data
for _ in range(num_rows):
    # Generate fake data
    email = fake.email()
    time = fake.date_time_this_year()
    title = fake.sentence()
    message = fake.paragraph()

    # Append data to lists
    emails.append(email)
    times.append(time)
    titles.append(title)
    messages.append(message)

# Create a dictionary from the lists
data = {
    'email': emails,
    'time': times,
    'title': titles,
    'message': messages
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('synthetic_dataset.csv', index=False)

print("Synthetic dataset created and saved as synthetic_dataset.csv")

df
