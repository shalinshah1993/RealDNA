#Author - Shalin Shah
#Mentor - Manish K Gupta
#Last Edited - December 4, 2014
#This python file generates the tile file for Square-Root of n
import TileDictionary
import ExtraModules
from operator import itemgetter
import math

precision = 4
total_tiles = 0
input_number_length = 0
assembly_height = 0
assembly_width = 0
total_edge_color = len(TileDictionary.edge_color)

print("######Tile File Generator for Square-Root of a Number#########")
input_number_decimal = input("Please enter a real number:")
precision = input("Please enter number of precision bits after decimal point:")

#Check if the input number is of odd length. Append 0 in that case. Also, find the total other numbers.
input_number, input_number_with_decimal = ExtraModules.DecimalToBinary(input_number_decimal, precision)
input_number_length = len(input_number)
if input_number_length % 2 != 0:
	input_number = "0" + input_number
	input_number_with_decimal = "0" + input_number_with_decimal
	input_number_length = input_number_length + 1

#print input_number, input_number_length

#The number of tiles used in the assembly
assembly_height = ((input_number_length/2) * 3) + 2
assembly_width = input_number_length + 2

#The number of tiles used for different computations
no_input_tiles = input_number_length
no_compare_tiles = 8 + 16
no_sub_shift_tiles = 16
no_shift_tiles = 8
no_insert_tiles = 8 + (input_number_length-1)*8
no_compare_right_boudary_tiles = 6
no_compare_left_boudary_tiles = input_number_length/2
no_sub_shift_right_boudary_tiles = 3
no_sub_shift_left_boudary_tiles = input_number_length
no_insert_right_boundary_tiles = 2
no_insert_left_boundary_tiles = (input_number_length/2) + (input_number_length/2)

#Create a SquareRoot.tile file and write the comments about Version Control and Authorship
if "int" in str(type(input_number_decimal)):
	open_file = open("SquareRoot_" + str(input_number_decimal) + ".tiles", "w")
else:
	open_file = open("SquareRoot_" + str(input_number_decimal).split(".")[0] + "_" + str(input_number_decimal).split(".")[1] + ".tiles", "w")
comments_tile_file = """%File Name: SquareRoot.tiles	
%Author: Shalin Shah 
%Mentor: Manish K Gupta
%This is the .tiles file for generating Square-Root of a number.

%The output can be observed in the left most column.

%Output Tiles - PURPLE (1) and WHITE (0)
%Tile Colors : Orange(00)	Blue(01)	Red(10)		Yellow(11)

%n = \t\t""" + str(input_number_decimal) + """\t\t\t""" + str(ExtraModules.DecimalToBinary(input_number_decimal, 0)[1]) + """
%sqrt(n)=\t""" + str(math.sqrt(float(input_number_decimal))) + """ \t\t""" + str(ExtraModules.DecimalToBinary(math.sqrt(float(input_number_decimal)), precision)[1])


