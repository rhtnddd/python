todo = {
    "월": [],
    "화": [],
    "수": [],
    "목": [],
    "금": [],
    "토": [],
    "일": []
}

def add_task(day, task):
    if day in todo:
        todo[day].append(task)
        print(f"[추가 완료] {day}요일에 '{task}' 추가됨.")
    else:
        print("[오류] 유효하지 않은 요일입니다.")

def view_tasks(day):
    if day in todo:
        print(f"\n📅 {day}요일의 할 일 목록:")
        if todo[day]:
            for i, task in enumerate(todo[day], 1):
                print(f"{i}. {task}")
        else:
            print("할 일이 없습니다.")
    else:
        print("[오류] 유효하지 않은 요일입니다.")

def delete_task(day, index):
    if day in todo:
        if 0 <= index < len(todo[day]):
            removed = todo[day].pop(index)
            print(f"[삭제 완료] '{removed}' 삭제됨.")
        else:
            print("[오류] 잘못된 번호입니다.")
    else:
        print("[오류] 유효하지 않은 요일입니다.")

def view_all():
    print("\n📋 전체 할 일 목록:")
    for day in ["월", "화", "수", "목", "금", "토", "일"]:
        print(f"{day}: {', '.join(todo[day]) if todo[day] else '없음'}")

def main():
    while True:
        print("\n====== 요일별 할 일 관리 프로그램 ======")
        print("1. 할 일 추가")
        print("2. 할 일 보기")
        print("3. 할 일 삭제")
        print("4. 전체 보기")
        print("5. 종료")
        choice = input("선택 >> ")

        if choice == "1":
            day = input("요일 입력 (월~일): ")
            task = input("할 일 내용 입력: ")
            add_task(day, task)

        elif choice == "2":
            day = input("요일 입력 (월~일): ")
            view_tasks(day)

        elif choice == "3":
            day = input("요일 입력 (월~일): ")
            view_tasks(day)
            if todo[day]:
                try:
                    index = int(input("삭제할 번호 입력: ")) - 1
                    delete_task(day, index)
                except ValueError:
                    print("[오류] 숫자를 입력하세요.")
            else:
                print("[안내] 삭제할 항목이 없습니다.")

        elif choice == "4":
            view_all()

        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("[오류] 잘못된 입력입니다.")

if __name__ == "__main__":
    main()