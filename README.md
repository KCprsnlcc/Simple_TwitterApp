# Twitter Profanity Filter and Referral System

This project is a Django web application that simulates a simple Twitter-like platform with an integrated profanity filter for both English and Tagalog languages. Users can post statuses and refer concerning statuses to a counselor for monitoring.

## Features

- Post statuses with real-time profanity filtering
- Support for English and Tagalog inappropriate word filtering
- Refer statuses to a counselor
- Counselor monitoring of referred statuses

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (recommended)

### Setup Instructions

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/twitter_project.git
   cd twitter_project
   ```

````

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply the migrations to set up the database:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

6. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

- **Post a Status:** Use the form on the homepage to post a new status. Profanity filtering is applied in real-time.
- **Refer a Status:** Click the "Refer" button next to any status to refer it to a counselor. A modal dialog will appear for you to provide a reason for the referral.
- **Monitor Referrals:** Counselors can view referred statuses by navigating to the URL.

```

Place this `README.md` file in the root of your project directory. This should provide a clear and concise guide on how to set up and run your Django project. If you need further customization or additional details, feel free to ask!
```
````
