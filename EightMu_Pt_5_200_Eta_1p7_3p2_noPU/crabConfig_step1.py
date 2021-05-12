import os
import CRABClient
from WMCore.Configuration import Configuration

SAMPLE = 'EightMu_Pt_5_200_Eta_1p7_3p2_noPU'
PSET_NAME = 'step_1_GEN-SIM_cfg.py'
UNITS_PER_JOB = 130
JOBS = 100

CMSSW_VERSION = os.environ['CMSSW_VERSION']
TOTAL_UNITS = UNITS_PER_JOB * JOBS # ~ 100k
STEP = PSET_NAME.replace('_cfg.py', '')
OUTPUT_PRIMARY_DATASET = 'GE0_{sample}'.format(sample=SAMPLE)
OUTPUT_DATASET_TAG = '{version}_{step}'.format(version=CMSSW_VERSION, step=STEP)
REQUEST_NAME = OUTPUT_PRIMARY_DATASET + '_' + OUTPUT_DATASET_TAG

################################################################################
# NOTE
################################################################################
config = Configuration()

config.section_("General")
config.General.requestName = REQUEST_NAME
config.General.transferOutputs = True
config.General.workArea = "crab_projects"

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = PSET_NAME

config.section_("Data")
config.Data.outputPrimaryDataset = OUTPUT_PRIMARY_DATASET
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = UNITS_PER_JOB
config.Data.totalUnits = TOTAL_UNITS
config.Data.publication = True
config.Data.outputDatasetTag = OUTPUT_DATASET_TAG

config.section_("Site")
config.Site.storageSite = 'T2_KR_KISTI'
