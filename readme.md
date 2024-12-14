# Quiz Application

## Problem Statement

Create a Django web application for a simple quiz app. The user should be able to:
1. Start a new quiz session.
2. Get random multiple-choice questions from a pre-existing set in the database.
3. Submit answers for the quiz.
4. View the results of the quiz, including details about correct, incorrect, and unattempted questions.

The application should have a clean UI with functionalities for restarting the quiz and viewing results after submission.

---

## Assumptions

1. There is only one type of user, and no authentication is required.
2. The database is pre-populated with questions and choices.
3. A quiz session ends once the user submits their answers, and they cannot reattempt the same quiz session.
4. A maximum of 20 questions are displayed per session, selected randomly from the database.
5. Sessions and state management are handled using Django's session framework.

---

## Approach

### Backend
- **Django Framework**: Used for handling APIs, business logic, and database interactions.
- **Database Models**:
  - Questions and choices are stored in a relational database.
  - Quiz sessions track user progress and submission details.
- **APIs**:
  - Fetch questions.
  - Submit quiz answers and calculate results.

### Frontend
- HTML/CSS for structuring and styling pages.
- JavaScript for dynamic interactions like:
  - Handling timers.
  - Navigating between questions.
  - Submitting answers via AJAX requests.

---

## Features

1. **User-Friendly Interface**:
   - Simple and intuitive UI for users to start the quiz, navigate questions, and view results.

2. **Randomized Question Selection**:
   - Each session presents 20 random questions from the database.

3. **Real-Time Interaction**:
   - Timer to track the remaining quiz time.
   - Immediate navigation between questions with dynamic state management.

4. **Result Analysis**:
   - Detailed breakdown of correct, incorrect, and unattempted questions.
   - View answers with appropriate color-coded indicators.

5. **Session Management**:
   - User session handling ensures quiz data is retained until submission.
   - Prevents re-submission of the same quiz session.

6. **Restart Functionality**:
   - Allows users to restart the quiz without re-entering their name.

---

## Workflow

1. **Welcome Page**:
   - The user enters their name and starts a new quiz session.
   - If a session already exists, the user is greeted with their name and given options to view results or restart the quiz.

2. **Quiz Page**:
   - Displays a random set of 20 multiple-choice questions.
   - Allows users to navigate between questions, mark questions for review, and submit their answers.

3. **Timer Functionality**:
   - A timer tracks the remaining time for the quiz (e.g., 15 minutes).
   - On timer expiration, the quiz is auto-submitted.

4. **Submit Quiz**:
   - The user submits their answers.
   - The backend evaluates the answers and calculates the results.

5. **Results Page**:
   - Displays the total number of questions, correct answers, incorrect answers, and unattempted questions.
   - Shows color-coded indicators for easy result visualization:
     - **Green**: Correctly answered questions.
     - **Red**: Incorrectly answered questions (with correct answers highlighted).
     - **Gray**: Unattempted questions.

6. **Restart Quiz**:
   - Allows the user to start a fresh session without re-entering their name.

---



## Table Structure

### **Question**
| Field        | Type         | Description                       |
|--------------|--------------|-----------------------------------|
| id           | Integer      | Primary key                      |
| text         | TextField    | The text of the question          |

### **Choice**
| Field        | Type         | Description                       |
|--------------|--------------|-----------------------------------|
| id           | Integer      | Primary key                      |
| text         | CharField    | The text of the choice            |
| is_correct   | BooleanField | Whether the choice is correct     |
| question_id  | ForeignKey   | Linked to the `Question` table    |

### **QuizSession**
| Field            | Type         | Description                       |
|------------------|--------------|-----------------------------------|
| id               | Integer      | Primary key                      |
| total_questions  | IntegerField | Number of questions in the quiz  |
| correct_answers  | IntegerField | Number of correct answers         |
| incorrect_answers| IntegerField | Number of incorrect answers       |
| created_at       | DateTimeField| When the session was created      |

---

## API Endpoints and Purpose

### **1. Start Quiz**
- **Endpoint**: `/quiz/start/`
- **Method**: POST
- **Purpose**: Initializes a new quiz session and stores the user name in the session.

### **2. Fetch Questions**
- **Endpoint**: `/quiz/get-questions/`
- **Method**: GET
- **Purpose**: Returns a random set of 20 questions with their choices.

### **3. Submit Quiz**
- **Endpoint**: `/quiz/submit/`
- **Method**: POST
- **Purpose**: Accepts user answers, calculates results, and updates the session with the quiz outcome.

### **4. View Results**
- **Endpoint**: `/quiz/results/`
- **Method**: GET
- **Purpose**: Displays the user's quiz results, including the breakdown of correct, incorrect, and unattempted questions.

### **5. Restart Quiz**
- **Endpoint**: `/quiz/restart/`
- **Method**: POST
- **Purpose**: Clears the previous session and starts a new quiz session while preserving the user's name.

---

## Steps to Clone Locally and Run

### Prerequisites
- Python 3.12+
- pip (Python package installer)
- Virtual environment (recommended)
- MySQL or SQLite for database

### Steps
1. **Clone the Repository**
   ```bash
   git clone git@github.com:thev19/QuizApp.git
   cd QuizApp
   python -m venv venv 
   venv\Scripts\activate # if you are using ubuntu : source venv/bin/activate 
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
```


