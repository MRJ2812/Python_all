# # # # # # color_dict = {'red':'#FF00joy',
# # # # # #           'green':'#008000',
# # # # # #           'black':'#000000',
# # # # # #           'white':'#FFFFFF'}

# # # # # # [print(i,color_dict[i]) for i in sorted(color_dict)]


# # # # # ## String assignment
# # # # # #7

# # # # # # sam = 'The lyrics is poor!'
# # # # # # sam2 = sam.replace('!', '')

# # # # # # no = sam2.find('not')
# # # # # # poor = sam2.find('poor')


# # # # # # if poor > no and no > 0:
# # # # # #     print(sam2.replace(sam2[no:poor+4],'good'))


# # # # # # find = False

# # # # # # for i in sam.split():
# # # # # #     if i == 'not':
# # # # # #         find = True
# # # # # #     if i == 'poor' and find == True:
# # # # # #         print("find")


# # # # # # for i in sam.split():
# # # # # #     if i == 'poor':
# # # # # #         print("yap")
# # # # # #         find = True
# # # # # #     if i == 'poor' and find == True:
# # # # # #         print("find")


# # # # #     # if i == 'not':

# # # # #     # if i == 'not':
# # # # #     #     print(sam[i]))


# # # # # # list1 = [10,20,30,40,50,60]

# # # # # # del list1[1:3]

# # # # # # # list1[1:3] = 'good'

# # # # # # print(list1)


# # # # # # func = lambda x : x%2 == 0

# # # # # # print(func(10))

# # # # # # lt = [10,15,20,25,30]

# # # # # # print(list(filter(lambda x : x%2 ==0,lt)))


# # # # # # def add(list1):
# # # # # #     return (list1 * list1)

# # # # # # list1 = [10,20,30]

# # # # # # print(list(map(lambda x : x*x,list1)))


# # # # # # add(list)


# # # # # # from functools import reduce

# # # # # # list1 = [10,20,30]

# # # # # # get = reduce(lambda x,y : x*y ,list1)
# # # # # # print(get)


# # # # # # def sum1(i):
# # # # # #     return i+i

# # # # # # def malti(i):
# # # # # #     return i*i

# # # # # # list1 = [sum1,malti]

# # # # # # print(list(map(lambda x: x(10) ,list1)))

# # # # # # def sum1(i):
# # # # # #      return i+i

# # # # # # list1 = [10,20,30,40,50]

# # # # # # print(list(map(sum1 ,list1)))

# # # # # # student = [{'id': 1, 'success': True, 'name': 'Lary'},
# # # # # #  {'id': 2, 'success': False, 'name': 'Rabi'},
# # # # # #  {'id': 3, 'success': True, 'name': 'Alex'}]

# # # # # # count = 0
# # # # # # for i in student:
# # # # # #     count += i['success']

# # # # # # print(count)


# # # # # # list1 = [10,20,30,40,50]

# # # # # # dic = current = {}

# # # # # # current[1] = {}
# # # # # # current = current[1]
# # # # # # print(current)

# # # # # # print(dic)


# # # # # # dic = {}
# # # # # # for i in range(len(list1)-1,-1,-1):
# # # # # #     if not i == -1:
# # # # # #         dic[list1[i]] = list1[i-1]
# # # # # #     # if i = len(list1):
# # # # # #     # dic[i] =

# # # # # #     # if not i+1 == len(list1):
# # # # # #     #     dic[list1[i]] = list1[i+1]

# # # # # # print(dic)

# # # # # # string = 'W3resource'

# # # # # # list1 = []
# # # # # # dic = {}
# # # # # # list2 = []

# # # # # # for i in string:
# # # # # #     list1.append(i)

# # # # # # for i in list1:
# # # # # #     if i not in list2:
# # # # # #         dic[i] = list1.count(i)
# # # # # #         print(i,"=",list1.count(i))
# # # # # #     list2.append(i)


# # # # # # student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

# # # # # # dic = {}

# # # # # # for keys,values in student_list.items():
# # # # # #     dic[keys.replace(' ','')] = values


# # # # # # print(dic)


# # # # # # name = 'hi my name is joy'

# # # # # # new = name.replace(' ','')

# # # # # # print(new)

# # # # # # list1 = []
# # # # # # for k,v in Sample_data.items():
# # # # # #     list1.append(v)

# # # # # # list1.sort(reverse = True)
# # # # # # dic = {}
# # # # # # n = 0

# # # # # # for i in list1:
# # # # # #     for k,v in Sample_data.items():
# # # # # #         if i == v:
# # # # # #             dic[k] = i

# # # # # # print(dic)


# # # # # # for k,v in dic.items():


# # # # # # Sample_data = {'item1': [10,20,30]}

# # # # # # new = list(map(len,Sample_data.values()))

# # # # # # print(new)

# # # # # # student_d= [
# # # # # #   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
# # # # # #   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
# # # # # #   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# # # # # # ]

