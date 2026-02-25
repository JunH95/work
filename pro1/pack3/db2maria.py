# 원격 데이터베이스 연동 프로그래밍
# MariaDB : driver file 설치 후 사용
# pip install mysqlclient

import MySQLdb
"""
conn = MySQLdb.connect(
    host='127.0.0.1',
    user ='root',
    password='123',
    database='test',
    port=3306
)

print(conn)
conn.close()
"""

# sangdata 자료 CRUD
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

def myFunc():    
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        # 자료 추가
        # isql = "insert into sangdata(code, sang, su, dan) values(5, '신상1', 5, 7800)"
        # cursor.execute(isql)
        # conn.commit()
        
        """
        isql = "insert into sangdata values(%s, %s, %s, %s)"
        # sql_data = (6, '신상2', 11, 5000)
        sql_data = 6, '신상2', 11, 5000
        cursor.execute(isql, sql_data)
        conn.commit()
        """

        # 자료 수정
        """
        명령만 내리고 결과에 대해서는 아무런 피드백을 주지 않습니다. 코드를 실행하는 우리 입장에서는 에러가 나지 않는 이상 "수정이 잘 되었는지", "몇 개의 데이터가 수정되었는지" 눈으로 바로 확인할 수 없습니다.

        usql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
        sql_data = ('물티슈', 66, 1000, 5)
        cursor.execute(usql, sql_data)
        conn.commit()
        """
        """
        파이썬의 MySQLdb 라이브러리에서 cursor.execute() 함수로 UPDATE, INSERT, DELETE 문을 실행하면, "몇 줄의 데이터가 변경되었는지"를 숫자로 반환해 줍니다.
        usql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
        sql_data = ('콜라', 77, 1000, 5)
        cou = cursor.execute(usql, sql_data)
        print('수정 건수 : ', cou)
        conn.commit()
        """

        # 자료 삭제
        code = '6'
        # dsql = "delete from sangdata where code=" + code    # 문자열 더하기 SQL완성 비권장 - secure coding 가이드라인 위배

        # dsql = "delete from sangdata where code=%s"
        # cursor.execute(dsql, (code,))

        dsql = "delete from sangdata where code='{0}'".format(code)
        # cursor.execute(dsql)
        cou = cursor.execute(dsql)  # 삭제 후 반환값 얻기 (0 또는 1 이상)
        if cou != 0:
            print('삭제 성공')
        else:
            print('삭제 실패')
        
        conn.commit()

        # 자료 읽기
        sql = "select code, sang, su, dan from sangdata"
        cursor.execute(sql)

        for data in cursor.fetchall():
            # print(data)
            print('%s %s %s %s'%data)

        print()
        cursor.execute(sql)
        for r in cursor:
            print(r[0], r[1], r[2], r[3])

        print()
        cursor.execute(sql)
        for code, sang, su, dan in cursor:
            print(code, sang, su, dan)

        print()
        cursor.execute(sql)
        for (a, b, 수량, 단가) in cursor:
            print(a, b, 수량, 단가)
                
    except Exception as e:
        print('err : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    myFunc()