#B問題の自分の解答。
#それぞれ部品をPi番目にして、重さの合計を取ろうとした。今気づいたけど、P[i]は重さの合計でないから不正解。

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

#B問題の模範解答

#かかった時間30分