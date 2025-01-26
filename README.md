# Retail Inventory Optimization

This project was developed as part of the **Business Intelligence and Database Management Capstone Project (IT 300)** at Tunis Business School. The goal is to create a Business Intelligence (BI) solution to optimize retail inventory, improve operational efficiency, and support strategic decision-making through actionable insights.

---

## 🚀 Features

- **Data Integration**: Processes and integrates data from various sources, including sales records, inventory logs, and promotional data.
- **Interactive Dashboards**: Visualizes key metrics such as sales trends, inventory levels, and promotional performance using Tableau.
- **Predictive Analytics**: Utilizes demand forecasting to maintain optimal inventory levels and prevent overstocking or stockouts.
- **Scalable Data Warehouse**: Implements a star schema for efficient data storage and analysis.
- **ETL Pipeline**: Automates data extraction, transformation, and loading for seamless processing.

---

## 📂 Project Structure

1. **Data Collection**: 
   - **Sources**: Retail sales data from [Kaggle](https://www.kaggle.com/datasets/balusami/retail-inventory-optimization), merged with additional store and product details.
   - **Formats**: CSV, JSON, and SQL.
   
2. **ETL Process**:
   - **Extract**: Reads raw data into pandas DataFrames.
   - **Transform**: Cleanses data by handling missing values, removing duplicates, and standardizing formats.
   - **Load**: Stores the processed data in a SQL-based data warehouse.

3. **Data Modeling**:
   - **Star Schema**: Includes fact tables for sales and dimension tables for stores, products, and time.
   - **Data Marts**: Optimized subsets for targeted business analysis.

4. **Data Analysis**:
   - **Store Performance**: Analyzes sales trends and inventory levels.
   - **Product Performance**: Identifies top-performing products and evaluates promotional impacts.
   - **Demand Analysis**: Forecasts demand and analyzes city-based trends.

---

## 💻 Code Overview

- **Main Program**: Orchestrates the BI pipeline.
- **ETL Scripts**:
  - **Extract**: Reads raw data.
  - **Transform**: Cleans and prepares data.
  - **Load**: Inserts data into the data warehouse.
- **Testing**: Validates ETL processes and database connections.

---

## 📊 Tools & Technologies

- **Languages**: Python (pandas, SQLAlchemy)
- **Database**: MySQL
- **BI Tool**: Tableau
- **IDE**: Visual Studio Code

---

## 📈 Results

The BI dashboard provides insights into:
- **Store Efficiency**: Highlights top-performing stores and their contribution to total sales.
- **Product Trends**: Identifies high-demand categories and evaluates promotions.
- **Future Planning**: Uses predictive analytics to forecast demand and guide inventory management.

---

## 🛠 Challenges & Future Enhancements

### Challenges
- Handling large datasets and ensuring data quality.
- Designing intuitive and meaningful visualizations.

### Future Enhancements
- Incorporate real-time data for dynamic analysis.
- Use advanced machine learning models to improve demand forecasting.
- Integrate external data sources like weather and regional economic trends.

---

## ✍️ Contributors

- **Saja Moussa** 
- **Yasmine Tbessi** 

---

## 📜 License

This project is for educational purposes only.
