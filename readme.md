# file-mon 
This is a program that checks files or directories to check if they are changed. This is a good
IR tool for detecting any tampering to important files in the Linux filesystem. 


### What is this for?
This will be used for ISTS 2020 as a blue team tool for monitoring any red team tampering. Will
also help with writing any IR related injects as It informs the user of the exact changes and when they happend


### Use
Written In python.
To use just download all file and put them in the same folder. Place all directory and file pathsin the respective
folder. The log file is where all logs will be placed. The program will run and respond with any found changes.
More detailed information will be placed in the log file. 

### Running Program
```
sudo python3 file_mon.py
```
