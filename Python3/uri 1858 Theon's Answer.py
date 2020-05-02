#1858 Theon's Answer

num = int(input())
person = list(map(int,input().split()[:num]))
min_hit = person.index(min(person))+1
print(min_hit)
