# run from within the wkspace directory

# don't include VI; only have data for 2017
for state in AK  AZ  CT  FL  IA  IN  LA  ME  MO  NC  NH  NV  OK  PR  SD  UT  VT  WV AL  CA  DC  GA  ID  KS  MA  MI  MS  ND  NJ  NY  OR  RI  TN  VA  WA  WY AR  CO  DE  HI  IL  KY  MD  MN  MT  NE  NM  OH  PA  SC  TX WI
do
	echo $state

	for year in 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017
	do
   		echo -e "\t$year"
   		# join files for state and year
   		awk '(NR ==1) || (FNR > 1)' $state/$year/split_* > $state/$year/$year-$state-all.csv
   		zip $state/$year/$year-$state-all.zip $state/$year/$year-$state-all.csv

   		# move to data dir in repo
   		mv $state/$year/$year-$state-all.zip ../hmda/data/$state/$year
	done
	echo -e "\n"
done
