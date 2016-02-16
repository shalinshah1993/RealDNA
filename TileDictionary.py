#Author - Shalin Shah
#Last Edited - November 22, 2014
#This python file contains the mapping for glue colors with numbers.

edge_color = {
	#Computational Tile Glue Color
	"0": "1",
	"1": "2",
	"00": "3",
	"01": "4",
	"10": "5",
	"11": "6",
	"e": "7",
	"l": "8",
	"t": "9",
	"r": "10",
	">": "11", #Greater than
	"<": "12", #Less than
	"=": "13",

	"<0": "14",
	"<1": "15",
	">0": "16",
	">1": "17",
	"=0": "18",
	"=1": "19",
	
	"000": "20",
	"001": "21",
	"010": "22",
	"011": "23",
	"100": "24",
	"101": "25",
	"110": "26",
	"111": "27",

	#Border Tile Glue Colors
	"x(-1)": "28",
	# "$1": "29",
	# "$3": "30",
	# "$5": "31",
	# "$7": "32",

	# "$(-1)s": "33",
	# "$1s": "34",
	# "$3s": "35",
	# "$5s": "36",
	# "$(-1)ss": "37",
	# "$1ss": "38",
	# "$3ss": "39",
	# "$5ss": "40",

	# "$(-1)0": "41",
	# "$10": "42",
	# "$30": "43",
	# "$50": "44",
	# "$70": "45",
	# "$(-1)1": "46",
	# "$11": "47",
	# "$31": "48",
	# "$51": "49",
	# "$71": "50",

	#"dot": "50"

	#Input Glues
	"input_bit_1_L": "29",
	"input_bit_2_L": "30",
	"input_bit_3_L": "31",
	# "input_bit_4_L": "54",
	# "input_bit_5_L": "55",
	# "input_bit_6_L": "56",
	# "input_bit_7_L": "57",
	# "input_bit_8_L": "58",
	"input_bit_E_L": "32",

	#Insert Tile Glue
	# "#70": "60",
	# "#71": "61",
	# "#61": "62",
	# "#60": "63",
	# "#51": "64",
	# "#50": "65",
	# "#41": "66",
	# "#40": "67",
	# "#31": "68",
	# "#30": "69",
	# "#21": "70",
	# "#20": "71",
	# "#11": "72",
	# "#10": "73",
	# "#01": "74",
	# "#00": "75"
};

tile_position = {
	"00": "orange",
	"01": "blue",
	"10": "red",
	"11": "yellow",
	"1": "dark blue",
	"0": "dark blue",

	#Edge Positions
	"SL(0)": "white",
	"SSL(1)": "purple",
	"SSR": "cyan",
	"IL": "green",
	"IR": "green",
	"CL": "red",
	"CR": "red",

	#Border and Seed Positions
	"S0": "grey",
	"E0": "grey",
	"EL": "dark blue",
	"ER": "dark blue"
};
