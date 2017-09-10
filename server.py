from flask import Flask, render_template, request, session, redirect
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    # return render_template("index.html")

    if not 'gold' in session:
        # session['someKey'] = 1
        session['gold'] = 0
        session['activity'] = []
        # gold = session['gold']


    else:
        # print session['counter']
        session['gold'] = session['gold']

        # gold = session['gold']
        # win = False
        # print session['someKey']
    return render_template("index.html", gold = session['gold'], activities=session['activity'])

def activity(value, winLose, loc):
     DateTime = datetime.now().strftime("%Y/%m/%d %I:%M %p")
     if (loc == 'farm' or loc == 'cave' or loc == 'house' or loc == 'casino' and winLose == 0):
        #  session['activity'].append("working")
         session['activity'].append('Earned {} gold from the {}! @Time: {}'.format(value, loc, DateTime))
     elif (loc == 'casino' and winLose == 1):
         session['activity'].append('Lost {} gold from the {}! @Time: {}'.format(value, loc, DateTime))
     else:
         session['activity'].append('Error occured..')
@app.route('/process_money', methods = ['POST'])
def goldVal():


    hiddenVal = request.form['hidden']
    if hiddenVal == 'farm':
        farmVal = random.randrange(10,21)
        session['gold']+= farmVal
        # add activity here
        winLose = 0
        activity(farmVal, winLose, 'farm')
    elif hiddenVal == 'cave':
        caveVal = random.randrange(5,11)
        session['gold'] += caveVal
    #     # activity here
        winLose = 0
        activity(caveVal, winLose, 'cave')
    elif hiddenVal == 'house':
        houseVal = random.randrange(2,6)
        session['gold'] += houseVal
        winLose = 0
        activity(houseVal, winLose, 'house')
        #activity here
    elif hiddenVal == 'casino':
        winLose = random.randrange(0,2)
        casinoVal = random.randrange(0,51)
        if winLose == 0:
            session['gold'] += casinoVal

            activity(casinoVal, winLose, 'casino')
            # actitity here
        else:
            session['gold'] -= casinoVal
            #add activity here'

            activity(casinoVal, winLose, 'casino')
    else:
        print "something went wrong..."
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    gold = session['gold']
    #activity reset
    session['activity']=[]

    return redirect('/')


# def hello_world():
#     return render_template('index.html')
#
# @app.route('/projects')
# def success():
#     return render_template('projects.html')
#
# @app.route('/about')
# def hello():
#     return render_template('about.html')


app.run(debug=True)
