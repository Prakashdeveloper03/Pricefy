import joblib  # for loading model pickle file
import datetime  # for data & time functions
import numpy as np  # for array conversion

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()  # instance of FastAPI class

# mount static folder files to /static route
app.mount("/static", StaticFiles(directory="static"), name="static")

# loads the ML model
model = joblib.load(open("model/model.pkl", "rb"))

# sets the templates folder for the app
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home_index(request: Request):
    """
    Function to render `index.html` at route '/' as a get request
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `index.html`
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/predictor", response_class=HTMLResponse)
async def read_item(request: Request):
    """
    Function to render `predictor.html` at route '/predictor' as a get request
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `predictor.html`
    """
    return templates.TemplateResponse("predictor.html", {"request": request})


@app.post("/predictor/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    model_year: int = Form(...),
    present_price: float = Form(...),
    kms_driven: int = Form(...),
    owner: int = Form(...),
    fuel_type: str = Form(...),
    seller_type: str = Form(...),
    transmission_type: str = Form(...),
):
    """
    Function to predict car price
    and shows the result by rendering `predictor.html` at route '/predict'

    __Args__:
    - request (Request): request in path operation that will return a template
    - model_year (int): model year of the car
    - present_price (float): present price of the car
    - kms_driven (int): kilometers driven by the car till now
    - owner (int): no of owners used
    - fuel_type (str): car's fuel type
    - seller_type (str): car seller type
    - transmission_type (str): car's transmission type

    __Returns__:
    - Template: render `predictor.html`
    """
    # difference between current year and model year
    year = datetime.date.today().year - model_year

    # frequency encoding for fuel type
    if fuel_type.lower() == "petrol":
        fuel = 239
    elif fuel_type.lower() == "diesel":
        fuel = 60
    else:
        fuel = 2

    # frequency encoding for seller type
    seller = 106 if seller_type == "individual" else 195
    transmission = 261 if transmission_type == "manual" else 40

    # input features as a list
    input_list = [present_price, kms_driven, fuel, seller, transmission, owner, year]

    # list --> numpy array
    final_features = [np.array(input_list)]

    # prediction using model
    prediction = model.predict(final_features)

    # gets the predicted price value
    output = round(prediction[0], 2)
    return templates.TemplateResponse(
        "predictor.html", context={"request": request, "prediction": output}
    )
