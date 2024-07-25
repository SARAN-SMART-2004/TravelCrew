# Django Application

Welcome to the Django Application. This project includes unique features like chat options, location sharing, note-making and reminder options, travel tips, travel health tips, a better UI interface, and a chatbot for help assistance.



## Prerequisites and Dependencies

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (Optional but recommended)


### Dependencies
- Django
- Django Channels
- Django Allauth
- Tinymce
- djangorestframework
- channels
- crispy_forms
- fontawesomefree
- captcha
- crispy_bootstrap4
- allauth.account
- allauth.socialaccount
- allauth.socialaccount.providers.google

## Installation and Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/django_application.git
cd django_application.\
```

### Step 2: Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Configure Environment Variables
```bash
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
DATABASE_URL=your_database_url
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
# Recaptcha keys
RECAPTCHA_PUBLIC_KEY=your key
RECAPTCHA_PRIVATE_KEY=your key

# Twilio settings
TWILIO_ACCOUNT_SID=your key
TWILIO_AUTH_TOKEN=your key
TWILIO_PHONE_NUMBER= your numbr

```
### Step 5: Set Up the Database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
### Step 6: Run the Development Server
```bash
python manage.py runserver
```
###Visit this in your browser to view the application.
```bash
 http://127.0.0.1:8000/
```
### features

- Chat options
- Location sharing
- Note-making and reminder options
- Travel tips
- Travel health tips
- Better UI interface
- Chatbot for help assistance

  

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
If you want to contribute to this project, please fork the repository and submit a pull request.
For any inquiries, please contact saran152004s@gmail.com.




