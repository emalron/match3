# Test Code for Finding Matched Gems (Python3)

You can add/edit test cases in `test.txt`.

## Test Case Format

A test case looks like:

```
3,4
111
233
233
112
```

```
2,2
11
22
```

1. Each test case is separated by `\n\n`.
2. The first line defines the size of the grid in the format `(cols, rows)`.
3. From the second line to the last line, each number represents the color of a gem.

## How to Run

1. Put the Python file (`test.py`) and the text file (`test.txt`) in the same folder.
2. Run the following command:

   ```
   python3 test.py
   ```

## Result

Results would be like:
```
Size: (3, 5)
Grid:
[1, 1, 2, 2, 2]
[3, 1, 1, 3, 3]
[1, 3, 3, 2, 2]
# of color groups: 7
[(2, 0), (3, 0), (4, 0)]
[0, 0, 1, 1, 1]

Size: (3, 3)
Grid:
[1, 1, 1]
[2, 2, 1]
[2, 2, 1]
# of color groups: 2
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
[1, 1, 1]
[0, 0, 1]
[0, 0, 1]
```


The test code will read the test cases from `test.txt`, find the matched gems for each test case, and display the results.

Make sure to have Python 3 installed on your system before running the code.
