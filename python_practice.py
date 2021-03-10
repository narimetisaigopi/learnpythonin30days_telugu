userIds = [2,4,7,8,9,23,45,67,123]

target = 45

def linear_search(data,target):
    for x in range(len(userIds)):
        if data[x] == target:
            return True;
    return False;

res = linear_search(userIds,target)

print("target "+str(res))

def binary_search_iterative(data,target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low - high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

#res = binary_search_iterative(userIds,target)

#print("binary_search_iterative "+str(res))


def binary_search_recursive(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low - high) // 2
        if target == data[mid]: return True
        elif target < data[mid] : return binary_search_recursive(data,target,low,mid-1)
        else: return binary_search_recursive(data,target,mid+1,high)

#print("binary_search_recursive "+str(binary_search_recursive(userIds,target,0,len(userIds) - 1)))


str_name = "Sai gopi narimeti"
str_name2 = "Sai GopB Narimeti"
str_name3 = "sai gopi narimeti"

def find_uppercase_iterator(name):
    for x in range(len(name)):
        if name[x].isupper(): return name[x]
    return print("Not found uppercase letter")


print(find_uppercase_iterator(str_name))
print(find_uppercase_iterator(str_name2))
print(find_uppercase_iterator(str_name3))

def find_uppercase_recursive(name,index):
    if index == len(name)-1: return "Not there"
    if name[index].isupper() : return name[index]
    return find_uppercase_recursive(name,index+1)

print(find_uppercase_recursive(str_name,0))
print(find_uppercase_recursive(str_name2,0))
print(find_uppercase_recursive(str_name3,0))




