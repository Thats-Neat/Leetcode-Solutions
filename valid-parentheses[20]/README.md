<h1 align="center">
    <a style"font-size:large;">Leetcode: valid-parentheses[20]</a>
</h1>

<p align="center">
  <i align="center">Stats and Explanation</i>
</p>

<div align="center">
  <a href="https://opensource.org/license/mit/">
    <img src="https://img.shields.io/badge/Licence-MIT-blue" alt="continuous integration" style="height: 20px;">
  </a>
  <a>
    <img src="https://img.shields.io/badge/Python-v3.9.6-blue" alt="continuous integration" style="height: 20px;">
  </a>
</div>

## Stats

```bash
> Case Completion Time ⏰
16 ms

> Runtime Beat Percentage 🏃‍♂️
48.35%

> Memory Usage Beat Percentage 🧠
89.23% (13.2MB)

```

## Code

```python
class Solution(object):
    def isValid(self, s):

        open = []
        switch = {")": "(", "]": "[", "}": "{"}

        for char in s:

            if char in switch:
                if open and open[-1] == switch[char]:
                    open.pop()
                else:
                    return False
            else:
                open.append(char)

        return len(open) == 0

```

## Explanation

This is the very basic solution. Using a list to hold open parentheses then checking the list for an open parentheses when a closed parenthese is found.

## Author

[@ThatsNeat](https://github.com/Thats-Neat)
