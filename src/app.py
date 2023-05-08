from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todo = request.json
    todos.append(todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos  # declare todos as a global variable
    del todos[position]  # remove the todo at the specified position
    return jsonify(todos)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)