from flask import Flask, render_template, request, jsonify, make_response, json
from pusher import pusher
    
app = Flask(__name__)
    
pusher = pusher_client = pusher.Pusher(
    app_id='1564871',
    key='012c6fb8861020825989',
    secret='2a65749113336d021c91',
    cluster='us2',
    ssl=True
)
    
name = ''
    
@app.route('/')
def index():
    return render_template('index.html')
      
@app.route('/play')
def play():
    global name
    name = request.args.get('username')
    return render_template('play.html')
      
@app.route("/pusher/auth", methods=['POST'])
def pusher_authentication():
    auth = pusher.authenticate(
        channel=request.form['channel_name'],
        socket_id=request.form['socket_id'],
        custom_data={
          u'user_id': name,
          u'user_info': {
            u'role': u'player'
          }
        }
    )
    return json.dumps(auth)
      
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
name = ''