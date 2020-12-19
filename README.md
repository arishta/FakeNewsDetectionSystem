# FakeNewsDetectionSystem

## Objective 
It is a web application that predicts whether a particular news item is real or fake.

## GENERAL OUTLINE
1. Download the dataset.
2. Process / Prepare the data.
3. Basic data exploration.
4. Train and test the model.
5. Create a pipeline.

## Dataset used
The dataset has been taken from the following source:  [Kaggle dataset link](https://www.kaggle.com/c/fake-news/data?select=train.csv)
The dataset contains three .csv files - *train.csv* ,  *test.csv*   and   *submit.csv*.
The train.csv files contains the data upon which we train our model. It contains 20800 records, each having 5 attributes- namely: id, title, author, text, label.
The test.csv files contains the data upon which we test our model. It contains 5200 records, each having 4 attributes- namely: id, title, author, text.

## Technologies used
1. Python
2. Jupyter-lab

## Pre-requisites
1. Python 3.6

This setup requires that your machine has python 3.9 installed in it. Download Pythom from [here](https://www.python.org/downloads/).
In order to run Python directly, set up the PATH variables. 

2. jupyter-lab

To install jupyter lab 

```pip install jupyterlab```

3. You will also need to download and install the packages below using pip.

```pip install sklearn```

```pip install nltk```

```pip install wordcloud```

```pip install seaborn```
