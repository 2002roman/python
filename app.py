'''from flask import Flask, render_template,request, send_file
from flask_socketio import SocketIO

passwordTxt = open("password.txt", "r").read()
controllPanelHTML = open("templates/controllPanel.html","r").read()
explanationHTML = open("templates/explanation.html","r").read()
connectUser = ""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjrtnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
	return render_template('index.html')

@app.route('/ArTarumianBarak-Regular-8925.ttf')
def sendingFuckinFile():
	return send_file("ArTarumianBarak-Regular-8925.ttf", mimetype='image/gif')

@app.route('/bakcground.jpg')
def sendingFuckinFile2():
	return send_file("bakcground.jpg", mimetype='image/gif')

@app.route('/logo.png')
def sendingFuckinFile3():
	return send_file("logo.png", mimetype='image/gif')

@socketio.on('connect')
def hiToConnected():
	print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")

@socketio.on('reviewOfPasswrd')
def handle_my_custom_event(passwordS):
	print("review of paskkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
	if passwordTxt == passwordS:
		socketio.emit('answerOfPasswrd',controllPanelHTML,room = request.sid)
		socketio.emit('connectedInRobot',{
			'text':explanationHTML,
			'id':request.sid
		})
		global connectUser
		connectUser = request.sid
		print(connectUser+" "+request.sid)
	else:
		socketio.emit('answerOfPasswrd',False,room = request.sid)


@socketio.on('activateReview')
def handle_my_custom_event(okok):
	if connectUser != "":
		socketio.emit('answerOfConnect',explanationHTML,room = request.sid)
	else:
		socketio.emit('answerOfConnect',False,room = request.sid)
	print("connectedccccccccccccccccccccccccccccccccccccccccccccccccc")

if __name__ == '__main__':
	socketio.run(debug=False, host='0.0.0.0', port=5000)'''
from flask import Flask, render_template,request, send_file
#from flask_socketio import SocketIO

print("pkookok")
app = Flask(__name__)
#app.config['SECRET_KEY'] = 'vnkdjrtnfjknfl1232#'
#socketio = SocketIO(app)

@app.route('/')
def sessions():
	return "okokok"
	#return render_template('index.html')

'''@socketio.on('send_message')
def handle_source(msg):
	print(msg)
    socketio.emit('echo', msg)
'''
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
