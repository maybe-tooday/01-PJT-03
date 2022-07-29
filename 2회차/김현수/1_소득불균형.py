import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for i in range(1,T+1):
    N = int(input()) #갯수
    N_list = list(map(int,input().split()))
    avr = sum(N_list)/N #평균
    cnt = 0 #평균이하 인원수
    for n in N_list: #리스트에서 숫자를 하나씩 꺼내는 반복문을 쓰는데
        if n <= avr:  #평균보다 그숫자n가 낮거나 같으면
            cnt += 1  #카운트를 증가시킨다
    print(f'#{i} {cnt}')