import csv

# Function to extract first and last name from full name
def extract_name(full_name):
    names = full_name.split()
    first_name = names[0]
    last_name = ' '.join(names[1:]) if len(names) > 1 else ''
    return first_name, last_name

# Function to convert data into Moodle user upload format
def convert_to_moodle_format(data):
    moodle_users = []
    for entry in data:
        first_name, last_name = extract_name(entry['Name'])
        username = entry['Email'].split('@')[0]  # Use email as username
        password = entry['Password']
        email = entry['Email']
        city = entry['District']
        moodle_users.append([username, password, email, first_name, last_name, city])
    return moodle_users

# Parse data from CSV file
def parse_csv(filename):
    data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Input and output file names
input_filename = 'users.csv'
output_filename = 'moodle_user_upload.csv'

# Parse CSV file
data = parse_csv(input_filename)

# Convert data to Moodle user upload format
moodle_users = convert_to_moodle_format(data)

# Write Moodle user upload data to CSV file
with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['username', 'password', 'email', 'firstname', 'lastname', 'city'])  # Header row
    writer.writerows(moodle_users)

print(f"Successfully exported Moodle user data to '{output_filename}'.")