# # # # # # new_list = []

# # # # # # for i in student_d:
# # # # # #     new_list.append(i)


# # # # # # print(new_list)

# # # # #     # new_dic['id'] = student_d['id']
# # # # #     # new_dic['subject'] = i['subject']
# # # # #     # new_dic['V+VI'] = i['V'] + i['VI']

# # # # # # print(new_dict)

# # # # # # string = 'Thep lyrics is not that poor The lyrics is poor'

# # # # # # print(string.index('poor'))


# # # # # # list1 = ["j","o","y"]

# # # # # # list1.pop('j')

# # # # # # print(list1)


# # # # # # dic = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# # # # # # new_dic = {}

# # # # # # for k,v in dic.items():
# # # # # #     if v == None:
# # # # # #         pass
# # # # # #     else:
# # # # # #         new_dic[k] = v
# # # # # # print(new_dic)


# # # # # # list1 = [1,2,3,4]
# # # # # # dic = {}

# # # # # # for i in range(len(list1),-1,-1):
# # # # # #      dic[i]={}
# # # # # #      print(dic)

# # # # # # ------------------------------ 5
# # # # # # string = ('abc', 'xyz')
# # # # # # txt1 = string[1][:2] + string[0][-1]
# # # # # # txt2 = string[0][:2] + string[1][-1]


# # # # # # print(txt1 + " " + txt2)


# # # # # # string[0][0], string[0][1]   = string[1][0],string[1][1]
# # # # # # print(string)

# # # # # # emp = ''

# # # # # # for i in string:

# # # # # #     # emp += i+' '

# # # # # # print(emp)


# # # # # # get = input()

# # # # # # # if len(get) < 3:
# # # # # #     print(get)
# # # # # # else:
# # # # # #     if get[-3:] == "ing":
# # # # # #         print(get+'ly')
# # # # # #     else:
# # # # # #         print(get+'ing')


# # # # # # words_list = ["PHP", "Exercises", "Backend"]
# # # # # # word_len = []

# # # # # # for n in words_list:
# # # # # #         word_len.append((len(n), n))
# # # # # # word_len.sort()

# # # # # # print(word_len)


# # # # # # def test(n):
# # # # # #     new = ""
# # # # # #     new = n
# # # # # #     print(new)

# # # # # # test(100)


# # # # # # class triangle:
# # # # # #     height = 'joy'
# # # # # #     def __init__(self,base,height):
# # # # # #         print(self.height)
# # # # # #         self.base = base
# # # # # #         self.height = height

# # # # # #     def display(self):
# # # # # #         print(self.base * self.height)

# # # # # # std = triangle(10,20)
# # # # # # std1 = triangle(100,200)

# # # # # # std.display()
# # # # # # std1.display()

# # # # # # try:
# # # # # #    sum = 10 + 'h'
# # # # # #    print(sum)

# # # # # # except :
# # # # # #     print("yu")

# # # # # # finally:
# # # # # #     print("If exception can't handle then finally work")


# # # # # # def new(self,name,roll):
# # # # # #     self.name = name


# # # # # # class Student:
# # # # # #     def __init__(self,name,roll):
# # # # # #         self.name = name
# # # # # #         self.roll = roll

# # # # # # student_oj = Student('joy',100)

# # # # # # # print(student_oj.name)

# # # # # # print(getattr(student_oj,roll))


# # # # # # def function():
# # # # # #     return print


# # # # # # print(function())

# # # # # # def decor(func):
# # # # # #     def wrap():
# # # # # #         print("============")
# # # # # #         func()
# # # # # #         print("============")
# # # # # #     return wrap

# # # # # # def print_text():
# # # # # #     print("Hello world!")

# # # # # # decorated = decor(print_text)
# # # # # # decorated()


# # # # # # def xargs(*all):
# # # # # #     for i in all:
# # # # # #         print(i)

# # # # # # xargs(10,20,30,40)


# # # # # # print(10000/1.1**1)


# # # # # print("Enter dicount rate: ")
# # # # # R = int(input()) / 100
# # # # # print("Enter investment: ")
# # # # # C = int(input())
# # # # # print("enter year")
# # # # # temp = int(input())

# # # # # print("Enter all cashflow: ")

# # # # # sum = 0
# # # # # j = 1
# # # # # for i in range(temp):
# # # # #     sum += int(int(input())/ ((1+R)**j))
# # # # #     j += 1

# # # # # string2 = 'my name'


# # # # # print(string2.title())

# # # # # list2 = [1,2,3,4,5,6]
# # # # # get = sorted(list2,reverse=True)
# # # # # list1 = [1,2,3,4]

# # # # # get = (filter(lambda x : x%2 == 0, list1))

# # # # # for i in get:
# # # # #     print (i)


# # # # # for i in (lambda x : x%2 == 0, list1):
# # # # #     print (i)

