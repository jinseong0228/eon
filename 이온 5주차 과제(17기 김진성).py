n = int(input("숫자 입력 : "))  #숫자 입력

def a(n):      # 함수 정의 
    if n== 1 or n == 2:     # n=1,2 일때 1 리턴
        return 1 
    else:                    
        return a(n-1) + a(n-2)   # n>=3 일때 해당 수식 사용해서 리턴

print(a(n+1))  #a(n+1) 출력
