# 문1) jikwon 테이블 자료 출력
# 키보드로부터 부서번호를 입력받아, 해당 부서에 직원 자료 출력
# 부서번호 입력 : _______
# 직원번호 직원명 근무지역 직급
#    1      홍길동 서울  이사
# ...
# 인원 수 :

import MySQLdb
import pickle

'''
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}
'''

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        bu_no = input('부서번호 입력 : ')
        # print(bu_no)
        sql = """
            select jikwonno as 직원번호, jikwonname as 직원명,
            buserloc as 근무지역, jikwonjik as 직급
            from jikwon
            inner join buser on buserno=busernum
            where busernum={0}
        """.format(bu_no)
        # print(sql)

        cursor.execute(sql)

        datas = cursor.fetchall()
        # print(datas)
        
        if len(datas) == 0:
            print(bu_no + '번 부서는 없어요')
            return  # sys.exit(0)
        
        for jikwonno,jikwonname,buserloc,jikwonjik in datas:
            print(jikwonno,jikwonname,buserloc,jikwonjik)

        print('인원 수 : ', len(datas))
    except Exception as e:
        print('err : ', e)
        
    finally:
        cursor.close()
        conn.close()


if __name__=='__main__':
    chulbal()


# # 문1) jikwon 테이블 자료 출력
# # 키보드로부터 부서번호를 입력받아, 해당 부서에 직원 자료 출력

# import MySQLdb

# # 1. DB 연결 정보 세팅 (딕셔너리 형태)
# # 나중에 서버 주소나 비밀번호가 바뀌면 여기만 수정하면 됩니다.
# config = {
#     'host':'127.0.0.1',
#     'user':'root',
#     'password':'123',
#     'database':'test',
#     'port':3306,
#     'charset':'utf8'
# }

# def chulbal():
#     try:
#         # 2. DB와 연결 (레스토랑 문 열고 들어가기)
#         # **config는 딕셔너리의 키와 값을 한 번에 풀어넣어 주는 파이썬 문법입니다.
#         conn = MySQLdb.connect(**config)
        
#         # 3. 커서 생성 (주문받고 서빙할 웨이터 고용)
#         cursor = conn.cursor()
        
#         # 4. 사용자 입력 받기
#         bu_no = input('부서번호 입력 : ')
        
#         # 5. SQL 쿼리문 작성 (보안 패치 완료 🛡️)
#         # 값을 직접 넣지 않고 '%s'로 빈칸을 뚫어둡니다. (문자, 숫자 상관없이 %s 사용)
#         sql = """
#             select jikwonno as 직원번호, jikwonname as 직원명,
#             buserloc as 근무지역, jikwonjik as 직급
#             from jikwon
#             inner join buser on buserno=busernum
#             where busernum = %s
#         """
        
#         # 6. SQL 실행 (주방에 요리 주문)
#         # execute의 두 번째 인자로 빈칸(%s)에 들어갈 값을 '튜플' 형태로 넘겨줍니다.
#         # 이렇게 하면 DB가 해킹 공격(SQL Injection)을 알아서 필터링해 줍니다.
#         cursor.execute(sql, (bu_no,))

#         # 7. 결과 가져오기 (완성된 요리 손님상에 가져오기)
#         # fetchall()은 조회된 모든 데이터를 튜플들의 튜플 형태로 가져옵니다.
#         datas = cursor.fetchall()
        
#         # 8. 예외 처리: 데이터가 없을 경우
#         if len(datas) == 0:
#             print(bu_no + '번 부서는 없어요')
#             return  # 데이터가 없으면 함수를 바로 종료합니다.
        
#         # 9. 결과 출력 (포장지 벗겨서 예쁘게 보여주기)
#         for jikwonno, jikwonname, buserloc, jikwonjik in datas:
#             print(jikwonno, jikwonname, buserloc, jikwonjik)

#         # 총 인원수 출력
#         print('인원 수 : ', len(datas))
        
#     except Exception as e:
#         # DB 연결 실패나 SQL 문법 오류 등이 발생하면 프로그램이 안 뻗고 여기로 옵니다.
#         print('err : ', e)
        
#     finally:
#         # 10. 마무리 정리 (가장 중요 ⭐️)
#         # 에러가 나든 안 나든 무조건 실행되는 구역입니다.
#         # DB 연결을 계속 열어두면 서버가 과부하로 뻗을 수 있으므로 반드시 닫아줍니다.
#         cursor.close()
#         conn.close()

# # =====================================================================
# # 💡if __name__ == '__main__': 의 역할]
# #
# # 이 구문은 한마디로 "이 파이썬 파일이 '직접(메인으로)' 실행될 때만 작동해라!" 라는 뜻입니다.
# # 
# # 1. 내가 이 파일을 직접 실행(Run)했을 때:
# #    파이썬은 프로그램의 시작점인 이 파일의 이름을 몰래 '__main__'이라고 부릅니다.
# #    그래서 조건이 참(True)이 되어 아래의 chulbal() 함수가 정상적으로 실행됩니다.
# #
# # 2. 다른 파이썬 파일에서 이 파일을 부품(모듈)처럼 가져다 쓸 때 (import 할 때):
# #    예를 들어 다른 파일에서 `import 현재파일`을 하면, 
# #    이때는 이름이 '__main__'이 아니라 원래 파일명으로 인식됩니다.
# #    그래서 조건이 거짓(False)이 되어 아래 코드가 무시됩니다.
# #
# # 즉, "내가 주인공으로 나설 때만 실행되고, 남의 프로그램에 불려 갔을 때는
# # 조용히 부품 역할만 하겠다"는 아주 매너 있는 방어막(Guard)입니다!
# # =====================================================================

# if __name__ == '__main__':
#     chulbal()  # 내가 직접 실행했을 때만 전체 로직(chulbal)을 가동시켜라!
