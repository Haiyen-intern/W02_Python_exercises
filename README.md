# W02_Python-exercises
## Testing with Pytest

---

### 1. Prerequisites

Make sure you have Python 3.10+ installed. You can install `pytest` using `pip`:

```bash
pip install pytest
```

---

### 2. Running Tests

#### Run all tests

To execute all test cases in the repository, run:

```bash
pytest
```

#### Run with detailed output (verbose mode)

To see each test function name and its execution result:

```bash
pytest -v
```

#### Run a specific test file

If you only want to test a specific file, for example `test_exercises.py`, run:

```bash
pytest test_exercises.py
```

---

### 3. Test Structure

Tests are organized inside `test_exercises.py` and cover key functions across different sections:

* `test_custom_len()`: Verifies custom length calculations for lists.
* `test_pivot_list()`: Validates list partitioning based on a pivot value.
- `test_l1_distance()`: Tests L1 (Manhattan) distance calculations for tuples representing coordinates.
