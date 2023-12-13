<h1 align="center">
    <a style"font-size:large;">Leetcode: two-sum[1]</a>
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
367 ms

> Runtime Beat Percentage 🏃‍♂️
50.13%

> Memory Usage Beat Percentage 🧠
80.63% (14MB)

```

## Code

```python
class Solution(object):
    def twoSum(self, nums, target):

        for i, num in enumerate(nums):

            other = target - num

            if other in nums and nums.index(other) != i:
                return [i, nums.index(other)]

```

## Explanation

For this problem I started with the basic solution with a O(n^2) complexity but decided to go for O(n). I got to this solution by assigning a secondary variable with the result of the given target minus the given num. I then tooks this value and searched the given list for this value. If its was found and wasnt the same index as the given num it was returned.

## Author

[@ThatsNeat](https://github.com/Thats-Neat)