# # # # # def date_of_birth_func(date_of_birth):

# # # # #     if date_of_birth > 2022:
# # # # #         raise ValueError("You liar")

# # # # #     age = int(input())

# # # # #     print(f"Your age will 100 in year {( 100 - age) + 2022} ")

# # # # #     any_year = int(input())

# # # # #     print(f" {any_year - 1997} ")


# # # # # date_of_birth = int(input())
# # # # # date_of_birth_func(date_of_birth)


# # # # # try:
# # # # #     get = int(input())

# # # # #     minimum = int(input())
# # # # #     maximum = int(input())


# # # # # except Exception as e:
# # # # #     print("put inteteger asshole")
# # # # #     exit()

# # # # # if minimum > maximum:
# # # # #      raise ValueError("I will Kill you")
# # # # # elif minimum == maximum:
# # # # #     print("Fuck you")
# # # # # else:
# # # # #     for i in range(minimum,maximum+1):
# # # # #         if get % i == 0:
# # # # #             print(f"{get} is divisable by {i} ")
# # # # #         else:
# # # # #             print(f"{get} is not divisable by {i}")


# # # # # get = [int(i) for i in input().split()]
# # # # # new = []
# # # # # c = len(get)
# # # # # for i in get:
# # # # #     new.append(get[c-1])
# # # # #     c -= 1

# # # # # print(new)

# # # # # print(get[::-1])

# # # # # get.sort(reverse = True)
# # # # # print(get)


# # # # # for i in range(minimum,maximum+1):
# # # # #     if get % i == 0:
# # # # #             print(f"{get} is divisable by {i} ")
# # # # #     else:
# # # # #         print(f"{get} is not divisable by {i}")


# # # # # array=[10,20,30,40]
# # # # # list1 = array
# # # # # list1.sort(reverse=True)

# # # # # print(list1)
# # # # # print(array)

# # # # # get = str(input())

# # # # # new = ""
# # # # # for i in reversed(get):
# # # # #     new = new + i

# # # # # if get == new:
# # # # #     print("pelindrom")
# # # # # else:
# # # # #     print("not pelindrom")

# # # # # temp = get
# # # # # new = temp.sort(reverse=True)

# # # # # print(new)


# # # # # list1 = [int(i) for i in input().split()]

# # # # # new_list = []

# # # # # for l in list1:

# # # # #     if l < 10:
# # # # #         pass
# # # # #     else:
# # # # #         for i in range(l,l+100):
# # # # #             new = ""

# # # # #             for j in reversed(str(i)):
# # # # #                 new += j
# # # # #             if new == str(i):
# # # # #                 new_list.append(i)
# # # # #                 break

# # # # # print(new_list)


# # # # # get = input("Enter: ")
# # # # # get = "python is"
# # # # # get = get.lower().split()

# # # # # # print(get)

# # # # # list1 = ["python is not python","python is good","this is good"]
# # # # # new_list = []

# # # # # for i in list1:
# # # # #     count = 0

# # # # #     temp = []
# # # # #     temp = i.split()

# # # # #     for s in get:
# # # # #         for j in temp:
# # # # #             if s == j:
# # # # #                 count += 1

# # # # #     if count >= 1:
# # # # #         new_list.append(i)


# # # # # print(new_list)


# # # # # list1 = [10, 30, 40]

# # # # # for i in list1:
# # # # #     for j in list1:
# # # # #         if j > i:
# # # # #             print(f"{j}")
# # # # # list1[i],list1[j] = list1[j],list1[i]


# # # # # print(list1)

# # # # #

# # # # # num = int(input())

# # # # # def multiplication(num):
# # # # #     list1 = []
# # # # #     for i in range(1,10):
# # # # #         # print(f"{num} X {i} = {num*i}")
# # # # #         list1.append(num*i)
# # # # #     # print(list1)
# # # # #     return list1

# # # # # list1 = [6,12,18,26,30,36,42,48,54,60]

# # # # # def isCorrect(num_list,num):
# # # # #     for i in range(1,10):
# # # # #         if num_list[i-1] != i * num:
# # # # #             print(num_list[i-1])
    
# # # # # isCorrect(list1,6)








# # # # # from pip import main

# # # # # if __name__ == '__main__':

# # # # #     process = 5
# # # # #     P = process * process

# # # # #     allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]  

# # # # #     max = [[7,5,3],[3,2,2],[9,0,2],[4,2,2],[5,3,3]] 

# # # # #     available = [3,3,2]

# # # # #     need = [[0 for i in range(3)] for j in range(5)]     # Declare 2D array 

# # # # #     # Summation between maximum and allocation

  
# # # # #     for i in range(5):
# # # # #         for j in range(3):
# # # # #             need[i][j] = max[i][j] - allocation[i][j]

# # # # #     # for i in range(5):
# # # # #     #     for j in range(3):
# # # # #     #         print(f"{need[i][j]}")
# # # # #     #     print("\n")

            
    

