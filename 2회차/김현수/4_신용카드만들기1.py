import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
# 15자리 숫자를 줌, 마지막숫자N을 구해라
for i in range(1,T+1):
    sum_ = 0
    sum_num = 0
    card_num = list(map(int,input().split()))
    for j in range(len(card_num)):
        if j%2 == 0:
            sum_ += 2*(card_num[j])
            #print(sum_)
        elif j%2 == 1:
            sum_ += card_num[j]
            #print(sum_)
    else:
        sum_num = (10 - sum_%10)%10

    print(f'#{i} {sum_num}')