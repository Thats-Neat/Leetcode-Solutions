<h1 align="center">
    <a style"font-size:large;">Leetcode: best-time-to-buy-and-sell-stock[121]</a>
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
781 ms

> Runtime Beat Percentage 🏃‍♂️
45.9%

> Memory Usage Beat Percentage 🧠
67.39% (22.5MB)

```

## Code

```python
class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        profit = 0

        for price in prices[1:]:
            profit = max(profit, price - minPrice)
            minPrice = min(minPrice, price)

        return profit

```

## Explanation

A simple solution. Grabs a min price from the first index of the list. Then loop through everything besides that first index. It then finds the the best profit and resets the minimum if needed.

## Author

[@ThatsNeat](https://github.com/Thats-Neat)
