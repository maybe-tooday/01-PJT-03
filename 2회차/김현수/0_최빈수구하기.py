import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input()) #테스트 케이스 수 입력
#테스트 케이스 번호와 내용을 두줄로 같이 입력받는다 .1000명!!


for num in range(1,T+1):
    cnt_dict = dict() # ={}와 같다 반복될때마다 새로 정의해준다야하므로 반복문에 넣어준다
    case_num = int(input()) #string '1' '2' -int로 해도 되지않나
    case_list = list(map(int,input().split()))

    for i in case_list: #케이스리스트를 가지고 각숫자의갯수가 들어가는 리스트 작성
        if i in cnt_dict:
            cnt_dict[i] += 1
        else:
            cnt_dict[i] = 1
    #print(f'#{num} {cnt_dict}') #딕셔너리가 잘 만들어졌나 테스트

    max_number = 0 #최대수를 넣으려고했는데 비교대상이 필요하네. 카운터로 사용해야겟다
    number_ = 0 
    for key in cnt_dict: #key는 숫자, cnt_dict[key]는 key의갯수
        if max_number < cnt_dict[key]: #key값의 카운터가 더 높을떄
            max_number = cnt_dict[key] #해당 카운터 저장
            number_ = key #카운터가 높은숫자를 저장
        elif max_number == cnt_dict[key]: #key값과 카운터가 같을떄
            if number_ < key: #숫자가 높을것을 저장
                number_ = key
    print(f'#{num} {number_}')