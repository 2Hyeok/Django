# db.py
# pip install cx_Oracle
import cx_Oracle
import os

# 오라클을 직접 접속한 방법임
# 없어도 값은 들어감, 하지만 확실하게 넣기위해 설정 해주는것
location = "C:\oraclexe\instancelient_21_6"
os.environ["PATH"] = location + ";" + os.environ["PATH"] # 페스의 이름을 지정해줌, + 원래패스의 경로도 설정을 해주어야함

dsn = cx_Oracle.makedsn("localhost", "1521", "xe")
con = cx_Oracle.connect("bit","bit",dsn) # 오라클의 로그인 아이디 비번, 주소값
cursor = con.cursor()

#--------------------------------------------------------------------------------------

# insert
# sql = "insert into dbtest values( :1, :2, :3, :4, sysdate)" # 콜론을 넣음
# user = ("qqaa", "111", "홍길동", "1111-2222") # 튜플로 주어야함
# result = cursor.execute(sql, user)
# if result == 0:
#     print("가입 실패")
# else :
#     print("가입성공")

#--------------------------------------------------------------------------------------

# select
# 다 가져 오기
sql = "select * from dbtest"
cursor.execute(sql) # 보통은 받아서 처리하지만, 특이하게도 커서가 데이터를 가지고있음
# 커서를 바로 반복문 돌리면 됨
# for row in cursor :
#     # print(row) # 튜플로 가져옴
#     for column in row :
#         print(column, end="\t")
#     print()

# 커서가 가지고있는 데이터를 2차원 데이터로 꺼내옴
# rows = cursor.fetchall() # 여러줄 꺼내옴, 한줄일경우 fetchone()
# print(rows[0])
# print(rows[0][0]) # 커서의 있는것을 꺼내쓴것
# for row in rows :
#     for column in row :
#         print(column, end="\t")
#     print()
#
# # 회원수 출력
# sql = "select count(*) from dbtest"
# cursor.execute(sql)
# count = cursor.fetchone()[0] # 튜플로 넘어옴, 0번방 것만 꺼내라 라는뜻
# print("회원수 :",  count)
#
# # 한명만 가져오는경우
# sql ="select * from dbtest where id=:idx"
# cursor.execute(sql, idx="aaa") # 아이디 값도 튜플로 주어야함
# user = cursor.fetchone() # 튜플로 넘어옴, 그대로 출력해주면됨
# print(user)

#-----------------------------------------------------------------------------

# delete
id = "qqaa"
passwd = "111"
sql = "select * from dbtest where id=:idx"
cursor.execute(sql, idx=id)
user = cursor.fetchone()
if user == None :
    print("아이디가 없습니다")
else : 
    if passwd == user[1] :
        sql = "delete from dbtest where id=:idx" # 인덱스의 약자이므로 idx라고 명칭함 굳이 idx 할 필요 x
        result = cursor.execute(sql, idx=id)
        if result == 0 :
            print("탈퇴 실패")
        else :
            print("탈퇴 성공 :", id, "를 삭제했습니다.")
    else :
        print("비밀번호가 다릅니다")


#----------------------------------------------------------------------------

# update

# 스스로 해볼것



con.commit() # 커밋 해주어야함
con.close()
