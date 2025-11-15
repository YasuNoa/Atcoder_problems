# 1:
2つ以上のinputがあり、それぞれを整数で一気に受け取りたい場合。
a,b=map(int,input().split())
こんな感じにして、mapを使う

# 2:
list型でinputとっていきたい場合は、mapをlistで囲む。

# 3:
Bool型を使うことで判定系の問題を乗り越える。

find=False

for i in range(n):
    if c==a[1]:
        find=True
        break

if found :
    print("yes")
else :
    print("no)

# 4:
setは、重複する要素を自動的に取り除いてくれるデータ構造
今回は、up=set()で箱を作って、

up.add(taple(pattern))
これはupという集合に、tapleしたパターンという配列をくわえることで、データを文字列など変更可能なものに固定化し、変更できないようにした。

# 5:
 row_segment = S[r + i][c : c + M]
 スライスはc文字から何文字を切り出すかを書いたもの。
 この場合、CからM文字を切り出す。(r,c)=(2,1)、M=2の場合、
 配列Sの3行目の文字列から、2文字を取り出す操作
[c:c+M]は、c列目からc+M列未満を取り出す。



