import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
# 15자리 숫자를 줌, 마지막숫자N을 구해라
for i in range(1,T+1): 
    sum_ = 0
    sum_num = 0
    card_num = list(map(int,input().split()))
    for j in range(len(card_num)): #카드숫자를 순회하는데 홀수자리일때 와 짝수자리일때 나누어 변환 
        if j%2 == 0: #홀수 자리인 경우
            sum_ += 2*(card_num[j])
            #print(sum_)
        elif j%2 == 1: #짝수 자리인 경우
            sum_ += card_num[j]
            #print(sum_)
    else:
        # 모든수를 합해서 첫번쨰 자리수만 알면 N값을 구할수 잇다.
        sum_num = (10 - sum_%10)%10 #다 더한값을 10으로 나눈 나머지를 구해서 10에서 뺸 나머지를 출력한다 N=10일경우를 제외하기 위하여 마지막에 %10를 넣는다.

    print(f'#{i} {sum_num}')