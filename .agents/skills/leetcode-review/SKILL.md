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

   ### Alternative Solutions
   After the implemented solution's complexity comments, enumerate all known approaches for the problem:
   ```python
   # Alternative solutions:
   # 1. <Approach name> - <key DSAs (e.g., brute force, hash map, two pointers)>
   #    Time: O(...) | Space: O(...)
   # 2. <Approach name> - <key DSAs>
   #    Time: O(...) | Space: O(...)
   ```
   - Include the implemented approach in the list (mark it with `[implemented]`)
   - Order from least to most optimal
   - Cover all well-known approaches (brute force through optimal)

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
