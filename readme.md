# Pricefy
![made-with-python](https://img.shields.io/badge/Made%20with-Python-0078D4.svg)
![html5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![css3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![javascript](https://img.shields.io/badge/JavaScript-323330?logo=javascript&logoColor=F7DF1E)
![numpy](https://img.shields.io/badge/Numpy-777BB4?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit_learn-0078D4?logo=scikit-learn&logoColor=white)
![fastapi](https://img.shields.io/badge/fastapi-109989?logo=FASTAPI&logoColor=white)
![heroku](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Pricefy app used to predict the price of the car based on certain input parameters created using python's scikit-learn, fastapi, numpy and joblib packages.

## Dataset Description

This dataset contains information about used cars. This data can be used for a lot of purposes such as price prediction to exemplify the use of linear regression in Machine Learning.

The data contains the following columns:

| Feature Name  | Feature Description                      |
| ------------- | ---------------------------------------- |
| Name          | Name of the Car model                    |
| Present_Price | Present showroom price of the car        |
| Year          | Car Model Year                           |
| Kms_Driven    | Kilometers driven till now               |
| Owner         | No of Owners (0 or 1 or 2 or 3)          |
| Fuel_Type     | Type of Fuel (Petrol or Diesel or CNG)   |
| Seller_Type   | Whether seller is (Individual or Dealer) |
| Transmission  | Transmission type (Automatic or Manual)  |
| Selling_Price | Used Car selling price (Target) variable |

## Installation
Open Anaconda prompt and create new environment
```
conda create -n your_env_name python = (any_version_number)
```
Then Activate the newly created environment
```
conda activate your_env_name
```
Clone the repository using `git`
```
git clone https://github.com/Prakashdeveloper03/Pricefy.git
```
Change to the cloned directory
```
cd <directory_name>
```
To install all requirement packages for the app
```
pip install -r requirements.txt
```
Then, Run the app
```
uvicorn main:app --reload
```

## 📷 Screenshots
### Home page
![output_image](markdown/home.png)
### About section
![output_image](markdown/about.png)
### Developer section
![output_image](markdown/developer.png)
### Swagger UI
![output_image](markdown/swagger.png)
### Redoc UI
![output_image](markdown/redoc.png)
### Demo GIF
![demo_gif](markdown/demo.gif)
