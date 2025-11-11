import dao

# 설문 현황
def show_servey():
    serveys = dao.get_serveys()
    
    for idx, food in enumerate(serveys):
        print(f'{idx+1}. {food.name} ===> {food.vote.count}표')
    
# 설문 참여
def participate_servey():
    serveys = dao.get_serveys()
    
    for idx, food in enumerate(serveys, start=1):
        print(f'{idx}. {food.name}')
    print('0. 기타(직접입력)')
    
    try:
        select = int(input('선택: '))
    except Exception as msg:
        print('participate_servey Error!', msg)
    else:
        if select != 0 :
            select_food = None
            for idx, food in enumerate(serveys, start=1):
                if idx == select :
                    # print(food.id, food.name, food.vote.count)
                    select_food = food
            
            if select_food is None :
                print('없는 음식입니다.')
            else :
                vote_servey(select_food)
        else:
            food_name = input('음식 종류 입력: ')
            
            result = dao.insert_servey(food_name)
            
            if result > 0:
                print('등록되었습니다.')
                food.name = food_name
                food.vote.count = 0
                dao.update_servey(food)
            else:
                print('등록 실패')
            
# 설문 투표
def vote_servey(select_food):
    
    result = dao.update_servey(select_food)

    if result > 0:
        print('설문 완료')
    else:
        print('설문 실패')

# 프로그램 실행
def program_run():
    while True:
        print('★ 좋아하는 음식 종류 설문조사★')
        print('1. 설문 참여하기')
        print('2. 설문 현황보기')
        select:int
        try:
            select = int(input('선택: '))
        except Exception as msg:
            print('program_run Error!', msg)
            continue
        else:
            match select :
                case 1:
                    participate_servey()
                case 2: 
                    show_servey()
                case 999: 
                    print('임의 종료')
                    break

def init_db():
    dao.init_db()