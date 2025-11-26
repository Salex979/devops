from flask import Flask, jsonify
import requests
import random
import os

app = Flask(__name__)

# Адрес второго сервиса будем получать из переменных окружения
service_b_url = os.getenv('SERVICE_B_URL', 'http://localhost:5001')

@app.route('/')
def start_process():
    # Генерируем случайное число
    random_number = random.randint(1, 100)
    print(f"Service A generated number: {random_number}")

    try:
        # Отправляем число в Service B
        response = requests.post(f'{service_b_url}/process', json={'number': random_number})
        response_data = response.json()
        result_from_b = response_data.get('result', 'Error')
        print(f"Service A received result: {result_from_b}")

        return jsonify({
            'generated_number': random_number,
            'result_from_service_b': result_from_b
        })
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to connect to Service B: {e}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)