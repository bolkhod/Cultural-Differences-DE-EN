# Cultural Differences and Similarities in Perceptions of Artificial Social Agents (ASAs) - German version

## Summative round

**Author**: Boleslav Khodakov
**Date**: June 2023

**Contributors**: Bolek Khodakov, Emma Bokel, Nele Albers, Andrea Bönsch, Jonathan Ehret, and Willem-Paul Brinkman.

**OSF form for this part:** https://osf.io/g3729
**OSF form for previous part:** https://osf.io/adknw

**This codebase is based on code from:** Fengxiang Li

**This is a follow-up folder. For data pre-processing, and data files please go to the transformation folder.**

This file is meant to guide you through the steps to go through the evaluation (e.g. ICC values for items/constructs) of transformed data for the summative round.

Due to time constraints, the data transformed and analyzed in these files is only based on the first data collected between the 19th and 22nd of June. We are still aiming for 120 participants per questionnaire part for future work. In the first group  we collected from 72 bilingual participants with German primary tongue who are fluent German and fluent English speakers. In the second group, human-ASA interaction evaluation data of the last 46 items were collected from 82 bilingual participants with German primary tongue who are fluent German and fluent English speakers. The amount was artificially reduced to 72, since this codebase requires the two halves to have an equal amount of rows. Currently, data of 144 (72 per each half) participants is analyzed.

Out of 144 participants (72 per questionnaire), 141 recommended using their data. We use _all_ participants' (144) data for the evaluation, however.

### Explanation of what was done

The files in this section were used to calculate item-level ICC values, construct-level ICC values, variation between English and German ASA questionnaires, and to compare human-ASA interactions between different Cultural Backgrounds. Data was acquired from the survey platform Qualtrics, while recruiting participants for the study was done via Prolific. 
Two surveys were created (to reduce fatigue of participants) - the first and second halves of the ASA questionnaire items, with their respectful translations. Data from these surveys was first pre-processed. Herewith, the data was firstly redundantly checked (e.g. for passing attention checks), then unnecessary columns (e.g. attention checks) were removed, leaving only columns of question items (English and German).
The question items were of both halves were combined, and their ICC values were calculated. 

There were 14 attention checks (in each of the two surveys), which participants had to pass for their data to be valid. 7 are in English, 7 are in German.
In the survey, we asked participants on whether they recommend using their data for research purposes. We use _all_ participants' data for the evaluation, however.

### Examine Output of Code Run by Us

To see the transformation of qualtrics data into the format used for ICC calculation, access the files `Data Transformation Summative first half` (`.pdf` or `.rmd`) and `Data Transformation Summative second half` (`.pdf` or `.rmd`).
To see the calculation of ICC values, access the file `ICC calculation Summative` (`.pdf` or `.rmd`).

### Run Code Yourself

This section is to explain how you can run the code yourself.

#### Requirements

You need to have the R programming language installed. Version 4.2.3 was used for this study. We recommend using RStudio to view the `.rmd` files. The `.rmd` files contain code chunks which list/install the necessary dependencies. Some of these are commented out (else they install the dependency each time).

#### Steps to Reproduce Analyses

The reproduction of our code is based on RStudio. Take the following steps:

1. Make sure you have R installed. 
2. Open the file `ICC calculation Summative.rmd`. Run the file's contents. The file should access `summative_first_half_transformed.sav` and `summative_second_half_transformed.sav` and `data_culture_EN_DE.sav`. 
3. Once run, `ICC calculation Summative.rmd` will print the ICC values of individual items, the Grand Mean, Standard Deviation, Minimum and Maximum ICC values, and other analyses. We recommend knitting the `.rmd` files to PDF, if you want to save this data: The PDF  contains code, comments and printed analysis values.

#### A note on knitting R Markdown

Knitting the `.rmd` files into `.pdf` files requires `.tex` and `.bib` files. These are present in the current directory.  Data files needed for the `.rmd` code chunks are also present in this directory.

You may want to install dependencies present in the first code chunk of the `.rmd` file you wish to knit. If you have these installed, pressing the `knit` button in Rstudio should knit your file to PDF.

### Explanation of Files

Please note: The `.rmd` files contain extensive comments.

This directory contains the following files and folders:

- `README.md` and `README.pdf`: Short explanations of how to use files in current folder, and what those files are.
- `ICC calculation Summative.rmd/pdf`: Analysis of the pre-processed data.