

#splits huge file into smaller files of 100k rows each
#keeping header intact

tail -n +2 trip1.csv | split -l 100000 - split_
for file in split_*
do
    head -n 1 trip1.csv > tmp_file
    cat $file >> tmp_file
    mv -f tmp_file $file
done