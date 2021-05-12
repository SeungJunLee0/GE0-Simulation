```bash
cmsrel CMSSW_12_0_0_pre1
cd CMSSW_12_0_0_pre1/src
eval `scramv1 runtime -sh`
git-cms-addpkg Configuration/Generator
cp ../../genfragments/* Configuration/Generator
scram build -j
cd -
```
