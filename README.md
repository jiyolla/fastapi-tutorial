# fastapi-tutorial

A repository for step-by-step code snippets while following [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/).

## How is this repo organized?

### Tags
Each tag refers to code snippets used in the particular step. The code might be cumulative.

Tag name follows the URI(eg. 'https://fastapi.tiangolo.com/tutorial/first-steps/' for tag named 'first-steps').

### 'main' branch
The 'main' branch refers to the latest follow up.

### **UPDATE**
I originally planned to tag all the steps, but I soon found it quite meaningless. From this step([Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/)), I would rather compress multiple steps into one giving a proper tag with my best effort.


## Usage

To run the code snippets, install [Poetry](https://python-poetry.org/), a dependency manager for python.

To understand why you need such a tool(actually you don't need it for a project like this, but anyway), see [this article by Mario](https://modelpredict.com/wht-requirements-txt-is-not-enough#:~:text=is%20the%20problem.-,Your%20requirements.,running%20pip%20install%20%2Dr%20requirements.).

To activate the virtual environment,
```bash
poetry install
poetry shell
```
and you are ready to go.
