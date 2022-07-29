# # def prime(n):
# #     for i in range(2,n+1):
# #         c = 0
# #         for j in range(2,i):
# #             if i%j == 0:
# #                 c = 1
# #                 pass
# #         if c == 0:
# #             print(i)


# # prime(100)

# # def pelindrom(n):
# #     new = ''
# #     for i in reversed(n):
# #         new += i
# #     if new == n:
# #         print("pelindrom")
# #     else:
# #         print("Not a pelindrom")

# # get = input()

# # pelindrom(get)


# # def check(n,m):
# #     if m in n:
# #         print("substring ")
# #     else:
# #         print("Not saubstring ")

# # main = input()
# # txt2 = input()

# # check(main,txt2)


# # def highest(list1):
# #     new = list(set(list1))

# #     new.sort()

# #     print(new[1])

# # list1 = [10,13,14,7,4,31]

# # highest(list1)


# # list1 = [2,6,7,8,8,9,3,3,3]

# # # list1.count(object)
# # highest = 0
# # for i in list1:
# #     if list1.count(i) > highest:
# #         print
# #     highest =
# #     print(list1.count(i))

# # string = "aaaabbcdda"

# # for i in string:


# # for i in string:
# #     if i in list1:
# #         pass
# #     else:
# #         print(i,string.count(i))
# #         list1.append(i)


# # def remove(m):
# #     n = m.lower()
# #     for i in n:
# #         if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
# #             print(i,end='')

# # remove('How are you')


# # def leap(new):

# #     if '00' in new:
# #         new1 = int(new)
# #         if new1%400 == 0:
# #             print("leap year")
# #         else:
# #             print("not a leap year")

# #     else:
# #         new1 = int(new)
# #         if new1 %4 == 0:
# #             print("leap year")
# #         else:
# #             print("not a leap year")

# # leap(input())


# # def anagrams(str1,str2):
# #     c = 0
# #     for i in str2:
# #             if i not in str1:
# #                 print("not anagrams")
# #                 break
# #             else:
# #                 c = 1

# #     if c == 1:
# #         print("anagrams")

# # str1 = 'listen'
# # str2 = 'silent'

# # anagrams(str1, str2)

# # def substrings(str1):

# #     list1 = []
# #     for i in str1:
# #         list1.append(i)

# #     from itertools import combinations


# #     for i in range(len(list1)+1):
# #         [print(list(x)) for x in combinations(list1,i)]

# # substrings("Abcd")

# # def count(list1):
# #     list2 = list(set(list1))

# #     highest = 0
# #     new = []

# #     for i in list2:
# #         c = 0
# #         c += list1.count(i)
# #         if highest < c:
# #             highest = c
# #             new.append(i)

# #     print(new[-1],"have",highest)

# # list1 = [2,6,7,8,8,9,3,3,3]
# # count(list1)

# # string = "aaaabbcdda"
# # str1 = list(string)
# # str2 = []
# # str2.append(str1[0])

# # for i in str1:
# #     if str2[-1] == i:
# #         pass
# #     else:
# #         str2.append(i)

# # print(str2)

# # # [str2.append(i) for i in str1 if i not in str2]
# # str2.append(str1[0])
# # s = 0
# # for i in str1:
# #     if str2[s] == i:
# #         pass
# #     else:
# #         str2.append(i)
# #     s += 1

# # print(str2)

# # temp = []
# # s = 0

# # for i in str2:
# #     c = 0
# #     for j in str1[s:]:
# #         if i == j:
# #             c += 1
# #             s += 1
# #         else:
# #             break
# #     temp.append(f"{i}{c}")

# # print(temp)


# # for i in str1:
# #     if i in str2:
# #         pass
# #     else:

# # print(str2)


# # new_list = []
# # main = str1[0]
# # for i in str1:

# #     for j in str1:
# #         if i == j:
# #             print(j)
# #             c += 1
# # else:
# #     temp.append(f"{i}{c}")
# # j += 1


# # print(temp)


# # class student:
# #     name = ""
# #     roll = ""

# #     def __init__(self,name,roll):
# #         self.name = name
# #         self.roll = roll

# #     def concatinate(self):
# #         print(self.roll + 100)

# # man = student("joy",100)
# # man.name = 'JOy'
# # man.roll = 10

# # print(man.name)

# # man.concatinate()


# # def spell(txt):
# #     if len(txt) <= 0:
# #         return txt
# #     else:
# #         return txt[-1] + spell(txt[0:len(txt)-1])


# # print(spell('HELLO'))


# # class Student():
# #         def __init__(self,name,roll):
# #                 self.name = name
# #                 self.roll = roll

# #         def dispaly(self):
# #                 print(self.name)

# # class New(Student):
# #         def dispaly(self):
# #                 print(self.name)

# #         def add(self,x,y):
# #                 print(x+y)

# #         def add(self,x,y,z):
# #                 print(x + y + z)

# # new2 = New('joy',100)
# # new2.add(10,20)


# # class A:
# #         __private = 10
# #         def __init__(self):
# #                 print("This is A class")
# #         def display(self):
# #                 print(self.__private)

