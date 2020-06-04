from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('app.html')

@socketio.on('my event', namespace='/send')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    num1 = json['n1']
    num2 = json['n2']
    operation = json['operation_type']
    json_response = {}
    
    # Calculate operation
    try:
        if operation == 'add':
            sum = float(num1) + float(num2)
            history = str(float(num1)) + ' + ' + str(float(num2)) + ' = ' + str(float(sum))
            json_response = {'result': sum, 'history': history}
        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            history = str(float(num1)) + ' - ' + str(float(num2)) + ' = ' + str(float(sum))
            json_response = {'result': sum, 'history': history}
        elif operation == 'divide':
            sum = float(num1) / float(num2)
            history = str(float(num1)) + ' / ' + str(float(num2)) + ' = ' + str(float(sum))
            json_response = {'result': sum, 'history': history}
        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            history = str(float(num1)) + ' * ' + str(float(num2)) + ' = ' + str(float(sum))
            json_response = {'result': sum, 'history': history}
        else:
            json_response = {'result': 'Invalid Calculation', 'history': 'Invalid Calculation'}
    except:
        json_response = {'result': 'Invalid Calculation', 'history': 'Invalid Calculation'}

    socketio.emit('my response', json_response, broadcast=True, namespace='/send')

if __name__ == '__main__':
    socketio.run(app)
