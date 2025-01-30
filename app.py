from flask import Flask, render_template
import jinja2

app = Flask(__name__)
FEAR = []
SADNESS = []
ANGER = []
JOY = []
HAPPINESS = []

def fulfill_feelings(collection, br_n):
    cnt = 0 # count of break lines
    br_n_prev = br_n - 1
    take = False # append while take is true
    for line in feelings:
        if cnt == br_n_prev:
            take = True

        if take:
            collection.append(line)

        if line == '':
            cnt += 1
            if cnt == br_n:
                break

with open("feelings.txt", 'r', encoding='utf-8') as f:
    feelings = [i.strip() for i in f.readlines()]
    fulfill_feelings(FEAR, 1)
    fulfill_feelings(SADNESS, 2)
    fulfill_feelings(ANGER, 3)
    fulfill_feelings(JOY, 4)
    fulfill_feelings(HAPPINESS, 5)
    data = list(zip(FEAR, SADNESS, ANGER, JOY, HAPPINESS))

@app.route('/')
def main():
    return render_template('index.html', data=data)

app.run(reload=True)
