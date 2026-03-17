#  연습문제1) 리스트를 통해 직원 자료를 입력받아 가공 후 출력하기
from datetime import datetime

def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas

def processfunc(datas):
    print("-" * 80)
    print("사번\t이름\t기본급\t근무년수 근속수당 공제액 수령액")
    
    count = 0
    # datetime.now().year 2026년만 사용할 수 있는 프로그램이 아닌 컴퓨터에서 date 뽑을 수 있음
    # this_year = 2026    # 상수 값은 대문자로만 적어준다
    this_year = datetime.now().year
    for emp in datas:
        no = emp[0]
        name = emp[1]
        base_pay = emp[2]
        join_year = emp[3]

        years = this_year - join_year

        if 0 <= years <= 3:
            sudang = 150000
        elif 4 <= years <= 8:
            sudang = 450000
        else:
            sudang = 1000000

        total_pay = base_pay + sudang

        if total_pay >= 3000000:
            tax = 0.5
        elif total_pay >= 2000000:
            tax = 0.3
        else:
            tax = 0.15

        tax_amount = int(total_pay * tax)

        real_pay = total_pay - tax_amount

        print(f"{no}\t{name}\t{base_pay}\t{years}\t{sudang}\t{tax_amount}\t{real_pay}")

        count += 1

    print("-" * 80)
    print(f"처리 건수: {count} 건")

result_data = inputfunc()
processfunc(result_data)

# 연습문제2) 리스트를 통해 상품 자료를 입력받아 가공 후 출력하기

def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

def processfunc(datas):
    pt = {
        "새우깡": 450,
        "감자깡": 300,
        "양파깡": 350
    }

    qq = {
        "새우깡": 0,
        "감자깡": 0,
        "양파깡": 0
    }
    aa = {
        "새우깡": 0,
        "감자깡": 0,
        "양파깡": 0
    }

    tq = 0
    ta = 0

    print("상품명   수량   단가   금액")
    print("-" * 35)

    for data in datas:
        name, qty = data.split(",")
        qty = int(qty)

        price = pt[name]

        amount = qty * price

        print(f"{name:<6} {qty:<6} {price:<6} {amount}")

        qq[name] += qty
        aa[name] += amount

        tq += qty
        ta += amount

    print("\n소계")
    for name in pt:
        print(f"{name} : {qq[name]}건   소계액 : {aa[name]}원")

    print("\n총계")
    print(f"총 건수 : {tq}")
    print(f"총 액  : {ta}원")


datas = inputfunc()
processfunc(datas)
# CSV 구분자가 콤마 , 
def inputfunc_2():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas

def solution_func_second():
    price_by_name = {"새우깡":450, "감자깡":300, "양파깡": 450}

    arr_items = inputfunc_2()

    len_arr = len(arr_items) # 12개

    count_by_name = {name: 0 for name in price_by_name}
    # {'새우깡': 0, '감자깡': 0, '양파깡': 0}

    # amt_by_name == amount_by_name
    amt_by_name = {name: 0 for name in price_by_name}
    # {'새우깡': 0, '감자깡': 0, '양파깡': 0}

    names = []; cnts = []
    for arr_item in arr_items:

        # nms_dt == Names_data, cs_dt == cnts_data
        nms_dt, cs_dt = arr_item.split(",")
        names.append(nms_dt); cnts.append(cs_dt)
        # 이름, 갯수 모음

        int_cd, int_pp = int(cs_dt), int(price_by_name[nms_dt])
        # 정수형 변환

        count_by_name[nms_dt] += int_cd     
        # {'새우깡': 135, '감자깡': 115, '양파깡': 105}

        amt_by_name[nms_dt] += int_cd * int_pp
        # {'새우깡': 60750, '감자깡': 34500, '양파깡': 47250}

    # print(names); print(cnts) # 이름과 갯수의 리스트

    order_table = [[0] * 4 for _ in range(len_arr)] # 상품의 출력 보드

    for row, item in enumerate(arr_items):
        int_cnts, int_pp = int(cnts[row]), int(price_by_name[names[row]])

        order_table[row][0] = names[row]
        order_table[row][1] = cnts[row]
        order_table[row][2] = price_by_name[names[row]]
        order_table[row][3] = int_cnts * int_pp

    # print(order_table)

    print("출력 형태:")
    print(f"{'상품명':<6} {'수량':>6} {'단가':>5} {'금액':>6}")
    print("-" * 35)
    for row in range(len_arr):
        print(f"{order_table[row][0]:<6}  {order_table[row][1]:>6}  {order_table[row][2]:>6}  {order_table[row][3]:>8}")

    print("\n소계")

    sum_eps = 0; sum_as = 0
    for name in price_by_name:
        print(f"{name} : {count_by_name[name]}건   소계액 : {amt_by_name[name]}원")
        sum_eps += int(count_by_name[name])
        sum_as += int(amt_by_name[name])

    print("총계")
    print(f"총 건수 : {sum_eps}")
    print(f"총 액   : {sum_as}")





if __name__ == "__main__":
    solution_func_second()