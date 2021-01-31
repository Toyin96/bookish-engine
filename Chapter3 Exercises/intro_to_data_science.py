import statistics

values = (9, 11, 22, 34, 17, 22, 34, 22, 40)
mean = statistics.mean(values)
sorted_values = sorted(values)
median = statistics.median(sorted_values)
mode = statistics.mode(values)

print(f"The mean is: {mean:.2f}")
print(f"The median is: {median:.2f}")
print(f"The mode is: {mode:.2f}")