# # # # # process = []

# # # # # for x in range(2):
# # # # #     for r in range(5):
# # # # #         flag = False
# # # # #         for c in range(3):
# # # # #             if (available[c] < need[r][c]):
# # # # #                 break
            
# # # # #             else:
# # # # #                 flag = True
# # # # #                 available[c] = available[c] + allocation[r][c]
# # # # #         if flag == True:
# # # # #             process.append(r)

# # # # # print(process)

# # # # # allocation = [[int(i) for i in input().split()]for j in range(5)]

# # # # # print(allocation)
# # # # # for i in range(5):
# # # # #     for j in range(5):
# # # # #         print(allocation[i])

# # # # # from enum import Flag


# # # # # Process_num = int(input("Enter total process number : "))
# # # # # resource_num = int(input("Enter total resource number : "))

# # # # # print("Enter allocation matrix ")
# # # # # allocation = [[int(i) for i in input().split()]for j in range(Process_num)]

# # # # # print("Enter Max_need matrix ")
# # # # # max = [[int(i) for i in input().split()]for j in range(Process_num)]

# # # # # print("Enter available matrix ")
# # # # # available = [int(i) for i in input().split()]

# # # # # need = [[0 for i in range(resource_num)] for j in range(Process_num)]               # Declare 2D array


# # # # # # Summation between maximum and allocation
# # # # # for i in range(Process_num):
# # # # #     for j in range(resource_num):
# # # # #         need[i][j] = max[i][j] - allocation[i][j]

# # # # # process = []

# # # # # for r in range(5):
# # # # #     # flag = False

# # # # #     for c in range(4):
# # # # #         if available[c] < need[r][c]:
# # # # #             break           
# # # # #     else:
# # # # #         for col in range(4):
# # # # #             available[col] = available[col] + allocation[r][col]
# # # # #         process.append(r)

# # # # # print(process)
# # # #     # print("\n")








# # # # # for x in range(Process_num):
# # # # #     for r in range(Process_num):
# # # # #         flag = False
# # # # #         if r in process:
# # # # #             continue
# # # # #         for c in range(resource_num):
# # # # #             if (available[c] < need[r][c]):              
# # # # #                 break

# # # # #             else:
# # # # #                 print(f"-----------{r}----------------")
# # # # #                 print(f"{available[c] , need[r][c]} = {available[c] < need[r][c]} ")
                
# # # # #                 flag = True
# # # # #                 available[c] = available[c] + allocation[r][c]
        
# # # # #         if flag == True:
            
# # # # #             process.append(r)
    

# # # # # # print(process)

# # # # # if __name__ == '__main__':

# # # # #     Process_num = int(input("Enter total process number : "))
# # # # #     resource_num = int(input("Enter total resource number : "))

# # # # #     print("Enter allocation matrix ")
# # # # #     allocation = [[int(i) for i in input().split()]for j in range(Process_num)]

# # # # #     print("Enter Max_need matrix ")
# # # # #     max = [[int(i) for i in input().split()]for j in range(Process_num)]

# # # # #     print("Enter available matrix ")
# # # # #     available = [int(i) for i in input().split()]

# # # # #     need = [[0 for i in range(resource_num)] for j in range(Process_num)]               # Declare 2D array

# # # # #     # Summation between maximum and allocation
# # # # #     for i in range(Process_num):
# # # # #         for j in range(resource_num):
# # # # #             need[i][j] = max[i][j] - allocation[i][j]

# # # # #     print(need)
# # # # #     process = []

# # # # #     for x in range(Process_num):
# # # # #         if len(process) == Process_num:
# # # # #             break
# # # # #         for r in range(Process_num):
# # # # #             if r in process:
# # # # #                 continue

# # # # #             for c in range(resource_num):
# # # # #                 if (available[c] < need[r][c]):
# # # # #                     break

# # # # #             else:
# # # # #                 for col in range(resource_num):
# # # # #                     available[col] = available[col] + allocation[r][col]
# # # # #                 process.append(r)

# # # # #     print(process)

# # # # # 
# # # # # 

# # # # # Process_num = int(input("Enter total process number : "))
# # # # # resource_num = int(input("Enter total resource number : "))

# # # # # print("Enter allocation matrix ")
# # # # # allocation = [[int(i) for i in input().split()]for j in range(Process_num)]

# # # # # print("Enter Max_need matrix ")
# # # # # max = [[int(i) for i in input().split()]for j in range(Process_num)]

# # # # # print("Enter available matrix ")
# # # # # available = [int(i) for i in input().split()]

# # # # # need = [[0 for i in range(resource_num)] for j in range(Process_num)]               # Declare 2D array

# # # # # # Summation between maximum and allocation
# # # # # for i in range(Process_num):
# # # # #     for j in range(resource_num):
# # # # #         need[i][j] = max[i][j] - allocation[i][j]

