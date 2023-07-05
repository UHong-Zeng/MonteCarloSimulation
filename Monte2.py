import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

amount = 10000 # 點生成的數量
insideAmounts = 0

fig = plt.figure(figsize=(10,8))

x = np.linspace(-10,10,500)
print(len(x))
plt.plot(x, -(8*x**3 + x**2 - 9*x))
plt.axvline(1)
extremumX = 0.5721
extremumY = -(8*extremumX**3 + extremumX**2 - 9*extremumX)
plt.axhline(extremumY)
print("極值Y = {}".format(extremumY))

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('axes',.5))
ax.spines['left'].set_position(('axes',.5))
plt.ylim(-10,10)
plt.xlim(-2,2)

xSpots = np.random.uniform(0,1,size=amount) # X軸的隨機座標
ySpots = np.random.uniform(0,extremumY,size=amount) # Y軸的隨機座標
outSideX = []
outSideY = []
inSideX = []
inSideY = []
accuracy = []

total=0
for x, y in zip(xSpots, ySpots):
    total += 1
    if y > -(8*x**3 + x**2 - 9*x):
        outSideX.append(x)
        outSideY.append(y)
    else:
        inSideX.append(x)
        inSideY.append(y)
        insideAmounts += 1
    accuracy.append(extremumY*insideAmounts / total)

dotSize = 3
plt.scatter(outSideX,outSideY,color='orangered', s=dotSize)
plt.scatter(inSideX,inSideY,color='deepskyblue', s=dotSize)

fig1 = plt.figure(figsize=(10,8))
plt.plot(accuracy)
plt.axhline(13/6)
plt.xscale('log')

print('預測面積為: {}'.format(extremumY * insideAmounts / amount))
print('實際面積為: {}'.format(13/6))

plt.show()