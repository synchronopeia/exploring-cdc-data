# Exploring CDC Data

## Description

Start simple and gradually build up to something significant!

## Requirements

1) The CSV-based datasets are __NOT__ included in this repository. You must download and store them locally (but not in this project directory).
2) We are using data for _United States COVID-19 Cases and Deaths by State over Time_ available at (https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36)[data.cdc.gov].
3) You must create a .env file in this project directory. It must specify an environment variable DATASET_DIR with the path to your local directory where the CDC data files are being kept. For example:

```
DATASET_DIR=~/datasets/cdc
```

## TDOD

- [x] Start project (this README).
- [ ] Onboard Allison and confirm ```quick_look.py``` works.

### Fields

| submission_date | Date of counts | Date & Time
| --- | --- | --- |
| state  | Jurisdiction | Plain Text |
| tot_cases  | Total number of cases | Number |
| conf_cases  | Total confirmed cases | Number |
| prob_cases  | Total probable cases | Number |
| new_case  | Number of new cases | Number |
| pnew_case  | Number of new probable cases | Number |
| tot_death  | Total number of deaths | Number |
| conf_death  | Total number of confirmed deaths | Number |
| prob_death | Total number of probable deaths | Number |
| new_death  | Number of new deaths | Number |
| pnew_death | Number of new probable deaths | Number |
| created_at | Date and time record was created | Date & Time |
| consent_cases | If Agree, then confirmed and probable cases are included. If Not Agree, then only total cases are included. | Plain Text |
| consent_deaths | If Agree, then confirmed and probable deaths are included. If Not Agree, then only total deaths are included. | Plain Text |
