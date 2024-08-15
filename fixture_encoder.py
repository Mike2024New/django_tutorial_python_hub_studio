import os
import json

def fixture_encoder():
    """преобразование фикстур моделей в utf-8 для корректного отбражения кодировок,
    использовать после создания нового файла с фикстурой БД.
    модифицировать функцию на рекурсивный обход файлов в папке с фикстурами
    """
    fix_path = "fixtures/goods/" # временно путь к фикстурам прописан напрямую
    fixtures =[os.path.join(fix_path,file) for file in  os.listdir(path=fix_path)]

    for fixture in fixtures:
        with open(fixture,encoding='windows-1251') as f:
            data = json.load(f)

        with open(fixture,'w',encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

if __name__=="__main__":
    fixture_encoder()