
# 🎮 Steam Game Recommendation System

This project builds a recommendation engine for Steam games using user-tag data and game metadata. It leverages both content-based and collaborative filtering techniques to generate accurate and personalized game suggestions. The project is deployed as an interactive web application using **Streamlit**.

---

## 🗂️ Project Structure

```
├── DataSets/              # Raw and processed datasets
│   └── Raw/               # Original Steam data files (CSV)
├── Models/                # Saved recommendation models (PKL)
├── Notebooks/             # Jupyter notebooks for EDA and modeling
├── Outputs/               # Graphs, analysis results, and visualizations
├── Scripts/               # Python scripts for data processing and model training
├── src/                   # Core modules for data loading and recommendation
├── app/                   # Streamlit app files
│   ├── pages/             # Multi-page structure of the Streamlit app
├── requirements.txt       # Dependencies and package list
├── README.md              # Project documentation
└── LICENSE                # License information
```

---

## 🔧 Technologies Used

* **Python**: Core programming language.
* **Pandas, NumPy**: Data manipulation and analysis.
* **Matplotlib, Seaborn**: Data visualization.
* **Scikit-learn**: Machine learning models and evaluation.
* **Surprise**: Collaborative filtering library.
* **TF-IDF**: For content-based filtering.
* **Streamlit**: Interactive web application framework.

---

## 🚀 How to Run

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/username/steam-game-recommender.git
   cd steam-game-recommender
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:

   ```bash
   streamlit run app/app.py
   ```

4. **Explore the Jupyter Notebooks**:

   * Open and run the notebooks inside the `Notebooks/` directory:

     * `01_eda.ipynb`: Exploratory Data Analysis.
     * `02_collaborative_filtering.ipynb`: User-based recommendations.
     * `03_hybrid_recommender.ipynb`: Hybrid recommendation model.

---

## 🎯 Project Goals

* **Personalized Recommendations**: Suggest games that align closely with the user’s preferences, play history, and favorite genres.
* **Multi-Model Approach**: Combine content-based and collaborative filtering for accurate and diverse recommendations.
* **Interactive Visualization**: Present analytical insights through interactive charts and graphs.
* **Scalable Design**: Easily extendable with real-time data from Steam API.

---

## 📊 Machine Learning Models

### Content-Based Filtering

* Uses **TF-IDF Vectorization** to represent game metadata.
* Measures similarity using **Cosine Similarity**.
* Suitable for recommending similar games based on genres, tags, and descriptions.

### Collaborative Filtering (User-Based)

* Uses **Surprise Library** for building user-item interaction matrices.
* Predicts user preferences by identifying similar users.
* Suitable for personalized recommendations when sufficient user data is available.

### Hybrid Recommendation System

* Combines content-based and collaborative approaches.
* Uses a weighted average to blend both recommendation scores.
* Balances game metadata with user interaction data for more precise suggestions.

---

## 💻 Streamlit App Features

* **Home Page**: Introduction and navigation.
* **Recommendations**: Get personalized game suggestions based on selected game.
* **Analytics**: Visualize game trends, genre distributions, and player insights.
* **Search**: Find detailed information about any game.
* **Overview**: Summary and statistics of the game dataset.

---

## ✨ Key Features

* **Multi-Filter Options**: Filter recommendations by genre, rating, and price.
* **Game Search**: Quickly find any game and view its details.
* **Interactive Visualizations**: Genre distribution, rating analysis, and playtime metrics.
* **Customizable Recommendations**: Adjust the balance between content and collaborative filtering.

---

## 🌟 Future Improvements

* **Real-Time Data**: Integrate with the Steam API for live recommendations.
* **Deep Learning Models**: Implement neural collaborative filtering.
* **Enhanced UI/UX**: Add more customization and sorting options.
* **User Authentication**: Save favorite games and personalized settings.

---

## 📂 Dataset Information

* **Steam Game Data**: Includes game name, release date, ratings, price, genres, and developer.
* **Similarity Matrices**: Precomputed cosine similarity matrices for efficient recommendations.

---

## 💡 Why This Project Matters

The Steam Game Recommender provides gamers with a robust way to discover new games based on their interests. By leveraging both user behavior and game metadata, the system generates recommendations that are both relevant and diverse. The interactive web interface makes it easy to explore game suggestions and insights, offering a user-friendly experience.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.
