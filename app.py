import zxcvbn
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Define common password list for additional checks
COMMON_PASSWORDS = ['password', '123456', 'qwerty', 'abc123']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password_strength', methods=['POST'])
def check_password_strength():
    password = request.json['password']
    
    # Perform zxcvbn password strength check
    result = zxcvbn.zxcvbn(password)
    strength = result['score']  # Score ranges from 0 to 4
    
    # Check against common passwords
    is_common_password = password.lower() in COMMON_PASSWORDS
    
    # Provide feedback based on zxcvbn score
    feedback = {
        'score': strength,
        'feedback': result['feedback']['suggestions'],
        'common_password': is_common_password
    }
    
    return jsonify(feedback)

if __name__ == '__main__':
    app.run(debug=True)
