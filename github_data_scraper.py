import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load the GitHub token from .env
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Define headers with token
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Function to fetch users in Sydney with over 100 followers, with pagination
def fetch_users(location="Sydney", min_followers=100):
    url = "https://api.github.com/search/users"
    users_data = []
    page = 1
    
    while True:
        # Request with pagination
        params = {"q": f"location:{location} followers:>{min_followers}", "per_page": 100, "page": page}
        response = requests.get(url, headers=HEADERS, params=params)
        data = response.json().get("items", [])
        
        if not data:  # Stop if no more users are found
            break
        
        users_data.extend(data)
        page += 1
    
    return users_data

# Function to fetch user details and clean company name
def process_user_data(users_data):
    users = []
    for user in users_data:
        # Fetch full user details
        user_url = f"https://api.github.com/users/{user['login']}"
        user_details = requests.get(user_url, headers=HEADERS).json()
        
        # Clean up company name
        company = user_details.get("company", "")
        if company:
            company = company.lstrip("@").strip().upper()
        
        # Add user information
        users.append({
            "login": user_details.get("login"),
            "name": user_details.get("name", ""),
            "company": company,
            "location": user_details.get("location", ""),
            "email": user_details.get("email", ""),
            "hireable": user_details.get("hireable", False),
            "bio": user_details.get("bio", ""),
            "public_repos": user_details.get("public_repos", 0),
            "followers": user_details.get("followers", 0),
            "following": user_details.get("following", 0),
            "created_at": user_details.get("created_at", "")
        })
    return users

# Function to fetch up to 500 repositories per user with pagination
def fetch_repositories(username):
    repos = []
    url = f"https://api.github.com/users/{username}/repos"
    page = 1
    
    while len(repos) < 500:
        response = requests.get(url, headers=HEADERS, params={"per_page": 100, "page": page})
        data = response.json()
        
        if not data:  # Stop if no more repositories are found
            break
        
        repos.extend(data)
        page += 1
    
    return repos[:500]  # Limit to 500 repos

# Process repository data
def process_repository_data(users):
    repositories = []
    for user in users:
        repos = fetch_repositories(user["login"])
        for repo in repos:
            repositories.append({
                "login": user["login"],
                "full_name": repo.get("full_name", ""),
                "created_at": repo.get("created_at", ""),
                "stargazers_count": repo.get("stargazers_count", 0),
                "watchers_count": repo.get("watchers_count", 0),
                "language": repo.get("language", ""),
                "has_projects": repo.get("has_projects", False),
                "has_wiki": repo.get("has_wiki", False),
                "license_name": repo.get("license")["key"] if repo.get("license") else ""
            })
    return repositories

# Fetch, process, and save data to CSV
def save_data():
    # Fetch users and process data
    users_data = fetch_users()
    users = process_user_data(users_data)
    
    # Save users.csv
    users_df = pd.DataFrame(users)
    users_df.to_csv("users.csv", index=False)
    print("Saved users.csv")
    
    # Process repositories data and save
    repositories = process_repository_data(users)
    repos_df = pd.DataFrame(repositories)
    repos_df.to_csv("repositories.csv", index=False)
    print("Saved repositories.csv")

# Run the data collection
save_data()
