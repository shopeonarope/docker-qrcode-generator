import base64
from flask import Flask, Blueprint, request, render_template
from flask_qrcode import QRcode
from pathlib import Path

qrcode = Blueprint('qrcode', __name__)

generate_qrcode = QRcode()

@qrcode.route('/', methods=['GET'])
def get_qrcode():
    data = Path('/etc/convert_to_qr').read_text()
    image_bytes = generate_qrcode(data, error_correction='H', mode='raw')
    image_b64=(base64.b64encode(image_bytes.read())).decode()
    return render_template('index.html',image_b64=image_b64,password=data)
