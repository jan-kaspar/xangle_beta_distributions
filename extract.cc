#include "TFile.h"
#include "TH2D.h"

#include <vector>
#include <string>

using namespace std;

//----------------------------------------------------------------------------------------------------

TH2D* Process(const string &period, TH2D *input)
{
	TH2D *h = new TH2D(*input);

	// TODO

	return h;
}

//----------------------------------------------------------------------------------------------------

int main()
{
	// config
	vector<string> periods = {
		"2016_preTS2",
		"2016_postTS2",

		"2017_preTS2",
		"2017_postTS2",

		"2018_preTS1",
		"2018_TS1_TS2",
		"2018_postTS2",
	};

	TFile *f_out = TFile::Open("data/xangle_beta_distributions.root", "recreate");

	for (const auto &period : periods)
	{
		TFile *f_in = TFile::Open(("data/" + period + ".root").c_str());
		
		TH2D* h2 = (TH2D *) f_in->Get("h2_betaStar_vs_xangle");

		gDirectory = f_out->mkdir(period.c_str());

		h2->Write("h2_betaStar_vs_xangle_original");
		Process(period, h2)->Write("h2_betaStar_vs_xangle");

		delete f_in;
	}

	delete f_out;

	return 0;
}
