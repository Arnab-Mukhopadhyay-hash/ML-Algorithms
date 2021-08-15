n = int(input())
input_list1 = input().split()
list1 = [int(x) for x in input_list1]
input_list2 = input().split()
list2 = [int(x) for x in input_list2]
final_list = []
for x in range(n):
    final_list.insert(list2[x], list1[x])
for i in final_list:
    print(i, end=' ')