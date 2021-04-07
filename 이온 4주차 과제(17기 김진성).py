def array_slice(b):    #리스트 슬라이싱 함수 선언 , 인수 b는 리스트
   c= list(map(int,input('i번째, j번째, k번째 : ').split()))   #i, j, k  입력 -> 공백 제거 후 정수로 리스트 대입
   b = b[c[0]-1:c[1]]      #b[i-1]이상 b[j]미만 슬라이싱 -> b
   b.sort()                #리스트 b정렬
   return b[c[2]-1]        #리스트 b[k-1] 리턴

a = [1,5,2,6,3,7,4]      #리스트 a

print(array_slice(a))  #array_slice에 인수 a를 넣고 출력