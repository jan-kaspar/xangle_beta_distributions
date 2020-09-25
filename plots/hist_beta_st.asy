import root;
import pad_layout;

string f = "../data/xangle_beta_distributions.root";

string years[];
string y_periods[][];

years.push("2016"); y_periods.push(new string[] {"2016_preTS2", "2016_postTS2"});
years.push("2017"); y_periods.push(new string[] {"2017_preTS2", "2017_postTS2"});
years.push("2018"); y_periods.push(new string[] {"2018_preTS1", "2018_TS1_TS2", "2018_postTS2"});

xTicksDef = LeftTicks(1., 0.5);

xSizeDef = 9cm;

//----------------------------------------------------------------------------------------------------

for (int yi : years.keys)
{
	NewRow();

	NewPadLabel(years[yi]);

	for (int pei : y_periods[yi].keys)
	{
		string period = y_periods[yi][pei];

		NewPad("$\beta^*\ung{cm}$", "probability");

		RootObject h2 = RootGetObject(f, period + "/h2_betaStar_vs_xangle");
		RootObject h_xangle = h2.oExec("ProjectionY");

		draw(scale(1e2, 1), h_xangle, "n,vl", red);

		xlimits(24, 41, Crop);

		AttachLegend(replace(period, "_", "\_"));
	}
}

GShipout(vSkip=0mm);
