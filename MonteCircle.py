import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,8))
plt.plot()
plt.plot(0,0,color='red',marker='o',alpha=0.3)
plt.gca().annotate('O (0, 0)', xy=(0.05, 0.05), xycoords='data', fontsize=10) #顯示O點座標

angles = np.linspace(0,2*np.pi,100)
xs = np.cos(angles)
ys = np.sin(angles)

plt.plot(xs,ys, alpha=0.2) #畫圓，(alpha) = 0.2

amount = 10000 # 點生成的數量
insideAmounts = 0

xSpots = np.random.uniform(-1,1,size=amount) # X軸的隨機座標
ySpots = np.random.uniform(-1,1,size=amount) # Y軸的隨機座標
outSideX = []
outSideY = []
inSideX = []
inSideY = []
accurate = []

total=0
for x, y in zip(xSpots, ySpots):
    total += 1
    if x**2 + y**2 >= 1:
        outSideX.append(x)
        outSideY.append(y)
    else:
        inSideX.append(x)
        inSideY.append(y)
        insideAmounts += 1
    accurate.append(4*insideAmounts / total)

dotSize = 2
outSide = plt.scatter(outSideX,outSideY,color='orangered', s=dotSize) #用橘色點顯示圓外座標
inSide = plt.scatter(inSideX,inSideY,color='deepskyblue', s=dotSize) #用深天空藍色的點顯示圓內座標

plt.xlim(-1.01,1.01)
plt.ylim(-1.01,1.01)
plt.gca().set_aspect('equal') #使座標以1:1顯示，不會讓圓變形
plt.savefig('./circle.jpg')

# 顯示每個數量所計算出Pi的值
fig2 = plt.figure(figsize=(15,8))
plt.plot(accurate, linewidth=3)
plt.axhline(3.1415926)
plt.xlabel("Amount")
plt.ylabel("Simulation")
plt.xscale('log')
print(len(accurate))
plt.savefig('./simulation.jpg')

plt.show()

print("Pi: {:.10f}".format(4*insideAmounts / amount))