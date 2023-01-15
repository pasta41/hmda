# Home Mortgate Disclosure Act (HMDA) data set toolkit

This is an open-source toolkit that makes the HMDA datasets easy to use and accessible for research purposes. The author created this package as part of a [project](https://arxiv.org/abs/2301.11562) on variance in algorithmic fairness. More information can also be found at [arbitrar.ai](https://arbitrar.ai) 

This toolkit is under active development, and should currently be considered in alpha status. Development of this package, as well as how to use it, is described below.

## Citation information

If you make use of these datasets, please cite both of the following:

```
@misc{cooper2023variance,
      title={{Variance, Self-Consistency, and Arbitrariness in Fair Classification}}, 
      author={A. Feder Cooper and Solon Barocas and Christopher De Sa and Siddhartha Sen},
      year={2023},
      eprint={2301.11562},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

```
@misc{ffiec2022housingdata,
	  author = {{Federal Financial Institutions Examination Council}},
      institution={Consumer Financial Protection Bureau},
      title ={{HMDA Data Publication}},
      year = {2017},
      note = {Released due to the Home Mortgage Disclosure Act},
      url = {https://www.consumerfinance.gov/data-research/hmda/historic-data/}
}
```

## Project Status

- **alpha**: The entire 2007-2017 datasets have been cleaned, processed, and made available at public links [CURRENT]

- **beta**: The datasets can be accessed and manipulated via a python API (in progress; expected June 1, 2023)

- **1st major release**: The project is available in PyPI (future work; expected July 1, 2023)


## alpha 

The datasets are available in different repositories, according to year. Each repository has data for 52 states and territories (the 50 US states, Puerto Rico, and the District of Columbia). Each state has its own folder, which contains 3 zip files: 

- `<year>-<territory>-features.zip`: The core feature set
- `<year>-<territory>-protected.zip`: Corresponding demographic attributes
- `<year>-<territory>-target.zip`: Corresponding information about the action taken

We will fill out more information about the schema during the beta release. For now, please refer to the following related links:

- [Raw data for 2007-2017](https://www.consumerfinance.gov/data-research/hmda/historic-data/?geo=nationwide&records=all-records&field_descriptions=labels)
- [Record format](https://files.consumerfinance.gov/hmda-historic-data-dictionaries/lar_record_format.pdf)
- [Associated record numeric codes](https://files.consumerfinance.gov/hmda-historic-data-dictionaries/lar_record_codes.pdf)


### Data repositories 

- [2007](https://github.com/pasta41/hmda-data-2007)
- [2008](https://github.com/pasta41/hmda-data-2008)
- [2009](https://github.com/pasta41/hmda-data-2009)
- [2010](https://github.com/pasta41/hmda-data-2010)
- [2011](https://github.com/pasta41/hmda-data-2011)
- [2012](https://github.com/pasta41/hmda-data-2012)
- [2013](https://github.com/pasta41/hmda-data-2013)
- [2014](https://github.com/pasta41/hmda-data-2014)
- [2015](https://github.com/pasta41/hmda-data-2015)
- [2016](https://github.com/pasta41/hmda-data-2016)
- [2017](https://github.com/pasta41/hmda-data-2017)
