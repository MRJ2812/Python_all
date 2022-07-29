# from textwrap import shorten


# if __name__ == '__main__':

#     array = [] * 5
#     temp = [] * 5
    
#     num = int(input())

    
#     for i in range(num):
#         name = input()
#         score = float(input())
        
#         array.append([name,score])
#         temp.append(score)
        

    
#     temp = sorted(temp,reverse=True)
#     min = temp[-1]

#     value = 0
#     for i in temp:
#         if min < i:
#             for j in temp:
#                 if i <= j:
#                     value = i

    
#     final = []
#     for i in range(num):
#         if value == array[i][1]:
#             final.append(array[i][0])
            
#     final = sorted(final)
    
#     for i in range(len(final)):
#         print(final[i])
        
            
name, *line = input().split()

print(name)
print(line)