# # c = A()
# # c.display()


# # from abc import ABC, abstractmethod
# # class Car(ABC):
# #     def mileage(self):
# #         pass

# # class Tesla(Car):
# #     def mileage(self):
# #         print("The mileage is 30kmph")


# # class Renault(Car):
# #     def mileage(self):
# #             print("The mileage is 27kmph ")

# # # Driver code
# # t= Tesla ()
# # t.mileage()

# # r = Renault()
# # r.mileage()


# # from abc import ABC,abstractmethod

# # class parent():
# #     def __init__(self,x,y):
# #         self.x = x
# #         self.y = y

# # #     @abstractmethod
# #     def calculate(self):
# #         pass

# # c = parent(10,20)


# # from abc import ABC,abstractmethod

# # class Polygon(ABC):
# #    def __init__(self,x,y):
# #         self.x = x
# #         self.y = y

# #    @abstractmethod
# #    def sides(self):
# #       pass

# #    def new(self):
# #            print(new)


# # class Triangle(Polygon):

# #    def sides(self):
# #       print("Triangle has 3 sides")


# # c = Polygon()
# # c.new()

# # def display(x,y):
# #                 yield x
# #                 yield y


# # m,n = display(10, 20)             # Take same num of variable
# # print(m,n)

# # print((420000+18000)/420000)

# # def increase(n):
# #         yield n
# #         n += 1

# # g = increase(10)

# # print(next(g))
# # print(next(g))


# # from pip import main

# # if __name__ == '__main__':

# #     process = 5
# #     P = process * process

# #     allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]

# #     max = [[7,5,3],[3,2,2],[9,0,2],[4,2,2],[5,3,3]]

# #     available = [3,3,2]

# #     need = [[0 for i in range(3)] for j in range(5)]     # Declare 2D array

# #     # Summation between maximum and allocation


# #     for i in range(5):
# #         for j in range(3):
# #             need[i][j] = max[i][j] - allocation[i][j]

# # process = []
# # finish = False

# # for x in range(2):
# #         for r in range(5):

# #                 flag = False
# #                 for c in range(3):
# #                         if (available[c] < need[r][c]):
# #                                 break

# #                 else:
# #                         flag = True
# #                         available[c] = available[c] + allocation[r][c]
# #                 if flag == True:
# #                         process.append(r)
# #         if finish == True:
# #                 break
# # print(process)






# Process_num = int(input("Enter total process number : "))
# resource_num = int(input("Enter total resource number : "))

# print("Enter allocation matrix ")
# allocation = [[int(i) for i in input().split()]for j in range(Process_num)]

# print("Enter Max_need matrix ")
# max = [[int(i) for i in input().split()]for j in range(Process_num)]

# print("Enter available matrix ")
# available = [int(i) for i in input().split()]

# need = [[0 for i in range(resource_num)] for j in range(Process_num)]               # Declare 2D array

# # Summation between maximum and allocation
# for i in range(Process_num):
#     for j in range(resource_num):
#         need[i][j] = max[i][j] - allocation[i][j]


# process = []

# for x in range(Process_num):
#     if len(process) == Process_num:
#         break
#     for r in range(Process_num):
#         if r in process:
#             continue

#     for c in range(resource_num):
#         if (available[c] < need[r][c]):
#             break

#     else:
#             for col in range(resource_num):
#                 available[col] = available[col] + allocation[r][col]
#             process.append(r)
            

# print(process)


# get = int(input())

# print(get)



# if __name__ == '__main__':
#     print("Enter how many proceess :",end="")
#     n = int(input())
    
#     avwt = 0; avtat = 0
#     arrival = []
#     burst= []
#     completion = []
#     tat = []

#     for i in range(n):
#         arrival.insert(i,int(input(f"Arrival time for p{i+1}: ")))           # Take arrival time.
        
#     for i in range(n):
#         burst.insert(i,int(input(f"Burst time for p{i+1}: ")))           # Take burst time.  
        
    # get = sorted(arrival,reverse=True)
    
    
    # min_at = [0]
    # for i in range(n):
    #     if 
        
      
# if __name__ == "__main__":
#     print("how many process: ",end="")
#     p = int(input())
    
#     at = []
#     bt = []
#     for i in range(p):
#         print(f"Enter arrival time of process{i}: ",end="")
#         at.append(int(input()))
#         print(f"Enter burst time of process{i}: ",end="")
#         bt.append(int(input()))
    
#     wt = []
#     tat = []
#     finish = 0
    
#     for i in range(p):
#         finish += bt[i]
#         wt.append(finish-bt[i]-at[i])
#         tat.append(wt[i]+bt[i])
    
#     print("Witing time")    
#     print(wt)
#     print("Turn around time time")    
#     print(tat)
    
#     temp_wt = 0
#     temp_tat = 0
#     for i in range(p):
#         temp_wt += wt[i]
#         temp_tat += tat[i]
        
#     print(temp_wt/p)
#     print(temp_tat/p)
    

list1 = [0,1,2,4]

list1.pop()

print(list1)