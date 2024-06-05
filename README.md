
# Laptop Price Prediction:


## Project OverView
- Created a tool that estimates price of laptops on noon store to help users descide which company they will buy from based on their budget.
- Scraped over 863 laptops descriptions from noon store using python,beautifulsoup and selenium
- Engineered features from the text of each laptop description to extract the features that affect on the price of laptops.

- Optimized Linear, Random Forest, and XGboost  Regressors using GridsearchCV to reach the best model.
- Built a client wep app using streamlit
## Resources Used

- language:python 
- libraries:pandas, numpy, sklearn, matplotlib, seaborn, selenium, beautifulsoup, pickle,streamlit
to install the libraries use this command:

```bash
  pip install 'name of library'
```    
## Documentation
[Beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/)

[Streamlit](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)






## Web Scraping
I scrapped over 863 laptops from noon website
and extract from the description the following features:
- price
- Category
- Inch
- Core
- Processor
- Ram
- Memory
- Opysys
## Data Cleaning
- after i scrapped the data i needed to clean it up,so i check for missing values and apply some technique to fill it.
- change the datatypes to make it valid for the model 
- remove unusful characters from each feature


## EDA Analysis
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights:

![alt text](https://github.com/Mannar324/Laptop_price_prediction/blob/main/EDA%20analysis/newplot.png "price distribution")
![alt text](https://github.com/Mannar324/Laptop_price_prediction/blob/main/EDA%20analysis/count%20category.png "Category Count")
![alt text](https://github.com/Mannar324/Laptop_price_prediction/blob/main/EDA%20analysis/pricebercat.png "price ber Category")


## Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Squared Error.

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Random Forest Regressor** – Because the ensamble model work effectivly and higher performance.
*	**XGboost Regressor** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 
## Model Evaluation
after experimant i found that the **RandomForest** had the less error in both training and testing 
so i fine tune them using grid search to have more accurate performance
## Productionization 
In this step, I built a streamlit web app that was run on a local device, it requests list of values from user and returns an estimated price.


## Demo


[Web app](https://github.com/Mannar324/Laptop_price_prediction/blob/main/webapp.mkv)
