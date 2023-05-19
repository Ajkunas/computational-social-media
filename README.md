# Sentiment analysis on ChatGPT tweets

Team :
- Barbara Ruvolo (barbara.ruvolo@epfl.ch)
- Ajkuna Seipi (ajkuna.seipi@epfl.ch) 
- Hongyi Shi (hongyi.shi@epfl.ch) 

## Datasets 

ChatGPT is a converastional artificial intelligence released since November 2022. On twitter, and on social media in general, the topic was and still is viral. 

Even though, the concept is revolutionary, it still raises multiple questions about ethic, privacy and security.
Thus, we will analyse the impact of the emergence of AI on the population, based on ChatGPT tweets. 

To do so, we will use some datasets from Kaggle. 
* https://www.kaggle.com/datasets/konradb/chatgpt-the-tweets
* https://www.kaggle.com/datasets/charunisa/chatgpt-sentiment-analysis
* https://www.kaggle.com/datasets/pcminh0505/chatgpt-twitter


## Data preprocessing 

To train our dataset, we first need to preprocess it. The main steps are: 
* Lower cases 
* Removing hyperlinks and html links 
* Removing hashtags and mentions 
* Removing emojis and special characters 
* Removing repeating words 
* Removing english stopwords 
* Removing punctuations 
* Removing short words
* Tokenize and normalize the dataset 

## Best model

The selected model is the CNN for sentiment analysis. 
The labeled dataset was trained and tested with the best model and we got an accuracy of 0.8. 

## Sentiment analysis

To predict the labels of the datasets, we trained the model with the labeled dataset and we used this pre-trained model for prediction (the pre-trained model is saved in `.h5`, but we could not pushed it in github because of the size of the file). 

The datasets pre-processed and predicted can be found in the folder `datasets/`. 

You can find the notebooks in the following drive for further training with other models and with the selected model: 
https://drive.google.com/drive/folders/1hOBFblE2JyF-w4dUEh-9epAOJ_-7rukF?usp=share_link

## Files 

In the root of the project: 

* `data_analysis.ipynb` : initial analysis of the datasets. 
* `data_preprocessing.ipynb` : the pre-processing functions used in the analysis and the pre-processing of the datasets can be found here. 
* `data_training.ipynb` : simulation of different models to select the best one. 
* `training.ipynb` : training of the labeled dataset with the best model, saving the pre-trained model. 
* `predict.ipynb` : sentiment analysis (prediction of the labels) of the pre-processed datasets. 
* `scientists_analysis.ipynb` : classifier to predict if the user is a scientist/researcher or not. Model trained and labeled predicted.

Inside the `datasets/` folder:

* `chatgptfirst.csv` : dataset containing the tweets of the first month of launch. 
* `sentiment.csv` : dataset containing the labeled tweets used for training.
* `preprocessed_sentiment.csv` : preprocessed labeled tweets.
* `preprocessed_chatgptfirst.csv` : preprocessed first month of launch tweets.
* `preprocessed_chatgpt2last.csv` : preprocessed two last months of tweets (march and april).
* `sentiment_chatgptfirst.csv` : sentiment prediction of first month of launch tweets.
* `sentiment_chatgpt2last.csv` : sentiment prediction of two last months of tweets (march and april). 
* `sample_user_descr.csv` : sample of 200 users description labeled with 1 and 0, where 1 means the user is a scientist/researcher and 0 means they are not.
* `sentiment_scientists.csv` : sentiment prediction of the tweets of only scientists/researcher. 

**Note** : the dataset used to extract the two months of tweets was not pushed into github because of the size of the file. It should be put locally in the repo for further use. 

