#Author - Shalin Shah
#Last Edited - December 2, 2014
import TileDictionary
from operator import itemgetter

def DecimalToBinary(input_number, precision):
	if "." in str(input_number):
		input_number_1, input_number_2 = str(input_number).split(".")
		output_number_1 = str(bin(int(input_number_1)))[2:]
		output_number_2 = ""
		input_number_2 = float("0." + input_number_2)
		while precision != 0:
			precision = precision - 1
			output_number_2 = output_number_2 + str(input_number_2 * 2).split(".")[0]
			input_number_2 = (input_number_2 * 2) % 1
		output_number = str(output_number_1) + str(output_number_2)
		output_number_with_decimal = str(output_number_1) + "." + str(output_number_2)
	else:
		output_number = str(bin(int(input_number)))[2:]
		output_number_with_decimal = str(output_number) + "."
		while precision != 0:
			precision = precision - 1
			output_number = output_number + "0"
			output_number_with_decimal = output_number_with_decimal + "0"
	return output_number, output_number_with_decimal

def GetCompareTiles():
	output_string = """
%-----------Comparison Tiles[Total = 8 + 16]----------------- 
{"""+ TileDictionary.edge_color["000"] + """ """ + TileDictionary.edge_color["=0"] + """ """ + TileDictionary.edge_color["00"]+ """ """ + TileDictionary.edge_color["=0"] + """}(""" + TileDictionary.tile_position["00"]+ """)
{"""+ TileDictionary.edge_color["001"] + """ """ + TileDictionary.edge_color["=0"] + """ """ + TileDictionary.edge_color["00"]+ """ """ + TileDictionary.edge_color["=1"] + """}(""" + TileDictionary.tile_position["00"]+ """)
{"""+ TileDictionary.edge_color["010"] + """ """ + TileDictionary.edge_color["<1"] + """ """ + TileDictionary.edge_color["01"]+ """ """ + TileDictionary.edge_color["=0"] + """}(""" + TileDictionary.tile_position["01"]+ """)
{"""+ TileDictionary.edge_color["011"] + """ """ + TileDictionary.edge_color["<1"] + """ """ + TileDictionary.edge_color["01"]+ """ """ + TileDictionary.edge_color["=1"] + """}(""" + TileDictionary.tile_position["01"]+ """)
{"""+ TileDictionary.edge_color["100"] + """ """ + TileDictionary.edge_color[">0"] + """ """ + TileDictionary.edge_color["10"]+ """ """ + TileDictionary.edge_color["=0"] + """}(""" + TileDictionary.tile_position["10"]+ """)
{"""+ TileDictionary.edge_color["101"] + """ """ + TileDictionary.edge_color[">0"] + """ """ + TileDictionary.edge_color["10"]+ """ """ + TileDictionary.edge_color["=1"] + """}(""" + TileDictionary.tile_position["10"]+ """)
{"""+ TileDictionary.edge_color["110"] + """ """ + TileDictionary.edge_color["=1"] + """ """ + TileDictionary.edge_color["11"]+ """ """ + TileDictionary.edge_color["=0"] + """}(""" + TileDictionary.tile_position["11"]+ """)
{"""+ TileDictionary.edge_color["111"] + """ """ + TileDictionary.edge_color["=1"] + """ """ + TileDictionary.edge_color["11"]+ """ """ + TileDictionary.edge_color["=1"] + """}(""" + TileDictionary.tile_position["11"]+ """)

{"""+ TileDictionary.edge_color["000"] + """ """ + TileDictionary.edge_color[">0"] + """ """ + TileDictionary.edge_color["00"]+ """ """ + TileDictionary.edge_color[">0"] + """}(""" + TileDictionary.tile_position["00"]+ """)
{"""+ TileDictionary.edge_color["000"] + """ """ + TileDictionary.edge_color["<0"] + """ """ + TileDictionary.edge_color["00"]+ """ """ + TileDictionary.edge_color["<0"] + """}(""" + TileDictionary.tile_position["00"]+ """)

{"""+ TileDictionary.edge_color["001"] + """ """ + TileDictionary.edge_color[">0"] + """ """ + TileDictionary.edge_color["00"]+ """ """ + TileDictionary.edge_color[">1"] + """}(""" + TileDictionary.tile_position["00"]+ """)
{"""+ TileDictionary.edge_color["001"] + """ """ + TileDictionary.edge_color["<0"] + """ """ + TileDictionary.edge_color["00"]+ """ """ + TileDictionary.edge_color["<1"] + """}(""" + TileDictionary.tile_position["00"]+ """)

{"""+ TileDictionary.edge_color["010"] + """ """ + TileDictionary.edge_color[">1"] + """ """ + TileDictionary.edge_color["01"]+ """ """ + TileDictionary.edge_color[">0"] + """}(""" + TileDictionary.tile_position["01"]+ """)
{"""+ TileDictionary.edge_color["010"] + """ """ + TileDictionary.edge_color["<1"] + """ """ + TileDictionary.edge_color["01"]+ """ """ + TileDictionary.edge_color["<0"] + """}(""" + TileDictionary.tile_position["01"]+ """)

{"""+ TileDictionary.edge_color["011"] + """ """ + TileDictionary.edge_color[">1"] + """ """ + TileDictionary.edge_color["01"]+ """ """ + TileDictionary.edge_color[">1"] + """}(""" + TileDictionary.tile_position["01"]+ """)
{"""+ TileDictionary.edge_color["011"] + """ """ + TileDictionary.edge_color["<1"] + """ """ + TileDictionary.edge_color["01"]+ """ """ + TileDictionary.edge_color["<1"] + """}(""" + TileDictionary.tile_position["01"]+ """)

{"""+ TileDictionary.edge_color["100"] + """ """ + TileDictionary.edge_color[">0"] + """ """ + TileDictionary.edge_color["10"]+ """ """ + TileDictionary.edge_color[">0"] + """}(""" + TileDictionary.tile_position["10"]+ """)
{"""+ TileDictionary.edge_color["100"] + """ """ + TileDictionary.edge_color["<0"] + """ """ + TileDictionary.edge_color["10"]+ """ """ + TileDictionary.edge_color["<0"] + """}(""" + TileDictionary.tile_position["10"]+ """)

{"""+ TileDictionary.edge_color["101"] + """ """ + TileDictionary.edge_color[">0"] + """ """ + TileDictionary.edge_color["10"]+ """ """ + TileDictionary.edge_color[">1"] + """}(""" + TileDictionary.tile_position["10"]+ """)
{"""+ TileDictionary.edge_color["101"] + """ """ + TileDictionary.edge_color["<0"] + """ """ + TileDictionary.edge_color["10"]+ """ """ + TileDictionary.edge_color["<1"] + """}(""" + TileDictionary.tile_position["10"]+ """)

{"""+ TileDictionary.edge_color["110"] + """ """ + TileDictionary.edge_color[">1"] + """ """ + TileDictionary.edge_color["11"]+ """ """ + TileDictionary.edge_color[">0"] + """}(""" + TileDictionary.tile_position["11"]+ """)
{"""+ TileDictionary.edge_color["110"] + """ """ + TileDictionary.edge_color["<1"] + """ """ + TileDictionary.edge_color["11"]+ """ """ + TileDictionary.edge_color["<0"] + """}(""" + TileDictionary.tile_position["11"]+ """)

{"""+ TileDictionary.edge_color["111"] + """ """ + TileDictionary.edge_color[">1"] + """ """ + TileDictionary.edge_color["11"]+ """ """ + TileDictionary.edge_color[">1"] + """}(""" + TileDictionary.tile_position["11"]+ """)
{"""+ TileDictionary.edge_color["111"] + """ """ + TileDictionary.edge_color["<1"] + """ """ + TileDictionary.edge_color["11"]+ """ """ + TileDictionary.edge_color["<1"] + """}(""" + TileDictionary.tile_position["11"]+ """)\n"""
	return output_string

