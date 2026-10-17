import timeit

#optimised bubble sort
def optimised_bubble_sort(lst):
    comparisons = 0
    swaps = 0
    n = len(lst)
    swapped = True

    while swapped:
        swapped = False
        for j in range(n - 1):
            comparisons += 1 # count each comparison
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swaps += 1
                swapped = True
        n -= 1
    return lst, comparisons, swaps

#snippet to time
snippet = 'optimised_bubble_sort(lst.copy())' #change to call function with parameters

#setup code (initialise lists)
setup_best = 'lst = list(range(1, 21))'
setup_worst = 'lst = list(range(20, 0, -1))'

#run the timings
best_opt = timeit.repeat(stmt=snippet, setup=setup_best, repeat=3,
number=10, globals=globals())
worst_opt = timeit.repeat(stmt=snippet, setup=setup_worst, repeat=3,
number=10, globals=globals())

#print results
print("=== OPTIMISED BUBBLE SORT ===")
print("Best case:", [f"{t:.2e}" for t in best_opt])
print("Minimum time:", f"{min(best_opt):.2e} seconds\n")

print("Worst case:", [f"{t:.2e}" for t in worst_opt])
print("Minimum time:", f"{min(worst_opt):.2e} seconds\n")


#selection sort
def selection_sort(lst):
    comparisons = 0
    swaps = 0

    for i in range(len(lst)):
        smallest = i

        for j in range(i + 1, len(lst)):
            comparisons += 1 # counting the comparison
            if lst[j] < lst[smallest]:
                smallest = j

        if smallest != i:
            lst[i], lst[smallest] = lst[smallest], lst[i]
            swaps += 1
    return lst, comparisons, swaps

#snippet to time
snippet = 'selection_sort(lst.copy())' #change to call function with parameters

#setup code (initialise lists)
setup_best = 'lst = list(range(1, 21))'
setup_worst = 'lst = list(range(20, 0, -1))'

#run the timings
best_sel = timeit.repeat(stmt=snippet, setup=setup_best, repeat=3,
number=10, globals=globals())
worst_sel= timeit.repeat(stmt=snippet, setup=setup_worst, repeat=3,
number=10, globals=globals())

#print results
print("=== SELECTION SORT ===")
print("Best case:", [f"{t:.2e}" for t in best_sel])
print("Minimum time:", f"{min(best_sel):.2e} seconds\n")

print("Worst case:", [f"{t:.2e}" for t in worst_sel])
print("Minimum time:", f"{min(worst_sel):.2e} seconds\n")


#insertion sort
def insertion_sort(lst):
    comparisons = 0
    swaps = 0 #count shifts rather than swaps

    for i in range(1, len(lst)):
        value = lst[i]
        j = i - 1

        while j >= 0 and value < lst[j]:
            comparisons += 1
            lst[j + 1] = lst[j]
            swaps += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        lst[j + 1] = value

    return lst, comparisons, swaps


#snippet to time
snippet = 'insertion_sort(lst.copy())' #change to call function with parameters

#setup code (initialise lists)
setup_best = 'lst = list(range(1, 21))'
setup_worst = 'lst = list(range(20, 0, -1))'

#run the timings
best_ins = timeit.repeat(stmt=snippet, setup=setup_best, repeat=3,
number=10, globals=globals())
worst_ins = timeit.repeat(stmt=snippet, setup=setup_worst, repeat=3,
number=10, globals=globals())

#print results
print("=== INSERTION SORT ===")
print("Best case:", [f"{t:.2e}" for t in best_ins])
print("Minimum time:", f"{min(best_ins):.2e} seconds\n")

print("Worst case:", [f"{t:.2e}" for t in worst_ins])
print("Minimum time:", f"{min(worst_ins):.2e} seconds\n")
