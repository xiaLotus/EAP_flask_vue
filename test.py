import sys
# 更換
package_path = r".\python-3.9.12\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # 啟用跨域請求

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(debug=True)



# curl http://127.0.0.1:5000/api/message