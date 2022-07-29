import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for i in range(1,T+1):
    number = input()
    number = number.replace('-','') #'-'잘라서 붙여줘-> '-'잘라서 ''을 넣어줘
    #print(a)
    number_cnt = 16
    result_ = 0
    if number_cnt == len(number):
        if number[0] == '3' or number[0] == '4' or number[0] == '5' or number[0] == '6' or number[0] == '9':
            result_ = 1
    print(f'#{i} {result_}')