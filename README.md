# slik_python_package
This README documents the steps that are necessary to get the slik package up and running. The slik package is a data to pre-modeling package; what this means is that every step of the way before Data Modeling is handled in this package. Steps like NaN handling, outlier detection and removal, scaling, normaization, etc. This package was built with the aim of helping Data Scientists navigate the difficulties of data pre-processing. slik is available on PyPi and can be pip installed from the terminal. See how to pip install below:

! pip install slik-preprocessing

### What is this repository for? ###

* Quick summary: The application employs the modular style of putting the applications together. In total, there are four modules which takes care of reading any type of file, data preprocessing (Nan, outliers, etc), and other preprocessing steps such as One Hot Encoding, Scaling, Normalization, PCA, etc. There is a general module (which is the general_utils module) that contains a list of global attributes and data used throughout the project. The order in which the modules were buildt is highlighted below:

- general_utils: this is where the file is read. Handles reading of CVS, Excel and parquet files with input columns specified. All that is required here is a file path
- preprocessing: this inherits the attributes of the general_utils and takes it a step further by automatically identifying the type of columns, handling NaN values and outliers
- pipeline: this module handles building a data pipeline with several considerations. For a start, you can either choose to scale or do normalization. This will be extended to other custom pipeline
- save_object: here is where the pipeline object is saved as a sparse matrix and can be fed into any machine learning model

* Version: 1.0
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up: ensure you have python 3 up and running
* Configuration: ensure all modules are imported properly. They all depend on each other
* Dependencies: python 3, pandas, scikit-learn, sklearn pre-processing
* Database configuration: no required configuration
* How to run tests: no tests files used yet. Version 2 will come with test cases
* Deployment instructions: To use this package, use the Savepipeline method (which requires a file path and input columns as input parameters) in save_object module and call the compile_functions. The final output is a csv file and a pickle pipeline object.

"README.md" 27L, 1205C
* Repo owner: afolabimkay@gmail.com
