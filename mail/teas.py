import pathlib
from pathlib import Path

contacts='contacts.txt'

with open(Path("GitHub/python_projects/mail")/contacts) as file:
    # reader = csv.reader(file)  # for txt: file.readline()
    reader = file.readlines()
    # next(reader)  # Skip header row if csv with header line
    for email in reader:
        print(email.strip())
