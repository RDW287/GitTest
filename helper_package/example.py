# an example helper file which just prints text

def PrintHello():
  """
  Prints "Hello! :)".
    
  Example:
    >>> PrintHello()
    Hello! :)
  """
  print("Hello! :)")


def PrintString(message):
  """
  Prints the provided message.
  
  Args:
    message (str): The string to be printed.
    
  Returns:
    None: This function does not return any value. It simply prints the input string.
    
  Example:
    >>> PrintString("Hello hello!")
    Hello hello!
  """
  print(f"{message}")

def AddNumbers(num1, num2):
  """
  Returns the sum of the two given numbers.

  Args:
    num1 (int): The first number to be added.
    num2 (int): The second number to be added.

  Returns:
    int: The summation of num1 and num2.

  Example:
    >>> AddNumbers(1, 2)
    3
  """
  summed_num = num1 + num2
  return summed_num
  

def greet_user(name):
  """
  Greet a user by name.

  Args:
    name (str): The name of the user to greet

  returns:
    str: String greeting including the name of the user
  """
    return f"Hello, {name}! Welcome to Data Science Trends and Applications."
