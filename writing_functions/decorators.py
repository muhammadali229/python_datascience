import pandas as pd
import random
import numpy as np
# ----------------------------------------------
def load_data():
    return pd.DataFrame(data=[[72.1, 198.],
                              [69.8, 204.],
                              [63.2, 164.],
                              [64.7, 238.]], columns=['height', 'weight'])


def get_user_input(prompt='Type a command: '):
    command = random.choice(['mean', 'std', 'minimum', 'maximum'])
    print(prompt)
    print('> {}'.format(command))
    return command


# Add the missing function references to the function map
function_map = {
    'mean': np.mean,
    'std': np.std,
    'minimum': np.min,
    'maximum': np.max
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
print(function_map[func_name](data))
# ----------------------------------------------
def has_docstring(func):
    """Check to see if the function 
    `func` has a docstring.

    Args:
      func (callable): A function.

    Returns:
      bool
    """
    return func.__doc__ is not None

def as_2D(arr): 
    """Reshape an array to 2 dimensions"""
    return np.array(arr).reshape(1, -1)
# Call has_docstring() on the as_2D() function
ok = has_docstring(as_2D)

if not ok:
  print("as_2D() doesn't have a docstring!")
else:
  print("as_2D() looks ok")
# ----------------------------------------------
def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(a, b):
      return a - b
    return subtract
  else:
    print("I don't know that one")
    
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))
# ----------------------------------------------
def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])
# ----------------------------------------------
def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)
# ----------------------------------------------