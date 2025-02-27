def even_number_of_evens(numbers):
    total_even=0
    
    if numbers == []:
        return False
    
    for number in numbers:
         if number%2==0:
             total_even += 1
    
    if total_even==0:
        return False
    else:
        return  total_even%2==0
        
        
print("All test pass")

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"