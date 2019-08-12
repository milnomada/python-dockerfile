from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return make_response(jsonify({'status':'ok'}), 200)

if __name__ == '__main__':
	app.run(debug=True)