# Project Overview

Project Overview

This project marks my first real dive into machine learning. I can’t say I’ve mastered 
the architecture of ResNet-34, but I believe I’ve gained a good grasp of its core logic 
and the broader concepts involved. What I find especially exciting is the intersection 
of APIs and machine learning. It’s rewarding to work on both the model architecture — 
which brings intelligence to applications — and the interfaces that make these models 
accessible and usable. I’m definitely interested in exploring both fields more deeply.

As part of this project, I transitioned from Flask to FastAPI in order to make the core 
functionality asynchronous. This shift aligns better with modern development practices, 
especially those involving the integration of machine learning models into web applications.

Regarding the model itself, I experimented with both 10-epoch and 20-epoch training sessions. 
The results were surprisingly close and, overall, still far from ideal. I suspect the performance 
limitations may stem from the dataset, the model configuration, or other factors I haven’t yet 
identified. While the model does generate predictions, its accuracy is inconsistent—generally correct 
only about half the time, with slightly better results for certain classes. Twenty epochs turned out 
to be too many for the current setup, but they might prove more effective with the introduction of data 
augmentation techniques —such as random cropping, flipping, or color jitter — to enrich the training 
dataset and improve generalization.

The integration of the model into the app went smoothly. The core idea was to maintain two separate 
implementations: one for training and one for deployment. The training setup generates a .pth file 
containing the model’s state dictionary—essentially, the learned weights. The deployment 
implementation, used within the app, loads the model in evaluation mode and uses the pretrained .pth 
file to initialize its configuration. This enables the model to analyze data relevant to the app’s 
workflow, similar to what it was trained on.


## Project Structure

```
Jul-17-Leaf-Disease-Detection-API
│
├── app
│    ├── __init__.py
│    ├── config.py
│    ├── main.py
│    ├── ml_model.py
│    └── models.py
├── db_scripts
│    └── seed_db.py
├── public
│    ├── index.html
│    └── script.js
├── run.py
├── training
│    ├── prepare_data.py
│    └── train_model.py
└── utils
    ├── __init__.py
    ├── check.py
    └── smart_sleep.py

6 directories, 14 files
```

## Running the Application

### Database
Seed the database, if it hasn't been seeded yet:
```
python db_scripts/seed_db.py
```

### Backend
Start the FastAPI backend:
```
python run.py
```

### Frontend
The frontend is a static HTML/JS page. You can open `public/index.html` 
directly in the browser, or serve it with a simple HTTP server:
```
cd public
python -m http.server 8080
```
Access it at http://localhost:8080.