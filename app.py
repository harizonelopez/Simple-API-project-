from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    message = "Team Avengers"
    
    users = [
        {'id': 1, 'name': 'Josh Brolin', 'age': 51},
        {'id': 2, 'name': 'Brie Larson', 'age': 30},
        {'id': 3, 'name': 'Chris Evans', 'age': 122},
        {'id': 4, 'name': 'Jeremy Reener', 'age': 43},
        {'id': 5, 'name': 'Tony Stark', 'age': 32},
        {'id': 6, 'name': 'Dr. Steven Strange', 'age': 42},
        {'id': 7, 'name': 'Mark Ruffalo', 'age': 52},
        {'id': 8, 'name': 'Scarlet Johnson', 'age': 28},
        {'id': 9, 'name': 'Peter Parker', 'age': 19},
        {'id': 10, 'name': 'Chris Pratt', 'age': 22},
        {'id': 11, 'name': 'Zoe Saldana', 'age': 25},
        {'id': 12, 'name': 'Bradley Rocket', 'age': 23},
        {'id': 13, 'name': 'Chris Hemsworth', 'age': 102},
        {'id': 14, 'name': 'Steven Wong', 'age': 42},
        {'id': 15, 'name': 'Samuel L. Jackson', 'age': 66},
        {'id': 16, 'name': 'Dave Batista', 'age': 57},
        {'id': 17, 'name': 'Vin Diesel', 'age': 55},
        {'id': 18, 'name': 'Stan Lee', 'age': 99},
        {'id': 19, 'name': 'Nicholas Cage', 'age': 48},
        {'id': 20, 'name': 'Hugh Jackman', 'age': 110},
        {'id': 21, 'name': 'Ryan Raynolds', 'age': 30}
    ]
    
    return render_template('index.html', message=message, users=users)

if __name__ == '__main__':
    app.run(debug=True)
