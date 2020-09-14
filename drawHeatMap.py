import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def drawHeatMap(V, policy, vmin, vmax, trapDict, bonusDict, blockList):
    VPlot=V.copy()
    for bonus, bonusReward in bonusDict.items():
        VPlot[bonus]=bonusReward
    for trap, trapCost in trapDict.items():
        VPlot[trap]=trapCost
    x ,y, v=([x for (x, y), v in VPlot.items()], [y for (x, y), v in VPlot.items()], [v for (x, y), v in VPlot.items()])
    maxX, maxY=(max(x)+1, max(y)+1)
    label=[str(round(value,3)) for key,value in VPlot.items()]
    label, v=(np.array(label).reshape(maxX,maxY).transpose(), np.array(v).reshape(maxX,maxY).transpose())
    mask=np.array([(vi in blockList) for vi in V.keys()]).reshape(maxX,maxY).transpose()
    heatMap=sb.heatmap(v, annot=label, fmt="", cmap='RdYlGn', linewidths=0.30, vmin=vmin, vmax=vmax, center=0, mask=mask)
    for trap in trapDict.keys():
        xTrap, yTrap=trap
        plt.arrow(xTrap, yTrap, 1, 0, fc="r", ec="r", head_width=0.001, head_length=0.001)
        plt.arrow(xTrap, yTrap, 0, 1, fc="r", ec="r", head_width=0.001, head_length=0.001)
        plt.arrow(xTrap+1, yTrap, 0, 1, fc="r", ec="r", head_width=0.001, head_length=0.001)
        plt.arrow(xTrap, yTrap+1, 1, 0, fc="r", ec="r", head_width=0.001, head_length=0.001)
    for bonus in bonusDict.keys():
        xBonus, yBonus=bonus
        plt.arrow(xBonus, yBonus, 1, 0, fc="y", ec="y", head_width=0.001, head_length=0.001)
        plt.arrow(xBonus, yBonus, 0, 1, fc="y", ec="y", head_width=0.001, head_length=0.001)
        plt.arrow(xBonus+1, yBonus, 0, 1, fc="y", ec="y", head_width=0.001, head_length=0.001)
        plt.arrow(xBonus, yBonus+1, 1, 0, fc="y", ec="y", head_width=0.001, head_length=0.001)
    for s in [s for s in V.keys() if s not in list(trapDict.keys())+list(bonusDict.keys())+blockList]:
        x, y=s
        actions=policy[s].keys()
        for action in actions:
            plt.arrow(x+0.8, y+0.8, action[0]/10, action[1]/10, fc="k", ec="k", head_width=0.06, head_length=0.06)
    return heatMap


def drawFinalMap(V, policy, trapDict, bonusDict, blockList, normalCost):
    vmin=min([min(V.values())]+list(trapDict.values())+list(bonusDict.values()))
    vmax=max([max(V.values())]+list(trapDict.values())+list(bonusDict.values()))
    fig, ax=plt.subplots(figsize=(12,7))
    title=f"Value Map: R={normalCost}"
    plt.title(title, fontsize=18)
    ttl=ax.title
    ttl.set_position([0.5, 1.05])
    drawHeatMap(V, policy, vmin, vmax, trapDict, bonusDict, blockList)
    plt.savefig(f'valueIterationHeatMap_R={normalCost}.jpg')

def createAnimation(VRecord, policyRecord, trapDict, bonusDict, blockList, normalCost):
    vmin=min([min(V.values()) for V in VRecord]+list(trapDict.values())+list(bonusDict.values()))
    vmax=max([max(V.values()) for V in VRecord]+list(trapDict.values())+list(bonusDict.values()))
    def animate(i):
        fig.clear()
        title=f"Value Map: Round {i}, R={normalCost}"
        plt.title(title, fontsize=18)
        ttl=ax.title
        ttl.set_position([0.5, 1.05])
        heatmap=drawHeatMap(VRecord[i], policyRecord[i], vmin, vmax, trapDict, bonusDict, blockList)
        return heatmap
    fig, ax=plt.subplots(figsize=(12,7))
    ani = animation.FuncAnimation(fig, animate, len(VRecord))
    ani.save(f'valueIteration.gif',writer='pillow')