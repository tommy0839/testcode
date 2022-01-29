import nltk
nltk.download('punkt')

import pykakasi
import alkana
alkana.add_external_data('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/alkana/sample.csv')

text = u"ゆったり癒しのジャズ ～冬に楽しめるピアノ"
kakasi = pykakasi.kakasi()
kakasi.setMode("H","K") # Hiragana to ascii, default: no conversion
kakasi.setMode("K","K") # Katakana to ascii, default: no conversion
kakasi.setMode("J","K") # Japanese to ascii, default: no conversion
kakasi.setMode("a","K") # Japanese to ascii, default: no conversion
conv = kakasi.getConverter()
result = conv.do(text)

sentence = "Smooth Jazz Background"
t = nltk.word_tokenize(sentence)

print(result)
print(t)

for _ in t:
    print(alkana.get_kana(_),end="")

print("\ndone")