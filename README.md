# RecipesAPI
RecipesAPI is an API containing a collection of delicious recipes with informations on how to make them.The API is built using Django and Railway was used for deployment. 
You can try it here: recipesppm-production.up.railway.app

## What you can do with RecipesPPM
* Browse recipes: Explore a wide variety of recipes with ingredients and preparation steps uploaded by other users.
* Add recipes: You can add your own recipes describing ingredients and preparation steps.
* Delete recipes: If you no longer want to share your recipe you can delete it.
* Edit recipes: You can edit your own recipe if you need to.
# How to Setup and Run RecipesPPM Locally
## Prerequisites
* Python 3.10
* pip
## Steps
* Clone the repository to your local machine using git:
  ```
  git clone https://github.com/Nayla-k/RecipesPPM.git
  
  ```

* Navigate to the project directory:
  ```
  cd RecipesAPI
  
  ```
* Create a virtual environment:
  ```
  python -m venv env
  
  ```
* Activate the virtual environment:
  On Windows:
  ```
  .\env\Scripts\activate
  
  ```
  On Unix or MacOS:
  C
* Install the required dependencies:
  ```
  pip install -r requirements.txt
  
  ```
* Apply the migrations (if applicable):
  ```
  python manage.py migrate
  
  ```
* Run the server (if applicable):
  ```
  python manage.py runserver
  
  ```
Now, you can access the project locally at http://127.0.0.1:8000/.

# Contact
For any questions or suggestions, please contact Nayla-k.
