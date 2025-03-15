# Searchlyzer - SEO Data Analysis & Optimization

## Overview
Searchlyzer is a Python-based tool designed to analyze and optimize website performance using key SEO metrics. It processes data, assigns performance scores, predicts conversion rates using machine learning, and provides actionable insights for SEO improvement.

## Features
- **Data Conversion**: Transforms textual representations of figures (e.g., '2M', '3.5 billion') into numeric values for accurate analysis.
- **Point-Based Scoring System**: Evaluates websites based on metrics like monthly traffic, bounce rate, session duration, page load time, mobile friendliness, backlinks, and domain authority.
- **Machine Learning Predictions**: Utilizes a Random Forest Regressor to predict conversion rates based on SEO metrics.
- **Data Visualization**: Generates plots to visualize relationships between various SEO factors and website performance.
- **Optimization Recommendations**: Identifies areas for improvement and suggests actionable strategies to enhance SEO performance.

## Repository Structure
- **01 - Convert_to_numeric.py**: Contains functions to convert textual data representations into numeric values.
- **02 - PBS.py**: Implements the point-based scoring system for website evaluation.
- **03 - Forest_Regresson_Model.py**: Trains and applies a Random Forest model to predict conversion rates.
- **04 - Data_Visualization.py**: Produces visualizations to explore data relationships and trends.
- **05 - Final_suggestions.py**: Analyzes results and provides optimization recommendations.

## Technologies Used
- **Python**: Core programming language.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.
- **Scikit-Learn**: Machine learning modeling.
- **Matplotlib & Seaborn**: Data visualization.
- **Excel**: Data input and output.

## Getting Started
### 1. Clone the repository:
```bash
git clone https://github.com/elecxDev/Searchlyzer.git
cd Searchlyzer
```

### 2. Install dependencies:
Ensure you have Python installed. Then, install the required packages:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl
```

### 3. Prepare your data:
- Ensure your dataset is in Excel format (`.xlsx`) and matches the expected structure.
- Place your dataset in the project directory or update the file paths in the scripts accordingly.

### 4. Run the scripts in sequence:
#### Start with data conversion:
```bash
python "01 - Convert_to_numeric.py"
```
#### Proceed with the point-based scoring system:
```bash
python "02 - PBS.py"
```
#### Train and apply the Random Forest model:
```bash
python "03 - Forest_Regresson_Model.py"
```
#### Generate data visualizations:
```bash
python "04 - Data_Visualization.py"
```
#### Review final suggestions:
```bash
python "05 - Final_suggestions.py"
```

## Future Enhancements
- **Real-Time Data Integration**: Incorporate live data fetching from websites for up-to-date analysis.
- **Enhanced Machine Learning Models**: Experiment with other algorithms to improve prediction accuracy.
- **User-Friendly Interface**: Develop a GUI or web-based interface for easier interaction.

## License
Searchlyzer is a **source-available** project. The code is open for personal and research use, but commercial usage requires permission. See the LICENSE file for details.

## Contact
For business inquiries or licensing, feel free to reach out via email: **[elecdev.business@gmail.com](mailto:elecdev.business@gmail.com)**. Companies interested in implementing Searchlyzer can contact me directly.
