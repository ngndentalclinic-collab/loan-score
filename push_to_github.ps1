# GitHub Push Script for Loan Scoring System
# PowerShell Version
# Run: .\push_to_github.ps1

Write-Host "========================================"
Write-Host "GitHub Push Setup Script (PowerShell)" -ForegroundColor Cyan
Write-Host "========================================"
Write-Host ""

# Check if git is installed
try {
    git --version | Out-Null
} catch {
    Write-Host "ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host "Download from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Get user inputs
Write-Host ""
$GITHUB_USER = Read-Host "Enter your GitHub username"
$GIT_EMAIL = Read-Host "Enter your email (for commits)"
$GIT_NAME = Read-Host "Enter your name (for commits)"

# Configure git
Write-Host ""
Write-Host "Configuring git..." -ForegroundColor Yellow
git config --global user.email $GIT_EMAIL
git config --global user.name $GIT_NAME

# Set remote
Write-Host "Setting remote repository..." -ForegroundColor Yellow
git remote add origin "https://github.com/$GITHUB_USER/loan-scoring-system.git"

# Check remote
Write-Host ""
Write-Host "Checking remote:" -ForegroundColor Yellow
git remote -v

# Stage files
Write-Host ""
Write-Host "Staging all files..." -ForegroundColor Yellow
git add .

# Create commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Modern loan scoring system with Flask and scikit-learn"

# Set main branch
Write-Host "Setting main branch..." -ForegroundColor Yellow
git branch -M main

# Important step
Write-Host ""
Write-Host "========================================"
Write-Host "IMPORTANT: Before continuing..." -ForegroundColor Yellow
Write-Host "========================================"
Write-Host "1. Go to: https://github.com/new"
Write-Host "2. Create repository: 'loan-scoring-system'"
Write-Host "3. DO NOT check 'Add a README file'"
Write-Host "4. Click 'Create repository'"
Write-Host ""
Read-Host "Press Enter when you've created the repository..."

# Push to GitHub
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "(Enter your Personal Access Token when prompted for password)" -ForegroundColor Green
Write-Host ""
git push -u origin main

# Success message
Write-Host ""
Write-Host "========================================"
Write-Host "SUCCESS!" -ForegroundColor Green
Write-Host "========================================"
Write-Host "Your repository is now at:"
Write-Host "https://github.com/$GITHUB_USER/loan-scoring-system" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to exit"
