import requests
# “noaa_gfs_global_sflux_0.12d”は気象データのID
url = "http://api.planetos.com/v1/datasets/noaa_gfs_global_sflux_0.12d/point"
querystring = {
"lat":"35.70", # 緯度
"lon":"139.80" # 経度,
"var":"Temperature_surface", # 温度
"count":"500", # データ取得数
"apikey":"xxxx" # xxxxはアカウント設定で取得したAPIキー
}
response = requests.request( “GET”, url, params=querystring )