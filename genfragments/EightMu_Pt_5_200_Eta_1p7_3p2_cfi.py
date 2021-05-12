import FWCore.ParameterSet.Config as cms

# Modified from Configuration/Generator/python/TenMuExtendedE_0_200_pythia8_cfi.py
# CMS-TDR-016, Geometric acceptance in abs(eta): 2.03 - 2.8

generator = cms.EDFilter("Pythia8PtGun",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(200.0),
        MinPt = cms.double(5.0),
        ParticleID = cms.vint32(-13,-13,13,13),
        AddAntiParticle = cms.bool(True),
        MaxEta = cms.double(3.2),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(1.7),
        MinPhi = cms.double(-3.14159265359) ## in radians

    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts

    psethack = cms.string('Eight mu pt 5 to 200 eta 1.7 to 3.2'),
    firstRun = cms.untracked.uint32(1),
    PythiaParameters = cms.PSet(parameterSets = cms.vstring())

)
