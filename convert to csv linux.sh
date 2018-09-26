#Rename the xlsx file
#computer clicks

#Convert
sudo apt-get install gnumeric
ssconvert input.xlsx output.csv

#Looping
for f in *.xls ; do xls2csv "$f" "${f%.xls}.csv" 
