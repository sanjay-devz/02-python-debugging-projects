old_list = [1,2,3,4,5,6,7,8,9,10,45,12,45,124,124,48,14,52,13]

odd_list = []
odd_no = 0
even_list = []
even_no = 0

for odd in old_list[:]:
    if odd % 2 == 0:
        
        odd_list.append(odd)
        odd_no += 1


for even in old_list[:]:
    if even % 2 == 1:

        even_list.append(even)
        even_no += 1         


print()
print("odd list:",odd_list) 
print(f"The total odd numbers in the list: {odd_no}")
print()
print("even list:",even_list)
print(f'The total even numbers in the list: {even_no}')
print()
        


        