# # # # # print(allocation)
# # # # # print(available)
# # # # # print(need)
# # # # # process = []

# # # # # for x in range(Process_num):
# # # # #     # if len(process) == Process_num:
# # # # #     #     break
# # # # #     # for r in range(Process_num):
# # # # #     #     if r in process:
# # # # #     #         continue

# # # # #     for c in range(resource_num):
# # # # #         if (available[c] < need[r][c]):
# # # # #             break

# # # # #     else:
# # # # #             for col in range(resource_num):
# # # # #                 available[col] = available[col] + allocation[r][col]
# # # # #             process.append(r)

# # # # # print(process)




# # # # # Process_num = int(input("Enter total process number : ")) 
# # # # # resource_num = int(input("Enter total resource number : ")) 
# # # # # print("Enter allocation matrix ") 
# # # # # allocation = [[int(i) for i in input().split()]for j in range(Process_num)] 
# # # # # print("Enter Max_need matrix ") 
# # # # # max = [[int(i) for i in input().split()]for j in range(Process_num)] 
# # # # # print("Enter available matrix ") 
# # # # # available = [int(i) for i in input().split()] 
# # # # # need = [[0 for i in range(resource_num)] for j in range(Process_num)] # Declare 2D array 

# # # # # # Summation between maximum and allocation 
# # # # # for i in range(Process_num): 
# # # # #     for j in range(resource_num): 
# # # # #         need[i][j] = max[i][j] - allocation[i][j] 
        
# # # # # process = [] 

# # # # # for x in range(Process_num): 
# # # # #     if len(process) == Process_num: 
# # # # #         break 
# # # # #     for r in range(Process_num): 
# # # # #         if r in process: 
# # # # #             continue 
# # # # #         for c in range(resource_num): 
# # # # #             if (available[c] < need[r][c]): 
# # # # #                 break 
# # # # #         else: 
# # # # #             for col in range(resource_num): 
# # # # #                 available[col] = available[col] + allocation[r][col] 
# # # # #             process.append(r) 
        
# # # # # print(process)


# # # # # from pip import main


# # # # # if __name__ == '__main__':
# # # # #     n = int(input())
# # # # #     arr = list(map(int, input().split()))
    
    
# # # # #     max = arr[0]
# # # # #     for i in range(len(arr)):
# # # # #         if max < arr[i]:
# # # # #             max = arr[i]
          
# # # # #     temp = 0
    
# # # # #     for i in range(len(arr)):
# # # # #         if  arr[i] < max :
# # # # #             for j in range(len(arr)):
# # # # #                 if arr[i] > arr[j]:
# # # # #                     temp = arr[i]

# # # # #             if temp == 0:
# # # # #                 temp = arr[i]
                
# # # # #     print(temp)


# # # # # if __name__== '__main__':
    
# # # # #     arr = list(set(list(map(int, input().split()))))
    
# # # # #     arr.sort()
    
# # # # #     print(arr[-2])



# # # # # from pip import main


# # # # # if __name__ == '__main__':
# # # # #     n = 3; bt=[24,3,3]; avwt = 0; avtat = 0
    
# # # # #     wt = []
# # # # #     tat = []
    
# # # # #     wt.insert(0,0)                   # First process waiting time is always 0
    
      
    
# # # # #     for i in range(1,3):
# # # # #         wt.insert(i,bt[i-1]+wt[i-1])     # Here arrival time will minus

# # # # #     print("Processes  Burst Time  Waiting Time  Turnaround Time")
    
# # # # #     for i in range(3):
# # # # #        tat.insert(i,bt[i]+wt[i])
# # # # #        avwt+=wt[i]
# # # # #        avtat+=tat[i]
       
# # # # #        print(f"p{[i]}        {bt[i]}            {wt[i]}           {tat[i]}")
       
# # # # #     avwt/=3
# # # # #     avtat/=3
    
# # # # #     print(f"Average waiting time{avwt}") 
# # # # #     print(f"Average turnaround time {avtat}") 
        
    

# # # # # if __name__ == '__main__':
# # # # #     print("Enter how many proceess :",end="")
# # # # #     n = int(input())
    
# # # # #     arrival = []
# # # # #     burst= []
# # # # #     completion = []
# # # # #     tat = []

# # # # #     for i in range(n):
# # # # #         arrival.insert(i,int(input(f"Arrival time for p{i+1}: ")))           # Take arrival time.
        
# # # # #     for i in range(n):
# # # # #         burst.insert(i,int(input(f"Burst time for p{i+1}: ")))           # Take burst time.  
        
# # # # #     check_burst = sorted(burst,reverse=True)
    
    
        
# # # # # class RoundRobin:

# # # # #     def processData(self, no_of_processes):
# # # # #         process_data = []
# # # # #         for i in range(no_of_processes):
# # # # #             temporary = []
# # # # #             process_id = int(input("Enter Process ID: "))

