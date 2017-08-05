from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'Wua6DZUxpJtwXRNMbk4gocDQPraEokbeHN8onaZWUZTzfkwsWMBrBZpwz}GpXjVn'

@app.route('/')
def index():

    if 'goldcount' not in session:
        session['goldcount'] = 0
    
    if 'activity' not in session:
        session['activity'] = []

    print session
    return render_template("index.html", number = 4)



@app.route('/process_money', methods=['POST'])
def buildingvisit():

    goldwon = 0
    
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        goldwon = random.randrange(10, 21)
        session['goldcount'] += goldwon
    if session['building'] == 'cave':
        goldwon = random.randrange(5, 11)
        session['goldcount'] += goldwon
    if session['building'] == 'house':
        goldwon = random.randrange(2, 5)
        session['goldcount'] += goldwon
    if session['building'] == 'casino':
        goldwon = random.randrange(-50, 51)
        session['goldcount'] += goldwon




    session['activity'] += [(request.form['building'],goldwon,datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))]

    if session['building'] == 'reset':
        session.pop('goldcount')
        session.pop('activity')
        session.pop('building')


    return redirect('/')




app.run(debug=True)

