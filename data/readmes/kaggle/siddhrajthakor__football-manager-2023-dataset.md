# FM23 Complete Player Stats: 90k+ player records

Complete attributes for 90,000+ players from the FM23 database.

# Football Manager Players Dataset

## Overview
Dive into the ultimate treasure trove for football enthusiasts, data analysts, and gaming aficionados! The **Football Manager Players Dataset** is a comprehensive collection of player data extracted from a popular football management simulation game, offering an unparalleled look into the virtual world of football talent. This dataset includes detailed attributes for thousands of players across multiple leagues worldwide, making it a goldmine for analyzing player profiles, scouting virtual stars, and building predictive models for football strategies.

Whether you're a data scientist exploring sports analytics, a football fan curious about your favorite virtual players, or a game developer seeking inspiration, this dataset is your ticket to unlocking endless possibilities!

## Dataset Description
This dataset is a meticulously curated compilation of player statistics from five CSV files, merged into a single, unified dataset (`merged_players.csv`). It captures a diverse range of attributes for players from various clubs, nations, and leagues, including top-tier competitions like the English Premier Division, Argentina's Premier Division, and lower divisions across the globe.

### Key Features
- **Rich Player Attributes**: Over 70 columns covering essential metrics such as:
  - **Basic Info**: UID, Name, Date of Birth (DOB), Nationality, Height, Weight, Age
  - **Club & Position**: Club, Position (e.g., AM, DM, GK), Based (league/division)
  - **Performance Stats**: Caps, Appearances (AT Apps), Goals (AT Gls), League Appearances, League Goals
  - **Technical Skills**: Acceleration, Passing, Dribbling, Finishing, Tackling, and more
  - **Mental Attributes**: Work Rate, Vision, Leadership, Determination
  - **Physical Attributes**: Pace, Strength, Stamina, Agility
  - **Market Value**: Transfer Value (e.g., $0 to millions)
  - **Miscellaneous**: Preferred Foot, Media Handling, Injury Proneness
- **Global Coverage**: Players from diverse regions, including Europe (England, Spain, Italy), South America (Argentina, Brazil), Asia (South Korea, China), Africa (Ivory Coast, Burkina Faso), and North America (USA, Mexico).
- **Varied Player Types**: From young prospects (15–18 years old) to veteran stars (up to 45 years old), including amateurs, youth players, and professionals.
- **Realistic Insights**: Includes attributes like Media Description (e.g., "Young winger," "Veteran striker") and injury status, mirroring real-world football dynamics.

### Dataset Size
- **Rows**: Thousands of player records (exact count depends on deduplication).
- **Columns**: 70+ attributes per player.
- **File**: `merged_players.csv` (UTF-8 encoded for compatibility with special characters).

## Potential Use Cases
- **Sports Analytics**:
  - Analyze player attributes to identify key traits for success by position (e.g., what makes a top goalkeeper?).
  - Predict transfer values based on skills, age, and performance stats.
  - Cluster players by playing style or potential using machine learning.
- **Scouting & Strategy**:
  - Build a dream team by filtering players based on specific attributes (e.g., high Pace and Dribbling for wingers).
  - Compare young talents vs. experienced veterans for team-building strategies.
- **Gaming & Modding**:
  - Create custom Football Manager databases or mods.
  - Analyze game balance by studying attribute distributions.
- **Visualization**:
  - Develop interactive dashboards to explore player stats by league, nationality, or position.
  - Map player origins to visualize global football talent distribution.
- **Education & Research**:
  - Use as a teaching tool for data science, exploring data cleaning, merging, and analysis.
  - Study correlations between mental/physical attributes and in-game performance.

## Why This Dataset Stands Out
- **Comprehensive**: Covers every aspect of a player's profile, from technical skills to personality traits.
- **Diverse**: Includes players from top-tier to lower divisions, offering a broad spectrum of talent.
- **Engaging**: Perfect for football fans and data enthusiasts alike, blending gaming with real-world analytics.
- **Ready-to-Use**: Merged and cleaned for immediate analysis, with consistent column structure across all records.

## Getting Started
1. **Download**: Grab `merged_players.csv` and load it into your favorite tool (Python/pandas, R, Excel, etc.).
2. **Explore**: Check out columns like `Transfer Value`, `Position`, and `Media Description` to start your analysis.
3. **Analyze**: Use Python (e.g., pandas, scikit-learn) or visualization tools (e.g., Tableau, Power BI) to uncover insights.
4. **Share**: Build models, visualizations, or scouting reports and share your findings with the Kaggle community!

## Example Questions to Explore
- Which young players (&lt;18 years) have the highest potential based on attributes like Technique and Determination?
- How do transfer values correlate with attributes like Pace, Finishing, or Leadership?
- Can you identify undervalued players with high stats but low transfer fees?
- What are the most common attributes for top strikers vs. defenders?

## Notes
- **Data Cleaning**: Some fields (e.g., `Rc Injury`, `AT Apps`) may contain missing or placeholder values (`-`). Consider imputing or filtering as needed.
- **Duplicates**: Check for duplicate UIDs if you want unique player records (use `df.drop_duplicates(subset=['UID'])` in pandas).
- **Encoding**: The dataset uses UTF-8 to handle special characters in player names (e.g., José González, Yang Xiaofeng).

## Call to Action
⚽ **Kick off your data journey!** Download this dataset, dive into the world of virtual football, and uncover hidden gems. Whether you're scouting the next virtual Messi or analyzing global talent trends, this dataset has it all. **Upvote if you love football and data!** Share your insights, notebooks, or visualizations in the Kaggle community, and let's build the ultimate football analytics hub together!

출처: Kaggle (siddhrajthakor/football-manager-2023-dataset)
태그: video games, football, sports, exploratory data analysis, data analytics
라이선스: CC BY-SA 4.0
수정일: 2025-10-01T18:34:21.197Z
