all_values = [3,-7,0,1,-2,9,-5]

pos = []
neg = []

for values in all_values:
    if values > 0:
        pos.append(values)
    elif values < 0:
        neg.append(values)

print(f"Positive numbers: {pos}")
print(f"Negative numbers: {neg}") 
