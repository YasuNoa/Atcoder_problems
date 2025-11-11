#B問題の自分の解答。
#それぞれ部品をPi番目にして、重さの合計を取ろうとした。今気づいたけど、P[i]は重さの合計でないから不正解。
#キモとして、p[i]とw[]の関係、Boolを使って、部品のあるなしから計算を加えるとこなど。
#W[P[i]-1]が、対応関係だったということに気付けるか、だった。


X=int(input())
N=int(input())
W=list(map(int,input().split()))
Q=int(input())

array_parts=[X]
input_P=list(map(int,input().split()))

for P[i] in input_P :
  if P[i] in array_parts :
    array_parts.remove(P[i])
    i+=1
  
  else:
    array_parts.append(P[i])
    i+=1
    
print(sum(array_parts))

#B問題の模範解答。
X = int(input())
N = int(input())
W = list(map(int, input().split()))
b = [False] * N # b[i] := i 種類目のパーツがついていれば True, そうでなければ False
Q = int(input())
for q in range(Q):
    P = int(input())
    P -= 1
    if b[P]: # すでについていたら
        b[P] = False # 外す
    else: # ついていなければ
        b[P] = True # つける
    # 重さを求める
    weight = X
    for i in range(N):
        if b[i]: # =Trueなら重さをつける。
            weight += W[i] # 重さを足す
    print(weight)
    # print(sum((w if f else 0 for w, f in zip(W, b)), X))
    # と書いてもいい

#別解答
X = int(input())
N = int(input())
W = list(map(int, input().split()))
#これは重さのList
b = [False] * N # b[i] := i 種類目のパーツがついていれば True, そうでなければ False
weight = X # 現在の重さ
Q = int(input())
for q in range(Q):
    P = int(input())
    P -= 1
    if b[P]: # すでについていたら
        b[P] = False # 外して
        weight -= W[P] # 重さも減らす
    else: # ついていなければ
        b[P] = True # つけて
        weight += W[P] # 重さを増やす
    print(weight)



#かかった時間30分