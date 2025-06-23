# Travel Crew (New Travel System)!

## Overview

Welcome to the Django Application. This project make the revolutionary in travel system. This project includes unique features like chat options, location sharing, note-making and reminder options, travel tips, travel health tips, a better UI interface, and a chatbot for help assistance.


## Prerequisites and Dependencies

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (Optional but recommended)

## Dependencies

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

## Features

- Chat options
- Location sharing
- Note-making and reminder options
- Travel tips
- Travel health tips
- Better UI interface
- Chatbot for help assistance



## Installation and Setup Instructions

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/Santhosh174/Email-OTP-Authentication.git
    cd Email-OTP-Authentication
    ```

2. **Create and Activate a Virtual Environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```
3. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt 
    ```

4. **Configure Environment Variables:**
    Create a `.env` file in the root directory and add:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    EMAIL_SERVICE=your_email_service_provider
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

4. **Set Up the Database:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```
 5. **Run the Development Server:**
    ```sh
    python manage.py runserver
    ```


5. **Access the Application:**
    Open your browser and navigate to `[http://localhost:5000](http://127.0.0.1:8000/)`



## Screenshots

![image](https://github.com/SARAN-SMART-2004/TravelCrew/blob/main/githubimages/image1.png?raw=true)
*Description: Screenshot of Dashboard which shows all routing paths*

![image](https://github.com/SARAN-SMART-2004/TravelCrew/blob/main/githubimages/image2.png?raw=true)
*Description: Screenshot of All travel post by the users*

![image](https://github.com/SARAN-SMART-2004/TravelCrew/blob/main/githubimages/5.png?raw=true)
*Description: Screenshot showing the searching of the travel plan web page.*

![image](https://github.com/SARAN-SMART-2004/TravelCrew/blob/main/githubimages/4.png?raw=true)
*Description: Screenshot showing the complete user profile and history of the users.*

![image](https://github.com/SARAN-SMART-2004/TravelCrew/blob/main/githubimages/3.png?raw=true)
*Description: Screenshot showing the user upcoming travel plan.*

![image](https://github.com/SARAN-SMART-2004/TravelCrew/blob/main/githubimages/1.png?raw=true)
*Description: Screenshot showing the navigation bar in the mobile responsive format*

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you want to contribute to this project, please fork the repository and submit a pull request.
For any inquiries, please contact saran152004s@gmail.com.








