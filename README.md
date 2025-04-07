🎬 MovieMentor – A Content-Based Movie Recommendation System
MovieMentor is a personalized movie recommendation system that uses content-based filtering to suggest films tailored to individual user preferences. This part of the project focuses solely on the preprocessing stage — a vital step to prepare the dataset for building an efficient and accurate recommendation model.

🔧 Preprocessing Overview
1. Merging the Datasets
Two datasets, movies.csv and credits.csv, are merged based on the movie title. This ensures all relevant information such as overview, genres, cast, crew, and keywords is available in a single structured format.

2. Selecting Relevant Columns
Only the essential columns are retained for the recommendation system. These include:

Movie ID

Title

Overview

Genres

Keywords

Cast

Crew

Removing unnecessary columns helps reduce noise and improve performance.

3. Handling Missing Values
Rows with missing or null values in important fields are identified and removed to maintain data quality and avoid processing errors during model training.

4. Cleaning & Transforming Data
The metadata fields such as genres, keywords, cast, and crew are initially in complex nested structures. These are simplified by:

Extracting genre names

Selecting top cast members

Identifying the director from the crew

Splitting the movie overview into keywords

This makes the data usable for text-based similarity analysis.

5. Creating a Unified ‘Tags’ Column
To consolidate all important descriptive data, a new column called tags is created. It combines:

Overview

Genres

Keywords

Cast

Crew (Director)

This column represents the core content-based features for each movie in a single textual format.
