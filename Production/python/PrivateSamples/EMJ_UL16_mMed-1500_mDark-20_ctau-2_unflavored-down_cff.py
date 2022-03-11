import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-1.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-10.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-11.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-12.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-13.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-14.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-2.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-4.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-7.root',  
'root://hepcms-0.umd.edu:1094////store/group/EMJRunII/Oct2021/UL16/step4_MINIAODv2_mMed-1500_mDark-20_ctau-2_unflavored-down_n-500_part-9.root',
] )
