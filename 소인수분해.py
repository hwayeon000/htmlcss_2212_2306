# ctrl + F5

# 소인수분해
# def solution(n):
#     answer = []
#     div = 2
#     while n > 1:
#         if n % div == 0:
#             answer.append(div)
#             n /= div
#             int(n)
#         else:
#             div += 1
#     answer = sorted(list(set(answer)))
#     return answer

# 7의 개수
# def solution(array):
#     answer = 0
#     a = ""
#     for j in array:
#         a += str(j)
#     for i in a:
#         if i == "7":
#             answer += 1
#     return answer
# 다른사람 1
# def solution(array):
#     return ''.join(map(str, array)).count('7')
# 다른사람 2
# def solution(array):
#     return str(array).count('7')


# 공 던지기
# def solution(numbers, k):
#     answer = numbers[2*(k-1)%len(numbers)]
#     return answer
# numbers = [1, 2, 3, 4, 5, 6]
# k = 5
    
# 영어가싫어요
# def solution(numbers):
#     nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     for index, num in enumerate(nums):
#         numbers = numbers.replace(num, str(index))
#     numbers = int(numbers)
#     return numbers


# import re
# text = "ABC123ABC456DEF789"
# for text in re.finditer('ABC',text):
#     print(text.start())


# 잘라서 배열로 저장하기
my_str = "abcdef123"
n = 3
ans = ""
res = []
# div = int(len(my_str)/n)
# while div > 0:
#     for i in range(n):
#         ans += my_str[i]
#     my_str = my_str.replace(ans,"")
#     res.append(ans)
#     ans = ""
#     div -= 1
# if my_str != "" :
#     res.append(my_str)
# print(res)

# for i, str in enumerate(my_str, start=1):
#     ans += str
#     if i % n == 0:
#         my_str = my_str.replace(ans,"")
#         res.append(ans)
#         ans = ""
# if my_str != "":
#     res.append(my_str)
# print(res)




# 컨트롤제트
def solution(a):
    a = a.split(" ")
    print(a)
    res = 0
    j = 0
    for i in a:
        if i == "Z":
            res -= (int(a[j-1]))
        else:
            res += int(a[j])
        j += 1
    return res












# cnt = 1
# if cnt:
#     print("1")