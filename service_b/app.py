from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_number():
    data = request.get_json()
    number = data.get('number', 0)

    # Умножаем число на 2 (простая логика обработки)
    result = number * 2
    print(f"Service B received number: {number}, calculated result: {result}")

    return jsonify({'result': result, 'original_number': number})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)