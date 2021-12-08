from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# @socketio.on('message')
# def handle_message(data, message):
#     print('received ' + data + ': ' + message)
#     send(message)


def decodeMorse(morseCode):
    if morseCode:
        MORSE_DICT = {
            '.-': 'A', '.--.': 'P', '.....': '5',
            '-...': 'B', '--.-': 'Q', '-....': '6',
            '-.-.': 'C', '.-.': 'R', '--...': '7',
            '-..': 'D', '...': 'S', '---..': '8',
            '.': 'E', '-': 'T', '----.': '9',
            '..-.': 'F', '..-': 'U', '-----': '0',
            '--.': 'G', '...-': 'V',
            '....': 'H', '.--': 'W',
            '..': 'I', '-..-': 'X',
            '.---': 'J', '-.--': 'Y',
            '-.-': 'K', '--..': 'Z',
            '.-..': 'L', '.----': '1',
            '--': 'M', '..---': '2',
            '-.': 'N', '...--': '3',
            '---': 'O', '....-': '4',
        }

        results = []
        for letter in morseCode.split(' '):
            results.append(MORSE_DICT.get(letter))

        return results



@socketio.on('message')
def handle_message(self, data):
    print('received message: ' + data)
    decode_result = decodeMorse(data)
    send(decode_result)


@app.route('/index', methods=['POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)
