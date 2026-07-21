# Python Debug Notes 


<!-- Ex 3.5  -->

## 1. Infinite Loop Prevention
* Problem: Forgot to update `a` or `b` inside `while` loop -> Condition stayed true forever -> PC froze.
* Fix:
  -  Double-check if loop variables actually change every cycle.
## 2. Input Validation
* Problem: Skipped checking `f(a) * f(b) > 0` -> Ran logic with bad data -> Returned wrong result or stuck.
* Fix:
  - Place `if` validation checks at the very top of the function.

