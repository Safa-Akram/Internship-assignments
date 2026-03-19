import time
import numpy as np

# Create 1 million numbers
size = 1_000_000

# Python List
python_list = list(range(size))

# NumPy Array
numpy_array = np.arange(size)

# ---- Test 1: Multiply each element by 2 ----

# Python List timing
start = time.time()
python_result = [x * 2 for x in python_list]
end = time.time()
print("Python List Time:", end - start)

# NumPy Array timing
start = time.time()
numpy_result = numpy_array * 2
end = time.time()
print("NumPy Array Time:", end - start)