def GetCompareRightBoundaryTiles():
	output_string = "%-----------Comparison Right Boundary[Total = 6]-----------------\n"

	for x in {"<", ">", "="}:
		for y in {"0", "1"}:
			output_string = output_string + """{"""+ TileDictionary.edge_color[x] + """ """ + TileDictionary.edge_color["0"] + """ """ + TileDictionary.edge_color["e"]+ """ """ + TileDictionary.edge_color[x + y] + """}(""" + TileDictionary.tile_position["CR"]+ """)\n"""
	return output_string


#Add the lower tile for Compare glue($-1) which is pre-defined and then upper tiles along with their glue strengths.
def GetCompareLeftBoundaryTiles(n, total_edge_color):
	output_string = "%-----------Comparison Left Boundary[Total = (n/2)]-----------------\n"
	TileDictionary.edge_color.update({"$(-1)s" : str(total_edge_color + 1)})
	output_string = output_string + """{""" + TileDictionary.edge_color["$(-1)s"] + """ """ + TileDictionary.edge_color["=0"] + """ """ + TileDictionary.edge_color["x(-1)"]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["CL"]+ """)\n"""
	output_glue_string = " 1"
	total_edge_color = total_edge_color + 1

	for x in xrange(1, n/2):
		TileDictionary.edge_color.update({"$" + str(2*x - 1) + "s" : str(total_edge_color + 1)})
		TileDictionary.edge_color.update({"x" + str(2*x - 1) : str(total_edge_color + 2)})
		output_glue_string = output_glue_string + " 1 2"
		total_edge_color = total_edge_color + 2
		output_string = output_string + """{"""+ TileDictionary.edge_color["$" + str(2*x - 1) + "s"] + """ """ + TileDictionary.edge_color["=0"] + """ """ + TileDictionary.edge_color["x" + str(2*x - 1)]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["CL"]+ """)\n"""
		#print "$" + str(2*x - 1), TileDictionary.edge_color["$" + str(2*x - 1)]
		

	#We need to add last glue since this will be used in INSERT tile and frame tiles at TOP.
	TileDictionary.edge_color.update({"x" + str(n - 1) : str(total_edge_color + 1)})
	total_edge_color = total_edge_color + 1
	output_glue_string = output_glue_string + " 2"

	#print sorted(TileDictionary.edge_color.items(), key=itemgetter(1)), "compare", str(n)

	return output_string, total_edge_color, output_glue_string

