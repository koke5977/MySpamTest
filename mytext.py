import pickle, tfidf
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.models import model_from_json


# 独自のテキストでテスト
text1 = """
会社から支給されているiPhoneの調子が悪いのです。
修理に出しますので、しばらくはアプリのテストができません。
明日また別のAndroidで改めて連絡します。
"""
text2 = """
昨日映画館に行ってきました。とても迫力がありました。
週末によくNetflixで昔の映画を３作品ほど観賞しますが、
巨大なスクリーンと音響による臨場感に勝るものはありません。
"""
text3 = """
億万長者になれる方法を教えます。
すぐに以下のメールアドレスに返信して、稼ぐチャンスを
モノにしましょう！まずは月１００万以上を目指しましょう。
"""
text4 = """
セキュリティ警告です。
お使いになっているPCがウィルスに感染されている危険があります。
今すぐこちらのサイトから無料の検証作業を行ってください。
"""

# TF-IDFの辞書を読み込む
tfidf.load_dic("./spam-tdidf.dic")

# Kerasのモデルを定義&重みデータを読み込む
nb_classes = 2
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(6765,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(nb_classes, activation='softmax'))
model.compile(
    loss='categorical_crossentropy',
    optimizer=RMSprop(),
    metrics=['accuracy'])
model.load_weights('./spam-model.hdf5')

# テキストを指定して判定
def check_genre(text):
    LABELS = ["OKです。", "スパムです！"]
    data = tfidf.calc_text(text)
    model._make_predict_function()
    pre = model.predict(np.array([data]))[0]
    n = pre.argmax()
    print(LABELS[n], "(", pre[n], ")")
    return LABELS[n], float(pre[n]), int(n) 

if __name__ == '__main__':
    check_genre(text1)
    check_genre(text2)
    check_genre(text3)
    check_genre(text4)

