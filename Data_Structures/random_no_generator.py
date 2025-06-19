import random
start_range = 1
end_range = 10
number_of_randoms = 14

random_list_loop = []

#first way to generate the random list of numbers in the range 1-10. 
#10 is inclusive in this approach
for _ in range(number_of_randoms):
    random_list_loop.append(random.randint(start_range, end_range))
print(random_list_loop)
#removes duplicates from the random_list_loop
print(set(random_list_loop))


#second way to generate random list of numbers 
random_list_comprehension = [random.randint(start_range, end_range) for _ in range(number_of_randoms)]
print(random_list_comprehension)
#removes duplicates from the random_list_comprehension
print(set(random_list_comprehension))
