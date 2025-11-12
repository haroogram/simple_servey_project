import os, json
from dataclasses import asdict
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
SAVE_DIR = os.path.join(BASE_DIR, 'save')

def save_file(serveys: list):
    
    content = json.dumps([asdict(item) for item in serveys], ensure_ascii=False, indent=2)
    
    file_name = datetime.now().strftime('%y%m%d')
    
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(f'{SAVE_DIR}/{file_name}','w', encoding='utf8') as file:
        file.write(content)
        
def load_file():

    file_name = datetime.now().strftime('%y%m%d')
    data = None
    try:
        with open(f'{SAVE_DIR}/{file_name}','r', encoding='utf8') as file:
            data = json.load(file)
    except Exception as msg:
        print('load_file Error!', msg)
        
    return data

        