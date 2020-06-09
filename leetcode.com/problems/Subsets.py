class Solution(object):
    def subsets(self, nums):
        num_bits = len(nums)
        bit_strings = []  # len(2^n) * O(1)
        subsets = []

        # Leading zero
        if num_bits < 10:
            leading_zeros = "{:0"
        else:
            leading_zeros = "{:"
        leading_zeros += (str(num_bits) + "b}")

        # Generate all 2^n bit strings
        # O(2^n)
        for i in range(0, 2 ** num_bits, 1):
            bit_string = leading_zeros.format(i)
            bit_strings.append(bit_string)

            print(bit_string)

        # Map each number to an index, bit flipped on @ that index
        # represents the number being present in that combination
        index_mapping = {}
        nums.sort()
        index = 0

        # O(n) where n is the number of elements in given list
        for num in nums:
            index_mapping[index] = num
            index += 1

        print(index_mapping)

        # O(2^n * n)
        # Parse each bitstring
        for bit_string in bit_strings:  # O(2^n) -> O(1) 2^n times
            index = 0
            current_subset = []

            # O(n) where n is the number of elements in given list
            # Populate each subset
            while index < num_bits:  # O(1) -> n times
                is_present = bit_string[index] == "1"
                if is_present:
                    current_subset.append(index_mapping[index])

                index += 1

            subsets.append(current_subset)

        return subsets

