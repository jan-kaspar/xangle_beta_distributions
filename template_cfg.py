import sys 
import os
import FWCore.ParameterSet.Config as cms
import copy

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

# filter on unprescaled HLT bits from the SingleMuon dataset
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
process.hltFilter = copy.deepcopy(hltHighLevel)
process.hltFilter.TriggerResultsTag = cms.InputTag("TriggerResults", "", "HLT")

year="$year"

if year == "2016":
  process.hltFilter.HLTPaths = ['HLT_IsoMu24_v*']
if year == "2017":
  process.hltFilter.HLTPaths = ['HLT_IsoMu27_v*']
if year == "2018":
  process.hltFilter.HLTPaths = ['HLT_IsoMu24_v*']

# configure plotter
process.load("Validation.CTPPS.ctppsLHCInfoPlotter_cfi")
process.ctppsLHCInfoPlotter.outputFile = "output.root"

# processing sequence
process.path = cms.Path(
    process.hltFilter

    * process.ctppsLHCInfoPlotter
)
