import sys

sys.stdin = open("_암호문1.txt")

#리스트를 좌우로 나눈 다음에 중간에 값을 더하고 합하는게 편할것 같다.
def list_merge(list_,cut_,end_): #리스트, 컷할지점, 끝지점 - 나누어서 2개의 리스트로 반환한다 
    

    pass
    return


for T in range(10): #전체 케이스수 10개
    N = int(input()) #원본 암호문의 길이
    N_list = list(map(int,input().split())) #원본 암호문
    N_ord = int(input()) #명령어의 개수
    order_ = input().split('I') #I기준으로 잘라서 넣어줘 인덱스0 뺴고 차례대로 명력어가 입력된다.
    order_2 = dict()
    for n in range(1,N_ord+1):
        order_2[n-1] = list(map(int,order_[n].split()))
    print(N)
    print(N_list)
    print(N_ord)
    print(order_)
    print(order_2) #{넘버 :I규칙,
# N: 17
# N_list: [376463, 344210, 520543, 173961, 644251, 888643, 564430, 812181, 501113, 579019, 976154, 231393, 225736, 760717, 684571, 271257, 500013]
# N_ord: 5
# order_2 {
#   0: [8, 1, 141946], 
#   1: [9, 1, 199979], 
#   2: [0, 1, 596308], 
#   3: [14, 3, 719634, 168119, 401905], 
#   4: [7, 3, 787798, 136503, 153477]}
    #for i in range(N_ord): #0123456 입력 order_2.get(i)
        #order_2.get(i)[0] 몇번쨰부터 시작할까(인덱스 자리)
        #order_2.get(i)[1] 몇자리까지 갈까
        #order_2.get(i)[2~N_ord] 나머지 숫자