import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring()
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('vallot_Run2010B.root')
)

#process.load("PFAnalyses.TTbarDIL.Sources.ELE.RD.patTuple_Run2010B_Nov4ReReco_cff")
process.source.fileNames = [
    'rfio:/castor/cern.ch/user/j/jhgoh/TopAnalysis/pf2pat/ElEl/RD/20101209/Electron_Run2010B-Nov4ReReco_v1_1.root',
    'rfio:/castor/cern.ch/user/j/jhgoh/TopAnalysis/pf2pat/ElEl/RD/20101209/Electron_Run2010B-Nov4ReReco_v1_2.root',
    'rfio:/castor/cern.ch/user/j/jhgoh/TopAnalysis/pf2pat/ElEl/RD/20101209/Electron_Run2010B-Nov4ReReco_v1_3.root',
]

process.load("KoPFA.TopAnalyzer.topAnalysis_cff")
process.ElEl.doResJec = cms.untracked.bool(True)
process.ee.doResJec = True

process.p = cms.Path(
    process.topElElAnalysisRealDataSequence
)

