import numpy as np

def calculateMaxDD(cumret):
    highwatermark = np.zeros(cumret.shape)
    drawdown = np.zeros(cumret.shape)
    drawdowndurration = np.zeros(cumret.shape)
    for t in np.arange(1, cumret.shape[0]):
        highwatermark[t] = np.maximum(highwatermark[t - 1], cumret[t])
        drawdown[t] = (1 + cumret[t]) / (1 + highwatermark[t]) - 1
        if drawdown[t] == 0:
            drawdowndurration[t] = 0
        else:
            drawdowndurration[t] = drawdowndurration[t-1] + 1
    
    maxDD , i  =  np.min(drawdown) , np.argmin(drawdown) #duel variable assignment
    #drawdown < 0 always
    maxDDD = np.max(drawdowndurration)
    return maxDD, maxDDD, i







