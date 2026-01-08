---
layout: page
permalink: /ia-mobilite/vibe-workshop/
title: Vibe Coding Workshop - Create with AI
description: Practical workshop to discover AI-assisted development with Mistral Vibe - Perfect for programming beginners
title-fr: Atelier Vibe Coding - Créer avec l'IA
lang: en
page_id: vibe-workshop
---

# 🎨 Vibe Coding Workshop: Your First Web Project with AI

**Welcome to the era of AI-assisted development!** This workshop will guide you step by step to create your first website with the help of **Mistral Vibe**, even if you have **no programming experience**.

**🎯 Workshop Objectives:**
- Understand how AI assistants work for development
- Create a functional website to present your project
- Learn to collaborate effectively with Mistral Vibe
- Discover AI possibilities for engineering and mobility

**📚 Target Audience:** Engineering students in automotive field with no programming experience

---

## 🤖 Understanding Mistral Vibe and Its Capabilities

### **1. What is Mistral Vibe?**

Mistral Vibe is an **AI-powered development assistant** that can help you:

- **Write code** in different languages (HTML, CSS, JavaScript, Python, etc.)
- **Create project structures** automatically
- **Generate web designs** and prototypes
- **Analyze data** and create visualizations
- **Automate repetitive** development tasks

**💡 How it works:** You describe what you want in natural language, and Mistral Vibe generates the corresponding code!

### **2. Use Cases for Your Project**

**For this workshop, we'll focus on:**

| Domain | Example Tasks | Benefits for You |
|---------|-------------------|-------------------|
| **Web Development** | Create HTML pages, add CSS, JavaScript | Present your project professionally |
| **Prototyping** | Create mockups, test ideas quickly | Visualize concepts before development |
| **Data Analysis** | Process mobility data, create charts | Analyze real transportation data |
| **Automation** | Generate repetitive code, create scripts | Save time on technical tasks |

**🎓 Why this is important for you:**
- **Save time:** Focus on your ideas, not syntax
- **Learn gradually:** AI guides you and explains code
- **Rapid prototyping:** Test concepts in minutes
- **Professional preparation:** These tools are used in industry

---

## 🛠️ Setting Up Your Environment

### **1. Follow the Installation Guide**

Before starting, make sure everything is installed:

👉 **[Mistral Vibe Complete Guide](/ia-mobilite/guide-mistral-vibe/)**

**What you need:**
- ✅ Python 3.8+ installed
- ✅ Mistral Vibe configured
- ✅ Your Mistral AI API key (free for students)
- ✅ A working terminal (PowerShell, Terminal, or iTerm2)

### **2. Test Your Configuration**

Open a terminal and verify everything works:

```bash
# Check if Mistral Vibe is accessible
mistral-vibe --version

# Check if your API key is configured
echo $MISTRAL_API_KEY  # macOS/Linux
$env:MISTRAL_API_KEY   # Windows

# Test connection (should return "OK")
mistral-vibe test-api
```

**⚠️ If something doesn't work:**
1. Recheck the installation guide
2. Verify you followed all steps correctly
3. Ask the teacher for help

---

## 🧪 Simple Experiments to Start

### **1. Your First Project with Vibe**

Create a folder for your workshop and start exploring:

```bash
# Create a folder for the workshop
mkdir my-vibe-project
cd my-vibe-project

# Ask Mistral Vibe to create a basic structure
mistral-vibe run "Create a web project structure with:
- a 'src' folder for code
- an 'assets' folder for images
- a 'docs' folder for documentation
- a basic 'index.html' file
- a 'README.md' file to describe the project"
```

**📁 Explore what was created:**
```bash
# List created files
ls -la

# Open the created HTML file
# On Windows: start index.html
# On macOS: open index.html
```

### **2. Modify and Improve**

Now ask Mistral Vibe to enhance your project:

```bash
# Add content to the HTML file
mistral-vibe run "In index.html, add:
- a title 'My Smart Mobility Project'
- a paragraph describing an intelligent parking project
- an 'About' section with your name
- a footer with today's date"

# Create a CSS file for styling
mistral-vibe run "Create a 'style.css' file in assets/ with:
- a modern font
- blue and white colors
- mobile-responsive design
- simple animations"
```

### **3. Experiment with Different Content Types**

Try these commands to understand capabilities:

```bash
# Generate content for your project
mistral-vibe run "Create a 'project.md' file explaining:
- objectives of an intelligent parking system
- technologies used (AI, sensors, applications)
- benefits for users and the city"

# Create a simple Python script
mistral-vibe run "Create an 'analysis.py' script that:
- reads a CSV data file
- calculates basic statistics
- generates a simple report"

# Generate project ideas
mistral-vibe run "Give me 5 innovative ideas to improve urban mobility using AI"
```

**💡 Tips for better requests:**
- Be **specific** in your requests
- Give **examples** when possible
- Ask for **explanations** if code isn't clear
- Don't hesitate to **ask for modifications**

---

## 🌐 Main Project: Create Your Project Website

### **1. Prepare Your Project**

**Required materials:**
- A document describing your project (Word, PDF, or notes)
- Images or diagrams if available
- A clear idea of what you want to present

**📝 Plan your website:**
1. **Home page:** General project presentation
2. **"About" page:** Your team and objectives
3. **"Technology" page:** Technical solutions used
4. **"Impact" page:** Benefits for mobility
5. **"Contact" page:** How to reach you

### **2. Step-by-Step Methodology**

#### **Step 1: Planning (15-30 minutes)**

