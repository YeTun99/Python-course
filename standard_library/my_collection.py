from collections import Counter

strs="How many times does does does"
split_strs=strs.split()
print(split_strs)

common_values=Counter(split_strs)
print(Counter(split_strs))
print(common_values.most_common(3))
print(sum(common_values.values()))