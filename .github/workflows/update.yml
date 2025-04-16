name: Auto Update MIU Tracker

on:
  schedule:
    - cron: '*/30 * * * *'  # Runs every 30 minutes
  workflow_dispatch:  # Optional: lets you trigger manually

jobs:
  update-html:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install Dependencies
        run: pip install requests beautifulsoup4

      - name: Run Update Script
        run: python update_html.py

      - name: Commit and Push Changes
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"
          git add index.html
          git commit -m "Auto update patient numbers"
          git push
