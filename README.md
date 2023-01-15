# HMDA Data

This repository contains the scripts used to pre-process the HMDA dataset, as well as the library toolkit for accessing and manipulating subsets of the data.

Related links:

- [Raw data for 2007-2017](https://www.consumerfinance.gov/data-research/hmda/historic-data/?geo=nationwide&records=all-records&field_descriptions=labels)
- [Record format](https://files.consumerfinance.gov/hmda-historic-data-dictionaries/lar_record_format.pdf)
- [Associated record numeric codes](https://files.consumerfinance.gov/hmda-historic-data-dictionaries/lar_record_codes.pdf)

## Cleaning procedure

### Do once per raw year file [DONE]
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

### Cleaning into per-territory files [IN PROGRESS]

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

### Rejoining and finalizing files for the package [IN PROGRESS]

This final step is manual, per-territory (intentionally)

#### For a single territory

- We then rejoin the split-and-filtered files for the state of interest by going to the directory where the filtered files have been stored (above, `"NY/"`), and running `awk '(NR ==1) || (FNR > 1)' split_* > ny_all_<year>.csv` (pick your own output file name).


**Manual final check**: The last step is to clean the resulting state-year-specific data (above, `ny_all_<year>.csv`) to make sure there are no missing values, and to split into feature, target, and protected attribute files. This can be done locally with the `src/clean_state.ipynb` Jupyter notebook


## Current status

- Download all data [DONE]
	- 2017 [DONE] 
	- 2016 [DONE] 
	- 2015 [DONE] 
	- 2014 [DONE] 
	- 2013 [DONE] 
	- 2012 [DONE] 
	- 2011 [DONE] 
	- 2010 [DONE] 
	- 2009 [DONE] 
	- 2008 [DONE] 
	- 2007 [DONE] 
- Split all data [DONE]
	- 2017 [DONE] 
	- 2016 [DONE] 
	- 2015 [DONE] 
	- 2014 [DONE] 
	- 2013 [DONE] 
	- 2012 [DONE] 
	- 2011 [DONE]  
	- 2010 [DONE] 
	- 2009 [DONE] 
	- 2008 [DONE]  
	- 2007 [DONE] 
- Bulk clean all data [DONE]
	- 2017 [DONE]
	- 2016 [DONE]
	- 2015 [DONE]
	- 2014 [DONE]
	- 2013 [DONE]
	- 2012 [DONE]
	- 2011 [DONE]
	- 2010 [DONE]
	- 2009 [DONE]
	- 2008 [DONE]
	- 2007 [DONE]
- Bulk scrub all data [IN PROGRESS]
	- 2017 [DONE]
	- 2016 [DONE]
	- 2015 [DONE]
	- 2014 [DONE]
	- 2013 [DONE]
	- 2012 [DONE]
	- 2011 [IN PROGRESS]
	- 2010 [IN PROGRESS]
	- 2009 [IN PROGRESS]
	- 2008 [IN PROGRESS]
	- 2007 [IN PROGRESS]
- Rejoining and manual finalization [IN PROGRESS]
	- 2017 [IN PROGRESS] (53 territories)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': **DONE**, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': **DONE**, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': **DONE**, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': **DONE**, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2016 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2015 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2014 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2013 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2013 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2011 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2010 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2009 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO

	- 2008 [TODO] (52 territories; no VI)
		
		'AK': TODO, 'AL': TODO, 'AR': TODO, 'AZ': TODO, 'CA': TODO, 'CO': TODO, 'CT': TODO, 'DC': TODO, 'DE': TODO, 'FL': TODO, 'GA': TODO, 'HI': TODO, 'IA': TODO, 'ID': TODO, 'IL': TODO, 'IN': TODO, 'KS': TODO, 'KY': TODO, 'LA': TODO, 'MA': TODO, 'MD': TODO, 'ME': TODO, 'MI': TODO, 'MN': TODO, 'MO': TODO, 'MS': TODO, 'MT': TODO, 'NC': TODO, 'ND': TODO, 'NE': TODO, 'NH': TODO, 'NJ': TODO, 'NM': TODO, 'NV': TODO, 'NY': TODO, 'OH': TODO, 'OK': TODO, 'OR': TODO, 'PA': TODO, 'PR': TODO, 'RI': TODO: TODO, 'SC': TODO, 'SD': TODO, 'TN': TODO, 'TX': TODO, 'UT': TODO, 'VA': TODO, 'VI': TODO, 'VT': TODO, 'WA': TODO, 'WI': TODO, 'WV': TODO, 'WY': TODO


TODO: in the toolkit version / bulk files, 
TODO: keep applicant demographic info separate, but munge back in as needed
TODO: binarize co-applicant info, as needed
TODO: tooling for action_taken, as needed
TODO: tooling for pulling in raw vs. removing NaNs, as needed

I will put all of our processing scripts on a dev branch when this is done, and then work to finish tthe software toolkit for accessing the cleanly pre-processed data as dataframes. I will then register main as a PyPI package, so that using the dataframes in future research is as easy as pip installing this package and running a few lines of code. It is this package that ideally I would want to integrate with Fairlearn, if there is interest.
