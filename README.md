
# ChatGPT-based Chatbot using Django

Introduction
The purpose of this project is to develop a chatbot using the ChatGPT model integrated into a Django web application. The chatbot will allow users to interact with the model, generating responses based on their input. The Django framework will be employed to facilitate web development, handling user input, and displaying chat interactions.S

## Project Components

1. Django Setup <br>
The project utilizes the Django framework to structure the web application. Django provides a robust and scalable foundation for building web applications, handling routing, views, and templates.

2. Chat App<br>
A Django app named 'chat' is created to encapsulate the functionality related to the chatbot. This includes handling user input, integrating with the ChatGPT model, and rendering the chat interface.

3. Chat Form<br>
A Django form is implemented to capture user input. The form, defined in the 'chat' app, includes a text field for users to type their messages. This form facilitates the submission of user queries to the ChatGPT model.

4. OpenAI API Integration<br>
The OpenAI API is employed to interact with the ChatGPT model. An API key is obtained from OpenAI, and the Django application is configured to make requests to the API. User input is sent to the ChatGPT model, and the generated responses are received and processed.

5. Chat View<br>
A Django view, named chat_view, is responsible for handling the user's input, making requests to the ChatGPT model, and rendering the chat interface. The view uses the OpenAI API to obtain responses and updates the conversation in real-time.

6. Frontend<br>
A simple HTML template is designed to display the chat interface. The template incorporates AJAX or Django forms to enable real-time updates as users interact with the chatbot. CSS styles can be added to enhance the visual appeal of the interface.

## Run Locally

Clone the project

```bash
  git clone https://github.com/tusharsingh00/chatbot_django.git
```

Go to the project directory

```bash
  cd chatbot_django
```
Create a virtual environment (optional)
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```
Run migrations
```bash
python manage.py migrate
```
Install dependencies

```bash
  pip install django
```
```bash
  pip install openai
```

Start the server

```bash
  python manage.py runserver
```


## Acknowledgements

 - [CodeWithHarry](www.youtube.com/@CodeWithHarry)
 - [freecodecamp.org](https://www.youtube.com/@freecodecamp)
 - [CodeWithClinton](www.youtube.com/@CodeWithClinton)
 - [Chatgpt](https://chat.openai.com/auth/login)

