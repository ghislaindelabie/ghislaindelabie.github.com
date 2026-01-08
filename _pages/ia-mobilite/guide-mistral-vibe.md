---
layout: page
permalink: /ia-mobilite/guide-mistral-vibe/
title: Mistral Vibe Guide - Complete Setup
description: Complete guide to set up Mistral Vibe on Windows and macOS for your AI & Mobility projects
lang: en
---

# 🚀 Complete Mistral Vibe Guide for AI & Mobility

**Optimized configuration for Windows and macOS.** This guide explains how to install and configure **Mistral Vibe** for your development projects, with a special focus on AI & Mobility applications like "Gare Ton Char".

---

## 🆕 Account Creation & API Key Setup

### 1. Create Your Mistral AI Account

**Sign up at the official Mistral AI platform:**

👉 **[Mistral AI Signup](https://mistral.ai/)** *(Official website)*

**Steps to create your account:**
1. Go to [https://mistral.ai/](https://mistral.ai/)
2. Click "Sign Up" or "Get Started"
3. Choose your preferred signup method (email, Google, GitHub)
4. Complete the registration form
5. Verify your email address

**🎉 Special Offer for Students & Developers:**
- The **Devstral-2** model is currently **FREE** for all users
- You can use advanced AI capabilities **without any charges**
- Even after any promotional periods, smaller models remain free for basic usage

### 2. Generate Your API Key

**After logging in:**
1. Navigate to your **Account Settings** or **API Dashboard**
2. Look for "API Keys" or "Developer Settings"
3. Click "Generate New API Key"
4. Copy your API key immediately (it won't be shown again)

**⚠️ Important Security Notes:**
- **Never share your API key** publicly
- **Don't commit it to Git repositories**
- Store it securely in environment variables or secret managers
- Mistral AI uses **token-based billing** - you only pay for what you use

### 3. Configure API Key for Mistral Vibe

**Recommended setup methods:**

#### Option A: Environment Variable (Most Secure)
```bash
# Windows (PowerShell)
$env:MISTRAL_API_KEY="your-api-key-here"

# macOS/Linux (Bash)
export MISTRAL_API_KEY="your-api-key-here"

# To make it permanent, add to your shell profile
# (.bashrc, .zshrc, or .bash_profile)
echo 'export MISTRAL_API_KEY="your-api-key-here"' >> ~/.zshrc
```

#### Option B: Mistral Vibe Configuration File
Create a `.env` file in your project root:
```env
MISTRAL_API_KEY=your-api-key-here
MISTRAL_MODEL=devstral-2  # Use the free model
```

**💡 Pro Tip:** Add `.env` to your `.gitignore` file to prevent accidental commits:
```gitignore
# Add this to your .gitignore
.env
*.env
.env*.local
```

### 4. Verify Your Setup

Test your API key configuration:
```bash
# Check if environment variable is set
echo $MISTRAL_API_KEY  # Should show your key (macOS/Linux)
$env:MISTRAL_API_KEY   # Should show your key (Windows)

# Test Mistral Vibe connection
mistral-vibe test-api
```

**✅ Billing Information:**
- **Current promotion**: Devstral-2 model is FREE
- **Standard pricing**: Pay-as-you-go for advanced models
- **Free tier**: Smaller models available for free usage
- **Student benefits**: Check [Mistral AI Education](https://mistral.ai/education) for special programs

---

## 📋 Common Prerequisites

### 1. Install Python

Mistral Vibe requires **Python 3.8 or higher** :

#### Windows
```bash
# Check version
python --version

# If Python is not installed:
# 1. Download from [python.org](https://www.python.org/downloads/windows/)
# 2. Check "Add Python to PATH" during installation
# 3. Restart your terminal
```

#### macOS
```bash
# Check version
python3 --version

# If Python is not installed (via Homebrew):
brew install python

# Or from official site:
# Download from [python.org](https://www.python.org/downloads/mac-osx/)
```

---

## 🛠️ Environment Setup

### 1. Create a Virtual Environment

#### Windows
```bash
# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate
```

#### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate
```

✅ **Your terminal should now display `(venv)`** indicating the environment is active.

---

## 🤖 Using Mistral Vibe

### 1. Launch Mistral Vibe

Open Mistral Vibe in your terminal and start a new session.

### 2. Describe Your Project

**Be precise** for best results:

**Example for a project like "Gare Ton Char"**:
> "I want to create a web application to showcase an intelligent parking project called 'Gare Ton Char'. The site should include: a home page with a demo video, a section explaining AI features, a link to the mobile app, and a contact form for partners."

**Tips**:
- Mention desired technologies (React, Flask, etc.)
- Specify key features
- Indicate if API integration is needed

### 3. Plan with Mistral Vibe

Ask for a structured work plan:
> "Generate a step-by-step plan for this project with necessary checks at each phase."

Mistral Vibe will create a detailed plan with:
- Specific tasks
- Recommended tools
- Checkpoints

### 4. Execute Commands Automatically

Mistral Vibe can execute commands for you:

#### Windows
```bash
mistral-vibe run "Create a folder 'gare-ton-char' with subfolders: src, public, components, assets"
mistral-vibe run "Install react, react-dom, and axios via npm"
```

#### macOS/Linux
```bash
mistral-vibe run "Create a folder 'gare-ton-char' with subfolders: src, public, components, assets"
mistral-vibe run "Install react, react-dom, and axios via npm"
```

### 5. Verification and Validation

Validate work at each step:

```bash
# Check structure
mistral-vibe check "Verify all necessary files are present"

# Test code
mistral-vibe test "Run unit tests for React components"
```

---

## 🎯 Specific Configuration for AI & Mobility

### Install AI Tools

For projects like "Gare Ton Char":

```bash
# Install AI dependencies
mistral-vibe run "Install tensorflow scikit-learn pandas numpy matplotlib"

# Configure data environment
mistral-vibe run "Create a 'data' folder for mobility datasets"

# Install visualization tools
mistral-vibe run "Install plotly seaborn geopandas"
```

### Terminal Configuration

#### Windows (PowerShell)
```bash
# Customize terminal
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Import-Module posh-git
Import-Module oh-my-posh

# Install recommended fonts
mistral-vibe run "Install Cascadia Code and Fira Code fonts"
```

#### macOS (Terminal/iTerm2)
```bash
# Install command line tools
xcode-select --install

# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install useful tools
brew install git wget curl tree htop

# Install fonts
brew tap homebrew/cask-fonts
brew install --cask font-cascadia-code font-fira-code
```

---

## 💻 Development with AI Assistance

Use Mistral Vibe to:

### 1. Generate Code
> "Create a React component to display an interactive parking map with Leaflet"

### 2. Integrate APIs
> "Add integration with Google Maps API for real-time geolocation"

### 3. Optimize Performance
> "Analyze and optimize code for mobile performance with lazy loading techniques"

### 4. Manage Data
> "Create a processing pipeline for urban mobility data using Pandas"

---

## 🔧 Troubleshooting

### Common Issues and Solutions

| Issue | Windows Solution | macOS Solution |
|-------|------------------|----------------|
| `Python not found` | Check PATH | `brew link python` |
| `venv not activated` | `venv\Scripts\activate` | `source venv/bin/activate` |
| Commands blocked | Run as admin | `chmod +x` on scripts |
| Dependency errors | `pip install --upgrade` | `pip3 install --upgrade` |
| Slow terminal | Use PowerShell 7+ | Use iTerm2 |

---

## 📚 Additional Resources

- [Official Mistral Vibe Documentation](#) *(coming soon)*
- [Advanced Guide for AI Projects](#) *(coming soon)*
- [Student Project Examples](#) *(coming soon)*

---

**Ready to revolutionize your development?** With this guide, set up Mistral Vibe on any platform and create innovative applications faster than ever! 🚀