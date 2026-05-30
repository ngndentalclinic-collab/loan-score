# 📤 GitHub Push Complete Guide

## ⚠️ First: Install Git

### Windows
1. Download from: https://git-scm.com/download/win
2. Run the installer and follow default options
3. Restart PowerShell/Terminal

### Verify Git is installed:
```powershell
git --version
```

---

## 🚀 Push Your Project to GitHub

### Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `loan-scoring-system`
   - **Description**: Modern loan scoring system using Machine Learning (Flask + scikit-learn)
   - **Visibility**: Public (optional: Private)
3. **IMPORTANT**: Do NOT check "Add a README file"
4. Click **"Create repository"**

### Step 2: Copy Your Repository URL
After creating, you'll see a page with:
- HTTPS URL (e.g., `https://github.com/YOUR_USERNAME/loan-scoring-system.git`)
- Copy this URL

### Step 3: Configure Git
Open PowerShell and run:
```powershell
git config --global user.email "your.email@example.com"
git config --global user.name "Your Name"
```

### Step 4: Add Remote and Push

**Replace `YOUR_USERNAME` with your GitHub username**

```powershell
cd "c:\Users\user\Desktop\loan scoring"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/loan-scoring-system.git

# Verify it worked
git remote -v

# Set main branch and push
git branch -M main
git push -u origin main
```

### Step 5: Enter Your GitHub Credentials

When prompted, choose one option:

#### 🔑 Option A: Personal Access Token (Recommended)
1. Go to GitHub: Settings > Developer settings > Personal access tokens > Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name: "loan-scoring-push"
4. Select scopes: ✅ `repo` (Full control of private repositories)
5. Click "Generate token"
6. Copy the token (⚠️ You won't see it again!)
7. Paste it as the password when prompted

#### 🔐 Option B: GitHub CLI
```powershell
# Install GitHub CLI first: https://cli.github.com/
gh auth login

# Then run push commands above
```

---

## ✅ Verify Success

After pushing, check:
1. Go to `https://github.com/YOUR_USERNAME/loan-scoring-system`
2. You should see:
   - ✅ All your files (app.py, templates/, requirements.txt, etc.)
   - ✅ README.md with full documentation
   - ✅ Green "Code" button to clone/download

---

## 📥 To Download Your Project Later

```powershell
# Clone the repository
git clone https://github.com/YOUR_USERNAME/loan-scoring-system.git

# Navigate into it
cd loan-scoring-system

# Install dependencies
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run the app
python app.py
```

---

## 🔄 Future Updates

After making changes:
```powershell
git add .
git commit -m "Your commit message describing changes"
git push
```

---

## 🆘 Troubleshooting

### "fatal: 'origin' does not appear to be a 'git' repository"
```powershell
# Check if remote is set
git remote -v

# If empty, add it again
git remote add origin https://github.com/YOUR_USERNAME/loan-scoring-system.git
```

### "Authentication failed"
- Make sure you're using Personal Access Token, not your GitHub password
- Token must have `repo` scope

### "branch 'main' already exists"
```powershell
# Just push directly
git push -u origin main --force
```

---

## 📚 Useful Commands

```powershell
# Check git status
git status

# View commit history
git log --oneline

# See what changed
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Start fresh
git init
git add .
git commit -m "Initial commit"
```

---

💡 **Need help?** Check: https://docs.github.com/en/get-started/quickstart
