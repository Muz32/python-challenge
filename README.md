# python-challenge
This assignment challenge contains two different Analysis stored in two diffrent subfolders within the repository. 

1. Pybank Subfolder:
This subfolder contains a Python script that analyzes financial data from a given CSV file located in the 'resources' folder.
When executed, the script calculates and prints the following financial analysis from the dataset:
-Total number of months
-Net total profit/losses
-Average changes in profit/losses
-Greatest increase in profits
-Greatest decrease in profits

2. Pypoll Subfolder:
This subfolder, houses a Python script to calculate election results.
This script analyses election results from the provided data in the 'resources' folder.
Upon execution, it calculates and prints the following election analysis:
-Total votes cast
-List of candidates
-Amount of votes and respective percentage of votes received by each candidate
-Result for the winner of the election


Both scripts conclude by exporting their output to a text file within the relevant analysis folders. 


** Please note: The Python script relies on relative file references from a different folder, which may result in "File Not Found" errors during execution. Based on my experience with my computer, I have found out that the following prevents this issue from occuring:

-Download the entire repository and open the relevant folders directly from Visual Studio (VS) Code.

-Use the 'Open Folder' option in VS Code to open the 'Pybank' or 'Pypol' subfolders individually. Then click the python file ('main.py') in the epxlorer pane on the left to see the code and execute it. Ensure to open each subfolder in a new window and avoid opening both simultaneously in one window. 

-Avoid opening files directly from your computer system menu of folders, as it may trigger the 'File Not Found' error when exceuting the code. Instead, ensure that you open the folder directly from within VS Code.

-Check the colour of status bar at the bottom in VS code: If it's purple, no folder is recognized in the workspace. Only when it's blue does VS Code recognises an open folder or workspace.

If you also encounter the "File Not Found Error" problem, please follow the above guide to troubleshoot the problem effectively.  

