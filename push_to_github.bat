@echo off
REM GitHub Push Script for Loan Scoring System
REM Run this script after creating your GitHub repository

setlocal enabledelayedexpansion

echo ========================================
echo GitHub Push Setup Script
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Download from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo.
echo Step 1: Enter your GitHub username
set /p GITHUB_USER="GitHub Username: "

echo.
echo Step 2: Enter your email (for commits)
set /p GIT_EMAIL="Email: "

echo.
echo Step 3: Enter your name (for commits)
set /p GIT_NAME="Name: "

echo.
echo Configuring git...
git config --global user.email "%GIT_EMAIL%"
git config --global user.name "%GIT_NAME%"

echo.
echo Setting remote repository...
git remote add origin https://github.com/%GITHUB_USER%/loan-scoring-system.git

echo.
echo Checking remote...
git remote -v

echo.
echo Staging all files...
git add .

echo.
echo Creating initial commit...
git commit -m "Initial commit: Modern loan scoring system with Flask and scikit-learn"

echo.
echo Setting main branch...
git branch -M main

echo.
echo ========================================
echo IMPORTANT: Before continuing...
echo ========================================
echo 1. Go to: https://github.com/new
echo 2. Create repository: "loan-scoring-system"
echo 3. DO NOT check "Add a README file"
echo 4. Click "Create repository"
echo.
pause /P "Press Enter when you've created the repository... "

echo.
echo Pushing to GitHub...
echo (Enter your Personal Access Token when prompted for password)
echo.
git push -u origin main

echo.
echo ========================================
echo SUCCESS!
echo ========================================
echo Your repository is now at:
echo https://github.com/%GITHUB_USER%/loan-scoring-system
echo.
pause