# # # # #             arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))

# # # # #             burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))

# # # # #             temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
# # # # #             '''
# # # # #             '0' is the state of the process. 0 means not executed and 1 means execution complete
            
# # # # #             '''
# # # # #             process_data.append(temporary)

# # # # #         time_slice = int(input("Enter Time Slice: "))

# # # # #         RoundRobin.schedulingProcess(self, process_data, time_slice)

# # # # #     def schedulingProcess(self, process_data, time_slice):
# # # # #         start_time = []
# # # # #         exit_time = []
# # # # #         executed_process = []
# # # # #         ready_queue = []
# # # # #         s_time = 0
# # # # #         process_data.sort(key=lambda x: x[1])
# # # # #         '''
# # # # #         Sort processes according to the Arrival Time
# # # # #         '''
# # # # #         while 1:
# # # # #             normal_queue = []
# # # # #             temp = []
# # # # #             for i in range(len(process_data)):
# # # # #                 if process_data[i][1] <= s_time and process_data[i][3] == 0:
# # # # #                     present = 0
# # # # #                     if len(ready_queue) != 0:
# # # # #                         for k in range(len(ready_queue)):
# # # # #                             if process_data[i][0] == ready_queue[k][0]:
# # # # #                                 present = 1
# # # # #                     '''
# # # # #                     The above if loop checks that the next process is not a part of ready_queue
# # # # #                     '''
# # # # #                     if present == 0:
# # # # #                         temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
# # # # #                         ready_queue.append(temp)
# # # # #                         temp = []
# # # # #                     '''
# # # # #                     The above if loop adds a process to the ready_queue only if it is not already present in it
# # # # #                     '''
# # # # #                     if len(ready_queue) != 0 and len(executed_process) != 0:
# # # # #                         for k in range(len(ready_queue)):
# # # # #                             if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
# # # # #                                 ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
# # # # #                     '''
# # # # #                     The above if loop makes sure that the recently executed process is appended at the end of ready_queue
# # # # #                     '''
# # # # #                 elif process_data[i][3] == 0:
# # # # #                     temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
# # # # #                     normal_queue.append(temp)
# # # # #                     temp = []
# # # # #             if len(ready_queue) == 0 and len(normal_queue) == 0:
# # # # #                 break
# # # # #             if len(ready_queue) != 0:
# # # # #                 if ready_queue[0][2] > time_slice:
# # # # #                     '''
# # # # #                     If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
# # # # #                     '''
# # # # #                     start_time.append(s_time)
# # # # #                     s_time = s_time + time_slice
# # # # #                     e_time = s_time
# # # # #                     exit_time.append(e_time)
# # # # #                     executed_process.append(ready_queue[0][0])
# # # # #                     for j in range(len(process_data)):
# # # # #                         if process_data[j][0] == ready_queue[0][0]:
# # # # #                             break
# # # # #                     process_data[j][2] = process_data[j][2] - time_slice
# # # # #                     ready_queue.pop(0)
# # # # #                 elif ready_queue[0][2] <= time_slice:
# # # # #                     '''
# # # # #                     If a process has a remaining burst time less than or equal to time slice, it will complete its execution
# # # # #                     '''
# # # # #                     start_time.append(s_time)
# # # # #                     s_time = s_time + ready_queue[0][2]
# # # # #                     e_time = s_time
# # # # #                     exit_time.append(e_time)
# # # # #                     executed_process.append(ready_queue[0][0])
# # # # #                     for j in range(len(process_data)):
# # # # #                         if process_data[j][0] == ready_queue[0][0]:
# # # # #                             break
# # # # #                     process_data[j][2] = 0
# # # # #                     process_data[j][3] = 1
# # # # #                     process_data[j].append(e_time)
# # # # #                     ready_queue.pop(0)
# # # # #             elif len(ready_queue) == 0:
# # # # #                 if s_time < normal_queue[0][1]:
# # # # #                     s_time = normal_queue[0][1]
# # # # #                 if normal_queue[0][2] > time_slice:
# # # # #                     '''
# # # # #                     If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
# # # # #                     '''
# # # # #                     start_time.append(s_time)
# # # # #                     s_time = s_time + time_slice
# # # # #                     e_time = s_time
# # # # #                     exit_time.append(e_time)
# # # # #                     executed_process.append(normal_queue[0][0])
# # # # #                     for j in range(len(process_data)):
# # # # #                         if process_data[j][0] == normal_queue[0][0]:
# # # # #                             break
# # # # #                     process_data[j][2] = process_data[j][2] - time_slice
# # # # #                 elif normal_queue[0][2] <= time_slice:
# # # # #                     '''
# # # # #                     If a process has a remaining burst time less than or equal to time slice, it will complete its execution
# # # # #                     '''
# # # # #                     start_time.append(s_time)
# # # # #                     s_time = s_time + normal_queue[0][2]
# # # # #                     e_time = s_time
# # # # #                     exit_time.append(e_time)
# # # # #                     executed_process.append(normal_queue[0][0])
# # # # #                     for j in range(len(process_data)):
# # # # #                         if process_data[j][0] == normal_queue[0][0]:
# # # # #                             break
# # # # #                     process_data[j][2] = 0
# # # # #                     process_data[j][3] = 1
# # # # #                     process_data[j].append(e_time)
# # # # #         t_time = RoundRobin.calculateTurnaroundTime(self, process_data)
# # # # #         w_time = RoundRobin.calculateWaitingTime(self, process_data)
# # # # #         RoundRobin.printData(self, process_data, t_time, w_time, executed_process)

