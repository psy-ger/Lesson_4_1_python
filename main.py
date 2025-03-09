start_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
sum_number_list = start_list.count(0)
#v1
for _ in range(sum_number_list):
    start_list.remove(0)
    start_list.insert(len(start_list), 0)

print(start_list)
#v2
while range(sum_number_list):

    start_list.insert(len(start_list), 0)
    sum_number_list -= 1
else:
    print(start_list)