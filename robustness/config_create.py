import json

params = {}

#Flags for Trajectory Selection
params['csel'] = True #True for executing CheckSel during training
params['resume'] = False #True for resuming training where it was left off

#Flags for Data Valuation
params['retain_scores'] = False #False for new/replaced computation of data values, True for using existing ones

#Flags for finding subset if required
params['findsubset'] = True #Flag for obtaining subset
params['simsel'] = False #Flag for using SubSel to obtain subset

#Hyperparameters during Trajectory Selection
params['trainbatch'] = 100 #Training data batch size
params['testbatch'] = 100 #Test data batch size
params['epochs'] = 2 #Training epochs
params['num_freqep'] = 40 #Optional ; Frequency of epochs at which VTruST will be executed
#60% of 200000 = 120000 i.e 1200 batches, selecting 1300 batches
params['num_trajpoint'] = 1300 #Number of to-be selected trajectories

#Path
params['root_dir'] = './main/'

with open("config.json", "w") as outfile:
    json.dump(params, outfile)
