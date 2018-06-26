def is_factor_of_20(n):
    if 20 % n == 0:
        return True
    else:
        return False


filtered = filter(is_factor_of_20, range(1, 20))
factors_of_20 = list(filtered)
print(factors_of_20)

# class node:
#     def __init__(self):
#         self.val = None
#         self.nxt = None

#     def get_val(self):
#         return self.val

#     def get_nxt(self):
#         return self.nxt

#     def set_val(self, newval):
#         self.val = newval

#     def set_nxt(self, newnxt):
#         self.nxt = newnxt

# class linked_list:
#     def __init__(self):
#         self.n = 0
#         self.head = None

#     def get

#     def set

#     def length

#     def indexing(self, i):
#         i 번 next 따라가시면 됨
#         curr = get_head()
#         for i ...
#             ????
#         curr == i번째 노드
#         리턴 curr

#     def insert(self, i, v):
#         i-1번째 노드 = indexing(self, i):
#         ???
#         ???

#     def append

#     def delete(self, i)



