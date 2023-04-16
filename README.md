# Sentiment analysis on ChatGPT tweets

Team :
- Barbara Ruvolo (barbara.ruvolo@epfl.ch)
- Ajkuna Seipi (ajkuna.seipi@epfl.ch) 
- Hongyi Shi (hongyi.shi@epfl.ch) 

## Datasets 

ChatGPT is a converastional artificial intelligence released since November 2022. 
On twitter, and on social media in general, the topic was and still is viral. 

Eventhough, the concept is revolutionary, it still raises multiple questions about ethic, privacy and security.
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

## Features conversion 

To train text, we need to vectorize them and give them a mathematical meaning. To achieve this, we compare three feature conversion techniques: 
* Bag Of Words 
* TIF-IDF
* Word2Vec 

## Training 

To select the best model with the best achievable accuracy and F1 score, we compare different models: 
* Logistic Regression 
* SVM 
* Random Forest
* CNN 

You can find the notebooks in the following drive for further training: 
https://drive.google.com/drive/folders/1hOBFblE2JyF-w4dUEh-9epAOJ_-7rukF?usp=share_link