```bash
# Create a detailed plan with Mistral Vibe
mistral-vibe run "Help me plan a website for my smart parking project.
The site should include:
- A home page with a banner and description
- A section explaining the technology used
- An image or diagram gallery
- A contact page with a form
Give me a complete HTML structure with comments."
```

**📋 Check the generated plan:**
- Is the code well organized?
- Are all necessary sections present?
- Are the comments clear?

#### **Step 2: Create Structure (30-45 minutes)**

```bash
# Create the basic HTML structure
mistral-vibe run "Generate complete HTML code for my website according to the plan.
Include:
- Navigation between pages
- Placeholders for content
- Modern and professional design
- Well-commented code so I can understand it"

# Create the corresponding CSS file
mistral-vibe run "Generate CSS for my website with:
- A blue and white theme (mobility colors)
- A professional font
- Mobile-responsive design
- Subtle animations"
```

**🔍 Test locally:**
```bash
# Open your page in a browser
# On Windows: start index.html
# On macOS: open index.html

# Check that:
- Design is consistent
- Navigation works
- Site is readable on mobile
```

#### **Step 3: Add Content (45-60 minutes)**

Now customize with your real content:

```bash
# Add your specific content
mistral-vibe run "Help me add content to my home page:
- A title: 'Gare Ton Char - Smart Parking Solution'
- A subtitle: 'Revolutionizing urban parking with AI'
- A paragraph explaining our project in 3-4 sentences
- A list of main features"

# Add images
mistral-vibe run "Show me how to add images to my site.
Explain how to:
- Create an image gallery
- Add captions
- Optimize images for the web"
```

**📸 For your images:**
- Use project diagrams
- Add screenshots if available
- Use royalty-free images (Unsplash, Pexels)

#### **Step 4: Enhancements (30-45 minutes)**

Once the base is complete, improve your site:

```bash
# Add a contact form
mistral-vibe run "Create a complete contact form with:
- Fields for name, email, message
- Input validation
- A styled submit button
- Spam protection"

# Add interactive elements
mistral-vibe run "Add an interactive map to my site.
Use a simple solution like:
- A Leaflet or Google Maps map
- Mark the location of our project
- Add an explanatory legend"

# Improve the design
mistral-vibe run "Suggest 3 design improvements for my site:
1. A welcome animation
2. Hover effects
3. A progress bar"
```

### **3. Validation and Testing**

**✅ Checklist before finishing:**

```bash
# Test all features
mistral-vibe run "Create a test checklist for my website"
```

**Tests to perform:**
- [ ] All pages display correctly
- [ ] Navigation works between pages
- [ ] Site is readable on mobile (test with your phone)
- [ ] Images display correctly
- [ ] Links work
- [ ] Contact form is usable
- [ ] Design is consistent across all pages

---

## 🤝 How to Get Help

### **1. Ask Mistral Vibe for Help**

**Examples of good questions:**
```bash
# If you don't understand something
mistral-vibe run "Explain this part of the code to me: [paste code here]"

# If something isn't working
mistral-vibe run "Why isn't my image displaying? Here's my code: [code]"

# For suggestions
mistral-vibe run "How can I improve this section? [describe section]"
```

### **2. Ask the Teacher for Help**

**When to ask for human help:**
- You've been stuck for more than 15 minutes
- You don't understand Mistral Vibe's explanations
- You need advice on project direction
- You want feedback on your design

**How to ask effectively:**
1. **Describe** what you're trying to do
2. **Show** the code or error
3. **Explain** what you've already tried
4. **Ask** a specific question

---

## 🚀 Go Further (If You Finish Early)

### **1. Experiment with Other Features**

```bash
# Mobility data analysis
mistral-vibe run "Create a Python script that:
- Analyzes traffic data
- Generates visualizations
- Predicts parking trends"

# API Integration
mistral-vibe run "Show me how to integrate a weather API into my site"

# Mobile App Creation
mistral-vibe run "Generate base code for a mobile parking app"
```

### **2. Project Ideas for Automotive Engineering**

**Projects you could explore with Mistral Vibe:**

1. **Parking Prediction System**
   - Historical data analysis
   - Available space prediction
   - IoT sensor integration

2. **Route Optimization**
   - Optimal route calculation
   - Traffic reduction
   - Public transport integration

3. **Smart Traffic Management**
   - Traffic flow analysis
   - Real-time solution proposals
   - Scenario simulation

4. **Autonomous Vehicles**
   - Behavior simulation
   - Sensor data analysis
   - Algorithm optimization

### **3. Prepare for Your Future Projects**

Use Mistral Vibe to:
- **Document** your projects
- **Create professional** presentations
- **Analyze complex** data
- **Rapidly prototype** ideas

---

## 📚 Additional Resources

- **[Mistral Vibe Documentation](https://mistral.ai/docs)** *(Official documentation)*
- **[Project Examples](https://mistral.ai/examples)** *(Inspiration for your projects)*
- **[Mistral AI Community](https://mistral.ai/community)** *(To ask questions)*

---

**🎉 Congratulations!** You've created your first website with AI assistance. You're now ready to use these tools for your engineering projects and beyond!

**💡 Remember:**
- Save your work regularly
- Experiment and have fun
- AI is here to help, not replace your creativity
- The skills you learned today are in high demand in industry

**Next steps:**
- Continue exploring Mistral Vibe's capabilities
- Apply these techniques to your real projects
- Share your creations with the community
- Stay updated with the latest AI advancements for mobility