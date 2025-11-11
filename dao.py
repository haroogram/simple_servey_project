import pymysql, vo

def get_connection() -> pymysql.Connection:
    conn = pymysql.connect(
        host='localhost',
        user='testuser',        # 사용자 계정
        password='test1234',
        database='testdb',  # 연결할 DB (없어도 무관)
    )
    return conn

def init_db():
    
    conn = get_connection()
    
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS food_serveys")
            sql = '''
            CREATE TABLE food_serveys(
                id INT PRIMARY KEY AUTO_INCREMENT,
                food VARCHAR(20) UNIQUE NOT NULL,
                vote INT DEFAULT 0
            )
            '''
            cur.execute(sql)
            sql = '''
            INSERT INTO food_serveys (food)
            VALUES ('한식'), ('중식'), ('일식'), ('양식')
            '''
            cur.execute(sql)
            
            conn.commit()
    except Exception as msg:
        print('init_db Error!', msg)
        raise Exception('DB 초기화 실패...프로그램 종료.')
    finally:
        conn.close()

def get_serveys() -> list[vo.FOOD]:
    
    conn = get_connection()
    food_serveys: list = []
    
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM food_serveys')
            items = cur.fetchall()
            
            for item in items:
                food = vo.FOOD(item[0],item[1],vo.VOTE(item[2]))
                food_serveys.append(food)
    except:
        print('get_serveys Error!')
    finally:
        conn.close()
    
    return food_serveys

def update_servey(select_food: vo.FOOD):

    food_name = select_food.name
    food_vote = select_food.vote.count
    
    conn = get_connection()
    result:int = 0
    
    try:
        with conn.cursor() as cur:
            sql = 'UPDATE food_serveys SET vote = (%s + 1) WHERE food = %s'
            result = cur.execute(sql,(food_vote, food_name))
            conn.commit()
    except Exception as msg:
        print('update_servey Error!', msg)
    finally:
        conn.close()
    
    return result

def insert_servey(food_name: str):
    
    conn = get_connection()
    result:int = 0
    
    try:
        with conn.cursor() as cur:
            sql = 'INSERT INTO food_serveys (food) VALUES (%s)'
            result = cur.execute(sql, (food_name,))
            conn.commit()
    except Exception as msg :
        print('insert_servey Error!', msg)
    finally:
        conn.close()
        
    return result