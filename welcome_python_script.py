# This script generates and prints a personalized welcome message.
# It can be easily adapted for any name and purpose.

def create_welcome_message(name, message_purpose):
  """
  Creates a custom welcome message.

  Args:
    name (str): The name of the person introducing themselves.
    message_purpose (str): A brief description of the purpose or context of the welcome.

  Returns:
    str: A formatted welcome string.
  """
  if name == "James Nelson":
    return f"Hey, it's the awesome AI Director, {name}!"
  else:
    return f"Hello Pursuit Cohorts, I'm {name}! {message_purpose}"

def main():
  """
  The main function to run the personalized welcome script.
  Uses hardcoded values to create a welcome message.
  """
  # Set the user's name
  user_name = "James Nelson"

  # Set the welcome message
  purpose_description = "I'm excited to learn with all of you"

  # Generate the welcome message using the function
  welcome_text = create_welcome_message(user_name, purpose_description)

  # Print the generated message
  print(welcome_text)

# This ensures that the main function runs only when the script is executed directly.
if __name__ == "__main__":
  main() 