#set1.py
def union(s1,s2):
    return s1|s2
def intersection(s1,s2):
    return s1&s2
def difference(s1,s2):
    return s1-s2
def symmetric_difference(s1,s2):
    return s1^s2
import set1
s1 = set(map(int, input("enter elements of set1:").split()))
s2 = set(map(int,input("enter elements of set2:").split()))
print("union:", s1.union(s2))
print("intersection:", s1.intersection(s2))
print("difference:", s1.difference(s2))
print("sdiff:",s1.symmetric_difference(s2))