#Make the string to write the .tile code of SEED tile.
input_tile_file = """

%------------Seed Tile---------------
{"""+ TileDictionary.edge_color["x(-1)"] + """ """ + TileDictionary.edge_color["input_bit_1_L"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["0"] + """}(""" + TileDictionary.tile_position["S0"]+ """)
"""
total_tiles = total_tiles + 1

#Write Glue strength for all the edge colors
glue_strength_tile_file = """binding strengths={1 1 1 1 1 1 1 1 1 1 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2"""

	
#For a 1 or 2 bit numbers, we ave only 2 input tiles so else clause
if input_number_length > 2:
	# Also, first 2 input tiles have right position bit 1, 0 so manually written.
	input_tile_file = input_tile_file + """%------------Input Tiles-------------
{"""+ TileDictionary.edge_color[input_number[0] + "0"] + """ """ + TileDictionary.edge_color["input_bit_2_L"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["input_bit_1_L"] + """}(""" + TileDictionary.tile_position[input_number[0] + "0"]+ """)
{"""+ TileDictionary.edge_color[input_number[1] + "1"] + """ """ + TileDictionary.edge_color["input_bit_3_L"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["input_bit_2_L"] + """}(""" + TileDictionary.tile_position[input_number[1] + "1"]+ """)\n"""

	total_tiles = total_tiles + 2

	#Loop to write INPUT tiles
	for i in xrange(2, input_number_length-1):
		TileDictionary.edge_color.update({"input_bit_" + str(i+2) + "_L": str(total_edge_color + 1)})
		glue_strength_tile_file = glue_strength_tile_file + " 2"
		input_tile_file = input_tile_file + """{"""+ TileDictionary.edge_color[input_number[i] + "0"] + """ """ + TileDictionary.edge_color["input_bit_" + str(i+2) + "_L"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["input_bit_"+ str(i+1) +"_L"] + """}(""" + TileDictionary.tile_position[input_number[i] + "0"]+ """)\n"""
		total_edge_color = total_edge_color + 1
		total_tiles = total_tiles + 1

	#TileDictionary.edge_color.update({"input_bit_" + str(input_number_length) + "_L": str(total_edge_color + 1)})
	glue_strength_tile_file = glue_strength_tile_file + " 2"
	input_tile_file = input_tile_file + """{""" + TileDictionary.edge_color[str(input_number[input_number_length-1]) + "0"] + """ """ + TileDictionary.edge_color["input_bit_E_L"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["input_bit_"+ str(input_number_length) +"_L"] + """}(""" + TileDictionary.tile_position[input_number[input_number_length-1] + "0"]+ """)\n"""
	input_tile_file = input_tile_file + """{""" + TileDictionary.edge_color["e"] + """ """ + TileDictionary.edge_color["0"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["input_bit_E_L"] + """}(""" + TileDictionary.tile_position["E0"]+ """)"""
	total_tiles = total_tiles + 2
	total_edge_color = total_edge_color + 1
else:
	input_tile_file = input_tile_file + """%------------Input Tiles-------------
{"""+ TileDictionary.edge_color[input_number[0] + "0"] + """ """ + TileDictionary.edge_color["input_bit_2_L"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["input_bit_1_L"] + """}(""" + TileDictionary.tile_position[input_number[0] + "0"]+ """)
{"""+ TileDictionary.edge_color[input_number[1] + "1"] + """ """ + TileDictionary.edge_color["input_bit_E_L"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["input_bit_2_L"] + """}(""" + TileDictionary.tile_position[input_number[1] + "1"]+ """)
{""" + TileDictionary.edge_color["e"] + """ """ + TileDictionary.edge_color["0"] + """ """ + TileDictionary.edge_color["0"]+ """ """ + TileDictionary.edge_color["input_bit_E_L"] + """}(""" + TileDictionary.tile_position["E0"]+ """)\n"""
	total_tiles = total_tiles + 3
	
#Add compare tiles to the total number of tiles.
total_tiles = total_tiles + no_compare_tiles
input_tile_file = input_tile_file + ExtraModules.GetCompareTiles()

#Add the frame tiles for Comparison - Right and Left
total_tiles = total_tiles + no_compare_right_boudary_tiles
input_tile_file = input_tile_file + ExtraModules.GetCompareRightBoundaryTiles()

total_tiles = total_tiles + no_compare_left_boudary_tiles
tiles, total_edge_color, glue_strength = ExtraModules.GetCompareLeftBoundaryTiles(input_number_length, total_edge_color)
input_tile_file = input_tile_file + tiles
glue_strength_tile_file = glue_strength_tile_file + glue_strength

#Add Subtract/Shift tiles to the total number of tiles - Right and Left
total_tiles = total_tiles + no_sub_shift_tiles
input_tile_file = input_tile_file + ExtraModules.GetSubShiftTiles()

total_tiles = total_tiles + no_shift_tiles
input_tile_file = input_tile_file + ExtraModules.GetShiftTiles()

#Add the frame tiles for Subtract/Shift - Right and Left
total_tiles = total_tiles + no_sub_shift_right_boudary_tiles
input_tile_file = input_tile_file + ExtraModules.GetSubShiftRightBoundaryTiles()

total_tiles = total_tiles + no_sub_shift_left_boudary_tiles
tiles, total_edge_color, glue_strength = ExtraModules.GetSubShiftLeftBoundaryTiles(input_number_length, total_edge_color)
input_tile_file = input_tile_file + tiles
glue_strength_tile_file = glue_strength_tile_file + glue_strength

tiles, total_edge_color, glue_strength = ExtraModules.GetShiftLeftBoundaryTiles(input_number_length, total_edge_color)
input_tile_file = input_tile_file + tiles
glue_strength_tile_file = glue_strength_tile_file + glue_strength

#Add the insert bit tiles to the total number of tiles
total_tiles = total_tiles + no_insert_tiles
tiles, total_edge_color, glue_strength = ExtraModules.GetInsertTiles(input_number_length, total_edge_color)
input_tile_file = input_tile_file + tiles
glue_strength_tile_file = glue_strength_tile_file + glue_strength

#Add the frame tiles for inserting a bit - Right and Left
total_tiles = total_tiles + no_insert_right_boundary_tiles
input_tile_file = input_tile_file + ExtraModules.GetInsertRightBoundaryTiles()

total_tiles = total_tiles + no_insert_left_boundary_tiles
input_tile_file = input_tile_file + ExtraModules.GetInsertLeftBoundaryTiles(input_number_length)



#Calculate the total number of glues and tiles and write it to .tile file
total_calculate_tile_file = """
tile edges matches {{N E S W}*}
num tile types=""" + str(total_tiles) + """
num binding types=""" + str(total_edge_color) + """
tile edges={
"""

#Close the bracket for binding strength
glue_strength_tile_file = glue_strength_tile_file + """}
size=24
block=12
T=2
seed=31,1
"""

#Close the bracket for input tile types
input_tile_file = input_tile_file + "\n}"

open_file.writelines(comments_tile_file + total_calculate_tile_file + input_tile_file + "\n" + glue_strength_tile_file)
print "You tile file for", str(input_number_decimal), "with precision of", str(precision), " bits has been created in the folder."
#print sorted(TileDictionary.edge_color.items(), key=itemgetter(1))
#print sorted(TileDictionary.edge_color.items())
#print total_edge_color, len(TileDictionary.edge_color)  
#print input_tile_file
