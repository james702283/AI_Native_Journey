# This script generates and prints a personalized welcome message.
# It can be easily adapted for any name and purpose.

# Import the datetime library to check the current time
from datetime import datetime

def create_welcome_message(name, message_purpose):
  """
  Creates a custom welcome message.
  Includes a special case for a specific name and time-sensitive greetings for others.

  Args:
    name (str): The name of the person introducing themselves.
    message_purpose (str): A brief description of the purpose or context of the welcome.

  Returns:
    str: A formatted welcome string.
  """
  # First, check for the special name case. This overrides other greetings.
  if name == "James Nelson":
    return f"Hey, it's the awesome AI Director, {name}!"
  
  # Get the current hour (in 24-hour format)
  current_hour = datetime.now().hour

  # Determine the correct greeting based on the time of day
  if 5 <= current_hour < 12:
    greeting = "Good morning"
  elif 12 <= current_hour < 18:
    greeting = "Good afternoon"
  else:
    greeting = "Good evening"

  # For all other names, return the time-sensitive welcome message
  return f"{greeting} Pursuit Cohorts, I'm {name}! {message_purpose}"

def main():
  """
  The main function to run the personalized welcome script.
  Uses hardcoded values to create a welcome message.
  """
  # Set a generic user's name to demonstrate the time-based greeting
  user_name = "Alex"

  # Set the welcome message
  purpose_description = "I'm excited to learn with all of you"

  # Generate the welcome message using the function
  welcome_text = create_welcome_message(user_name, purpose_description)

  # Print the generated message
  print(welcome_text)
  
  # Test the "James Nelson" case as well
  print("\n--- Testing Special Case ---")
  welcome_text_jn = create_welcome_message("James Nelson", purpose_description)
  print(welcome_text_jn)


# This ensures that the main function runs only when the script is executed directly.
if __name__ == "__main__":
  main()