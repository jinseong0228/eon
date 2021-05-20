def addbook():    #도서추가 함수 정의
    a = input('도서명 저자 출판연도 출판사명 장르 순으로 입력하시오. : ')
    with open("C:/파이썬/input.txt","a") as file:
     file.write('\n'+ a)
     print('해당 도서가 추가되었습니다.')
def searchbook():   #도서검색 함수 정의
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
        
