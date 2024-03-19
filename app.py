from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = ('aladinh00-10montext')

@app.route('/', methods=['GET', 'POST'])
def hello():
    title_message = "Team Avengers"
    
    users = [
        {'id': 1, 'name': 'Josh Brolin', 'age': 51},
        {'id': 2, 'name': 'Brie Larson', 'age': 30},
        {'id': 3, 'name': 'Chris Evans', 'age': 122},
        {'id': 4, 'name': 'Tony Stark', 'age': 32},
        {'id': 5, 'name': 'Paul Betany', 'age': 31},
        {'id': 6, 'name': 'Dr. Steven Strange', 'age': 42},
        {'id': 7, 'name': 'Mark Ruffalo', 'age': 52},
        {'id': 8, 'name': 'Scarlet Johnson', 'age': 28},
        {'id': 9, 'name': 'Peter Parker', 'age': 19},
        {'id': 10, 'name': 'Jeremy Reener', 'age': 30},
        {'id': 11, 'name': 'Miss Pots', 'age': 30},
        {'id': 12, 'name': 'Nicholas Cage', 'age': 61},
        {'id': 13, 'name': 'Chris Hemsworth', 'age': 102},
        {'id': 14, 'name': 'Steven Wong', 'age': 42},
        {'id': 15, 'name': 'Samuel L. Jackson', 'age': 66},
        {'id': 16, 'name': 'Hugh Jackman', 'age': 110},
        {'id': 17, 'name': 'Ryan Reynolds', 'age': 55},
        {'id': 18, 'name': 'Stan Lee', 'age': 99},
        {'id': 19, 'name': 'Bradley Cooper', 'age': 23},
        {'id': 20, 'name': 'Dave Batista', 'age': 57},
        {'id': 21, 'name': 'Vin Diesel', 'age': 55},
        {'id': 22, 'name': 'Pom Klementief ', 'age': 24},
        {'id': 23, 'name': 'Karen Gillain', 'age': 25},
        {'id': 24, 'name': 'Zoe Saldana', 'age': 30},
        {'id': 25, 'name': 'Chris Pratt', 'age': 32}
    ]
    
    return render_template('index.html', message=message, users=users)

if __name__ == '__main__':
    app.run(debug=True)
