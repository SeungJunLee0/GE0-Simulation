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

# How to get a list of datasets published in phys03
```bash
DATASET="/GE0_*/seyang-*/USER"
dasgoclient --limit 0 --query "dataset=${DATASET} instance=prod/phys03 system=dbs3"
```
