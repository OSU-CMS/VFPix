import FWCore.ParameterSet.Config as cms
import sys
import math
import os

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('SecondariesAnlyzer')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.TFileService = cms.Service ('TFileService',
  fileName = cms.string ("output.root")
)
process.maxEvents = cms.untracked.PSet (
  input = cms.untracked.int32 (-1)
)
process.source = cms.Source ('PoolSource',
fileNames = cms.untracked.vstring (
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/00970C32-B983-E611-A0D8-0025905B8566.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/0215FC42-A283-E611-A23C-003048FFD75A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/0261A007-B183-E611-822F-0025905B85D0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/0617AA9F-CD83-E611-89C2-0025905A60D0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/064419F3-A683-E611-85AF-0CC47A4D7694.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/06AB20D9-B183-E611-9422-0CC47A7C35B2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/088DD5BD-A783-E611-82D2-0CC47A4C8F10.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/0A7BB9A9-A183-E611-A1E4-0CC47A7C3404.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/0E5D1C9E-A583-E611-B0B5-0025905A608A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/0E703203-B883-E611-B36A-0CC47A7C35C8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/10410F45-AD83-E611-94D0-0CC47A4D76D0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/109644F3-1984-E611-83F2-0CC47A4D76A0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/14FC761E-A883-E611-AF0D-0CC47A4C8E98.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/1835F2B2-AB83-E611-AB33-0025905B85C0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/18A51C52-C283-E611-864D-0CC47A4D76D0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/1A3D056D-A283-E611-B09F-0CC47A4D75EE.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/1AC72A44-A883-E611-99B0-0025905B85BC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/1ECA2E7C-B083-E611-AA95-0025905B855A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/20C27C1C-B483-E611-96F6-0025905B85C6.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/20C87D36-C583-E611-BE42-0025905B8592.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/20D96276-9E83-E611-8AA0-0CC47A4C8ECA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/20F37B60-A483-E611-8C0F-0CC47A7C34A0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/241EAC5F-A583-E611-AAF0-0025905B85A0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/246CC96C-AA83-E611-870A-0025905A48F0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/26CE5D07-A983-E611-96F9-0025905B85E8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/2805AD3D-BD83-E611-972B-0CC47A78A446.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/2805DE69-B083-E611-ABA1-0CC47A78A2EC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/2886CE31-CC83-E611-836A-003048FFD7AA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/28F71EDB-9D83-E611-8D3F-0CC47A7C34A0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/2ADBF6DB-A283-E611-B09D-0025905A608C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/30390D58-A283-E611-B7B5-0CC47A7C347A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/30F4854D-B083-E611-8E3C-0CC47A4D762A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/3294F54E-9D83-E611-AC05-0CC47A4C8F06.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/32DAE67E-D683-E611-828B-0CC47A78A41C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/32E50F28-AE83-E611-98A8-0CC47A4D76C0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/32EC1CE7-A883-E611-824D-0CC47A4C8ECA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/32F04254-D083-E611-871E-0025905A6118.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/34FE8C4A-9E83-E611-A113-0025905B85CC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/361E50D2-B383-E611-BBC8-0025905B8592.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/364EF95C-A583-E611-A560-0025905A6110.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/36906C4E-B883-E611-B3E6-0025905A60AA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/36BF4736-9E83-E611-8C8A-0CC47A4D7616.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/387FB8B6-B383-E611-AEF5-0025905A610C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/3EE29439-BE83-E611-86CC-0CC47A4D761A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/40C0FF34-A583-E611-9DDE-0CC47A4D7616.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/42DC8977-B083-E611-8D09-0CC47A4D769E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/4496B55F-A483-E611-B8E0-0CC47A4C8F2C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/46412E94-B383-E611-A067-0CC47A4C8E34.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/468E033F-BE83-E611-BFC3-0CC47A4D7606.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/46F1F30A-A483-E611-9D9D-0CC47A7C35B2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/489FF83A-AB83-E611-A470-0025905A60BE.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/4A273B02-A983-E611-8E03-0025905B855C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/4C29FF63-B683-E611-959D-0025905A48BA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/503029BE-AE83-E611-8869-0025905A606A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/50E76B3C-C883-E611-94D2-0CC47A4C8ED8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/5419BD06-A983-E611-B9CE-0025905A6068.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/54D35E9A-B483-E611-9D9C-0025905A6110.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/5638CFB6-C083-E611-8ADC-0CC47A4C8ECA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/56DE4171-A283-E611-A27C-0CC47A4D76B2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/5A2D7A19-9783-E611-A2AE-0025905A48FC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/5AD7E6D0-AA83-E611-8298-0025905B858E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/5AF9363E-A883-E611-8A51-0025905A613C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/5CE961A0-A183-E611-9A90-0CC47A7C353E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/5E6D21E1-9D83-E611-ADB2-0CC47A4D7694.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/609B86D1-9F83-E611-8637-0025905A6060.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/60EA919D-B083-E611-A3D8-0025905A48F0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/62DE3C89-AB83-E611-8677-0CC47A4D7606.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/64447238-A583-E611-BB54-0CC47A74525A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/648DD422-C483-E611-B081-0025905A611E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/6691ABB7-C083-E611-9460-0CC47A4C8E86.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/6A101325-AF83-E611-AB15-0CC47A4D76B2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/6ACC8B5D-A683-E611-BF1F-0025905A608A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/6E5C8D32-A583-E611-9BB3-0CC47A4D765E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/70BDAC5C-9E83-E611-9108-0025905A606A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/70E1F38D-A283-E611-A40D-0025905A48BC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/72038D69-A583-E611-ADA8-0025905B858E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/728C0286-D083-E611-915B-0025905B85D0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/7461B156-CF83-E611-9B6C-0CC47A4C8F12.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/781CEF82-B083-E611-8516-0025905B859E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/7884570E-AA83-E611-904D-0025905B85DC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/7A60016D-B983-E611-BF80-0CC47A4D7614.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/7E6EBED1-BC83-E611-8B79-0CC47A4D76D0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/8017BA43-C783-E611-9581-0CC47A4C8F12.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/824A0E3C-A583-E611-B389-0CC47A78A45A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/82CD5A35-A583-E611-B355-0CC47A4C8EEA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/845043EC-B283-E611-B82F-0025905A611E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/8483F086-AB83-E611-AEC7-0CC47A4D7666.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/84B8F746-BE83-E611-95C9-0CC47A4D7632.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/84FDC56D-A283-E611-8EE9-0CC47A7C3610.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/86262578-A983-E611-9632-0025905A60C6.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/86B59DBF-A583-E611-B3A6-0025905A60BE.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/8A3163C4-A183-E611-8DEF-0025905A48B2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/8A33E5C8-A083-E611-93DC-0CC47A7C360E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/8AB9001E-B483-E611-90E0-0025905A606A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/8CEB127B-9D83-E611-AB81-0CC47A4D76A0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/8CF47E47-AC83-E611-8EE8-0CC47A4C8E20.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/8E7FCFF7-A583-E611-8BCE-0CC47A4C8F18.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/90159A62-9783-E611-A4B7-0CC47A4D7616.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/92858A09-A283-E611-960F-0CC47A4C8E98.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/92A6DFA5-F383-E611-A540-0CC47A78A41C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/92FDFBF3-A583-E611-8DDC-0CC47A7C35B2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/94DFE595-D683-E611-B959-0025905A497A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/9603692B-A283-E611-AA2C-0025905B85D8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/962559BE-A783-E611-831F-0CC47A7C3404.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/963FF5EA-B583-E611-91DE-0025905A60C6.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/989DDA8C-9783-E611-A4D8-0025905B857E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/9EA3E6E1-9D83-E611-9F0E-0CC47A4C8F2C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A280E84A-AC83-E611-B79F-0025905A607A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A2D0B85F-A483-E611-9CDC-0CC47A4C8E1E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A2DC158A-B183-E611-92F3-0CC47A7C3408.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A2E312B5-AF83-E611-B13F-0CC47A4D766C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A4727C1F-B983-E611-B45B-003048FFD7A4.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A4E7C9BC-AE83-E611-953D-0025905A48B2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A6DDD758-A883-E611-BF01-0025905A6092.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A6F588B2-A383-E611-837D-0025905A612C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A8615011-A683-E611-948B-0025905A6118.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A88859B5-B383-E611-A9BD-0025905A6118.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/A8C5F7AB-B983-E611-BA16-003048FFD7AA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/AA0B1E88-B083-E611-942D-0025905A60F4.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/AAF769E0-A783-E611-B2B8-0025905B85CC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/AE5FD300-9E83-E611-90F6-0025905A48B2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/AEC7BE03-A783-E611-A879-0025905A6084.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/AECC1E55-A583-E611-8B47-0025905A612C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/AEFE26DE-D283-E611-B395-0025905B85AA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/B01129D8-A383-E611-BEED-0CC47A4C8ED8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/B4447470-A283-E611-93DD-0CC47A4C8E82.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/B4DFC3DA-B183-E611-A815-0CC47A4C8F06.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/B603FB39-A583-E611-9B1F-0CC47A4D76D0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/B686FEDD-A283-E611-A9BC-0025905A6064.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/BA69E7D0-A883-E611-8E95-0CC47A7C3612.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/BEF9FF78-A983-E611-BFDF-0025905A609E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C0098EAC-B283-E611-8C76-0CC47A78A3D8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C0A321FD-B183-E611-91E5-0025905B8612.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C2AA0C1F-AB83-E611-9B66-0CC47A4D75EE.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C2B7407A-A583-E611-90C1-0CC47A4D7606.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C2F70DD7-BD83-E611-9C7F-0025905B85EE.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C4699068-9F83-E611-BA49-0CC47A4C8F10.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C47E00D0-B283-E611-B08F-0025905A48D0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C4FE8700-9E83-E611-A72E-0025905B85DC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/C65035FD-B383-E611-9FD5-0CC47A78A4BA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/CCB3A409-A283-E611-8C4E-0CC47A4C8EEA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D0CE1F29-BB83-E611-AB11-0025905B85E8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D20A9351-A583-E611-A033-0025905B8560.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D2472645-B983-E611-9F5A-003048FFD72C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D2856860-B483-E611-B418-0CC47A4C8ECE.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D2D0CBC6-0884-E611-9C3A-0CC47A4D765A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D2DE1511-1B84-E611-9803-0025905A60D6.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D402674D-AE83-E611-9429-0CC47A7C353E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D40A6D1E-D983-E611-889B-0CC47A4C8ED8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D6602818-A983-E611-95C0-0CC47A7C353E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D6C4E392-A583-E611-ABAD-0025905B85D8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D6DC6C1E-AB83-E611-8B2C-0CC47A7C3610.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D8146A36-A283-E611-B237-003048FFD722.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D8323B05-9E83-E611-85EE-0025905A611E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/D8FAD646-B783-E611-B2B8-0025905B85DC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/DCBC8EBC-D283-E611-A7D4-0CC47A4C8F2C.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/DCCE407D-9E83-E611-B2E4-0CC47A7C3450.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/DE3BFD68-1D84-E611-AC05-0CC47A4D765A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/DE7B5A85-1D84-E611-AEE9-0CC47A4C8EEA.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/DE8EA808-9E83-E611-B1DD-0025905B8572.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/DEF53565-BB83-E611-AD19-0CC47A4C8E46.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/E099DF43-BF83-E611-8535-0025905B859E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/E229475A-A583-E611-95E8-0025905B85D6.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/E44813E3-9D83-E611-9B41-0CC47A4D7664.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/E6C47737-9E83-E611-BEE6-0025905B8612.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/E83545E2-A883-E611-8CB6-0CC47A4D76A2.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/E8EE197A-A183-E611-ABDB-0CC47A7C3412.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/EC2FF5FC-BC83-E611-B93C-0025905A611E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/EC33BE94-9E83-E611-8837-0CC47A4D76C0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/EC64CE38-BE83-E611-B55D-0CC47A4C8ECE.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/F0E3B27B-BE83-E611-A408-0CC47A4C8F12.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/F6249030-B383-E611-BAAF-0CC47A7C34A0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/F654BC45-AB83-E611-88C7-0025905A60A0.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/F6A1CA21-A683-E611-8DE2-0025905A60F8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/F6D20061-AA83-E611-B946-0CC47A7C360E.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/F89F223C-A283-E611-91FC-0CC47A7C35A8.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/FC649548-B983-E611-810F-0CC47A4D767A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/FC86651C-BC83-E611-80F2-0025905B85CC.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/FC9A56EC-C383-E611-BD92-0025905B855A.root',
'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/FCD70D49-AF83-E611-883A-0025905A608C.root',






)
)



process.SecondariesAnalyzer = cms.EDAnalyzer ('SecondariesAnalyzer',
  jets = cms.InputTag ("ak4PFCHSJets", ""),
  jetsNoCHS = cms.InputTag ("ak4PFJets", ""),
  trackJets = cms.InputTag ("ak5TrackJets", ""),
  pus = cms.InputTag ("addPileupInfo", ""),
  vertices = cms.InputTag ("offlinePrimaryVertices", ""),
  trackingVertices = cms.InputTag ("mix","MergedTrackTruth"),
  tracks = cms.InputTag ("generalTracks", ""),
  trackingParticles = cms.InputTag ("mix","MergedTrackTruth"),
  genParticles = cms.InputTag ("genParticles", ""),
  simTracks = cms.InputTag ("g4SimHits", ""),
  pfCandidates = cms.InputTag ("particleFlow", ""),
)

process.myPath = cms.Path (process.SecondariesAnalyzer)
