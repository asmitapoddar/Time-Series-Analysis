for f in *.xlsx ; do ssconvert "$f" "${f%.xlsx}.csv" ; done
#for i in *.xlsx; do sudo libreoffice --headless --convert-to csv "$i" ; done

#chmod +x loop_convert.sh
#./loop_convert.sh
