from rootpy.io import root_open
from root_numpy import hist2array
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np
import itertools
from rootpy.plotting.style import get_style, set_style

set_style('ATLAS', mpl=True)


#myFile = root_open("ttgamma_SR1_ejets__HFT_MVA2_histos.root")
#ttgamma = myFile.Get("HFT_MVA2_ttgamma")
#hadronfakes = myFile.Get("HFT_MVA2_hadronfakes")

myFile = root_open("ttgamma_SR1_ejets__HFT_MVA_histos.root")
ttgamma = myFile.Get("HFT_MVA_ttgamma")
hadronfakes = myFile.Get("HFT_MVA_hadronfakes")

# Get the values for each bin
# This determins how many times each 
# Value will get duplicated
ttgamma_array = hist2array(ttgamma)
hadronfakes_array = hist2array(hadronfakes)
values_tmp = np.concatenate((ttgamma_array,hadronfakes_array))
values = np.round(values_tmp)

# Get predictions
# This is actually completely dependent on the
# Binning being chosen
nbins = len(ttgamma_array)
ttgamma_predictions = []
hadronfakes_predictions = []
for i in range(1,nbins+1):
    pred = i/float(nbins)
    ttgamma_predictions.append(pred)
    hadronfakes_predictions.append(pred)

# Set labels for each process
ttgamma_scores = np.ones(nbins)
hadronfakes_scores = np.zeros(nbins)
# Concatenate everything into long arrays
scores_tmp = np.concatenate((ttgamma_scores,hadronfakes_scores))
predictions_tmp = np.concatenate((ttgamma_predictions,hadronfakes_predictions))


scores_tmp2 = []
predictions_tmp2 = []
for i in range(0,len(scores_tmp)):
    scores_tmp2.append(np.repeat(scores_tmp[i],values[i]).tolist())
    predictions_tmp2.append(np.repeat(predictions_tmp[i],values[i]).tolist())

# Flatten into long lists
scores = list(itertools.chain(*scores_tmp2))
predictions = list(itertools.chain(*predictions_tmp2))

# Plotting stuff
false_positive_rate, true_positive_rate, thresholds = roc_curve(scores,predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)
plt.title('')
plt.plot(1-false_positive_rate,true_positive_rate, 'b',
label='AUC = %0.2f'% roc_auc)
plt.legend(loc='upper right')
plt.plot([1,0],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('Background Rejection')
plt.xlabel('Signal Efficiency')
from matplotlib import rcParams
rcParams['text.usetex'] = True
plt.rc('font', family='sans-serif')
plt.rc('font', serif='Helvetica')
ax = plt.axes()
ax.text(0.08, 1.08, r'{{\it \textbf {\Huge ATLAS}}}')
ax.text(0.4, 1.08, r'{\huge Internal}')
plt.show()

