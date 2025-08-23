# ❤️ Smart Job & Messaging Bot (KivyMD App)

This project is a **KivyMD desktop/mobile application** that combines three powerful features into a single app:  

- 📩 **Job Email Bot** → Fetches the latest jobs (via DuckDuckGo search) and emails them to any recipient.  
- 🔍 **Web Search Bot** → Asks questions, fetches search results, summarizes web pages, and displays them in-app with clickable links.  
- 💌 **Custom Messaging** → Send personalized messages directly via email.  
- 🎨 **Customizable Background** → Change the app's background with your own images.  

---

## 🚀 Features
- **Job Finder & Email Sender**
  - Search jobs by keyword, location, and experience range (0–10 years).  
  - Sends job details (title, description, and links) via Gmail.  
  - Keeps track of previously sent jobs (avoids duplicates).  

- **Smart Web Bot**
  - Search the web using `duckduckgo_search`.  
  - Summarizes the first few paragraphs of pages using `BeautifulSoup`.  
  - Clickable links to open in your browser.  

- **Messaging**
  - Send a **custom plain-text email** to any recipient.  
  - Simple form interface for email and message content.  

- **UI & Theming**
  - Built with **KivyMD** (Material Design for Kivy).  
  - Toggle between **Light/Dark theme**.  
  - Select custom background images (stored in `background_config.json`).  

---

## 🛠️ Tech Stack
- **Framework**: [Kivy](https://kivy.org/) & [KivyMD](https://kivymd.readthedocs.io/)  
- **Email**: `smtplib` with Gmail SMTP  
- **Search**: [duckduckgo_search](https://pypi.org/project/duckduckgo-search/)  
- **Web Scraping**: `BeautifulSoup`  
- **Storage**: JSON (`sent_jobs.json`, `background_config.json`)  
- **Other**: Python Standard Libraries (`datetime`, `os`, `json`, `webbrowser`, etc.)  

---

## 📂 Project Structure
