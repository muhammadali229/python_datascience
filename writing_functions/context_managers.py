# Open "alice.txt" and assign the file to "file"
import contextlib
import time
with open('D:/python_Data_Science/writing_functions/alice.txt') as file:
    text = file.read()

n = 0
for word in text.split():
    if word.lower() in ['cat', 'cats']:
        n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

# -----------------------------------------------------------
# Add a decorator that will make timer() a context manager


@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    start = time.time()
    # Send control back to the context block
    yield start
    end = time.time()
    print('Elapsed: {:.2f}s'.format(end - start))


with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)
# -----------------------------------------------------------


@contextlib.contextmanager
def open_read_only(filename):
    """Open a file in read-only mode.

    Args:
      filename (str): The location of the file to read

    Yields:
      file object
    """
    read_only_file = open(filename, mode='r')
    # Yield read_only_file so it can be assigned to my_file
    yield read_only_file
    # Close read_only_file
    read_only_file.close()


with open_read_only('D:/python_Data_Science/writing_functions/alice.txt') as my_file:
    print(my_file.read())
# -----------------------------------------------------------