# FakeNewsDetectionSystem

## Objective 
It is a web application deployed on Heroku that predicts whether a particular news item is real or fake.

## Technologies used
1. Python==3.9.1
2. jupyterlab==3.0.0
3. HTML5
4. CSS3
5. Flask 1.1.2

## Dataset used
The dataset has been taken from the following source:  [Kaggle dataset link](https://www.kaggle.com/c/fake-news/data?select=train.csv)
The dataset contains three .csv files - *train.csv* ,  *test.csv*   and   *submit.csv*.
The train.csv files contains the data upon which we train our model. It contains 20800 records, each having 5 attributes- namely: id, title, author, text, label.
The test.csv files contains the data upon which we test our model. It contains 5200 records, each having 4 attributes- namely: id, title, author, text.

## General outline
1. Download the dataset.
2. Process / Prepare the data.
3. Basic data exploration.
4. Train and test the model.
5. Create a pipeline.
6. Create a flask that uses this pipeline and makes predictions 
7. Deploy the app to Heroku 

## How to set up the project
1. Install Python: 

This setup requires that your machine has python 3.9 installed in it. Download Pythom from [here](https://www.python.org/downloads/).
In order to run Python directly, set up the PATH variables. 

2. Install jupyter-lab

```pip install jupyterlab```

3. You will also need to download and install the packages below using pip.

```pip install sklearn```

```pip install nltk```

```pip install wordcloud```

```pip install seaborn```

4. To install flask 
```pip install flask```

5. Open Terminal and go to the App folder and type 
``` flask run```
This will give you the link to the local server : http://127.0.0.1:5000/

6. Copy and paste the local server link on your web browser to run the app.

## Screenshots

![alt text](https://github.com/arishta/FakeNewsDetectionSystem/blob/main/screeenshots/user_search.PNG)
![alt text](https://github.com/arishta/FakeNewsDetectionSystem/blob/main/screeenshots/output.PNG)


## Heroku app link
[FakeNewsDetectionSystem](https://fakenewsdetector001.herokuapp.com/)


