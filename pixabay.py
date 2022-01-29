import requests

endpoint = "https://pixabay.com/api"

headers= {

}
params={
    "key":"24899478-743f75f0aec062c77fa7d0e86",
    "q":"勉強",
    "lang":"ja",
    "image_type":"photo"
}

result = requests.get(endpoint, headers=headers, params=params)

res = result.json()

print(res["total"])
for hit in res["hits"]:
    print("詳細URL："+hit["pageURL"])
    print("イメージタイプ："+hit["type"])
    print("カテゴリ："+hit["tags"])
    print("プレビュー画像URL："+hit["previewURL"])
    print("画像URL："+hit["largeImageURL"])
    print("ダウンロード数："+str(hit["downloads"]))
    print("お気に入り数："+str(hit["likes"]))
    print("---------------------------")