## Youtube 📺 Data Mining & Analysis 📈 End-End Data Engineering & Data Science Project 

### 📌 Demo app Link 

<a href="https://youtube-data-mining-analysis.streamlit.app/"><img src="https://camo.githubusercontent.com/767be70c92254555bd347ab07908fec67854c2264b77702581bd230fd7eac54f/68747470733a2f2f7374617469632e73747265616d6c69742e696f2f6261646765732f73747265616d6c69745f62616467655f626c61636b5f77686974652e737667"></a>

### 📌 Dataset Overview:
For this Project, I have used 2 Types of Data as mentioned below:
<ul>
<li> <b>Trending YouTube Video Statistics Data</b> which is taken from Kaggle.

**Data Link: https://www.kaggle.com/datasets/datasnaek/youtube-new**

<b>1. Csv File - </b>Each region’s data is in a separate file. Data includes the video title, channel title, publish time, tags, views, likes and dislikes, description, and comment count. <br>
<b>2. Json File -</b> Is in Key-Value format, where for each Region it has 30 nested K-V Pairs which include the id as a Primary Key and Channel_id & Category Name where the videos are categorized into different categories like Film & Animations, Sports, Science & Technology, Entertainment, Music & Many More etc. 

<li> <b>Youtube Data Scrapped via Youtube Data API </b> according to the search word entered by the user, for our case I have used as 'Data Science'
</ul>

### 📌 The Project is divided into 3 Parts: 🎯

🧩 **Real-Time User Authentication & Authorization via Firebase & Show/Post Posts via Firestore on Streamlit App** ⇢ [ Visit Streamlit_App Folder ]
<ul>
<li>Any User can First Sign Up with an Email, Password, and unique Username and then log in to the Web App - Make Sure that the Email and username are different for each User - at the Backend I have used Firebase.
<li>Users has the option to post their thoughts or Queries in Post Notes Space, also they can see other People's Posts & can delete their Posts according to their Need. I have used Firestore (No SQL Real Time Database) which stores the data in Documents [ Unique Username ] and it includes a Collection that has Post's ordered w.r.t User_ID for each User.
</ul>

🧩 **Analytic Platform with end - end ETL Data Pipeline For Trending YouTube Video Statistics via Aws Services** ⇢ [ Visit ETL_AWS Folder ]

Workflow Link: https://drive.google.com/drive/u/0/folders/19idDsEe7xafxWRVmEaYkRSfAbbYlmCbb

🧩 **Youtube Data Scrapping & Performing Data Wrangling, Pre-Processing, EDA & Text Mining - NLP Tasks on the Youtube Data to predict to which Category the Video Belongs!!** ⇢ [ Visit DataScrapping_Viz_Nlp_Tasks Folder ]

This Section is further divided into 2 Parts:

▶️ **Scrapping Youtube data, Pre-Processing, Wrangling, and Visualizing Data via different Charts & Graphs.**

⇢ Youtube data is scrapped by using Youtube Data API according to search Data Science & we have Attributes such as:
<ul>
<li> <b> For Different Channel's Data:</b>
Attributes s.a. Channel Name, subscribers, Total Views, Total Videos, Playlist ID
<li> <b> For each Channel Data:</b>
Attributes s.a. Video title, Video id, Video Description, Published date, Likes, Dislikes, Views, Comments
<li> After that I Performed Data Processing, Wrangling operations on the Data mentioned above & then Performed EDA (uni, Bi, Tri) Variate Data Visualization on the Cleaned Data
</ul>

📄🔍 **Text Mining - Performing NLP Tasks on the Youtube Statistics Data**

⇢ Predict the Category_id (Y) Based on Video_Title (X)
<ul>
<li> <b>Text Pre Processing 1 --</b> Tokenize [Sentences, Words] ➡️ Text Cleaning { Regex - remove Punctuations, Special Chars, extra white spaces} ➡️ Remove StopWords ➡️ Stemming & Lemmatization ➡️ POS Tagging ➡️ NER
<li> <b>Text Pre Processing 2 --</b> Word Embeddings { Ml Embeddings - BOW, TF-IDF, Word2Vec, DL Embeddings - LSTM/ Bi - Dir LSTM with Word Embeddings }
<li> Model Building & Training
<li> Evaluation and tuning of Parameters
<li> Comparing all the Word Embeddings Model
<li> At the end map the Category_id to 16 different Category Name s.a [ Film & Animations, Sports, Science & Technology, Entertainment, Music, News, Daily Vlogs ] etc.
</ul>

### Watch the Below Video for working of the App

[![Main_Page_ss](https://github.com/KunalAnand2907/Youtube_DataMining_Analysis-End-End-Data-Engineering-Data-Science-Project/assets/46574881/b480838d-991b-4387-994c-bb3c90e9a081)](https://youtu.be/GaeUzR9szVM)
