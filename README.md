# AWS_BEDROCK_GENAI

# AWS Bedrock Poem Generator

This project is a Python application that generates Shakespearean poems using machine learning models hosted on AWS Bedrock. Follow the steps below to set up and run the application on your local environment.

## Prerequisites

Before proceeding, ensure you have:

- An AWS account
- Access to AWS Bedrock Foundation Models
- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your machine
- Visual Studio Code installed for code editing

## Setup Instructions

### Step 1: Create an AWS Account

Sign up for an AWS account at [AWS Sign In](https://signin.aws.amazon.com/).

### Step 2: Set Up Billing Budget

To monitor your cloud expenses:
1. Go to **Billing and Cost Management** > **Budgets**.
2. Create a new budget to track your cloud spending.

### Step 3: Create an IAM User

1. Go to **IAM** > **Users**.
2. Create a new user and assign necessary permissions.
3. Once the user is created, generate access keys for **CLI** use.

### Step 4: Request AWS Bedrock Access

1. Navigate to **AWS Bedrock** > **Bedrock Configurations**.
2. Request access to AWS Bedrock Foundation Models.

### Step 5: Set Up Your Local Environment

1. Create a folder on your local machine for the project.
2. Open the folder in **VS Code**.

### Step 6: Create a Virtual Environment

Open the terminal in VS Code and run:


conda create -p genaivenv python==3.12


## conda activate genaivenv/

### Step 7: Create requirements.txt file and install the dependencies


boto3

awscli

response

pypdf

langchain

langchain_community

streamlit

faiss-cpu


## pip install -r requirements.txt


### Step 8: Configure AWS CLI

aws configure

You will be prompted to enter the following information:

AWS Access Key ID

AWS Secret Access Key

Default region: us-east-1

Default output format: json

### Step 9: Create app.py


### Step 10: Run the Application


python app.py




