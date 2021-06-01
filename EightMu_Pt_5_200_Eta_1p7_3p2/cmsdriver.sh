#!/bin/bash

# modified from https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_0_0_pre1__UPSG_Std_2026D76noPU-TenTau_15_500_Eta3p1-00001
cmsDriver.py EightMu_Pt_5_200_Eta_1p7_3p2_cfi \
	--beamspot HLLHC \
	--conditions auto:phase2_realistic_T21 \
	--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
	--datatier GEN-SIM \
	--era Phase2C11I13M9 \
	--eventcontent FEVTDEBUG \
	--fileout "file:step1.root" \
	--geometry Extended2026D76 \
	--no_exec \
	--number 10 \
	--python_filename step_1_GEN-SIM_cfg.py \
	--relval 9000,100 \
	--step GEN,SIM

# modified from https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_0_0_pre1__UPSG_Std_2026D76PU200_highPU-TenTau_15_500_Eta3p1-00001
cmsDriver.py step2 \
	--conditions auto:phase2_realistic_T21 \
	--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
	--datatier GEN-SIM-DIGI-RAW \
	--era Phase2C11I13M9 \
	--eventcontent FEVTDEBUGHLT \
	--filein "file:step1.root" \
	--fileout "file:step2.root" \
	--geometry Extended2026D76 \
	--no_exec \
	--number -1 \
	--pileup AVE_200_BX_25ns \
	--pileup_input das:/RelValMinBias_14TeV/CMSSW_12_0_0_pre1-113X_mcRun4_realistic_v7_2026D76noPU-v1/GEN-SIM \
	--python_filename step_2_GEN-SIM-DIGI-RAW_cfg.py \
	--step DIGI:pdigi_valid,L1TrackTrigger,L1,DIGI2RAW,HLT:@fake2

cmsDriver.py step3 \
	--conditions auto:phase2_realistic_T21 \
	--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
	--datatier GEN-SIM-RECO \
	--era Phase2C11I13M9 \
	--eventcontent FEVTDEBUGHLT \
	--filein "file:step2.root" \
	--fileout "file:step3.root" \
	--geometry Extended2026D76 \
	--no_exec \
	--number -1 \
	--python_filename step_3_GEN-SIM-RECO_cfg.py \
	--step RAW2DIGI,L1Reco,RECO,RECOSIM,PAT
