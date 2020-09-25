all: extract

extract: extract.cc
	g++ -O3 -Wall -Wextra -Wno-attributes --std=c++11 -g `root-config --libs` `root-config --cflags` \
		extract.cc -o extract
