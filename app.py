from flask import Flask, send_file
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/rs-pdf', methods=['GET'])
def rs_pdf():
    try:
        # 固定的PDF文件路径
        pdf_path = ('梁慧_运维开发_广科大_2024.pdf')  # 替换为你的PDF文件路径

        # 检查文件是否存在
        if not os.path.exists(pdf_path):
            raise FileNotFoundError("PDF文件未找到")

        # 读取PDF文件
        with open(pdf_path, 'rb') as pdf_file:
            pdf_data = pdf_file.read()

        # 返回文件
        return send_file(
            BytesIO(pdf_data),
            mimetype='application/pdf',
            as_attachment=True,
            download_name='梁慧_运维开发_广科大_2024.pdf'
        )

    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
