def print_2dlist(list):
    print("List")
    for row in list:
        print(row)

list_2d = [[0 for _ in range(10)]] * 5
print_2dlist(list_2d)
list_2d[0][0] = 1
print_2dlist(list_2d)
