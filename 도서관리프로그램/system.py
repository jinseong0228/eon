def addbook():    #도서추가 함수 정의
    a = input('도서명 저자 출판연도 출판사명 장르 순으로 입력하시오. : ')
    with open("C:/파이썬/input.txt","a") as file:
     file.write('\n'+ a)
     print('해당 도서가 추가되었습니다.')

def searchbook():   #도서검색 함수 정의
    b = int(input('검색할 방법을 숫자로 입력하세요. \n1.전체검색\n2.개별검색:'))
    if b == 1:
     import glob
     import re

     s = input('검색할 단어를 입력하세요. : ')

     p = re.compile(s)

     for i in glob.glob(r'C:/파이썬/input.txt'):
        with open(i, 'r') as f:
           for x, y in enumerate(f.readlines(),1):
               m = p.findall(y)
               if m:
                print('검색명 : %s' %(m))
                print('해당 도서 정보 : %s' %y)
           print()
    elif b == 2:
     with open("C:/파이썬/input.txt","r") as file:
        a = int(input("검색할 분야의 숫자를 입력하시오. \n1.도서명\n2.저자\n3.출판연도\n4.출판사명\n5.장르\n : "))
        while True:
            line = file.readline()
            if not line:
                break
            list = line.split(" ")
            if a == 1:
                print(list[0])
            elif a == 2:
                print(list[1])
            elif a == 3:
                print(list[2])
            elif a == 4:
                print(list[3])
            elif a == 5:
                print(list[4])
            else:
                print("잘못 입력하셨습니다.")
    else:
        print("잘못 입력하셨습니다.")                    

def correctbook():  #도서수정 함수 정의
    viewall()
    new_text_content = ''
    target_word = input('수정하려는 부분을 입력하세요:')
    new_word = input('변경하려는 단어를 입력하세요:')
    with open('C:/파이썬/input.txt','r') as file:
        lines = file.readlines() 
        for i, l in enumerate(lines):
            new_string = l.strip().replace(target_word,new_word)
            if new_string:
                new_text_content += new_string + '\n'
            else:
                new_text_content += '\n'
                
    with open('C:/파이썬/input.txt','w') as file:
        file.write(new_text_content)
    print('변경되었습니다.')

def removebook():   #도서삭제 함수 정의
    with open("C:/파이썬/input.txt", "r") as infile:
         lines = infile.readlines()
    viewall()
    c = int(input('삭제하고 싶은 번호를 입력하세요: '))
    with open("C:/파이썬/input.txt", "w") as outfile:
       for pos, line in enumerate(lines):
        if pos != c-1:
            outfile.write(line)  
    print('삭제되었습니다.')

def viewall():    #도서전체보기 함수 정의
    with open("C:/파이썬/input.txt", "r") as file:
      line_num = 1
      line = file.readline()
      while line:
        print('%d. %s' %(line_num, line))
        line = file.readline()
        line_num += 1   