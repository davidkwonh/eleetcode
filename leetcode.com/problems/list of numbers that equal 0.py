#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
import random


class Solution(object):
    def sumZero(self, n):
        nums = []
        no = set([])  # WE are using sets for a quick lookup for the use of "in"

        if n == 0:
            return nums  # base case in case n = 0
        else:
            counter = 0  # keep track of how many values that have been populated into the set
            while counter < n - 1:  # savining the last value in n for the negative value of all other numbers combined (sum)
                randNum = random.randint(0, n * 100000)  # generating random numbers
                while randNum in no:  # if random number is in the set, remake random number
                    randNum = random.randint(0, n * 100000)
                nums.append(randNum)  # putting randomnumbers into the list
                no.add(randNum)  # putting randomnumbers into the set
                counter += 1  # increasing count IMPORTANT

            sum = 0
            for i in nums:  # creating a sum of all number from 0 to n-2
                sum += i

            nums.append(sum * -1)  # last number of the list is the negative number of all the prev numbers

            return nums
