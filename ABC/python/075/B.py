import sys
H,W = map(int,input().split())
array = []
for I in range(H):
    array.append(list(map(str,input())))

if not (1 <= H <= 50 and 1 <= W <= 50):
    sys.exit()

#作業用配列(オリジナルより一回り大きい。つまり縦横それぞれ+2)初期化
result = [[0]*(W+2) for i in range((H+2))]
#８近傍処理(中心位置の処理無し)
def input_result_array(x,y,result):
    result[x-1][y-1] += 1
    result[x-1][y] += 1
    result[x-1][y+1] += 1
    result[x][y-1] += 1
    result[x][y+1] += 1
    result[x+1][y-1] += 1
    result[x+1][y] += 1
    result[x+1][y+1] += 1
    return result

bomb_point = [] #bomb位置記録用
for I in range(H):
    for J in range(W):
        if array[I][J] == '#':
            bomb_point.append([I,J])
            result = input_result_array(I+1,J+1,result)

#作業用配列にはbombが無いので追加
for I in range(len(bomb_point)):
    x,y = bomb_point[I]
    result[x+1][y+1] = '#'

#作業用配列から必要な部分だけ切り出し整形表示
str_result = ''
for I in [I[1:-1] for I in result[1:-1]]:
    for J in I:
        str_result += str(J)
    str_result += '\n'
print(str_result)