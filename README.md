
# CA3 - First Fit Memory Allocation

## Project Overview
This project demonstrates an implementation error in the First Fit memory allocation algorithm and its correction.

## Problem
The original program used an incorrect comparison condition:
blocks[j] < processes[i]

This caused processes to be allocated to memory blocks that were too small, resulting in negative memory values.

## Solution
The condition was corrected to:
blocks[j] >= processes[i]

Now, a process is allocated only when the available memory block is large enough.

## Technologies Used
- Python 3
- Ubuntu Linux
- Visual Studio Code

## Files
- main.py - Corrected memory allocation program
- test_cases.py - Test cases for validation

## Testing
Three test cases were performed:
1. Normal memory allocation
2. No suitable memory block
3. Exact memory match

All three tests passed.

## Conclusion
The corrected First Fit algorithm allocates memory safely and avoids negative remaining memory values.
