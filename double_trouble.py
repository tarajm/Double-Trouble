'''Double Trouble
Create a function that changes a given array to list each original element twice, retaining original order. 
Convert [4,"Ulysses",42,false] to [4,4,"Ulysses","Ulysses",42,42,false,false].'''

def double(lst):
    result =[]
    for i in lst:
        result.extend([i]*2)
    return result

print(double([4,"Ulysses",42,False]))