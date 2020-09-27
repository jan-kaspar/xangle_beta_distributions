import root;
import pad_layout;

string f = "../data/xangle_beta_distributions.root";

string years[];
string y_periods[][];

years.push("2016"); y_periods.push(new string[] {"2016_preTS2", "2016_postTS2"});
years.push("2017"); y_periods.push(new string[] {"2017_preTS2", "2017_postTS2"});
years.push("2018"); y_periods.push(new string[] {"2018_preTS1", "2018_TS1_TS2", "2018_postTS2"});
years.push("2021"); y_periods.push(new string[] {"2021"});

TH2_x_min = 80;
TH2_x_max = 190;
TH2_y_min = 0.15;
TH2_y_max = 0.65;

xTicksDef = LeftTicks(10., 5.);

xSizeDef = 9cm;

//----------------------------------------------------------------------------------------------------

for (int yi : years.keys)
{
	NewRow();

	NewPadLabel(years[yi]);

	for (int pei : y_periods[yi].keys)
	{
		string period = y_periods[yi][pei];

		NewPad("xangle$\ung{\mu rad}$", "$\be^*\ung{cm}$");

		draw(scale(1, 1e2), RootGetObject(f, period + "/h2_betaStar_vs_xangle"));

		limits((90, 24), (190, 41), Crop);
		//limits((80, 10), (200, 90), Crop);

		AttachLegend(replace(period, "_", "\_"), NW, NW);
	}
}

GShipout(vSkip=0mm);
