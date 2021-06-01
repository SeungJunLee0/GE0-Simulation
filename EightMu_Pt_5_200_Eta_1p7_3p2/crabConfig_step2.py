import os
import CRABClient
from WMCore.Configuration import Configuration

################################################################################
# NOTE
################################################################################
SAMPLE = 'EightMu_Pt_5_200_Eta_1p7_3p2'
GEOMETRY =  '2026D76'
PU = 'PU200'
PSET_NAME = 'step_2_GEN-SIM-DIGI-RAW_cfg.py'
INPUT_DATASET = None

################################################################################
# NOTE
################################################################################
CMSSW_VERSION = os.environ['CMSSW_VERSION']
STEP = PSET_NAME.replace('_cfg.py', '')

OUTPUT_PRIMARY_DATASET = 'GE0_{sample}'.format(sample=SAMPLE)

OUTPUT_DATASET_TAG = '{version}_{geometry}{pu}_{step}'.format(
    version=CMSSW_VERSION,
    geometry=GEOMETRY,
    pu=PU,
    step=STEP)

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
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = PSET_NAME
config.JobType.maxMemoryMB = 5000

config.section_("Data")
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.inputDBS = 'phys03'
config.Data.publication = True

config.Data.inputDataset = INPUT_DATASET
config.Data.outputDatasetTag = OUTPUT_DATASET_TAG

# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Using_pile_up
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.whitelist = ['T2_US_Purdue'] # pile-up site
config.Site.storageSite = 'T2_KR_KISTI'
