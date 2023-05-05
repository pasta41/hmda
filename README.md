# HMDA Data Cleaning Branch

This repository contains the scripts used to pre-process the HMDA dataset, as well as the library toolkit for accessing and manipulating subsets of the data.

Related links:

- [Raw data for 2007-2017](https://www.consumerfinance.gov/data-research/hmda/historic-data/?geo=nationwide&records=all-records&field_descriptions=labels)
- [Record format](https://files.consumerfinance.gov/hmda-historic-data-dictionaries/lar_record_format.pdf)
- [Associated record numeric codes](https://files.consumerfinance.gov/hmda-historic-data-dictionaries/lar_record_codes.pdf)


## New Cleaning Procedure (altogether, then split) 

- Download the raw data files to the cluster environment [DONE]
- Tunnel/ open a Jupyter interactive session
- Load up a given year file into the manual cleaning notebook `clean_year.ipynb` and execute a line at a time

- Status [DONE]
	- 2007 [DONE]
	- 2008 [DONE]
	- 2009 [DONE]
	- 2010 [DONE]
	- 2011 [DONE]
	- 2012 [DONE]
	- 2013 [DONE]
	- 2014 [DONE]
	- 2015 [DONE] 
	- 2016 [DONE]
	- 2017 [DONE] 
		- This data is missing the sequence number entirely; for now, when pull in a year, drop sequence number; removed VI for alignment with other years

### For making one large dataset
- Join per-year bulk files into one bulk file: (`awk '(NR ==1) || (FNR > 1)' hmda_* > hmda_all_bulk.csv`)

- Load up the entire bulk file; drop `sequence_number` (it's empty for 2017; this is the easiest thing to do); split off target from the df; save a features_df (which contains demographic info) and the target_df; Save 

### For splitting into year-state features, protected, target

- Use the `split_by_year_state.ipynb` to split up each `hmda_<year>_bulk.csv`
	- 2007 [DONE]
	- 2008 [DONE]
	- 2009 [DONE]
	- 2010 [DONE]
	- 2011 [DONE]
	- 2012 [DONE]
	- 2013 [DONE]
	- 2014 [DONE]
	- 2015 [DONE]
	- 2016 [DONE]
	- 2017 [DONE]
- Run `zip.sh` to walk through the data folder and zip each of the split files [TODO]
- Make sure that all data .csv files are in .gitignore [DONE]
- Put each year in its own repo [DONE]
- Move everything here into a `dev` branch; update `main` to have a new README [DONE]

## Old Cleaning Procedure (state/year-focused)

### Do once per raw year file
- Download the entire year of data to a cluster environment
- Unzip the data, and run the script `src/csv_split.sh` to divide the file into chunks. We used a chunk size of 100,000: From inside the directory where the splits will be created:

```
<path_to_script>/csv_split.sh <path_to_raw_data>/hmda_<year>_nationwide_all-records_labels.csv 100000 <year>
```

- Create a new directory for cleaning the resulting split files.

- On each output chunk csv file, we run `clean_split` in a python REPL (in `src/clean_split.py`) to drop columns that contain alphanumeric data (which has numeric codes in other columns), proxy variables, and rows that do not have state-specific information

```
import glob
import clean_split as clean
files = glob.glob("splits/split_*") # we stored the cleaned splits at this location
for f in files:
	clean.clean_split(f, "clean_splits/")
```

### Divide cleaned data into per-territory, per-year files

#### For a single territory

- We then filter each split to the specific state of interest. To do so, start a python REPL and run:

```
import glob
import clean_split as clean
files = glob.glob("clean_splits/split_*") # we stored the cleaned splits at this location
for f in files:
	clean.filter_state("NY", f, "NY/") # make sure the path exists; pick state of interest
```
#### For all territories at once

To do all at once, iterate through the territories list, then create directories based on that list, and use that information to clean:

- Get the unique territories for the year:
```
year = <>
import glob
import clean_split as clean
states = set()
files = glob.glob("{y}_clean_splits/split_*".format(y=year)) # we stored the cleaned splits at this location
for f in files:
	states.update(clean.unique_state(f))
```

- Create dirs for each of them:
```
import os
for s in states:
	os.mkdir("{s}/{y}".format(s=s, y=year))
```

```
i = 1
for s in states:
	print("{i}/{t}: Scrubbing {s}".format(s=s, i=i, t=len(states)))
	i += 1
	for f in files:
		clean.filter_state(s, f, "{s}/{y}/".format(s=s, y=year)) # make sure the path exists; pick state of interest
```

### Rejoining and finalizing files for the package

This final step is manual, per-territory (intentionally)

#### For a single territory

- We then rejoin the split-and-filtered files for the state of interest by going to the directory where the filtered files have been stored (above, `"NY/"`), and running `awk '(NR ==1) || (FNR > 1)' split_* > ny_all_<year>.csv` (pick your own output file name).


**Manual final check**: The last step is to clean the resulting state-year-specific data (above, `ny_all_<year>.csv`) to make sure there are no missing values, and to split into feature, target, and protected attribute files. This can be done locally with the `src/clean_state.ipynb` Jupyter notebook
