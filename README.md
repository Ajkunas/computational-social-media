# Project for the Computational Social Media course

Team :
- Barbara Ruvolo (barbara.ruvolo@epfl.ch)
- Ajkuna Seipi (ajkuna.seipi@epfl.ch) 
- Hongyi Shi (hongyi.shi@epfl.ch) 

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

To select the best model with the best achievable accuracy, we compare different models: 
* Logistic Regression 
* SVM 
* Random Forest 
* KNN 
* CNN 

You can find the notebooks in the following drive for further training: 
https://drive.google.com/drive/folders/1hOBFblE2JyF-w4dUEh-9epAOJ_-7rukF?usp=share_link
