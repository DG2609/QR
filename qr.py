from flask import Flask, make_response, request
from qrcode import make
from io import BytesIO

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def qr_code():
    url = request.args.get('url')
    img = make(url)
    buf = BytesIO()
    img.save(buf)
    buf.seek(0)
    response = make_response(buf.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='qr_code.png')
    return response

if __name__ == '__main__':
    app.run()
