import sys 
import os
import FWCore.ParameterSet.Config as cms

process = cms.Process("PPSXangleBetaExtraction")

from Configuration.AlCa.GlobalTag import GlobalTag
from CondCore.CondDB.CondDB_cfi import *
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag = GlobalTag(process.GlobalTag, "106X_dataRun2_v28")

sys.path.append(os.path.relpath("./"))

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring("cout"),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string("WARNING")
  )
)

# input data 
from input_files import input_files
process.source = cms.Source("PoolSource",
  fileNames = input_files
)

# apply JSON file
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
JSONfile = "../../../selection.json"
myLumis = LumiList.LumiList(filename = JSONfile).getCMSSWString().split(',')
process.source.lumisToProcess.extend(myLumis)

# number of events to process
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(-1)
)

# configure plotter
process.load("Validation.CTPPS.ctppsLHCInfoPlotter_cfi")
process.ctppsLHCInfoPlotter.outputFile = "output.root"

# processing sequence
process.path = cms.Path(
    process.ctppsLHCInfoPlotter
)
