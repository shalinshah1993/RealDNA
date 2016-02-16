
####Computing Real Numbers using DNA Self-Assembly

- This is a small `python` script which takes a number as input and generates a `XGrow` simulation file as output. To understand how this algorithm works, please refer our paper `Computing Real Numbers using DNA Self-Assembly` ![here](http://arxiv.org/abs/1502.05552)

- To run the script for number `42.25` with number of precision bits `4`, type

        $ python Tile.py
        
        ######Tile File Generator for Square-Root of a Number#########
        Please enter a real number: 42.25
        Please enter number of precision bits after decimal point:4
        You tile file for 42.25 with precision of 4  bits has been created in the folder.
        
- This will generate a tile file `SquareRoot_42_25.tiles` in the same folder. 

- Once you have tile file, just take it to the XGrow executable folder and type 

        $ ./xgrow SquareRoot_42_25.tiles

__Note__ : You need python 2.7 installed on your system to run our program. To know more about XGrow modules and installation, please refer ![Winfree's XGrow Documentation](http://www.dna.caltech.edu/Xgrow/)
