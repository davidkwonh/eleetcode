class Solution(object):

    # Values strictly increasing

    def buildArray(self, target, n):
        pp = []  # list of push and pops
        for i in range(1, target[len(target) - 1] + 1):  # pushes all values from 0 to n
            pp.append("Push")
            if i not in target:  # if one of the values are not in the target list, then return a pop
                pp.append("Pop")
        return pp

