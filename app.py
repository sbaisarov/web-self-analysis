from flask import Flask, render_template

app = Flask(__name__)
FEAR = []
SADNESS = []
ANGER = []
JOY = []
HAPPINESS = []
FLAWS = []

def fulfill_feelings(collection, br_n):
    cnt = 0 # count of break li nes 
    br_n_prev = br_n - 1
    take = False # append while take is true
    for line in feelings:
        if line == '':
            cnt += 1
            if cnt == br_n:
                break
            continue
        
        if cnt == br_n_prev:
            take = True

        if take:
            collection.append(line)

def fulfill_flaws(collection):
    for flaw in feelings:
        collection.append(flaw)


with open("feelings.txt", 'r', encoding='utf-8') as f:
    feelings = [i.strip() for i in f.readlines()]
    fulfill_feelings(FEAR, 1)
    fulfill_feelings(SADNESS, 2)
    fulfill_feelings(ANGER, 3)
    fulfill_feelings(JOY, 4)
    fulfill_feelings(HAPPINESS, 5)

with open("flaws.txt", 'r', encoding='utf-8') as f:
    flaws = [i.strip() for i in f.readlines()]    
    fulfill_flaws(FLAWS)
    
@app.route('/')
def main():
    return render_template('index.html', FEAR=FEAR, SADNESS=SADNESS, ANGER=ANGER,
                           JOY=JOY, HAPPINESS=HAPPINESS, FLAWS=FLAWS)

app.run(reload=True)
