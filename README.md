# Treatment Text Tool

Manipulates texts, hiding sensitive data and performing other types of necessary treatments

## Requirements

- Python >= 3.10

## How To Use

The files to be manipulated must be copied to the input directory. The run the program.

```
python treattext.py
```

You will be asked for the name of the file you want to process. Enter the name of the file, including the file extension, and press enter.

The following options will be presented:

```
SELECT THE OPTION DESIRED:
1 - FORMAT NAME OF FILE
2 - REMOVE EXTRA WORDS OF NAME OF FILE
3 - REPLACE PART OF THE NAME OF FILE TO OTHER TEXT
4 - FORMAT CSV FILE
5 - HIDE SENSITIVE DATA
0 - EXIT
```

## Hiding Sensitive Data

Assuming we have a csv file with sensitive data, as shown in the example below:

```csv
ID;NAME;CPF
1;Jon Snow;614.067.195-41
2;Arya Stark;751.201.387-73
3;Daenerys Targaryen;447.727.006-88
4;Cersei Lannister;892.046.972-79
5;Theon Greyjoy;406.104.157-11
6;Margaery Tyrell;|152.553.483-16
7;Catelyn Stark;462.841.450-17
8;Stannis Baratheon;106.795.584-85
9;Eddard Stark;962.315.553-22
10;Jaime Lannister;101.612.462-53
11;Samwell Tarly;214.625.311-75
12;Sansa Stark;107.585.047-68
13;Davos Seaworth;125.436.423-79
14;Viserys Targaryen;360.709.816-91
15;Robb Stark;928.981.689-34
16;Yara Greyjoy;489.059.089-27
17;Tyrion Lannister;872.832.196-49
18;Brienne de Tarth;607.265.591-08
19;Euron Greyjoy;134.652.973-97
20;Bran Stark;121.377.397-43
```

We copy the file into the input folder and then run the following command:

```
python treattext.py
```

The program will ask for the name of the field where the sensitive data is located. Enter the name of the file and select the option 5. Next enter the name of the field to be processed. In this case, we will inform the name of the third field (CPF).

The new version of the file with the data hidden will then be saved in the output directory.

```csv
ID;NAME;CPF
1;Jon Snow;614******41
2;Arya Stark;751******73
3;Daenerys Targaryen;447******88
4;Cersei Lannister;892******79
5;Theon Greyjoy;406******11
6;Margaery Tyrell;152******16
7;Catelyn Stark;462******17
8;Stannis Baratheon;106******85
9;Eddard Stark;962******22
10;Jaime Lannister;101******53
11;Samwell Tarly;214******75
12;Sansa Stark;107******68
13;Davos Seaworth;125******79
14;Viserys Targaryen;360******91
15;Robb Stark;928******34
16;Yara Greyjoy;489******27
17;Tyrion Lannister;872******49
18;Brienne de Tarth;607******08
19;Euron Greyjoy;134******97
20;Bran Stark;121******43
```
