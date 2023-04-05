import yaml
import os
from datetime import datetime
import re


def set_reminder(message, date, time):
    reminder_data = {
        'message': message,
        'date': date,
        'time': time
    }
    
    reminders_file = 'reminders.yml'
    
    if os.path.exists(reminders_file):
        with open(reminders_file, 'r') as f:
            current_reminders = yaml.safe_load(f)
            
            if current_reminders is None:
                current_reminders = []
    else:
        current_reminders = []

    current_reminders.append(reminder_data)
    
    with open(reminders_file, 'w') as f:
        yaml.dump(current_reminders, f)



def extract_reminder_details(input_text):
    # Use regular expressions to extract the message and time from the user's input
    time_pattern = r"(\d{1,2}:\d{2}(?:\s?[apAP][mM])?)"
    message_pattern = r"to\s(.*)\sat\s"
    
    time_match = re.search(time_pattern, input_text)
    message_match = re.search(message_pattern, input_text)

    if time_match and message_match:
        time = time_match.group(1)
        message = message_match.group(1)
        return message, time
    else:
        return None, None

# # Example usage:
# user_input = "Remind me at 18:00 to Buy milk"

# message, time = extract_reminder_details(user_input)

# if message and time:
#     # Use extracted message and time in the set_reminder function
#     user_id = 1
#     date = "2023-04-05"
#     set_reminder(user_id, message, date, time)
# else:
#     print("Invalid input. Please try again.")






