from openturns.usecases import ishigami_function
import openturns as ot
import openturns.viewer as viewer
from matplotlib import pylab as plt
import numpy as np
ot.Log.Show(ot.Log.NONE)



ot.RandomGenerator.SetSeed(0)
formula = ['((A*t*h*K)/L)']
model = ot.SymbolicFunction(['K', 'L', 'A','h','t'], formula)
distribution = ot.ComposedDistribution([ot.Uniform(0.0, 10.0)] * 5)
print(distribution)
sensitivityAnalysis = ot.FAST(model, distribution, 101)
print(sensitivityAnalysis.getFirstOrderIndices())


y = np.array(sensitivityAnalysis.getFirstOrderIndices())
mylab=['K', 'L', 'A','h','t']
plt.pie(y,labels=mylab)
plt.show() 


#print('First order FAST indices:', firstOrderIndices)
#print('Total order FAST indices:', totalOrderIndices)

#graph = ot.SobolIndicesAlgorithm.DrawImportanceFactors(
    #sensitivityAnalysis.getFirstOrderIndices, distribution.getDescription(), 'FAST first order indices')
#view = viewer.View(graph)
#plt.show()
