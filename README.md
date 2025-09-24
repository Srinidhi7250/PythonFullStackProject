# Smart Food Recommendation System

A Smart Food Recommendation System suggests food or recipes to users based on their preferences, diet, and health goals.
It analyzes nutritional content like calories, protein, fat, and carbs, and combines it with user data such as vegetarian, vegan, or keto.
The system then recommends meals that match the user’s taste and dietary needs.

🔹 Features:

Personalized Suggestions – shows foods you might like.

Diet-based Filtering – only shows foods for your diet (vegetarian, vegan, etc.).

Nutrition Awareness – can pick foods by calories, protein, fat, or carbs.

User Feedback – learns from your choices to give better suggestions.

## Project Structure

## Project Structure:

 SmartFoodRecommendation/
|
|----src/             #core application logic
|    |-----logic.py   #business logic and task 
operations
|     |__db.py        #Database operations
|
|
|----- api/            #Backend API
|        |___main.py   #FastAPI endpoints
|----frontend/         #frontend application
|      |___app.py      #Streamlit web interface
|
|___requirements.txt    #Python Dependencies
|
|____README.md          #Project documentation
|
|____.env               # Python variables  




## Quick Start

### Prerequisites

-Python 3.8 or higher
-A Supabase Account
-Git(Push,cloning)
 
### 1.Clone or download the project
 # Option 1: Clone with Git
 git clone <repository url>

 # Option 2:Download and extract the ZIP file

### 2.Install Dependencies
  
  # install all required python packages
  pip install -r  requirements.txt

###  3.Setup supabase database

1.Create a supabase project
2.Create the task tables:
   -Go to the sql editor in your supabase  dashboard
   -Run this sql command:
   ```sql
CREATE TABLE foods (
    food_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    ingredients TEXT,
    calories INT,
    protein FLOAT,
    fat FLOAT,
    carbs FLOAT,
    tags TEXT   -- e.g., 'vegetarian, vegan, keto'
);
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,           -- optional, or use Supabase Auth
    diet_preference TEXT     -- e.g., 'vegetarian', 'vegan', 'non-veg', 'keto'
);
CREATE TABLE preferences (
    pref_id SERIAL PRIMARY KEY,
    user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    food_id INT REFERENCES foods(food_id) ON DELETE CASCADE,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE recommendations (
    rec_id SERIAL PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    food_id INT REFERENCES foods(food_id),
    reason TEXT,                -- e.g., "similar to your choice"
    created_at TIMESTAMP DEFAULT NOW()
);

```
3. **Get Your Credentials:

### 4.Configure environment Variable

1.Create a `.env` file in the project root

2.Add your Supabase credentials to `.env`;
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**Example:**
SUPABASE_URL ="https://gpbydptskbkujczuudte.supabase.co"
SUPABASE_KEY ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdwYnlkcHRza2JrdWpjenV1ZHRlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI2MDAsImV4cCI6MjA3MzY1ODYwMH0.AXMK6IR7VTUGZFC5SvrFgIMkhiBAKPBlJREjlW1qK-w"



### 5. Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at `http://localhost:8080`

## FastAPI Backend

cd API
python main.py
 
The API will be available at `http://localhost:8081`

## How to use

**Frontend**:Streamlit(Python web framework)
**Backend**:FastAPI(Python REST API framework)
**Database**:Supabase(PostgreSQL-based backend-as-a-service)
**Language**:Python 3.8+

### Key Components

1.**`src/db.py`** :Database operations
   - Handles all CRUD operations with Supabase
2.**`src/logic.py`**:Business logic
    - Task validation and processing


## Troubleshooting

## Common Issues

1.**"Module not found" Errors**
     - Make sure you've installed all dependencies: `pip install -r requirements.txt`
     - Check that you've running commands from the correct directory
    
## Future Enhancements

Ideas for extending this project:

- **USer Authentication**:Add user accounts and login
- **Task Categories**:Organize tasks by subject or category
- **Notifications**:Email or push notifications for due dates
- **File Attachments**:Attach files to tasks
- **Collaboration**:Share tasks with classmates
- **Mobile App**:React Native or Flutter mobile version
- **Data Export**:Export tasks to CSV or PDF
-  **TAsk Templates**:Create reusable task templates

## Support

If you encounter any issues or have questions:
Phone number:`6300442414`
Email:`dharmagallasrinidhi@gmail.com`