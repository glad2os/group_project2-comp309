# Project Setup Instructions

## Step 1: Create a Virtual Environment

To isolate our project's dependencies, we'll use a virtual environment. This helps to keep your global Python environment clean and manage project-specific dependencies more effectively. Run the following command to create a virtual environment named `venv`:

```shell
python -m venv venv
```

## Step 2: Activate the Virtual Environment

After creating the virtual environment, you need to activate it. This will ensure that any Python packages you install will be contained within this environment. Use the following command to activate it:

On Windows, use:

```shell
venv\Scripts\activate
```


## Step 3: Install Required Packages

Now that your virtual environment is active, install the required packages as defined in the `requirements.txt` file. This file lists all the necessary Python packages for the project. Run this command to install them:

```shell
pip install -r requirements.txt
```