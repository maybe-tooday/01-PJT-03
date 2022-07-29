import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for i in range(1,T+1):
    # 직사각형은 이루는 숫자가 2개밖에 없다.
    # 같은 숫자 2개를 제외하면 4번째 변의길이와 같은 값이 남는다
    # 3개의 숫자를 비교해서 같은면 빠지고 나머지 한개의 숫자가 4번쨰 변의길이와 같다
    a = list(map(int,input().split())) 
    b = 0 #4번쨰 변의 길이 넣을 변수
    if a[0] == a[1]:
        b = a[2]
    elif a[0] == a[2]:
        b = a[1]
    elif a[1] == a[2]:
        b = a[0]
        
    print(f'#{i} {b}')