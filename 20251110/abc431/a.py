#自分の解答
h,b = map(int,input().split())

if h >b :
  print (h-b)
  
else :
  print(0)

#模範解答は2通りあった。上のもいいけど、こっちの方が綺麗。
H, B = map(int, input().split())
print(max(H, B) - B)

#かかった時間10分