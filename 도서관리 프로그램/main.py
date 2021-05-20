import database  
def library():    #database의 book class에서 run함수 실행하는 library함수 정의
    app = database.book()
    app.run()

library()
    