# # # # #     def calculateTurnaroundTime(self, process_data):
# # # # #         total_turnaround_time = 0
# # # # #         for i in range(len(process_data)):
# # # # #             turnaround_time = process_data[i][5] - process_data[i][1]
# # # # #             '''
# # # # #             turnaround_time = completion_time - arrival_time
# # # # #             '''
# # # # #             total_turnaround_time = total_turnaround_time + turnaround_time
# # # # #             process_data[i].append(turnaround_time)
# # # # #         average_turnaround_time = total_turnaround_time / len(process_data)
# # # # #         '''
# # # # #         average_turnaround_time = total_turnaround_time / no_of_processes
# # # # #         '''
# # # # #         return average_turnaround_time

# # # # #     def calculateWaitingTime(self, process_data):
# # # # #         total_waiting_time = 0
# # # # #         for i in range(len(process_data)):
# # # # #             waiting_time = process_data[i][6] - process_data[i][4]
# # # # #             '''
# # # # #             waiting_time = turnaround_time - burst_time
# # # # #             '''
# # # # #             total_waiting_time = total_waiting_time + waiting_time
# # # # #             process_data[i].append(waiting_time)
# # # # #         average_waiting_time = total_waiting_time / len(process_data)
# # # # #         '''
# # # # #         average_waiting_time = total_waiting_time / no_of_processes
# # # # #         '''
# # # # #         return average_waiting_time

# # # # #     def printData(self, process_data, average_turnaround_time, average_waiting_time, executed_process):
# # # # #         process_data.sort(key=lambda x: x[0])
# # # # #         '''
# # # # #         Sort processes according to the Process ID
# # # # #         '''
# # # # #         print("Process_ID  Arrival_Time  Rem_Burst_Time   Completed  Original_Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time")
# # # # #         for i in range(len(process_data)):
# # # # #             for j in range(len(process_data[i])):

# # # # #                 print(process_data[i][j], end="				")
# # # # #             print()

# # # # #         print(f'Average Turnaround Time: {average_turnaround_time}')

# # # # #         print(f'Average Waiting Time: {average_waiting_time}')

# # # # #         print(f'Sequence of Processes: {executed_process}')


# # # # # if __name__ == "__main__":
# # # # #     no_of_processes = int(input("Enter number of processes: "))
# # # # #     rr = RoundRobin()
# # # # #     rr.processData(no_of_processes)




# # # # # if __name__ == '__main__':
# # # # #     print("Enter how many proceess :",end="")
# # # # #     n = int(input())
    
# # # # #     avwt = 0; avtat = 0
# # # # #     arrival = []
# # # # #     burst= []
# # # # #     completion = []
# # # # #     tat = []

# # # # #     for i in range(n):
# # # # #         arrival.insert(i,int(input(f"Arrival time for p{i+1}: ")))           # Take arrival time.
        
# # # # #     for i in range(n):
# # # # #         burst.insert(i,int(input(f"Burst time for p{i+1}: ")))           # Take burst time.  
        
        
# # # # #     temp_burst = get = sorted(burst,reverse=True)
    
    


# # # # from cProfile import run
# # # # from pip import main
# # # # # def waiting_time(p,at,bt):



# # # # if __name__ == "__main__": 
# # # #     print("Enter how many process")
# # # #     p = int(input())


# # # #     at = [] * p
# # # #     bt = [] * p
# # # #     wt = [] * p

# # # #     for i in range(p):
# # # #         print("Arrival time of process",i)
# # # #         at.append(int(input()))
        
# # # #     for i in range(p):
# # # #         print("Burst time of process",i)
# # # #         bt.append(int(input()))
    
 
    
# # # #     running_time = 0
    
# # # #     finish = 0
    
# # # #     for i in range(p):
# # # #         if at[i] == running_time:          
# # # #             finish = finish + bt[i] 

# # # #             wt.append(finish - at[i] - bt[i])
        
# # # #         running_time += 1
    
# # # #     print(wt)


