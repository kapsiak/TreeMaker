import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_0.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_1.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_3.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_4.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_5.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_6.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_7.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_8.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_9.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_10.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_11.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_12.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_13.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_14.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_15.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_16.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_17.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_18.root",
"/store/user/ngogate/SUSY_MINIAOD//CN600_sgetGlGl_31_Jul_2022_19.root",
] )
