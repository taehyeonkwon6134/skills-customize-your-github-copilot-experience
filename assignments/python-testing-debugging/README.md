# 📘 Assignment: Python Testing and Debugging

## 🎯 Objective

Learn how to use `pytest` to check Python code automatically, identify bugs from failing tests, and improve a program with regression tests.

## 📝 Tasks

### 🛠️ Write Your First Tests

#### Description

Copy the downloaded `starter-code.py` file as `starter_code.py`, then create a test file named `test_starter_code.py`. Use `pytest` to test the `is_even()` function from `starter_code.py`.

#### Requirements
Completed program should:

- Import `is_even()` from `starter_code`.
- Include tests for an even number, an odd number, zero, and a negative number.
- Run successfully with the command `pytest`.
- Use clear test names that describe the behavior being checked.

### 🛠️ Find and Fix Bugs

#### Description

Use tests to check the `calculate_discount()` and `find_longest_word()` functions. Read the failing test output, identify the cause of each bug, and update the implementation in `starter-code.py`.

#### Requirements
Completed program should:

- Verify that a discount percentage is applied correctly.
- Test a zero-percent discount and a 100-percent discount.
- Return the longest word in a list, including when two words have the same length.
- Make `find_longest_word([])` raise a clear `ValueError`.
- Pass all tests after the bugs are fixed.

### 🛠️ Add Exception and Regression Tests

#### Description

Complete the test suite by checking invalid inputs and preserving the behavior that already works. Add tests for invalid discount percentages, negative prices, and division by zero.

#### Requirements
Completed program should:

- Confirm that invalid discount percentages raise `ValueError`.
- Confirm that negative prices raise `ValueError`.
- Confirm that `safe_divide()` raises `ZeroDivisionError` when the divisor is zero.
- Keep all earlier tests passing after each change.
- Include at least 10 meaningful tests in total.

Run the tests with:

```bash
pip install pytest
pytest
```
