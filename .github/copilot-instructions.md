# GitHub Copilot Instructions for OctoFit Tracker Project

## Overview
This file provides instructions for GitHub Copilot to assist in the development of the OctoFit Tracker application. The project is based on the Monafit Tracker structure and adapted for Mergington High School's requirements.

## References
- `docs/mona-high-school-fitness-tracker.md`: Provides the structure and requirements for the Monafit Tracker application.
- `docs/octofit_story.md`: Details the story and goals for the OctoFit Tracker application.

## Project Structure
The OctoFit Tracker application will have the following structure:

```
octofit-tracker/
├── backend/
│   ├── venv/
│   ├── requirements.txt
│   ├── monafit_tracker/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── settings.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
└── frontend/
    ├── node_modules/
    └── README.md
```

## Backend Setup
1. Create a Python virtual environment in `octofit-tracker/backend`.
2. Add a `requirements.txt` file in `octofit-tracker/backend` with the following dependencies:
   - Django==4.1
   - djangorestframework==3.14.0
   - django-allauth==0.51.0
   - django-cors-headers==4.5.0
   - dj-rest-auth
   - djongo==1.3.6
   - pymongo==3.12
   - sqlparse==0.2.4
   - stack-data==0.6.3
   - sympy==1.12
   - tenacity==9.0.0
   - terminado==0.18.1
   - threadpoolctl==3.5.0
   - tinycss2==1.3.0
   - tornado==6.4.1
   - traitlets==5.14.3
   - types-python-dateutil==2.9.0.20240906
   - typing_extensions==4.9.0
   - tzdata==2024.2
   - uri-template==1.3.0
   - urllib3==2.2.3
   - wcwidth==0.2.13
   - webcolors==24.8.0
   - webencodings==0.5.1
   - websocket-client==1.8.0
3. Install the required packages using `pip install -r requirements.txt`.

## Frontend Setup
1. Create a React application in `octofit-tracker/frontend`.
2. Install Bootstrap and import it into the project.

## MongoDB Setup
1. Install MongoDB using `apt-get`.
2. Start MongoDB with the following commands:
   ```bash
   sudo service mongodb start
   sudo service mongodb status
   ```

## Notes
- Follow the project structure and requirements as outlined in the documentation.
- Ensure all dependencies are installed correctly before proceeding to the next steps.