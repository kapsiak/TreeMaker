import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/02F335E3-34F9-F54F-BBBA-62AAF598739B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/2143A27B-6D04-5144-9E0C-8CB66D500DE1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/28161002-7227-804B-88EC-1688EED93082.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/33467742-35A0-9C4B-91A8-C9E5713563A6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/361FEBA5-DC73-8244-8D27-C5DC6ADA86EE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/6DB2DE13-CD8C-794A-A563-1D935E843794.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/6EAEAC91-6368-5D4A-A7EF-5C20406B548D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/70DFA37D-9E4C-C746-9620-39B9DCB0FBB6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/91DD1879-87EC-EA49-9B17-8BD79F082258.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/BD914A98-F442-3442-830A-D2B777A4B8BA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/F6D96BFC-C6ED-DA41-BDD0-8A7CC36767C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/0103E515-8A85-E247-8727-FEC5D7AF81DA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/03001870-D4F9-4D4D-B35F-0CE65FE687FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/1B183630-1EC9-B743-B659-C448C571DE7E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/3F38DC08-3387-6747-97C6-6EE1D89E6E12.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/58AAFE7F-AF34-C044-82F5-5DAAD6265574.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/5E1622A4-B6A5-4247-B7EB-60F8FC796A50.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/6C72B4B0-2ED2-AF40-965F-FFE644D8267E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/79EE6793-BC2F-AE49-8A0C-BEC5BD9E27A8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/A57449A2-B1C1-144B-80F1-E19F7B094828.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/AD3737D0-DDD9-2B4D-BEF4-944AE304A41E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/D291DAD9-AE7C-8C46-97BC-51D7C3A6B454.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/0EC1C6C1-4EBC-8E47-B396-EE458335A522.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/507C1A2C-1C35-BF48-84F2-35B8C0B7A07F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/6F00F097-A7A8-0C47-8EC6-626F7B269496.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/86CC2EF2-F0BD-D746-83E2-C5A479A3E481.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/DE21084C-9026-6F4C-A16D-3DE15A98F88B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/063F26C8-975B-C94B-83CD-34314CAC452D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0991AE2E-6C0B-B341-BE10-43538852463C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/2015B567-06B0-934B-AA35-08113E7B18AF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/4E6BD01E-1C08-8F42-A92D-C87A2A9BC46E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/8E269F0E-4D50-4C40-B384-42FF9A725703.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F3212F09-E720-7741-9F27-79CEC0A9F19D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/002AD5BF-F3C3-7843-92F1-D6A85C081686.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/03E8DDFB-D034-2243-B0F6-9E389BC1F3BC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/062DB5EB-393C-CA4B-AC5E-52F37994D9CD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/0CE2E200-C0CD-9147-AA64-7FFE2D449530.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/13416CC2-C511-5442-8BD4-4503F7CCAAD4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/1975CD40-6C4C-F240-8895-C32AE14334FF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/1C0F9822-C4F1-F14B-A3F4-403FA9C5C4AD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/216E5D79-7F55-6E40-BFF5-EDB2E46CD112.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/23E1FB10-FF2E-6B44-9596-DCC35B8EAE8D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/25C4A680-5B71-134D-948B-1D5CA32BC7B9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/28BBD07F-0B00-7742-B458-CACEA2694564.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/2A2C7126-5233-6446-8968-9288BA354152.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/2A720943-04A8-C746-8F54-572203D3BB9B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/2CD6753E-70CF-D046-9EF9-C3BAEECA8CE7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/2FDBD819-713C-0E4E-9710-7FA7B26702A4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/372AC57C-7220-5A42-A25B-67AE51CE8FA2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/3895F543-B5CD-BB4F-BC9A-881AB07525B1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/395C26F8-DAE3-1F4D-8781-74FA39B8C7CE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/3D354AA4-9762-9142-9C0A-724C9B9558B1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/3D6144CA-845A-8B45-9F07-12719DF35927.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/3F5685D8-1DB3-4744-9A1D-12AD44DD70AC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/45B93771-97EF-3D4B-AC1A-CF7E401F46E2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/48E755E1-AA03-D946-A024-9A4760E6A394.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4A62EB77-930B-CA46-96B1-2FF26600A23A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/502E265B-F879-DB4F-B4FA-F4F93ACE5660.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/52AD1C74-68BA-8E41-B009-9383060B309C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/57376E4B-CE8B-924B-ABE7-6EBF8FD88889.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/5C504D23-B045-484F-801C-D7EEE621EC47.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/5D65CFAD-5FE4-E944-A827-235B1E314701.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/6BD010EE-0FE9-EA4D-90CC-450A27ADD041.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/6EB5687B-5A98-2947-98A0-8E437BD5B4AF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/7676DB9E-8BD4-1B41-B34B-92A1075C5254.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/76F8E01E-1679-4D45-A46C-FB7C8F4526C4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/7C4D7A85-9269-7349-B62B-05A6091AEBCD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/820180E3-5680-8246-A93A-214E492BDB68.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/841C4109-5F78-3A47-A179-B316047D6EBE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/8AADF8D7-6A98-C649-98D0-DBAACE029A5E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/98BAE9DA-9FE6-2C4E-863C-BE7BB637D187.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/9F80F2C8-F932-824F-987C-18403836A860.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A10B2BD8-D383-D148-91A9-28F74420DEF3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A80B8EAF-FA67-8142-A238-DC70FA381863.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A9400FE3-52ED-7B4D-8A17-86A1DE53FF97.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/AABF1C49-731A-4141-A272-72BCC8995F26.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B27CD9DC-7E8E-EE44-B698-3A767AB005DE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B3190609-EF34-4C4E-BE27-FF14D903B094.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/BE05982D-DB1C-C74C-9E7F-A519DEE9D941.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/BE6CBA84-1FB5-1349-A7D1-6AC90AD30C23.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/BF9AE63E-9CFB-9F4B-A540-02CBA57D637F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/C088C185-A389-9042-85BE-754AF90E791F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/C788BDF1-F42D-7145-9A57-92971EC4D8B4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/D23A65E8-E85A-8E47-BDBE-5DE63413149C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/DE74E6D9-C355-644E-9C8D-A39C591A65CA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/DEA425AA-97EE-EE45-BA7D-F1F2C50E2CCC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E23890CC-CF8C-FA42-9CE0-BFA771835FA8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E2D9363B-8FAC-C748-A654-503AB889E739.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E4A54C01-EC9B-3F40-8DFC-6166389F242B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E6299330-443F-7F4F-B33D-25FA79AF4541.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E73F80C9-E82A-E54A-B5F9-C97D6CA0CF3F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/EC5D5554-BE89-414B-B8FD-BE5730B2337A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/EEE64C7F-4347-D246-98F5-E27F2003AAF8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F314DB39-8DB1-2E40-97FC-7A7D6CEB8E04.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FC8A772D-FCAC-6D49-80CF-9C33297B9288.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FCF0F521-A8B1-0E48-A89C-1E70E40335C9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/69FA1ABC-B782-FC42-8422-794369BC60BA.root',
] )
