This package is used to extract beta*-vs-xangle 2D histograms from data.

Usage:
 * make
 * ./build_work_directories
 * ./submit -submit data/20*/Run*/*/block*
 * condor_submit "condor.sub"
 * with wd_control make sure that all processess finished successfully - if not resubmit
 * ./merge
 * ./extract
 * the final result is in data/xangle_beta_distributions.root
