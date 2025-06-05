import random

# ダミーの選手名リスト（日本人風の名前を50個用意）
names = [
    "佐藤健", "鈴木大輔", "高橋翔", "田中悠斗", "伊藤直樹", "渡辺亮", "山本健太", "中村優", "小林誠", "加藤大地",
    "吉田翔太", "山田陸", "佐々木駿", "山口和也", "松本悠真", "井上大樹", "木村拓海", "林優斗", "斎藤翼", "清水大輝",
    "山崎颯太", "森本健", "池田悠", "橋本大輔", "阿部翔", "石井大地", "村上直樹", "岡田健太", "長谷川翔", "近藤優",
    "石田陸", "坂本大輔", "遠藤翔太", "藤田悠斗", "青木健", "福田大地", "三浦翔", "西村優", "藤井健太", "岡本大輔",
    "松田翔太", "中島悠", "小川大地", "後藤健", "岡本翔", "村田優斗", "竹内大輔", "金子翔", "和田健太", "原田大地"
]

# タイムをランダム生成（9.56～12.99秒）
times = [round(random.uniform(9.56, 12.99), 2) for _ in range(50)]

# 選手リスト作成
runners = [{"name": name, "time": time} for name, time in zip(names, times)]

# バブルソートでタイム順に並び替え（アルゴリズムの過程を表示）
print("バブルソートによる並び替えの過程：")
n = len(runners)
for i in range(n):
    for j in range(0, n-i-1):
        if runners[j]["time"] > runners[j+1]["time"]:
            # 並び替え前の2人を表示
            print(f"入れ替え: {runners[j]['name']}({runners[j]['time']}) ↔ {runners[j+1]['name']}({runners[j+1]['time']})")
            runners[j], runners[j+1] = runners[j+1], runners[j]

# 上位5名を表示
print("\n上位5名のタイム：")
for i in range(5):
    print(f"{i+1}位: {runners[i]['name']} - {runners[i]['time']}秒")