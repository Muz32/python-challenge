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
The second subfolder, houses another Python script to calculate election results.
This script analyses election results from the provided data in the 'resources' folder.
Upon execution, it calculates and prints the following election analysis:
-Total votes cast
-List of candidates
-Amount of votes and respective percentage of votes received by each candidate
-Result for the winner of the election


Both scripts conclude by exporting their output to a text file within the relevant analysis folders. 

**Please note: As the python script reads data files using relative file references from a different folder, there maybe be occcurance of "File Not Found Error" when executing the code. To minimise this error, please downnload entire repository and open relevant folders directly from the Visual Studio (VS) code application. Use the 'open folder' option in VS code to view files. I notice that with my computer, opening the python file from the windows menu in VS code gives 'file not found error' when exceuting the code. It could be that VS code does not recognise that the file was opened from a folder so it would fail to locate and read files to extract data. I found out that if the status bar at the bottom of VS code application is purple, it means no folder is currently open in the workspace even though if you opened a file that was inside a folder. Only if the status bar is blue, it recognises that a folder or workspace is open. In order to see the blue bar, I have to open the folder from the VS code application. Then only I don't get errors on reading or writing files. 