def GetSubShiftTiles():
	output_string = "%-----------Sub/Shift Tiles[Total = 16]-----------------\n"

	for a in {"0", "1"}:
		for b in {"0", "1"}:
			for c in {"0", "1"}: 
				for d in {"0", "1"}:
					x = str(int(a) ^ int(b) ^ int(d))
					y = "0"
					if (int(b) + int(d) - int(a)) > 0:
						y = "1"
					output_string = output_string + """{"""+ TileDictionary.edge_color[x + c] + """ """ + TileDictionary.edge_color[d] + """ """ + TileDictionary.edge_color[a + b + c]+ """ """ + TileDictionary.edge_color[y] + """}(""" + TileDictionary.tile_position[x + c]+ """)\n"""
	return output_string

def GetShiftTiles():
	output_string = "%-----------Shift Tiles[Total = 8]-----------------\n"

	for a in {"0", "1"}:
		for b in {"0", "1"}:
			for c in {"0", "1"}: 
				output_string = output_string + """{"""+ TileDictionary.edge_color[a + c] + """ """ + TileDictionary.edge_color["t"] + """ """ + TileDictionary.edge_color[a + b + c]+ """ """ + TileDictionary.edge_color["t"] + """}(""" + TileDictionary.tile_position[a + c]+ """)\n"""
	return output_string

def GetSubShiftRightBoundaryTiles():
	output_string = "%-----------Sub/Shift Right Boundary[Total = 2 + 1]-----------------\n"

	for x in {"=", ">"}: 
		output_string = output_string + """{"""+ TileDictionary.edge_color["l"] + """ """ + TileDictionary.edge_color["0"] + """ """ + TileDictionary.edge_color[x]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["SSR"]+ """)\n"""
	output_string = output_string + """{"""+ TileDictionary.edge_color["l"] + """ """ + TileDictionary.edge_color["0"] + """ """ + TileDictionary.edge_color["<"]+ """ """ + TileDictionary.edge_color["t"] + """}(""" + TileDictionary.tile_position["SSR"]+ """)\n"""
	return output_string


def GetSubShiftLeftBoundaryTiles(n, total_edge_color):
	output_string = "%-----------Sub/Shift Left Boundary[Total = (n/2)]-----------------\n"
	TileDictionary.edge_color.update({"$11" : str(total_edge_color + 1)})
	output_string = output_string + """{""" + TileDictionary.edge_color["$11"] + """ """ + TileDictionary.edge_color["0"] + """ """ + TileDictionary.edge_color["$(-1)s"]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["SSL(1)"]+ """)\n"""
	output_glue_string = " 2"
	total_edge_color = total_edge_color + 1

	for x in xrange(1, n/2):
		TileDictionary.edge_color.update({"$" + str(2*x + 1) + "1" : str(total_edge_color + 1)})
		#print TileDictionary.edge_color["$" + str(2*x + 1) + "1"], "$" + str(2*x + 1) + "1"
		output_glue_string = output_glue_string + " 2"
		total_edge_color = total_edge_color + 1
		output_string = output_string + """{"""+ TileDictionary.edge_color["$" + str(2*x + 1) + "1"] + """ """ + TileDictionary.edge_color["0"] + """ """ + TileDictionary.edge_color["$" + str(2*x - 1) + "s"]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["SSL(1)"]+ """)\n"""

	#print sorted(TileDictionary.edge_color.items(), key=itemgetter(1)), "sub/shift"
	return output_string, total_edge_color, output_glue_string

