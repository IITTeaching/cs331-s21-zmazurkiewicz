from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):#help
    ### BEGIN SOLUTION
    i = low
    pivot = pivot_fn
    for j in range(low,high+1):
        if lst[j] > pivot:
            lst[i] = lst[j]
            lst[j] = lst[i]
            i += 1
    if i >= j:
        lst[i] = lst[high]
        lst[high] = lst[i]
    else:
        return i
    ### END SOLUTION

def pivot_first(lst,low,high):#what is supposed to be returned?
    ### BEGIN SOLUTION
    pivot = lst[0]
    return pivot
    ### END SOLUTION

def pivot_random(lst,low,high):#what is suppposed to be returned?
    ### BEGIN SOLUTION
    i = random.randrange(0, len(lst)-1)
    pivot = lst[i]
    return pivot
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):#help
    ### BEGIN SOLUTION
    medi = 0
    def median(lst, low, high):
        if (lst[(low + high) // 2] >= lst[low]):
            if (lst[(low + high) // 2] <= lst[high]):
                medi = (low + high) // 2
        elif (lst[low] >= (low + high) // 2):
            if (lst[low] <= lst[high]):
                medi = lst[low]
        else:
            medi = lst[high]
        return medi   
    median(lst[low], lst[(low + high) // 2], lst[high])
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
