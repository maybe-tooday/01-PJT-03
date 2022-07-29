import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input()) #전체 케이스 수

for t in range(1,T+1):
    N = list(input()) #문자리스트로 입력받아서 써야겟다
# b <=> d ,  p <=> q
    #print(N,type(N[0]))받은 문자 리스트
    for i in range(len(N)) : #문자열이 싫으면 아카식으로 바꿧다가 다시 문자로 바꿔서도 가능할거 같다.
        if N[i] == 'b':
            N[i] = 'd'        
        elif N[i] == 'p':
            N[i] = 'q'
        elif N[i] == 'd':
            N[i] = 'b'
        elif N[i] == 'q':
            N[i] = 'p'
    else:
        #print(N) 뒤집혔느지 확인용
        word = ''.join(N) #리스트를 다시 문자열로 합쳐줘. 
        word_rev = word[::-1] #역순으로 출력시켜줘
        print(f'#{t} {word_rev}')