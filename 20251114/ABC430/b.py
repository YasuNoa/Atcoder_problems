#自分の回答

'''
考えた方法

nからmの取り出し方は(n-m+1)^2
で、順番に入ってくる配列s[i,j]のインプットの仕方がわからなかったが、
それがinputできていれば、forループでs=iの時、jをm-1回増加させ、
その次にiをm-1回増加させることでマトリクスをとってきたかった。
それを取得できれば、あとは重複の確認で、1つのマトリクスを全探索するイメージかな？と
for文でs[0,0]s[0,1]s[1,0]s[1,1]のマトリックスのインデックス増やしていって、
増やした時の色が同じならFalseにし、その数を出力するイメージかなと、、。
めちゃくちゃではあるが、。
'''
n,m=map(int,inoput().split())
s=list(map(int,input().split()))

i=0
j=0
array1=[]
array2=[]

for j in range(m-1):
  array1+=s[j]
  j+=1
  
  for i in range(m-1):
    array2=[array1,j]
    i+=1
    
    
count=[]
  count=s[i,j]
  
#模範回答
# 1. 入力の受け取り
N, M = map(int, input().split())

# N行の文字列をリストSに格納する
# S = ['..#', '#.#', '..#'] のような形になる
S = []
for _ in range(N):
    S.append(input())

# 3. 見つけたユニークなパターンを保存するset
unique_patterns = set()

# 2. 全パターンの切り出し
# r (row) は 0 から N-M まで動く
for r in range(N - M + 1):
    # c (column) は 0 から N-M まで動く
    for c in range(N - M + 1):
        
        # 3. パターンの構築 (M x M マトリクスを切り出す)
        pattern = [] # 今回切り出すパターンを一時的に保存するリスト
        
        # r行目からM行分 (r ~ r+M-1行目)
        for i in range(M):
            # S[r+i] (r+i 行目) の c列目からM文字分 (c ~ c+M-1列目) をスライス
            row_segment = S[r + i][c : c + M]
            pattern.append(row_segment)
        
        # 4. 重複の確認 (setに追加)
        # pattern は ['#.', '.#'] のようなリスト
        # setに入れるために tuple('#.', '.#') のようなタプルに変換する
        unique_patterns.add(tuple(pattern))

# 5. 結果の出力
# setの要素数が、ユニークなパターンの種類数
print(len(unique_patterns))

'''
入力: s=list(map(int,input().split())) ではなく、
 for ループで input() を $N$ 回呼び出すのが正解です。
 2重ループ: for r in range(N - M + 1): と for c in range(N - M + 1): 
 ですべての開始位置 $(r, c)$ を試します。
 スライス: S[r + i][c : c + M] というスライス機能を使うと、
 $i$ 番目の行の $M$ 文字分を簡単に切り出せます。
 set と tuple: Pythonで重複を数える問題の定番テクニックです。
 リストは set に入れられないので、 tuple() でタプルに変換してから add() 
'''

#別解
