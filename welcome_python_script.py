# This script generates and prints a personalized welcome message.
# It can be easily adapted for any name and purpose.

def create_welcome_message(name, message_purpose):
  """
  Creates a custom welcome message.

  Args:
    name (str): The name of the person to be welcomed.
    message_purpose (str): A brief description of the purpose or context of the welcome.

  Returns:
    str: A formatted welcome string.
  """
  return f"Hello Pursuit Cohorts, I'm {name}! {message_purpose}"

def main():
  """
  The main function to run the personalized welcome script.
  It prompts the user for their name and a purpose, then prints the message.
  """
  # Get the user's name as input
  user_name = input("Please enter your name: ")

  # Generate the welcome message using the function
  welcome_text = create_welcome_message(user_name, "I'm excited to learn with all of you")

  # Print the generated message
  print(welcome_text)

# This ensures that the main function runs only when the script is executed directly.
if __name__ == "__main__":
  main() 