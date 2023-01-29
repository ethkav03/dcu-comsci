#!/usr/bin/env python3

def main():
  a = [1, 4, 7, 1, 5, 2]
  print(sum_nums(a))

def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])


if __name__ == "__main__":
    main()