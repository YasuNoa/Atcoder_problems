#B問題の自分の解答。

#問題文から、(A1,A2,A3,,,,AN)の和からMを引いた数が配列Aの中にあるあを判定する問題だと推測。
#ある＝Yes,ない=No


n,m=map(int,input().split())
a=list(map(int,input().split()))
b=0

for i in range(n) :
  b=b+a[i]
  
c=b-m


for i in range(n):
  if c =!a[i] :
      if i=n:
        print("No")
      else:
        i+=1
      
  else  :
    print("Yes")
   
'''
模範解答
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 1. 総和を計算
b = 0
for i in range(n):
    b = b + a[i]
# （別解: b = sum(a) と書くともっと簡単です）

# 2. 取り除くべき値 c を計算
c = b - m

# 3. c が a の中に存在するか調べる
found = False  # 「見つかったか」のフラグ（旗）。最初は「見つかってない(False)」
for i in range(n):
    if c == a[i]:
        found = True  # 見つかった！
        break         # 見つかったら、もうループを続ける必要はないので抜ける

# 4. ループが全て終わった後に、フラグを見て判定する
if found: # もし found が True なら
    print("Yes")
else:     # もし found が False (＝最後まで見つからなかった) なら
    print("No")

    #bool型を使えるようになりたい。

#別解
n, m = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) - m in a:
    print("Yes")
else:
    print("No")