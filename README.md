
# GitHub Follow Manager

This project helps you manage your GitHub followings by identifying users you follow who don't follow you back. It's a tool to audit and maintain reciprocal connections. The script is written in Python and requires your GitHub username and token to work.

## Features
- Identify users you follow but who don't follow you back on GitHub.
- Easy to use and manage your GitHub following list.
- Works by comparing your followers and following lists.

## Prerequisites
- Python 3.x
- A GitHub account
- A GitHub personal access token (for authentication)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/tonyfalcondevweb/github-follow-manager.git
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your GitHub username and token:
   ```txt
   GITHUB_USERNAME=your_username
   GITHUB_TOKEN=your_personal_access_token
   ```

## Usage

1. Run the script using Python:
   ```bash
   python github_follow_check.py
   ```
2. The script will output a list of users you follow but who don't follow you back.

## How It Works
- The script retrieves your GitHub followers and the people you're following.
- It compares both lists and identifies who you're following but who don't follow you back.
- The result is printed, showing those users.

## Security Note
- Keep your GitHub token secure. Never push your `.env` file to public repositories.
