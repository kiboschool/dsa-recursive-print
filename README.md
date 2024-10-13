# Recursive Print

In this exercise, you will use recursion to print the contents of a file in sequential order and then in reverse.

## Your Tasks

### 1. Implement recursive print

In `print.py`, you will find the function `print_file()`, which opens a file for reading as a Python file object `f`. This file handle is then passed to the `recursive_print()` function as a parameter.

Your first task is to implement `recursive_print()`, which should print the lines of the file `f` one at a time using recursion. Each recursive call to the `recursive_print()` function should print one line.

You can read in a line from the file using the `readline()` function: for example, `f.readline()`. You should store that line of text in a variable, and then print that line when needed.

Other notes:

* At the end of the file, `readline()` returns an empty string (`""`). For blank lines in the file, `f.readline()` returns a string with a newline character (`"\n"`), which allows you to distinguish them from the end of the file.
* When you print a line of text that was read-in using `readline()`, it contains the newline character (`\n`) that ended the line of text. `print()` itself also appends a newline character, so the output of your program may appear double-spaced. This is OK. If you want to remove the extra newline, you can use the optional parameter `end` to the print function:

```python
print(some_string, end='')
```

### 2. Implement *reverse* recursive print

Also in `print.py`, you will find a function `print_file_reverse()`. This function also opens a file for reading and calls a recursive function, this time `recursive_print_reverse()`, that you will implement using recursion.

`recursive_print_reverse()` should print the contents of the file *in reverse*; i.e., the last line of the file should be printed first, the second-to-last line of the file should be printed second, etc.

The same implementation tips as in (1) also apply here: use `readline()` to read in a line of text, and whenever `readline()` returns the empty string, you know that the file is complete.

Reversing the output of the prints should require just one small change to the `recursive_print()` version of the function.

## Testing

In the main script portion of `print.py`, there are sample calls to the functions listed above.
