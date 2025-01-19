# # # import time

# # # i = 0
# # # space = " "

# # # while True:
# # #     while i<=10:
# # #         print(f"{space*i}")
# # #         i+=1
# # #         time.sleep(0.1)

# # #     while i>1:
# # #         print(f"{space*i}")
# # #         i-=1
# # #         time.sleep(0.1)

# # import time

# # i = 0
# # space = " "
# # direction = 1  

# # while True:
# #     print(f"{space*i}🟥", end="\r")  
# #     i += direction

# #     if i > 50 or i < 0:
# #         direction *= -1  

# #     time.sleep(0.05)








# # n=3
# # stk = [[]]

# # while stk:
# #     current = stk.pop()
# #     if len(current) == n:
# #         print(current)

# #     else:
# #         for i in range(n):
# #             stk.append(current + [i])


# # str = "abcdefghijklm opqrstuvwxyz"

# # letters = set(char for char in str.lower() if 'a' <= char <= "z")

# # if len(letters) == 26:
# #     print("Panagram")
# # else:
# #     print("Not Pana")

# # integers = [2, 4, 0, 100, 4, 11, 2602, 36]

# # odd = [i for i in integers if i%2 != 0]
# # even = [i for i in integers if i%2 == 0]

# # if len(odd)==1:
# #     print(odd[0])
# # else:
# #     print(even[0])



# text = "the-stealth-warrior"

# words = text.replace("-", " ").replace("_"," ").split()

# camel = words[0] + "".join(i.capitalize() for i in words[1:])

# print(camel)