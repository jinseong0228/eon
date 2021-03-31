a = [] #a를 list로 사용
a.extend(map(int,input('오름차순으로 정렬할 수를 입력하세요: ').split())) #숫자입력을 받아 공백제거(split) 후 정수로 변환하고 a의 리스트에 대

def bubblesort(arr):     #bubblesort 함수 정의
 for x in range(0,len(arr)-1,1): #(다중 for 반복문) x를 0부터 [입력한 수의 개수-2]까지 1씩 증가하며 반복
  for y in range(x+1,len(arr),1): #y를 x+1부터 [입력한 수의 개수-1]까지 1씩 증가하며 반복
   if arr[x] > arr[y]:  #if문 배열 arr[x]가 > arr[y]보다 클때 true if문 실행
    temp = arr[x]     #true일때 arr[x]와 arr[y] 자리 바꾸기
    arr[x] = arr[y]
    arr[y]= temp
 return arr           

print(bubblesort(a))   #함수bubblesort의 인수에 a대입하여 출력