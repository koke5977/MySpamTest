import json
import flask
from flask import request
import mytext

TM_PORT_NO = 8084
app = flask.Flask(__name__)
print("http://localhost:" + str(TM_PORT_NO))

# テスト用
text1 = """
昨日映画館に行ってきました。とても迫力がありました。
週末によくNetflixで昔の映画を３作品ほど観賞しますが、
巨大なスクリーンと音響による臨場感に勝るものはありません。
"""

text2 = """
セキュリティ警告です！
お使いになっているPCがウィルスに感染されている危険があります！
今すぐこちらのサイトから無料の検証作業を行ってください！！
"""

label, per, no = mytext.check_genre(text1)
print(text1, label, per, no)
label, per, no = mytext.check_genre(text2)
print(text2, label, per, no)

@app.route('/', methods=['GET'])
def index():
    with open("index.html", "rb") as f:
        return f.read()

@app.route('/api', methods=['GET'])
def api():
    q = request.args.get('q', '')
    if q == '':
      return '{"label": "テキストボックスに文章を入れてください", "per":0}'
    print("q=", q)
    
    label, per, no = mytext.check_genre(q)
    return json.dumps({
      "label": label, 
      "per": per,
      "genre_no": no
    })
    
if __name__ == '__main__':

    app.run(debug=False, port=TM_PORT_NO)

