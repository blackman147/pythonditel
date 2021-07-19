num_list = [0, 5, 2, 4, 3, 6, 7, 9, 10, 12, 14, 15]


def sort_list(my_list):
    even_list = []
    odd_list = []
    for i in my_list:
        if i % 2 ==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    even_list.sort(), odd_list.sort()
    even_list.extend(odd_list)
    return even_list


print(sort_list(num_list))