# Election 2024: From polling to predictions

## Overview of the Project

This repo documents the steps and processes used in creating the paper "Predicting the 2024 U.S. Presidential Election: A Data-Driven Analysis of Swing State Outcomes". Taking polling data from  (FiveThirtyEight)[https://projects.fivethirtyeight.com/polls/president-general/2024/national/] and using it to model the result of the US election. his is don using Python and it's packages to model and display the data.

Use this folder to reproduce the results on your own.

Note on LLM usage: 
LLMs were used, GPT 4 was used as an a coding assistant to the data cleaning, modeling and graph generating aspect of this paper. The Chat has been pasted in the `other` section of the files.

## File Structure

The repo is structured as:

-   `data` contains the data sources used in analysis including the raw data.
-   `models` contains the model that was used in predicting the outcome of the election
-   `other` contains miscelaninous files, including the LLM documentation, and our pre-analysis data/graph sketches 
-   `scripts` contains the Python scripts used to simulate, download and clean data.
-   `paper` contains our bibtex bibliography, as well as the final paper and the qmd document that renders the paper. 

## Reproducability

In Order to run code in this repository first be sure to download th required packages to your local enviroment, using the following code `pip install -r requirements.txt`.