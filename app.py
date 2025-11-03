from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.before_request
def before_request():
    host = request.host.lower()
    if host.startswith('bf.') or host == 'bf':
        request.subdomain = 'bf'
    else:
        request.subdomain = None

@app.route('/')
def index():
    if hasattr(request, 'subdomain') and request.subdomain == 'bf':
        return render_template('bf.j2')
    return render_template('index.html')

@app.route('/utils/<path:filename>')
def utils(filename):
    return send_from_directory('utils', filename)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5200, debug=True)
