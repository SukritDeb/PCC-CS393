input_list = []
num_elements = int(input("Enter the number of elements in the list: "))
for _ in range(num_elements):
    element = input("Enter an element: ")
    input_list.append(element)
unique_list = list(set(input_list))
print("Unique elements:", unique_list)