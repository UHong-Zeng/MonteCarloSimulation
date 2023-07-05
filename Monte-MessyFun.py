import matplotlib.pyplot as plt
import numpy as np

amount = 10000 # 點生成的數量
insideAmounts = 0

def Function(x):
    return 2/(2*x**2+3*x-1)**2
requireRange = [[-1.5,0],[Function(-1.5),Function(0)]]
print(requireRange)

def IsOutSide(x,y):
    if y > 2/(2*x**2+3*x-1)**2:
        return True
    else:
        return False

fig = plt.figure(figsize=(10,8))

x = np.linspace(-5,5,500)
print(len(x))
plt.plot(x, Function(x))

#顯示座標
plt.plot(requireRange[0][1],requireRange[1][1],color='red',marker='o',alpha=1)
plt.gca().annotate('A (0, {})'.format(requireRange[1][1]), xy=(0.05, requireRange[1][1]), xycoords='data', fontsize=10) #顯示O點座標
plt.axvline(-1.5,color='orange')
plt.plot(requireRange[0][0],requireRange[1][0],color='red',marker='o',alpha=1)
plt.gca().annotate('B (-1.5, {})'.format(requireRange[1][0]), xy=(-1.45, requireRange[1][0]), xycoords='data', fontsize=10) #顯示O點座標

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('axes',.5))
ax.spines['left'].set_position(('axes',.5))
plt.ylim(-2.2,2.2)
plt.xlim(-3,3)

xSpots = np.random.uniform(-1.5,0,size=amount) # X軸的隨機座標
ySpots = np.random.uniform(0,2,size=amount) # Y軸的隨機座標
outSideX = []
outSideY = []
inSideX = []
inSideY = []
accuracy = []

total=0
for x, y in zip(xSpots, ySpots):
    if IsOutSide(x,y) :
        outSideX.append(x)
        outSideY.append(y)
    else:
        inSideX.append(x)
        inSideY.append(y)
        insideAmounts += 1
    total += 1
    accuracy.append(2*1.5*insideAmounts / total)
print('total:{}'.format(total))
dotSize = 2
outSide = plt.scatter(outSideX,outSideY,color='orangered', s=dotSize) #用橘色點顯示圓外座標
inSide = plt.scatter(inSideX,inSideY,color='deepskyblue', s=dotSize) #用深天空藍色的點顯示圓內座標

fig1 = plt.figure(figsize=(10,8))
plt.plot(accuracy)
plt.axhline(1.13)
plt.xscale('log')

print('{}個點的預測面積為: {:.10f}'.format(amount,2*1.5*insideAmounts / total))
print('實際面積為: {}'.format(1.13))

plt.show()