import os
from flask import Flask, render_template, request, jsonify, session, url_for, redirect

app = Flask(__name__)
app.secret_key = os.urandom(24)

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
TRAITS = []
formatted_string = ""

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
    

with open('static/needs.txt', 'r', encoding='utf-8') as f:
    needs = [i.strip() for i in f.readlines()]

fulfill(needs, NEEDS[1], 1)
fulfill(needs, NEEDS[2], 2)
fulfill(needs, NEEDS[3], 3)
fulfill(needs, NEEDS[4], 4)
fulfill(needs, NEEDS[5], 5)

with open("static/feelings.txt", 'r', encoding='utf-8') as f:
    feelings = [i.strip() for i in f.readlines()]
fulfill(feelings, FEAR, 1)
fulfill(feelings, SADNESS, 2)
fulfill(feelings, ANGER, 3)
fulfill(feelings, JOY, 4)
fulfill(feelings, HAPPINESS, 5)

with open("static/flaws.txt", 'r', encoding='utf-8') as f:
    flaws = [i.strip() for i in f.readlines()]    
fulfill(flaws, FLAWS, 1)
    
with open("static/fears.txt", "r", encoding='utf-8') as f:
    fears = [i.strip() for i in f.readlines()]
    
fulfill(fears, FEARS["fears"], 1)
fulfill(fears, FEARS["fears_to_be"], 2)
fulfill(fears, FEARS["fears_to_seem"], 3)
fulfill(fears, FEARS["fears_to_lose"], 4)

with open("static/principles.txt", "r", encoding="utf-8") as f:
    principles = [i.strip() for i in f.readlines()]

fulfill(principles, PRINCIPLES, 1)

with open("static/traits.txt", "r", encoding="utf-8") as f:
    principles = [i.strip() for i in f.readlines()]

fulfill(principles, TRAITS, 1)

@app.route('/create')
def main():
    total = session['total']
    current = session['current']
    if (current > total):
        return redirect(url_for('introductory'))
    return render_template('index.html', FEAR=FEAR, SADNESS=SADNESS, ANGER=ANGER,
                            JOY=JOY, HAPPINESS=HAPPINESS, FLAWS=FLAWS, FEARS=FEARS, DENIALS=DENIALS,
                            NEEDS=NEEDS, PRINCIPLES=PRINCIPLES, TRAITS=TRAITS, total=total)

@app.route('/count')
def count():
    session['total'] = int(request.args.get('total'))
    session['current'] = 1
    return redirect(url_for('main'))
    
@app.route('/')
def introductory():
    return render_template('introduction.html')

@app.route('/process', methods=['POST'])
def process():
    # parse data and return structured data for clipboard
    data = request.form
    session['current'] += 1
    if 'formatted_result' not in session:
        session['formatted_result'] = ""
    
    response = {
        "situation": data.get("situation", ""),
        "feelings": [data[key] for key in data if key.startswith("feeling")],
        "thought": data.get("thought", ""),
        "flaws": [data[key] for key in data if key.startswith("flaw")],
        "fears": [data[key] for key in data if key.startswith("fear")],
        "denials": [data[key] for key in data if key.startswith("denial")],
        "needs": [data[key] for key in data if key.startswith("need")],
        "role": [data[key] for key in data if key.startswith("role")],
        "correction": data.get("correction", ""),
        "correctionThought": data.get("correctionThought", ""),
        "principles": [data[key] for key in data if key.startswith("principle")],
        "traits": [data[key] for key in data if key.startswith("trait")]
    }

    for key in response.keys():
        result = response[key]
        if isinstance(result, list):
            response[key] = [value.lower() for value in result]
            
    formatted_string = f"""
    
C.: {response['situation']}

Ч.: {', '.join(response['feelings'])}

М.: {response['thought']}

Д.: {', '.join(response['flaws'])}

Стр.: {', '.join(response['fears'])}

О.: {', '.join(response['denials'])}

П./М.: {', '.join(response['needs'])}

Р.: {', '.join(response['role'])}

К.: {response['correction']}

В/М.: {response['correctionThought']}

Д/П.: {', '.join(response['principles'])}

Ч./Х.: {', '.join(response['traits'])}
"""
    session["formatted_result"] += formatted_string + '\n'
    session.modified = True
    
    total = session['total']
    current = session['current']
    if current > total:
        # reset session
        session['total'] = 0
        session['current'] = 1
        fresult = session["formatted_result"]
        session["formatted_result"] = ""
        return jsonify({"result": fresult.strip()})
    
    return redirect(url_for('main'))

app.run(debug=True)
