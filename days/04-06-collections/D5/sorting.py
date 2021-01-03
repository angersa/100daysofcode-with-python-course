disordered = {(10, 5): 'b', (3, 10): 'a', (5, 2): 'c'}

# sort keys, then get values from original - fast
sorted_list = sorted(disordered.items(), key=lambda x: x[0][1], reverse=True)

print(sorted_list)