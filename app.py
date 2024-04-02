from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize tasks dictionary with categories
tasks = {
    'personal': [],
    'family': [],
    'work_or_school': []
}

# Function to render the index page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Function to add tasks
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    category = request.form['category']
    tasks[category].append(task)
    return redirect(url_for('index'))

# Function to delete tasks
@app.route('/delete/<category>/<int:index>')
def delete(category, index):
    del tasks[category][index]
    return redirect(url_for('index'))

# Function to edit tasks (GET request)
@app.route('/edit/<category>/<int:index>', methods=['GET'])
def edit_get(category, index):
    return render_template('edit.html', category=category, index=index, task=tasks[category][index])

# Function to edit tasks (POST request)
@app.route('/edit/<category>/<int:index>', methods=['POST'])
def edit_post(category, index):
    tasks[category][index] = request.form['editedTask']
    return redirect(url_for('index'))

# Function to mark tasks as done
@app.route('/done/<category>/<int:index>')
def done(category, index):
    tasks[category][index] = f'{tasks[category][index]} (DONE)'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
