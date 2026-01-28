---
name: leetcode-review
description: Reviews a LeetCode solution file and generates complexity analysis and test cases
argument-hint: <file-path>
---

# LeetCode Solution Review

Reviews a LeetCode solution and generates missing metadata.

## Instructions

1. **Read the solution file** (`$ARGUMENTS`) to understand the algorithm

2. **Fetch problem details** from the LeetCode URL in the file header using WebFetch:
   - Problem description
   - Example test cases
   - Constraints

3. **Analyze and update the file** with:

   ### Header Format
   ```python
   # Problem: <url>
   # tags: <difficulty>

   # Time complexity: O(...) - <brief explanation>
   # Space complexity: O(...) - <brief explanation>
   # <1-2 line approach summary if non-trivial>
   ```

   ### Test Cases in main()
   ```python
   def main():
       s = Solution()
       print(s.methodName(args)) # Expected: <value>
       print(s.methodName(args)) # Expected: <value>
   ```

4. **Derive test cases from**:
   - Problem examples (primary)
   - Edge cases based on constraints
   - Keep to 2-4 representative cases

5. **Complexity analysis should**:
   - Reference variable names from constraints (n, m, etc.)
   - Include brief justification for non-obvious complexities
