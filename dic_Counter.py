from collections import Counter

food = ['apple', 'banana', 'apple', 'pear', 'apple', 'banana']
food_counter = Counter(food)
print(food_counter)
print(food_counter.most_common())
print(food_counter.most_common(2))
