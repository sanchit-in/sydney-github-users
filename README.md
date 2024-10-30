### Sydney GitHub Users Analysis

- The data was gathered using GitHub’s API to capture profiles of Sydney-based users with over 100 followers and details on their repositories.
- An interesting discovery was that Python and JavaScript are the dominant languages, hinting at their popularity among developers in Sydney.
- Developers aiming to increase followers should consider adding detailed documentation and enabling project boards for improved project visibility.

---

## Project Overview

This project uses the GitHub API to collect and examine data on Sydney-based GitHub users with a following of over 100. The data analysis provides insights into the user demographics, repository activity, and the programming languages commonly used by these developers.

### Files in This Repository

- **`users.csv`**: Contains key information on GitHub users in Sydney with over 100 followers. Each row includes:
  - `login`: GitHub username.
  - `name`: User’s full name.
  - `company`: Cleaned company name (whitespace trimmed, any `@` removed, converted to uppercase).
  - `location`: City of the user (i.e., Sydney).
  - `email`: User’s email address, if available.
  - `hireable`: Whether the user is open to work opportunities.
  - `bio`: Short description from the user’s profile.
  - `public_repos`: Total count of public repositories.
  - `followers`: Follower count.
  - `following`: Count of people the user follows.
  - `created_at`: Date when the GitHub account was created.

- **`repositories.csv`**: Contains up to 500 recent repositories for each user in `users.csv`. Each row includes:
  - `login`: The user’s GitHub login name.
  - `full_name`: Full repository name.
  - `created_at`: Date of repository creation.
  - `stargazers_count`: Star count on the repository.
  - `watchers_count`: Count of watchers on the repository.
  - `language`: Primary coding language used in the repository.
  - `has_projects`: Indicates if the repository has projects enabled.
  - `has_wiki`: Indicates if the repository has a wiki.
  - `license_name`: License name, if applicable.

---

## Methodology

1. **Data Collection**: The GitHub API was used to filter users by location (Sydney) and follower count (over 100), then gather up to 500 recent public repositories for each user.

2. **Data Processing**: Company names were formatted to remove extra spaces, `@` symbols, and standardized to uppercase. Empty values were replaced with empty strings, and booleans were converted to `true` or `false`.

3. **Data Analysis**: Trends in programming languages and repository attributes were analyzed to provide insights for the local developer community.

---

## Insights and Recommendations

1. **Programming Trends**: Python and JavaScript dominate among Sydney-based GitHub users, reflecting strong demand for these languages in the community.

2. **Engagement Tips**: Developers seeking to engage followers may benefit from adding robust documentation and enabling project boards to promote visibility and organization.

3. **Follower Growth**: Regularly updated repositories with collaboration features tend to attract more followers, showcasing developers’ active engagement and professionalism.


