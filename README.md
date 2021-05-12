# How to setup
```bash
cmsrel CMSSW_12_0_0_pre1
cd CMSSW_12_0_0_pre1/src
eval `scramv1 runtime -sh`
git-cms-addpkg Configuration/Generator
cp ../../genfragments/* Configuration/Generator
scram build -j
cd -
```

# How to invalidate dataset
https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Changing_a_dataset_or_file_statu
```bash
DATASET="/GE0_EightMu_Pt_5_200_Eta_1p7_3p2_noPU/seyang-CMSSW_12_0_0_pre1_step_1_GEN-SIM-12b46ca0dfd7084a8c784c8011b10b46/USER"
python $DBS3_CLIENT_ROOT/examples/DataOpsScripts/DBS3SetDatasetStatus.py --dataset=${DATASET} --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=INVALID --recursive=False
```

# How to get a list of datasets published in phys03
```bash
DATASET="/GE0_*/seyang-*/USER"
dasgoclient --limit 0 --query "dataset=${DATASET} instance=prod/phys03 system=dbs3"
```
