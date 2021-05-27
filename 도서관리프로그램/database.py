import system  
import os     
class book:  #클래스 book 정의
    def add_book(self):    #system의 addbook함수실행 함수
        system.addbook()
    def search_book(self):
        system.searchbook()
    def correct_book(self):
        system.correctbook()    
    def remove_book(self):
        system.removebook()
    def view_all(self):
        system.viewall()    
    def selectmenu(self):  
        os.system("cls")
        print("== 도서 관리 프로그램 ==") 
        print("1:도서 추가") 
        print("2:도서 검색")
        print("3:도서 수정") 
        print("4:도서 삭제") 
        print("5:전체 보기")
        print("6:종료 하기")
        return int(input("\n메뉴 입력 ◀:"))
    def run(self):
        while True:
            key = self.selectmenu()
            if key == 1:
                self.add_book()
            elif key == 2:
                self.search_book()   
            elif key == 3:
                self.correct_book()
            elif key == 4:
                self.remove_book()   
            elif key == 5:
                self.view_all()
            elif key == 6:
                print('프로그램을 종료합니다.')
                break    
            else:
                print("잘못 입력하셨습니다.")
            input("엔터 키를 누르세요.")
                
                
