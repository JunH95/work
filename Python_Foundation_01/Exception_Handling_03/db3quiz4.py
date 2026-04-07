# 문4)직원별 관리 고객 수 출력 (관리 고객이 없으면 출력에서 제외)
# 직원번호 직원명 관리 고객 수
# 1 홍길동 3
# 2 한송이 1

import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        sql = """
            select jikwonno as 직원번호, jikwonname as 직원명,
            count(*) as 관리고객수
            from jikwon
            inner join gogek on jikwonno=gogekdamsano
            group by jikwonno, jikwonname
        """

        cursor.execute(sql)
        datas = cursor.fetchall()

        
        for jikwonno, jikwonname, damgogeksu in datas:
            print(jikwonno, jikwonname, damgogeksu)

    except Exception as e:
        print('err : ', e)
        
    finally:
        cursor.close()
        conn.close()


if __name__=='__main__':
    chulbal()
