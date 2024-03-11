# Breast Cancer Detection

![Breast Cancer Detection](images/home.jpg)

### Problem :

Breast cancer is the most common cancer

### Solution:

Building an application that can predict the occurrence of breast cancer or the possible causes of it by indicating the highly relevant factors.

### Idea:

The application will be able to predict the occurrence of breast cancer by taking into account the following factors:

-
-

### Layout

```
├───images
├───Tabs
│   └───__pycache__
|   └─── home.py
|   └─── data.py
|   └─── predict.py
|   └─── visualize.py
|   └─── about.py
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
