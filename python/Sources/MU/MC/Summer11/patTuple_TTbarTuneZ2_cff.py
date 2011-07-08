import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = readFiles
)
readFiles.extend([
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_1_1_U4X.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_2_0_BnL.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_3_0_6ky.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_4_0_bUe.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_5_0_mBh.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_6_0_mLc.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_7_3_mbY.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_8_0_SMY.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_9_0_ggO.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_10_0_HFm.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_11_0_RpP.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_12_0_GJP.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_13_0_2YY.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_14_0_oIY.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_15_0_sBs.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_16_0_Amx.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_17_0_jxV.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_18_0_cmz.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_19_0_dl0.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_20_0_jfe.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_21_0_Ldm.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_22_0_ZzV.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_23_0_VnQ.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_24_0_FgR.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_25_0_gt1.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_26_0_O71.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_27_0_gEo.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_28_0_meQ.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_29_0_Qs2.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_30_0_OT7.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_31_0_kie.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_32_0_ct3.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MuMu/MC/20110621_1/TTbarTuneZ2_2/patTuple_skim_33_0_aEE.root",
])