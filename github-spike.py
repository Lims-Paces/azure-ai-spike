# import requests
# from datetime import datetime

# # GitHub repository details
# owner = 'Lims-Paces'
# repo = 'azure-ai-spike'

# # Date range
# since = '2024-06-16T00:00:00Z'  # Start date
# until = '2024-06-30T23:59:59Z'  # End date

# headers = {
#     'Authorization': f'token {token}',
#     'Accept': 'application/vnd.github.v3+json'
# }

# commits_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
# params = {
#     'since': since,
#     'until': until
# }

# response = requests.get(commits_url, headers=headers, params=params)
# commits = response.json()

# for commit in commits:
#     sha = commit['sha']
#     commit_detail_url = f'https://api.github.com/repos/{owner}/{repo}/commits/{sha}'
#     commit_detail_response = requests.get(commit_detail_url, headers=headers)
#     commit_detail = commit_detail_response.json()

#     print(f"Commit: {commit['commit']['message']}")
#     print(f"Author: {commit['commit']['author']['name']}")

#     for file in commit_detail['files']:
#         print(f"File: {file['filename']}, Changes: {file['changes']}")
#     print()


import json
import requests
from datetime import datetime

def get_changed_files(repo_path, github_token, repo_owner, repo_name, since_date, until_date):
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Get the list of commits in the specified period
    commits_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    commits_params = {
        'since': since_date,
        'until': until_date
    }
    commits_response = requests.get(commits_url, headers=headers, params=commits_params)
    commits = commits_response.json()
    
    changed_files = []

    for commit in commits:
        sha = commit['sha']
        
        # Get the details of each commit
        commit_details_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{sha}"
        print(commit_details_url)
        commit_details_response = requests.get(commit_details_url, headers=headers)
        commit_details = commit_details_response.json()

        for file in commit_details.get('files', []):
            changed_files.append({
                "filename": file['filename'],
                "status": file['status']
            })
    
    return changed_files

# owner = 'Lims-Paces'
# repo = 'azure-ai-spike'

# # Date range
# since = '2024-06-16T00:00:00Z'  # Start date
# until = '2024-06-30T23:59:59Z'  # End date

# Example usage
repo_path = "azure-ai-spike"

repo_owner = "Lims-Paces"
repo_name = "azure-ai-spike"
since_date = "2024-06-16T00:00:00Z"  # Example start date
until_date = "2024-06-30T23:59:59Z"  # Example end date

changed_files = get_changed_files(repo_path, github_token, repo_owner, repo_name, since_date, until_date)

for file in changed_files:
    print(f"File: {file['filename']}, Status: {file['status']}")
