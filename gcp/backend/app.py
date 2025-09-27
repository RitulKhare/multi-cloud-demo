from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    response = {"message": f"Hello {data['name']} from GCP backend!"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
