import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/FBF7333D-BE6F-9948-A867-7345CF59F4EE.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/D6B7C465-28CC-0B4A-995B-0D52D8001570.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/4774EAE0-DFE4-2B40-BFD4-8812B09EA70A.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/227B259B-09F6-A143-9A2A-CD8A23C05A10.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/F6B61F76-19D8-BE4F-9FA9-F8755F0A8B93.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/20782DAF-7079-9D41-8894-007528A14192.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/C0D65EE8-2B12-C643-A3B7-2014A2E390C7.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/346A27E7-B8A6-3D43-B60A-5E42DD6109F4.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/5C76CF8E-C0F5-0146-8777-F33845B892F1.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/CDD9D458-439B-124B-BDED-36BB3592EF06.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/DFAEAA76-E7F9-A74F-9B1B-9C200370C28C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/033D8CE4-A79F-D54E-BB28-1632C2ADE450.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/63888079-C4A1-724E-95AB-75F51110DF3C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/3C44F0B3-9E0A-D44C-8BFF-3832B5E3458A.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/429DB0CA-E032-3746-B4CE-C2FFC1FB02DA.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/AF7EC779-508A-B64D-9576-A645ED0A7A9C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/D52571C0-2AAF-5C42-A07C-BCFB2649E6A7.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/6AEE5A4A-7B02-7D4F-BA43-AAFBE9E7DD05.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/BCE2700E-FC52-FD45-B895-18A95623B73A.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/2BAB7472-E358-C440-8405-8E0CE5DD54B9.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/5CB81FF4-09B6-284F-B957-CFDCCE0F0767.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/EC5F592A-169F-064B-9A7E-F21E1791E0C4.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/C5DB3A95-64A3-4C42-AB29-152DF2F008F1.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/D79954CA-75C5-394B-A0B0-B6CB642E00FC.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/40246BCF-DB3E-1A45-AD72-968645F2410A.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/99A9CCD3-950F-F340-AE9F-545884EF2965.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/F64BFFD1-C646-5345-A829-CD40E7E72159.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/AA2B6A28-72D5-7045-B012-5D6E1A0D5B66.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/C2D6722F-4734-7346-BC58-1EE496D83D53.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/A98A3674-D2C6-9F46-B84A-85EC93540216.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/F78631F5-74E7-EE4D-A38E-3A143CCB692C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/7CB84AE0-F530-6C41-A122-9BABF77F1C13.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/5F57964B-04C7-1F49-B568-78FFE4DD8499.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/C3103834-7576-B04B-96D3-02B3CB2B2E84.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/AA4C8A49-EB98-9F45-8C26-C2B3AA0640A1.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/20FF75B2-7016-D94D-9CF4-7835C0923BA2.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/9C853B75-1119-AF45-A790-7C2371B23A0C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/9C18FA65-3CB9-B04A-BC9F-4E1692ED1C92.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/6751BBA6-BB2B-0C4E-8FDD-62E6EC719E23.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/CEA6B979-1688-C044-9CFB-D277EF6CBFBD.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/E78CD557-CE75-6345-8397-D88F2EB8E447.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/24FC277A-39E8-C54D-9A6D-9A312EBCBD7E.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/08E50D35-BD81-7C45-85A7-43B06117E234.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/729A4E90-19D6-8249-A764-92C5898754CD.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/E8FCB632-FD42-0740-A264-FE6D7093D602.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C0872E8E-8CEE-AD4D-82CD-76ECD33B69F3.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B363B3DD-541E-7940-8D83-F633D8FD13A8.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B9B68419-20F2-AC41-B572-AE5864CA78A6.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/5CEE8F4F-7600-F24E-BCC7-8CD87B071447.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B8955610-6395-DE4C-9792-79CA5AFEAE83.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8B625B74-7FE0-3249-93A6-70CBB2EA245B.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/31F044A0-53E2-D64C-A20B-E62F968C56A7.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/887DBBFC-7F55-6C47-8F10-508DA5AAF0CE.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/ECFD4C95-1CDF-BF49-9BDB-D94638D2855E.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/965F905B-1EFD-2B45-A45E-8769B643B475.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/BACAFC92-0070-204C-9B18-5B43643D6D23.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/DD3A09E2-2C27-A348-A3B7-F4A326484027.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/3E313DA1-26C6-4040-9775-613F7401D88C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/719C862B-BA89-DE40-B175-5C7086D5C11E.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/107C96AE-99E9-2B48-B06B-A14FFDBDF07E.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/87E928CF-37A8-9147-844E-34227C0565EE.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/DD58D5CA-0468-4248-BE2C-59CA48D1F98A.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/3351BFAC-BD03-DF46-A3C5-FBA69D17497C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/0583022A-51C7-294A-96AF-7DFF6C945374.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/1DB71666-FF26-DA4C-B371-F1F788E8163F.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/31C20954-63C0-A946-B4FB-EE0EF4DB7ACD.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/248578CE-D3B9-B947-945B-E0C7714B7FBA.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/86AA1105-AFCD-0A48-AE5B-C7947D353C2C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/25F5DC76-8F16-F04D-8506-284ECE0D79A8.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/5660A4C5-63C6-424E-8649-047BEAA8C307.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/EF75000B-5A4B-7C45-A108-695A7BE1F15F.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/89F735A2-11C3-F64C-B1CE-8EE3ADAD3B91.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/46142E4F-A1C4-9E4A-85E6-1433708D828A.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/2B84FDA2-59C6-E446-9CC4-ED005412755B.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/ACB64E58-A47C-184E-A795-AD45B39AA14B.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/ABFC70F7-2E5F-994B-82CF-7AD83A77B29B.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/F96FF09C-8365-F144-BB8A-27B5A2B585BE.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/E738815A-12F1-BB4A-BD71-E2102E18D4BE.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/2BA9F55B-3DE9-7D4E-81EB-D83434EF076E.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/F6F28A7A-48B3-9A4E-9183-DB128C0AF29D.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/1FB066BD-ECA3-3948-8B03-73E17108DB1E.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/F4350BAA-EC80-DF4A-A1A2-33050AA1FFC5.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/05614177-D102-1543-A2EA-403550E173E3.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/347D9E1B-C9C3-1349-8FF4-37F4A878EA16.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/3AC5E523-647F-1840-BEBB-B64A41E2208C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/CC69DF64-97DF-3244-B0A6-36982BE598F6.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/750D8579-4A40-9841-A3F0-41A2974B80A4.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/53FBAF42-19CE-4649-9725-D8F9CBCF101C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/CBB911F5-2DBC-364B-BE8C-681C548CF483.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/A28F4542-3453-3240-8930-D405BE8A98F5.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/5C0C89BC-68CF-8747-B703-90F9105B281B.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/1C8AE6B6-809A-3F4D-B5D3-2EF79C40D5BA.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/B9704F16-330C-E345-BFCA-20DF1E79F69A.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/1D730655-43B3-4842-832B-82FACFEC9A5C.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/5C210A01-E0C5-6E4C-ABAA-2649D776CA91.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/3553BC91-DF37-044B-9CE3-9852CA00243A.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/76815403-3DB5-1A4C-B1D5-9D1C363F9CA2.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/A18C8891-A94C-264C-B294-E106379DA86F.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/5748C55B-B894-D445-A5B9-BB500F5DFD27.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/A3035496-D8A3-164E-B9DC-D2D9BE027AC4.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/7B97CA75-0130-744D-B82C-250EC19695B7.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/043A21B9-DDF7-FA46-869F-CCF2F3328A40.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/B81A1AA3-BBF1-1448-929C-50AEAA45324E.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/B6456F8F-0F36-B046-8876-46645C66CB71.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/6191DBAA-A10A-F84B-BBF5-D3184F0DCA60.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/2CC76124-9890-F943-AAB1-D1B2D485255F.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/8D9E4F52-CB0B-9546-85ED-C5499C7F1E59.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/67D17092-3997-B148-ACDE-180F2E9610FC.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/875B7CAC-6C25-0D44-9153-4EEDC00B00FE.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/47917FA2-8F97-F74F-899D-7319F1DFB6FB.root',
    '/store/data/Run2017C/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/40000/C62CE079-437D-4240-9F88-7F3CE45DB18A.root',
] )