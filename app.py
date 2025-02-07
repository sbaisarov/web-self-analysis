from flask import Flask, render_template

app = Flask(__name__)
FEAR = []
SADNESS = []
ANGER = []
JOY = []
HAPPINESS = []
FLAWS = []
FEARS = {"fears": [], "fears_to_be": [], "fears_to_seem": [], "fears_to_lose": []}
DENIALS = ["Простое отрицание", "Минимализация", "Рационализация", "Интеллектуализация", "Проекция",
           "Фантазия", "Обвинение", "Отвлечение внимания", "Приукрашивание воспоминаний", "Планирование желаемого"]

def fulfill(collection_in, collection_out, br_n):
    cnt = 0 # count of break lines 
    br_n_prev = br_n - 1
    take = False # append while take is true
    for line in collection_in:
        if line == '':
            cnt += 1
            if cnt == br_n:
                break
            continue
        
        if cnt == br_n_prev:
            take = True

        if take:
            collection_out.append(line)
            
    collection_out.sort()

def fulfill_flaws(collection):
    flaws.sort()
    for flaw in flaws:
        collection.append(flaw)
        
def fulfill_denials(collection):
    pass

def fulfill_fears(collection):
    for fear in fears:
        pass

with open("feelings.txt", 'r', encoding='utf-8') as f:
    feelings = [i.strip() for i in f.readlines()]
    fulfill(feelings, FEAR, 1)
    fulfill(feelings, SADNESS, 2)
    fulfill(feelings, ANGER, 3)
    fulfill(feelings, JOY, 4)
    fulfill(feelings, HAPPINESS, 5)

with open("flaws.txt", 'r', encoding='utf-8') as f:
    flaws = [i.strip() for i in f.readlines()]    
    fulfill_flaws(FLAWS)
    
with open("fears.txt", "r", encoding='utf-8') as f:
    fears = [i.strip() for i in f.readlines()]
    
    fulfill(fears, FEARS["fears"], 1)
    fulfill(fears, FEARS["fears_to_be"], 2)
    fulfill(fears, FEARS["fears_to_seem"], 3)
    fulfill(fears, FEARS["fears_to_lose"], 4)
    

@app.route('/')
def main():
    return render_template('index.html', FEAR=FEAR, SADNESS=SADNESS, ANGER=ANGER,
                           JOY=JOY, HAPPINESS=HAPPINESS, FLAWS=FLAWS, FEARS=FEARS, DENIALS=DENIALS)

app.run(reload=True)
