import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_0.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_1.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_2.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_3.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_4.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_5.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_6.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_7.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_8.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_9.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_10.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_11.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_12.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_13.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_14.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_15.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_16.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_17.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_18.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_19.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_20.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_21.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_22.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_23.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_24.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_25.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_26.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_27.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_28.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_29.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_30.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_32.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_33.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_34.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_35.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_36.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_37.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_38.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_39.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_40.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_41.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_42.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_43.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_44.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_45.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_46.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_47.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_48.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_49.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_50.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_51.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_52.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_53.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_54.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_55.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_56.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_57.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_58.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_59.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_60.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_61.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_62.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_63.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_64.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_65.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_66.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_67.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_68.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_69.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_70.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_71.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_72.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_73.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_74.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_75.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_76.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_77.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_78.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_79.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_80.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_81.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_82.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_83.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_84.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_85.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_86.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_87.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_88.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_89.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_90.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_91.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_92.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_93.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_94.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_95.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_96.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_97.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_98.root",
"/store/user/ckapsiak/RPV_2w4j_mStop-1000_mSbot-700_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM/MainProd//MINIAODSIM_99.root",
] )
