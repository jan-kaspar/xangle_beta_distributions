#include "TFile.h"
#include "TH2D.h"

#include <vector>
#include <string>

using namespace std;

//----------------------------------------------------------------------------------------------------

TH2D* Process(const string &period, TH2D *input)
{
	TH2D *h = new TH2D(*input);

	// post-processing
	if (period == "2017_postTS2")
	{
		for (int bix = 1; bix <= h->GetNbinsX(); ++bix)
		{
			for (int biy = 1; biy <= h->GetNbinsY(); ++biy)
			{
				//const double x = h->GetXaxis()->GetBinCenter(bix);
				const double y = h->GetYaxis()->GetBinCenter(biy);

				if (y > 0.30001)
					h->SetBinContent(bix, biy, 0.);
			}
		}
	}

	return h;
}

//----------------------------------------------------------------------------------------------------

TH2D* MakeSingleBinHistogram(double xangle, double betaStar)
{
    TH2D* h2 = new TH2D("", ";xangle;betaStar", 3, xangle-1.5, xangle+1.5, 3, betaStar-0.015, betaStar+0.015);
    h2->Fill(xangle, betaStar);
    return h2;
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

		//h2->Write("h2_betaStar_vs_xangle_original");
		Process(period, h2)->Write("h2_betaStar_vs_xangle");

		delete f_in;
	}

	// add extra scenarios
	gDirectory = f_out->mkdir("2021");
	MakeSingleBinHistogram(140., 0.30)->Write("h2_betaStar_vs_xangle");

	delete f_out;

	return 0;
}
