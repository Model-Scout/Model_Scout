# LCK Spring 2024 Players Statistics

Comprehensive player, champion, and match data from LCK Spring 2024

This dataset provides an in-depth look at the League of Legends Champions Korea (LCK) Spring 2024 season. It includes detailed metrics for players, champions, and matches, meticulously cleaned and organized for easy analysis and modeling.

# Data Collection

The data was collected using a combination of manual efforts and automated web scraping tools. Specifically:

Source: Data was gathered from Gol.gg, a well-known platform for League of Legends statistics.
Automation: Web scraping was performed using Python libraries like BeautifulSoup and Selenium to extract information on players, matches, and champions efficiently.
Focus: The scripts were designed to capture relevant performance metrics for each player and champion used during the Spring 2024 split.

# Data Cleaning and Processing
The raw data obtained from web scraping required significant preprocessing to ensure its usability. The following steps were taken:

# Handling Raw Data:
Extracted key performance indicators like KDA, Win Rate, Games Played, and Match Durations from the source.
Normalized inconsistent formats for metrics such as win rates (e.g., removing %) and durations (e.g., converting MM:SS to total seconds).

# Data Cleaning:
Removed duplicate rows and ensured no missing values.
Fixed inconsistencies in player and champion names to maintain uniformity.
Checked for outliers in numerical metrics (e.g., unrealistically high KDA values).

#Data Organization:

Created three separate tables for better data management:

Player Statistics: General player performance metrics like KDA, win rates, and average kills.
Champion Statistics: Data on games played, win rates, and KDA for each champion.
Match List: Details of each match, including players, champions, and results.
Added sequential Player IDs to connect the three datasets, facilitating relational analysis.
Date Formatting:
Converted all date fields to the DD/MM/YYYY format for consistency.
Removed irrelevant time data to focus solely on match dates.

# Tools and Libraries Used
The following tools were used throughout the project:

**Python:
Libraries: Pandas, NumPy for data manipulation; BeautifulSoup, Selenium for web scraping.**
**Visualization: Matplotlib, Seaborn, Plotly for potential analysis.**
**Excel:**
Consolidated final datasets into a structured Excel file with multiple sheets.
**Data Validation:**
Used Python scripts to check for missing data, validate numerical columns, and ensure data consistency.
**Kaggle Integration:**
Cleaned datasets and a comprehensive README file were prepared for direct upload to Kaggle.

# Applications

This dataset is ready for use in:
Exploratory Data Analysis (EDA):
Visualize player and champion performance trends across matches.
Machine Learning:
Develop models to predict match outcomes based on player and champion statistics.
Sports Analytics:
Gain insights into champion picks, win rates, and individual player strategies.

# Acknowledgments
This dataset was made possible by the extensive statistics available on Gol.gg and the use of Python-based web scraping and data cleaning methodologies. It is shared under the CC BY 4.0 License to encourage reuse and collaboration.

출처: Kaggle (lukasrozado/lck-spring-2024-players-statistics)
태그: games, video games, computer science, programming, exploratory data analysis, data cleaning, python
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2024-12-01T15:02:54.620Z
