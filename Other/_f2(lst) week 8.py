import timeit

def f2(lst):
    total = 0
    for x in lst:
        if x % 2 == 0:
            total += x
        else:
            total += x * 2
    return total


#snippet to time
snippet = 'f2(lst)' #change to call function with parameters

#setup code (initialise lists)
setup1 = 'lst = list(range(10))'
setup2 = 'lst = list(range(100))'
setup3 = 'lst = list(range(1000))'

#run the timings
times1 = timeit.repeat(stmt=snippet, setup=setup1, repeat=3, number=10, globals=globals())

times2= timeit.repeat(stmt=snippet, setup=setup2, repeat=3, number=10, globals=globals())

times3 = timeit.repeat(stmt=snippet, setup=setup3, repeat=3, number=10, globals=globals())

#print results
print("Times for 10 items:", [f"{t:.2e}" for t in times1])
print("Minimum time:", f"{min(times1):.2e} seconds\n")

print("Times for 100 items:", [f"{t:.2e}" for t in times2])
print("Minimum time:", f"{min(times2):.2e} seconds\n")

print("Times for 1000 items:", [f"{t:.2e}" for t in times3])
print("Minimum time:", f"{min(times3):.2e} seconds")
