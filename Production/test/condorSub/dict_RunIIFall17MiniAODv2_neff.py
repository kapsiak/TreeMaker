#Made in python using
#import glob
#for f in glob.glob('RunIIFall17MiniAODv2/*'):
#     print  "\'"+f.replace("_cff.py","").replace("/",".")+"\',"

flist = [
'RunIIFall17MiniAODv2.TTJets_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_SingleLeptFromT_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_DiLept_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8_ext1',
'RunIIFall17MiniAODv2.TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8',
'RunIIFall17MiniAODv2.TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8_ext1',
'RunIIFall17MiniAODv2.TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8_ext1',
'RunIIFall17MiniAODv2.WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_80to120_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_80to120_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_120to170_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_170to300_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_170to300_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_300to470_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_300to470_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_470to600_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_600to800_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_600to800_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_800to1000_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_800to1000_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_170to300_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_600to800_TuneCP5_13TeV_pythia8_ext1',
'RunIIFall17MiniAODv2.QCD_Pt_80to120_TuneCP5_13TeV_pythia8',
'RunIIFall17MiniAODv2.QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_ext1',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_ext1',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_ext1',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1',
'RunIIFall17MiniAODv2.ZJetsToNuNu_HT-100To200_13TeV-madgraph',
'RunIIFall17MiniAODv2.ZJetsToNuNu_HT-200To400_13TeV-madgraph',
'RunIIFall17MiniAODv2.ZJetsToNuNu_HT-400To600_13TeV-madgraph',
'RunIIFall17MiniAODv2.ZJetsToNuNu_HT-600To800_13TeV-madgraph',
'RunIIFall17MiniAODv2.ZJetsToNuNu_HT-800To1200_13TeV-madgraph',
'RunIIFall17MiniAODv2.ZJetsToNuNu_HT-1200To2500_13TeV-madgraph',
'RunIIFall17MiniAODv2.ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph',
'RunIIFall17MiniAODv2.GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8_v2',
'RunIIFall17MiniAODv2.GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_v2',
'RunIIFall17MiniAODv2.GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_v2',
'RunIIFall17MiniAODv2.GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
'RunIIFall17MiniAODv2.ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8',
'RunIIFall17MiniAODv2.ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8',
'RunIIFall17MiniAODv2.ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'RunIIFall17MiniAODv2.ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'RunIIFall17MiniAODv2.ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'RunIIFall17MiniAODv2.ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'RunIIFall17MiniAODv2.WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph',
'RunIIFall17MiniAODv2.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8',
'RunIIFall17MiniAODv2.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8',
'RunIIFall17MiniAODv2.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2',
'RunIIFall17MiniAODv2.ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8',
'RunIIFall17MiniAODv2.TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8',
'RunIIFall17MiniAODv2.TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8',
'RunIIFall17MiniAODv2.TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8',
'RunIIFall17MiniAODv2.TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
'RunIIFall17MiniAODv2.TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
'RunIIFall17MiniAODv2.TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_ext1',
'RunIIFall17MiniAODv2.ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8',
'RunIIFall17MiniAODv2.ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8',
'RunIIFall17MiniAODv2.TTGamma_SingleLeptFromT_TuneCP5_PSweights_13TeV_madgraph_pythia8',
'RunIIFall17MiniAODv2.TTGamma_SingleLeptFromTbar_TuneCP5_PSweights_13TeV_madgraph_pythia8',
'RunIIFall17MiniAODv2.TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8',
'RunIIFall17MiniAODv2.TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
'RunIIFall17MiniAODv2.TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8',
'RunIIFall17MiniAODv2.TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8',
'RunIIFall17MiniAODv2.TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',
'RunIIFall17MiniAODv2.TTHH_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.TTTW_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.TTWH_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.TTWZ_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.TTZH_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.TTZZ_TuneCP5_13TeV-madgraph-pythia8',
'RunIIFall17MiniAODv2.WZZ_TuneCP5_13TeV-amcatnlo-pythia8',
'RunIIFall17MiniAODv2.ZZZ_TuneCP5_13TeV-amcatnlo-pythia8',
'RunIIFall17MiniAODv2.SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-TChiWZ_ZToLL_mZMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.RPV_2t6j_mStop-900_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSHH_2t4b_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
'RunIIFall17MiniAODv2.StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8',
]
