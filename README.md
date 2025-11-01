📽️ Movie Recommender System
An interactive movie recommendation app built with Streamlit, powered by content-based filtering using movie metadata and similarity scores.

🚀 Live Demo
👉 Click here to try it on Streamlit Cloud (https://movie-recommender-system-gpf7qy9d3wqgtga6x8yxek.streamlit.app/)

🧠 How It Works
Uses a precomputed similarity matrix based on movie features
Recommends top 5 similar movies for any selected title
Fetches movie posters using TMDB API for a rich visual experience
Clean UI built with Streamlit columns for responsive layout

📦 Tech Stack
Tool / Library	Purpose
Streamlit	UI and deployment
pandas, numpy	Data manipulation
scikit-learn	Similarity computation
requests	API calls for poster images
gdown	Loads large .pkl file from Google Drive
pickle	Loads precomputed similarity matrix

📁 Project Structure
Code
├── app.py                 # Streamlit app
├── movies.pkl            # Movie metadata
├── similarity.pkl        # Similarity matrix (loaded from Google Drive)
├── requirements.txt      # Dependencies
└── README.md             # Project overview
🛠️ Setup Locally
bash
git clone https://github.com/Tejcodings/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py
Note: similarity.pkl is loaded from Google Drive using gdown, so no need to download manually.

📌 Features
🎬 Choose any movie from the dropdown
🤖 Get 5 similar recommendations instantly
🖼️ View posters fetched dynamically via TMDB
☁️ Hosted on Streamlit Cloud for easy access

📣 Author
Tej — Independent Data Science Developer 🔗 GitHub Profile 💼 Actively seeking data science and ML engineer roles
