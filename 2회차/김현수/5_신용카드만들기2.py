import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
# 15자리 숫자를 줌, 마지막숫자N을 구해라
for i in range(1,T+1):
    number = input()
    number = number.replace('-','')
    #print(a)
    number_cnt = 16
    result_ = 0
    if number_cnt == len(number):
        if number[0] == '3' or number[0] == '4' or number[0] == '5' or number[0] == '6' or number[0] == '9':
            result_ = 1
    print(f'#{i} {result_}')