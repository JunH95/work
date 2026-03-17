
# 1. 단어를 저장할 빈 딕셔너리 만들기
voca_db = {} 

# 2. 무한 루프 시작
while True:
    print("\n--- 기억상실증 단어장 ---")
    print("1. 단어 추가 | 2. 단어 검색 | 3. 전체 보기 | 4. 종료")
    
    # 3. 사용자 입력 받기
    choice = input("원하는 메뉴 번호를 입력하세요: ")

    # 4. 선택 기능
    if choice == '1':
        eng = input("추가할 영어 단어: ")
        kor = input("한글 뜻: ")
        voca_db[eng] = kor  # 딕셔너리 자료 추가 방법
        print("단어가 추가되었습니다!")

    elif choice == '2':
        search_word = input("검색할 영어 단어: ")
        # get(key) 통해 값 출력(키 없어도 오류 발생 X, None 반환)
        print(voca_db.get(search_word))
        # 한가지 의문 검색을 한국어로 하고 싶다면?  
        
    elif choice == '3':
        print("--- 현재 저장된 단어장 ---")
        # 딕셔너리 키-값 쌍 출력 (가독성 향상)
        for eng, kor in voca_db.items():
            print(f"{eng} : {kor}")
    
    # 5. break를 통해 while 무한 루프 종료 프로그램 종료
    elif choice == '4':
        print("단어장을 종료합니다. 안녕히 가세요!")
        break

    else:
        print("잘못된 입력입니다. 1~4 사이의 숫자를 입력해주세요.")
