def get_sum(arr):        #get_sum 함수 선언
    
 total = 0           #total의 초기값 0 대입
 for x in arr:       #for 반복문 사용
     total = total + x
 return total        #반복문 끝나고 total 값 반환

a = []                #a를 list로 사용
a.extend(map(int,input('합을 구할 수를 입력하세요: ').split())) #숫자입력을 받아 공백제거(split) 후 정수로 변환하고 a의 리스트에 대입
print(get_sum(a))    #get_sum함수에 a 인수를 넣어 출력