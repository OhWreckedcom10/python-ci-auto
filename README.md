# Python CI – Stage 2 (Automated)

## Overview
This repository demonstrates **automated Continuous Integration (CI)** using **GitHub Actions**.  
You will learn how to fork, clone, set up a virtual environment, run tests, and see how automated CI ensures code quality before merging changes.

> In this stage, CI runs automatically on every push or Pull Request to the `master` branch.

---

## Project Structure

python-ci-auto/ # Project root folder
│
├── app/ # Source code folder
│ └── calculator.py # Python module with calculator functions
├── tests/ # Unit tests folder
│ └── test_calculator.py # Pytest tests for calculator functions
├── requirements.txt # Python dependencies (e.g., pytest)
├── .gitignore # Git ignore file to exclude venv, cache, OS files
├── README.md # Project documentation and instructions
└── .github/ # GitHub configuration folder
└── workflows/ # GitHub Actions workflows
└── python-ci.yml # CI workflow file (runs tests automatically)


---

## Step 1 – Fork the Repository

Go to the instructor's repository:

https://github.com/ronelkayam/python-ci-auto

Click **Fork** (top-right corner).  
Now you have a personal copy under your GitHub account.

> This is the repository you will work on and push changes to.

### Option B – Using GitHub CLI

Authenticate with GitHub CLI:

gh auth login
Fork the repository and clone it immediately:

gh repo fork ronelkayam/python-ci-auto --clone=true
cd python-ci-auto

###Step 2 – Clone the Repository (if not using CLI)
If you forked through the browser:

git clone https://github.com/ronelkayam/python-ci-auto
cd python-ci-auto
Always work from the project folder (cd python-ci-auto).

###Step 3 – Create a Virtual Environment
# Create a virtual environment named venv
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

###Step 4 – Run Tests Locally (Optional)
Even though CI will run tests automatically, you can test locally:

pytest
Expected output:

5 passed in 0.02s
Running tests locally helps catch errors before pushing changes.

###Step 5 – Understanding GitHub Actions CI
The .github/workflows/python-ci.yml workflow automatically does the following:

Trigger – runs on every push or Pull Request to master.

Checkout – pulls repository files to a GitHub runner (Ubuntu VM).

Setup Python – installs the specified Python version (3.11).

Install dependencies – installs packages from requirements.txt.

Run tests – executes all pytest tests in the tests/ folder.

Report results – marks the workflow as Success ✅ or Fail ❌ based on test results.

This automated process prevents broken code from being merged into master.

###Step 6 – Make Changes and Push
After editing code or adding tests:

git add .
git commit -m "Add new feature / fix bug"
git push origin master
GitHub Actions will automatically run the CI workflow.

If tests fail, your PR or push will show a failed CI, and you should fix it before merging.

###Step 7 – Optional: Test Functions Interactively

from app.calculator import add, divide

print(add(2, 3))       # Expected: 5
print(divide(10, 2))   # Expected: 5.0
About Pytest
Pytest is a popular testing framework for Python:

Automatically discovers and runs tests in your project.

Looks for files starting with test_ or ending with _test.py.

Looks for functions and classes starting with test_.

Running pytest ensures your code works correctly before committing or deploying changes.
CI automates this step so you don’t have to remember to run tests manually.

Summary
This stage introduces automated CI:

CI runs automatically on push or PR to master.

You no longer need to manually run tests before pushing.

It increases code quality, reduces bugs, and makes releases safer.

Next steps:
Experiment by making changes, adding new tests, and observe the CI results on GitHub.
Understand how automation prevents broken code from reaching master.