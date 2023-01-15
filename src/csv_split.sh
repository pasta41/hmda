# first arg should be the file name
# second should be the chunk size; been using 100000k
# third should be any tag info

tail -n +2 $1 | split -l $2 - split_$3_
for file in split_*
do
    head -n 1 $1 > tmp_file
    cat $file >> tmp_file
    mv -f tmp_file $file
done

