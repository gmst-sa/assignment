from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/api/convert-color', methods=['POST'])
def convert_color():
    try:
        color_code = request.json['color_code']
        r, g, b = (int(color_code[i:i+2], 16) for i in (0, 2, 4))
        return jsonify({'red': r, 'green': g, 'blue': b})
    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid input'})

@app.route('/v1/healthcheck')
def healthcheck():
    return jsonify(status='healthy')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
