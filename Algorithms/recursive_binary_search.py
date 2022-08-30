def recursive_binarysearch(list, target):
    """
    return true value if it exits or return false if it doesnt exist
    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binarysearch(list[midpoint+1:], target)
            else:
                return recursive_binarysearch(list[:midpoint], target)

def verify(result):
    print("target found: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binarysearch(numbers, 12)
verify(result)

result = recursive_binarysearch(numbers, 6)
verify(result)

"""
Recursive is one that calls on itself.
    with each call, list gets smaller. size of list will keep halving itself
you always need a stopping condition or, base case. the above function has two base case
empty list will be a base case bc it'll be a different set of instructions/stopping conditions. 
    return False and return True are the base cases in the above function

Recursive Depth = how many times function calls on itself

binary search = iterative solution(solution implemented using loop structure of some kind)
recursion solution = involves a set of stopping conditions and a function that calls itself
functional languages = avoid changing data/modifying variables and would prefer recursion

python prefers iterative solutions fyi
other languages may prefer recursive solution and don't care about recursion depth

TWO WAYS OF MEASURING EFFICIENCY OF AN ALGORITHM***
    TIME COMPLEXITY = how run time of algo grows and n grows larger
    SPACE COMPLEXITY = measure of how much working storage or extra storage it needs as a particular algo grows
        as data set grows larger, our algo needs to be able to work with that
        in binary search: algo finds solution for how much space is required for data set
"""

"""
Algorithm:
    the steps in the algo need to be in a very specific order
    the steps also need to be distinct
    the algo should produce a result
    the algo should complete in a finite amount of time
"""