#Since all the glues and their strengths are already added during Sub/Shift no need to add them again.
def GetShiftLeftBoundaryTiles(n, total_edge_color):
	output_string = "%-----------Shift Left Boundary[Total = (n/2)]-----------------\n"
	TileDictionary.edge_color.update({"$10" : str(total_edge_color + 1)})
	output_string = output_string + """{""" + TileDictionary.edge_color["$10"] + """ """ + TileDictionary.edge_color["t"] + """ """ + TileDictionary.edge_color["$(-1)s"]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["SL(0)"]+ """)\n"""
	output_glue_string = " 2"
	total_edge_color = total_edge_color + 1

	for x in xrange(1, n/2):
		TileDictionary.edge_color.update({"$" + str(2*x + 1) + "0" : str(total_edge_color + 1)})
		#print TileDictionary.edge_color["$" + str(2*x + 1) + "0"], "$" + str(2*x + 1) + "0"	
		output_glue_string = output_glue_string + " 2"
		total_edge_color = total_edge_color + 1
		output_string = output_string + """{"""+ TileDictionary.edge_color["$" + str(2*x + 1) + "0"] + """ """ + TileDictionary.edge_color["t"] + """ """ + TileDictionary.edge_color["$" + str(2*x - 1) + "s"]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["SL(0)"]+ """)\n"""
	return output_string, total_edge_color, output_glue_string

#Add all the new glues and their strengths first and then write tiles
def GetInsertTiles(n, total_edge_color):
	output_glue_string = ""
	output_string = "%-----------Insert Tiles[Total = (n-1)*8 + 16]-----------------\n"

	for i in xrange(0, n):
		output_glue_string = output_glue_string + " 1 1"
		TileDictionary.edge_color.update({"#" + str(i) + "1": str(total_edge_color + 1)})
		TileDictionary.edge_color.update({"#" + str(i) + "0": str(total_edge_color + 2)})
		total_edge_color = total_edge_color + 2

	#Generate the replace bit tiles first.
	for a in {"0", "1"}:
		for b in {"0", "1"}:
			for c in {"0", "1"}:
				output_string = output_string + """{"""+ TileDictionary.edge_color[a + c] + """ """ + TileDictionary.edge_color["#0" + b] + """ """ + TileDictionary.edge_color[a + b]+ """ """ + TileDictionary.edge_color["#0" + c] + """}(""" + TileDictionary.tile_position[a + c]+ """)\n"""

	#print sorted(TileDictionary.edge_color.items())
	#Generate the remaining tiles.
	for i in xrange(0, n-1):
		for a in {"0", "1"}:
			for b in {"0", "1"}:
				for c in {"0", "1"}:
					#print "#" + str(i+1) + c, "#" + str(i) + c
					output_string = output_string + """{"""+ TileDictionary.edge_color[a + b] + """ """ + TileDictionary.edge_color["#" + str(i) + c] + """ """ + TileDictionary.edge_color[a + b]+ """ """ + TileDictionary.edge_color["#" + str(i+1) + c] + """}(""" + TileDictionary.tile_position[a + b]+ """)\n"""	

	#print output_string
	return output_string, total_edge_color, output_glue_string

#Here we don't need to insert the glues and their strengths since they were already inserted in CL and SSL/SL
def GetInsertLeftBoundaryTiles(n):
	output_string = "%-----------Insert Left Boundary[Total = 2*(n/2)]-----------------\n"
	
	for x in xrange(0, n/2):
		#print TileDictionary.edge_color["$" + str(2*x + 1)], "$" + str(2*x + 1)
		output_string = output_string + """{"""+ TileDictionary.edge_color["x" + str(2*x + 1)] + """ """ + TileDictionary.edge_color["#" + str(2*x + 1) + "1"] + """ """ + TileDictionary.edge_color["$" + str(2*x + 1) + "1"]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["IL"]+ """)\n"""
		output_string = output_string + """{"""+ TileDictionary.edge_color["x" + str(2*x + 1)] + """ """ + TileDictionary.edge_color["#" + str(2*x + 1) + "0"] + """ """ + TileDictionary.edge_color["$" + str(2*x + 1) + "0"]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["IL"]+ """)\n"""
	return output_string

def GetInsertRightBoundaryTiles():
	output_string = "%-----------Insert Right Boundary[Total = 2]-----------------\n"

	for i in {"0", "1"}:
		output_string = output_string + """{"""+ TileDictionary.edge_color["e"] + """ """ + TileDictionary.edge_color["0"] + """ """ + TileDictionary.edge_color["l"]+ """ """ + TileDictionary.edge_color["#0" + str(i)] + """}(""" + TileDictionary.tile_position["IL"]+ """)\n"""
	return output_string

# print GetCompareLeftBoundaryTiles(6)
# print GetInsertTiles(8, 31)
#print GetInsertLeftBoundaryTiles(6)







