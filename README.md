# Anime-Recommendation
This Python script implements a simple anime recommendation system that suggests similar animes based on user input. Leveraging TF-IDF Vectorization and Cosine Similarity, the system analyzes a dataset containing anime names, genres, and types. Users input their favorite anime, and the script identifies close matches using the difflib library. The recommendation algorithm calculates similarity scores and presents a list of animes ranked by their similarity to the user's input. The project employs pandas for data manipulation, scikit-learn for TF-IDF Vectorization, and difflib for finding close matches. Whether you're an anime enthusiast or a Python developer looking to explore recommendation systems, this project provides a simple yet effective example.
## Getting Started

### Prerequisites

- Python 3.12
- Required Python packages can be installed using the following command:

```bash
pip install pandas scikit-learn
```

### Installation
1. Clone the repoaitory
```bash
git clone https://github.com/Mrinal-exe/Anime-Recommendation.git
```
2. Navigate to the project directory
```bash
cd Anime-Recommendation
```
3. Run the script
```bash
python main.py
```
### Usage
1. Enter your favorite anime when prompted.
2. The system will find close matches and suggest similar animes based on TF-IDF Vectorization and Cosine Similarity.

### Dataset 
The recommendation system uses anime data from the "anime.csv" file. The dataset includes information about anime names, genres, and types. The dataset was found on [Kaggle](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database/data).

### Customization
You can customize the recommendation system by modifying the script or using a different dataset.

### Acknowledgments
The recommendation system is built using pandas, scikit-learn, and difflib.
