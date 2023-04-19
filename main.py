import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user_info', methods=['GET'])
def get_user_info():
    try:
        user_id = request.args.get('user_id')
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/user_info'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        params = {'user_id': user_id}
        response = requests.get(url, headers=headers, params=params)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/user_create', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/user_create'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.post(url, headers=headers, json=data)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/user_update', methods=['PUT'])
def update_user():
    try:
        user_id = request.args.get('user_id')
        data = request.get_json()
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = f'https://prod.nevermet.io/user_update/{user_id}'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.put(url, headers=headers, json=data)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/user_delete', methods=['DELETE'])
def delete_user():
    try:
        user_id = request.args.get('user_id')
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = f'https://prod.nevermet.io/user_delete/{user_id}'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.delete(url, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/user_list', methods=['GET'])
def list_users():
    try:
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/user_list'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.get(url, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/user_authenticate', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/user_authenticate'
        headers = {
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        params = {'username': username, 'password': password}
        response = requests.post(url, headers=headers, params=params)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/verify_profile', methods=['POST'])
def verify_profile():
    try:
        data = request.get_json()
        user_id = data['user_id']
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = f'https://prod.nevermet.io/users/{user_id}/verify'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.post(url, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400
      
      
@app.route('/send_swipe', methods=['POST'])
def send_swipe():
    try:
        data = request.get_json()
        user_id = data['user_id']
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/swipes'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        params = {'user_id': user_id}
        response = requests.post(url, headers=headers, params=params)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_swipes', methods=['GET'])
def get_swipes():
    try:
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/swipes'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.get(url, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400
      
@app.route('/check_matches', methods=['GET'])
def check_matches():
    try:
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/matches'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.get(url, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400
      
@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        recipient_id = data['recipient_id']
        message = data['message']
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/messages'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        params = {'recipient_id': recipient_id, 'message': message}
        response = requests.post(url, headers=headers, params=params)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/messages'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.get(url, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/report_user', methods=['POST'])
def report_user():
    try:
        data = request.get_json()
        user_id = data['user_id']
        reason = data['reason']
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = f'https://prod.nevermet.io/users/{user_id}/report'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        params = {'reason': reason}
        response = requests.post(url, headers=headers, params=params)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/block_user', methods=['POST'])
def block_user():
    try:
        data = request.get_json()
        user_id = data['user_id']
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = f'https://prod.nevermet.io/users/{user_id}/block'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.post(url, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_block_list', methods=['GET'])
def get_block_list():
    try:
        auth_token = request.headers.get('Authorization').split()[1]
        timestamp = int(request.headers.get('Timestamp'))
        device_id = request.headers.get('Device-ID')
        app_id = request.headers.get('App-ID')
        app_version = request.headers.get('App-Version')
        os = request.headers.get('OS')

        url = 'https://prod.nevermet.io/users/blocked'
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Timestamp': str(timestamp),
            'Device-ID': device_id,
            'App-ID': app_id,
            'App-Version': app_version,
            'OS': os
        }
        response = requests.get(url, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

if __name__ == '__main__':
    app.run()