# # # lst = [['1', 'A', 2, 5, 45, 10],
# # #  ['2', 'B', 8, 15, 65, 20],
# # #  ['3', 'C', 32, 35, 25, 140],
# # #  ['4', 'D', 82, 305, 75, 90],
# # #  ['5', 'E', 39, 43, 89, 55],
# # #  ]

# # # lst = sorted(lst, key=lambda x: x[2])
# # # print(lst)

# # array = [10,3,4,9]
# # array = sorted(array,reverse=True)[1]

# # print(array)



# # value = 0
# # for i in array:
# #     if max < i:
# #          for j in array:
# #              if i <= j:
# #                  value = i

# # print(value)
        

# # # for i in array:
# # #     if i < max:
# # #         c = 0
# # #         for j in array:
# # #             if i > j:
# # #                 c+=1
# # #         if c == len(array):
# # #             value = i
        
# # # for i in range(len(array)-1):
    
    
# # marksheet = []
# # for _ in range(0,int(input())):
# #     marksheet.append([input(), float(input())])
    
# # second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]

    
    
# # for i in range(len(second_highest)):
# #     print(second_highest)


# # marksheet = [10,10,3,9,9]
# # for _ in range(0,int(input())):
# #     marksheet.append([input(), float(input())])

# # second_highest = sorted(list(set(marksheet)))[1]
# # print(second_highest)





# # for i in range(v):
# #       ar.append([input("Name: ",),int(input()),int(input()),int(input())])

# # v = int(input())

# # ar = [[str(i) for i in input().split()] for j in range(v)]
      
# # get = input("Enter search name: ")
# # sum = 0
# # for i in range(len(ar)):
# #     if ar[i][0] == get:
# #         for j in range(1,4):
# #             sum+= int(ar[i][j])
            
# # print("Average :",sum/3)     

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
        
#     query_name = input()
#     sum = 0
#     for k,v in student_marks.items():
#         if k == query_name:
#             for i in v:
#                 sum += i
    
#     length_key = len(student_marks[query_name])     
    
       
#     print(f"{sum/length_key :0.2f}")


# if __name__=='__main__':
    
   
    
#     get = int(input())
    
#     l1 = []
    
#     for i in range(get):
#         command ,*v= input().split()
        
#         len1 = len(v)
        
#         if len1 == 2:
#             index = int(v[0])
#             value = int(v[1])
#         elif len1 == 1:
#             value = int(v[0])
        
#         if command == 'insert':
#             l1.insert(index,value)
#         elif command == 'print':
#             print(l1)
#         elif command == 'remove':
#             l1.remove(value)
#         elif command == 'append':
#             l1.append(value)
#         elif command == 'sort':
#             l1.sort()
#         elif command == 'pop':
#             l1.pop()
#         elif command == 'reverse':
#             l1.reverse()
        
#     len1 = 0

# if __name__ == '__main__':
    
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
    
 
                    
                    
#     list1 = [([i,j,k]) for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
                    
#     print(list1)
    
       # [print(i) for i in range(2)]
    # list1 = []
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if (i+j+k) != n:
    #                 list1.append([i,j,k])
    
    
# if __name__ == '__main__':
#     get = int(input())
#     list1 = [int(i) for i in input().split() ]
#     print(hash(tuple(list1)))
    

# from types import coroutine


# if __name__ == '__main__':
#     X = int(input())
    
#     enter = [int(i) for i in input().split()]
    
#     dic = {}
#     temp = []
    
#     for i in enter:
#         if i in temp:
#             continue
#         count = 0
#         for j in enter:
#             if i == j:
#                 count += 1
#         dic[i] = count
#         temp.append(i)
        
#     counter = dic.keys()
    
            
#     N = int(input("how many customer"))
    
#     total_amount = 0
    
#     for i in range(N):
#         customer_input = [int(i) for i in input().split()]
        
#         if customer_input[0] in counter:
#             if dic[customer_input[0]] == 0:
#                 continue
#             else:
#                 dic[customer_input[0]] = dic[customer_input[0]] -1
#                 total_amount = total_amount + customer_input[1]
#     print(total_amount)


# if __name__ == '__main__':
#     # loop = int(input())
    
#     # get = []
    
#     # for i in range(loop):
#     #     get.append(int(input()))
        
#     # print(tuple(get))
        
#     value = [int(i) for i in input().split() for i in range(2)]
    # print(hash(tuple(value)))
    
# def merge(s,k):
#     for i in range(len(s)):
#         temp = ''
#         store = ''
#         if i%k == 0:
#             for j in range(i,i+k):
#                 temp = temp + s[j]
#             else:
#                 for st in temp:
#                     if st in store:
#                         continue
#                     else:
#                         store = store + st
#             print(store)
            
    
# if __name__ == '__main__':
#     s = input()
#     k = int(input())
    
#     merge(s,k)
    
S, N = input(), int(input()) 
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
    
    
                    


                    
               

# for i in range(5):
#     print(i)
#     break
# else:
#     print("joy")       
                  
        
            

    

            
    