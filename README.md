# Breast Cancer Detection

![Breast Cancer Detection](images/home.jpg)

### Problem :

Breast cancer is the most common cancer

### Solution:

Building an application that can predict the occurrence of breast cancer or the possible causes of it by indicating the highly relevant factors.

### Idea:

The application will be able to predict the occurrence of breast cancer by taking into account the following factors:

- radius_mean
- texture_mean 
- perimeter_mean 
- area_mean
- smoothness_mean
- compactness_mean
- concavity_mean
- concave_points_mean
- symmetry_mean
- fractal_dimension_mean

### Layout

```
├───images
├───Tabs
│   └───__pycache__
|   └─── home.py
|   └─── predict.py
|   └─── visualize.py
└───__pycache__
└─── main.py
└─── web_functions.py
└─── requirements.txt
```

### How to use

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment
For Windows:

```bash
.venv\Scripts\activate
```

For MacOS and Linux:

```bash
source .venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the app

```bash
streamlit run main.py
```

Deactivate the virtual environment when you are done

```bash
deactivate
```
