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
NEEDS = {1: [], 2: [], 3: [], 4: [], 5: []}
PRINCIPLES = []

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
    

with open('needs.txt', 'r', encoding='utf-8') as f:
    needs = [i.strip() for i in f.readlines()]

fulfill(needs, NEEDS[1], 1)
fulfill(needs, NEEDS[2], 2)
fulfill(needs, NEEDS[3], 3)
fulfill(needs, NEEDS[4], 4)
fulfill(needs, NEEDS[5], 5)

with open("feelings.txt", 'r', encoding='utf-8') as f:
    feelings = [i.strip() for i in f.readlines()]
fulfill(feelings, FEAR, 1)
fulfill(feelings, SADNESS, 2)
fulfill(feelings, ANGER, 3)
fulfill(feelings, JOY, 4)
fulfill(feelings, HAPPINESS, 5)

with open("flaws.txt", 'r', encoding='utf-8') as f:
    flaws = [i.strip() for i in f.readlines()]    
fulfill(flaws, FLAWS, 1)
    
with open("fears.txt", "r", encoding='utf-8') as f:
    fears = [i.strip() for i in f.readlines()]
    
fulfill(fears, FEARS["fears"], 1)
fulfill(fears, FEARS["fears_to_be"], 2)
fulfill(fears, FEARS["fears_to_seem"], 3)
fulfill(fears, FEARS["fears_to_lose"], 4)

with open("principles.txt", "r", encoding="utf-8") as f:
    principles = [i.strip() for i in f.readlines()]
    
fulfill(principles, PRINCIPLES, 1)

@app.route('/')
def main():
    return render_template('index.html', FEAR=FEAR, SADNESS=SADNESS, ANGER=ANGER,
                           JOY=JOY, HAPPINESS=HAPPINESS, FLAWS=FLAWS, FEARS=FEARS, DENIALS=DENIALS,
                           NEEDS=NEEDS, PRINCIPLES=PRINCIPLES)

app.run(reload=True)
