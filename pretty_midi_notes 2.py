# librosaをインポート
import librosa
# numpyをインポート（配列を生成するため）
import numpy as np
# matplotlibをインポート（グラフ描画するため）
import matplotlib.pyplot as plt

# 音楽ファイルのパスを設定（例："/foldername/filename.mp3"）
file_name = "MIDI_Pf_Bs_Ds_Bossa Nova_4_4_28_0.mp3"
# loadメソッドでy=音声信号の値（audio time series）、sr=サンプリング周波数（sampling rate）を取得
# 参考：https://librosa.org/doc/latest/generated/librosa.load.html?highlight=load#librosa.load
y, sr = librosa.load(file_name)
# 時間 = yのデータ数 / サンプリング周波数
# 参考：https://note.nkmk.me/python-numpy-arange-linspace/
time = np.arange(0,len(y)) / sr

# xにtime、yにyとしてプロット
plt.plot(time, y)
# x軸とy軸にラベルを設定（x軸は時間、y軸は振幅）
# 参考：https://techacademy.jp/magazine/19316
plt.xlabel("Time(s)")
plt.ylabel("Sound Amplitude")

# グラフを表示
plt.show()