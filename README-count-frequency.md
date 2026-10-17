## Frequency Counting and Performance Timing ##
### Overview ###
A Python exercise exploring how a dictionary can count the occurrences of items in a list. The script also uses Python's built-in timeit module to compare execution times for lists of different sizes.
### Features ###
- Defines a count_frequencies(items) function that builds and returns a dictionary.
- Increases an item's count when it has already appeared in the list.
- Starts an item's count at one when it appears for the first time.
- Benchmarks the function with lists containing 10, 100 and 1,000 integers.
- Repeats each timing test three times, with ten function calls per repeat, and prints the recorded times and minimum time.
### Concepts demonstrated ###
- Python functions and parameters
- Dictionaries and key-value pairs
- for loops and conditional logic
- Counting occurrences in a collection
- Basic performance measurement with timeit
### Requirements ###
- Python 3
- No external libraries are required; timeit is part of the Python standard library.
### How to run ###
1. Download or clone this repository.
2. Open a terminal in the folder containing count_frequencies.py.
3. Run:
   python3 count_frequencies.py
4. Review the timing results printed for each input size.
### Notes and limitations ###
The current benchmark lists are created with list(range(...)), so every value is unique. The script therefore measures the function on lists of increasing size, but does not currently demonstrate how it counts repeated values in its benchmark data. Timing results can also vary between runs and computers.