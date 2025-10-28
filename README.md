# 🎬 MovieMentor – A Content-Based Movie Recommendation System

**MovieMentor** is a personalized movie recommendation system that uses **content-based filtering** to suggest films tailored to individual user preferences.  
This section focuses on the **preprocessing stage**, which prepares the dataset for building an efficient and accurate recommendation model.

---

## 🔧 Preprocessing Overview

### 📌 1. Merging the Datasets
Two datasets – `movies.csv` and `credits.csv` – are merged using the **movie title** as the key.  
This ensures that information such as **overview, genres, cast, crew, and keywords** is unified into a single structured dataset.

---

### 📌 2. Selecting Relevant Columns
Only the essential columns are retained for the recommendation engine. These include:

- 🎥 `movie_id`  
- 🎞️ `title`  
- 📝 `overview`  
- 🎭 `genres`  
- 🗝️ `keywords`  
- 👥 `cast`  
- 🎬 `crew`  

Removing unnecessary columns reduces noise and improves the performance of the recommendation system.

---

### 📌 3. Handling Missing Values
Rows with **missing or null values** in key fields are identified and removed.  
This ensures high-quality data and prevents errors during feature extraction and model building.

---

### 📌 4. Cleaning & Transforming Data
Many of the metadata fields (like `genres`, `keywords`, `cast`, and `crew`) are stored as nested structures. These are cleaned and simplified by:

- ✅ Extracting names from the **genres** and **keywords** fields  
- ✅ Selecting the top **3 cast members** from the cast list  
- ✅ Extracting the **director's name** from the crew  
- ✅ Splitting the `overview` into individual words (tokens)  

This transformation makes the data suitable for **text-based similarity analysis**.

---

### 📌 5. Creating a Unified `tags` Column
To consolidate all descriptive features of a movie, a new column called `tags` is created. It combines:

- 📝 Overview  
- 🎭 Genres  
- 🗝️ Keywords  
- 👥 Cast  
- 🎬 Crew (Director)  

This column serves as the **core feature** for content-based recommendations, containing all essential textual information in a single place.

---

### 📌 6. Final Cleaned DataFrame
The final preprocessed DataFrame includes:

- 🎥 `movie_id`  
- 🎞️ `title`  
- 🏷️ `tags`  

This dataset is now ready for **vectorization** and **similarity calculations** using NLP techniques like **TF-IDF** and **cosine similarity**.

---

✨ **Next Step:**  
Creating a user interactive front-end using streamlit and it is still in prooduction stage.

---

![WhatsApp Image 2025-10-28 at 14 29 47_aa9ef734](https://github.com/user-attachments/assets/d6514ec8-85ba-416d-a58a-764d2c9ebb55)
