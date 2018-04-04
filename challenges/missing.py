"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """
    #step 1
    # new_set = set(nums)

    # for num in range(1, max_num):
    # 	if num not in new_set:
    # 		return num

    #step2

    nums.sort()

    for i in range(len(nums) - 1):
    	if nums[i + 1] - nums[i] > 1:
    		return nums[i] + 1



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
