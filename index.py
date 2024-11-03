#take a list of integers and rearranges it 
#so that all even numbers appear before all odd numbers

def special_rearrangement(nums):
    # Define two empty lists
    even_numbs = []
    odd_numbs = []
    
    #adding the numbers in the list using append
    for num in nums:
        if num % 2 == 0: 
            even_numbs.append(num)
        else:
            odd_numbs.append(num)
    
    # Concatinating even and odd numbers 
    return even_numbs + odd_numbs
    

nums = [6, 5, 1, 3, 2, 10,13] #--> [6,2,10,5,1,3,13]
result = special_rearrangement(nums)
print(result)  
