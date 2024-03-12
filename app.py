from flask import Flask, render_template 

app = Flask(__name__)
app.secret_key = "aladinh-montext"

@app.route('/', methods=['GET'])
def home():
    tittle_message = "Team Avengers"
    
    players = [
        {'id': 1, 'name': 'Josh Brolin', 'age': 51},
        {'id': 2, 'name': 'Brie Larson', 'age': 30},
        {'id': 3, 'name': 'Chris Evans', 'age': 122},
        {'id': 4, 'name': 'Jeremy Reener', 'age': 43},
        {'id': 5, 'name': 'Robert Downey Junior', 'age': 32},
        {'id': 6, 'name': 'Dr. Steven Strange', 'age': 42},
        {'id': 7, 'name': 'Mark Ruffalo', 'age': 52},
        {'id': 8, 'name': 'Scarlet Johnson', 'age': 28},
        {'id': 9, 'name': 'Tom Holland', 'age': 19},
        {'id': 10, 'name': 'Chris Pratt', 'age': 22},
        {'id': 11, 'name': 'Zoe Saldana', 'age': 25},
        {'id': 12, 'name': 'Bradley Cooper', 'age': 23},
        {'id': 13, 'name': 'Chris Hemsworth', 'age': 102},
        {'id': 14, 'name': 'Steven Wong', 'age': 42},
        {'id': 15, 'name': 'Samuel L. Jackson', 'age': 66},
        {'id': 16, 'name': 'Dave Bautista', 'age': 57},
        {'id': 17, 'name': 'Vin Diesel', 'age': 55},
        {'id': 18, 'name': 'Stan Lee', 'age': 82},
        {'id': 19, 'name': 'Nicholas Cage', 'age': 48},
        {'id': 20, 'name': 'Hugh Jackman', 'age': 110},
        {'id': 21, 'name': 'Ryan Raynolds', 'age': 30},
        {'id': 22, 'name': 'Karen Gillain', 'age': 33},
        {'id': 23, 'name': 'Paul Betany', 'age': 41},
        {'id': 24, 'name': 'Tobey Maguire', 'age': 52},
        {'id': 25, 'name': 'Andrew Carfield', 'age': 42}
    ]
    
    return render_template('index.html', tittle_message=tittle_message, players=players)

if __name__ == '__main__':
    app.run(debug=True)
