
# --- IMPORTS ---
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.button import MDRaisedButton
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from kivy.core.window import Window
from kivy.uix.image import Image
from bs4 import BeautifulSoup
from duckduckgo_search import ddg
import smtplib, datetime, requests, os, json, webbrowser

Window.size = (400, 700)

# --- CONFIG ---
EMAIL_SENDER = "hariprakashk0@gmail.com"
EMAIL_PASSWORD = "lkcnhukifxrjphwi"
SENT_JOBS_FILE = "sent_jobs.json"
BG_CONFIG_FILE = "background_config.json"
DEFAULT_BG = "background.png"

# --- DATA FUNCTIONS ---
def fetch_jobs_ddgs(keyword, location, min_exp=0, max_exp=10, max_results=10):
    query = f"{keyword} jobs in {location} {min_exp}-{max_exp} years experience"
    jobs = []
    seen = load_sent_jobs()
    results = ddg(query, region="in-en", safesearch="moderate", max_results=max_results)
    for r in results:
        title, link, desc = r.get("title", ""), r.get("href", ""), r.get("body", "")
        if title and link and link not in seen:
            jobs.append({"title": title, "link": link, "desc": desc or "No description available"})
    return jobs

def load_sent_jobs():
    if not os.path.exists(SENT_JOBS_FILE):
        return set()
    with open(SENT_JOBS_FILE, "r") as f:
        return set(json.load(f))

def save_sent_jobs(job_links):
    existing = load_sent_jobs()
    updated = existing.union(job_links)
    with open(SENT_JOBS_FILE, "w") as f:
        json.dump(list(updated), f)

def send_job_email(receiver_email, keyword="Data Analyst", location="India", min_exp=0, max_exp=3):
    jobs = fetch_jobs_ddgs(keyword, location, min_exp, max_exp)
    if not jobs:
        return "No new jobs found matching your filters."

    message = MIMEMultipart("alternative")
    message["Subject"] = f"🔍 {keyword} Jobs – {datetime.datetime.now():%d %b %Y}"
    message["From"] = EMAIL_SENDER
    message["To"] = receiver_email

    html_content = f"<h2>🧠 {keyword} Jobs in {location} ({min_exp}-{max_exp} yrs)</h2><ul>"
    sent_links = []

    for job in jobs:
        html_content += f"""
        <li>
            <b>{job['title']}</b><br>
            🔗 <a href="{job['link']}">{job['link']}</a><br>
            📝 {job['desc']}<br><hr>
        </li>
        """
        sent_links.append(job['link'])

    html_content += "</ul><p>— Sent by Smart Job Bot 🤖</p>"
    message.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, receiver_email, message.as_string())

    save_sent_jobs(sent_links)
    return f"✅ Sent {len(jobs)} job(s) to {receiver_email}!"

def send_custom_message(receiver_email, message_text):
    message = MIMEText(message_text, "plain")
    message["Subject"] = "📨 Message from Love App"
    message["From"] = EMAIL_SENDER
    message["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, receiver_email, message.as_string())
    return "✅ Custom message sent!"

def search_web(query, max_results=3):
    results = ddg(query, region="in-en", safesearch="moderate", max_results=max_results)
    return results if results else []

def summarize_page(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = ' '.join([p.text for p in paragraphs[:6]])
        return content[:1200] + "..." if len(content) > 1200 else content
    except Exception as e:
        return f"⚠️ Failed to summarize: {e}"

def get_background_image():
    if os.path.exists(BG_CONFIG_FILE):
        with open(BG_CONFIG_FILE, "r") as f:
            path = json.load(f).get("bg")
            if path and os.path.exists(path):
                return path
    return DEFAULT_BG

# --- UI LAYOUT ---
KV = '''
ScreenManager:
    HomeScreen:
    WebSearchScreen:
    MessageScreen:
    SendJobScreen:

<HomeScreen>:
    name: "home"
    MDFloatLayout:
        Image:
            source: app.bg_path
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1

        MDIconButton:
            icon: "theme-light-dark"
            pos_hint: {"x": 0.01, "top": 0.99}
            on_release: app.toggle_theme()

        MDIconButton:
            icon: "image"
            pos_hint: {"x": 0.85, "top": 0.99}
            on_release: app.open_file_manager()

        MDLabel:
            text: "[b][color=#FF69B4]❤ Love ❤[/color][/b]"
            markup: True
            halign: "center"
            font_style: "H5"
            pos_hint: {"center_y": 0.92}

        MDRaisedButton:
            text: "Send Job Email"
            pos_hint: {"center_x": 0.5, "center_y": 0.52}
            on_release: app.switch_screen("sendjob")

        MDRaisedButton:
            text: "Ask Web Bot"
            pos_hint: {"center_x": 0.5, "center_y": 0.38}
            on_release: app.switch_screen("web")

        MDRaisedButton:
            text: "Send Custom Message"
            pos_hint: {"center_x": 0.5, "center_y": 0.26}
            on_release: app.switch_screen("message")

<SendJobScreen>:
    name: "sendjob"
    MDFloatLayout:
        Image:
            source: app.bg_path
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1

        MDIconButton:
            icon: "theme-light-dark"
            pos_hint: {"x": 0.01, "top": 0.99}
            on_release: app.toggle_theme()

        MDRaisedButton:
            text: "⬅ Back"
            pos_hint: {"right": 0.98, "top": 0.99}
            on_release: app.switch_screen("home")

        MDTextField:
            id: receiver_email
            hint_text: "Receiver email"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            size_hint_x: 0.85

        MDTextField:
            id: keyword_input
            hint_text: "Keyword (e.g., Business Analyst)"
            pos_hint: {"center_x": 0.5, "center_y": 0.67}
            size_hint_x: 0.85

        MDTextField:
            id: location_input
            hint_text: "Location"
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            size_hint_x: 0.85

        MDTextField:
            id: min_exp
            hint_text: "Min Exp"
            pos_hint: {"center_x": 0.3, "center_y": 0.52}
            size_hint_x: 0.35
            input_filter: "int"

        MDTextField:
            id: max_exp
            hint_text: "Max Exp"
            pos_hint: {"center_x": 0.7, "center_y": 0.52}
            size_hint_x: 0.35
            input_filter: "int"

        MDRaisedButton:
            text: "Send Job Email"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.send_email()

<WebSearchScreen>:
    name: "web"
    MDFloatLayout:
        Image:
            source: app.bg_path
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1

        MDIconButton:
            icon: "theme-light-dark"
            pos_hint: {"x": 0.01, "top": 0.99}
            on_release: app.toggle_theme()

        MDRaisedButton:
            text: "⬅ Back"
            pos_hint: {"right": 0.98, "top": 0.99}
            on_release: app.switch_screen("home")

        MDTextField:
            id: query_input
            hint_text: "Enter your question"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            size_hint_x: 0.85

        MDRaisedButton:
            text: "Search"
            pos_hint: {"center_x": 0.5, "center_y": 0.63}
            on_release: app.do_search()

        ScrollView:
            size_hint: (1, 0.5)
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            MDLabel:
                id: result_label
                text: ""
                markup: True
                size_hint_y: None
                height: self.texture_size[1]
                halign: "left"
                on_ref_press: app.on_ref_press

<MessageScreen>:
    name: "message"
    MDFloatLayout:
        Image:
            source: app.bg_path
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1

        MDRaisedButton:
            text: "⬅ Back"
            pos_hint: {"right": 0.98, "top": 0.99}
            on_release: app.switch_screen("home")

        MDTextField:
            id: msg_email
            hint_text: "Receiver email"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            size_hint_x: 0.85

        MDTextField:
            id: msg_content
            hint_text: "Type your message"
            multiline: True
            pos_hint: {"center_x": 0.5, "center_y": 0.58}
            size_hint_x: 0.85
            height: "120dp"

        MDRaisedButton:
            text: "Send"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.send_custom_message()
'''

# --- SCREENS ---
class HomeScreen(Screen): pass
class WebSearchScreen(Screen): pass
class MessageScreen(Screen): pass
class SendJobScreen(Screen): pass

# --- MAIN APP ---
class CombinedBotApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bg_path = get_background_image()
        self.file_manager = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def toggle_theme(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

    def switch_screen(self, name):
        self.root.current = name

    def send_email(self):
        screen = self.root.get_screen("sendjob")
        email = screen.ids.receiver_email.text.strip()
        keyword = screen.ids.keyword_input.text.strip() or "Data Analyst"
        location = screen.ids.location_input.text.strip() or "India"
        try:
            min_exp = int(screen.ids.min_exp.text.strip() or 0)
            max_exp = int(screen.ids.max_exp.text.strip() or 3)
            if min_exp < 0 or max_exp > 10 or min_exp > max_exp:
                raise ValueError
        except ValueError:
            self.dialog = MDDialog(title="Invalid Input", text="❗ Experience must be 0 to 10 years.")
            self.dialog.open()
            return

        if not email or "@" not in email:
            self.dialog = MDDialog(title="Invalid Email", text="❗ Enter valid receiver email.")
            self.dialog.open()
            return

        result = send_job_email(email, keyword, location, min_exp, max_exp)
        self.dialog = MDDialog(title="Job Email", text=result)
        self.dialog.open()

    def send_custom_message(self):
        screen = self.root.get_screen("message")
        email = screen.ids.msg_email.text.strip()
        msg = screen.ids.msg_content.text.strip()
        if not email or not msg:
            self.dialog = MDDialog(title="Invalid", text="❗ Fill both fields.")
            self.dialog.open()
            return
        result = send_custom_message(email, msg)
        self.dialog = MDDialog(title="Message", text=result)
        self.dialog.open()

    def do_search(self):
        screen = self.root.get_screen("web")
        query = screen.ids.query_input.text.strip()
        if not query:
            screen.ids.result_label.text = "[color=ff0000]❗ Please enter a question.[/color]"
            return
        results = search_web(query)
        if not results:
            screen.ids.result_label.text = "❌ No results found."
            return
        combined = ""
        for r in results:
            summary = summarize_page(r['href'])
            link = f"[ref={r['href']}][color=0000ee]{r['title']}[/color][/ref]"
            combined += f"{link}\n[i]{summary}[/i]\n\n"
        screen.ids.result_label.text = combined

    def on_ref_press(self, instance, ref):
        webbrowser.open(ref)

    def open_file_manager(self):
        if not self.file_manager:
            self.file_manager = MDFileManager(select_path=self.select_bg_image, exit_manager=self.exit_file_manager)
        self.file_manager.show(os.getcwd())

    def select_bg_image(self, path):
        self.bg_path = path
        with open(BG_CONFIG_FILE, "w") as f:
            json.dump({"bg": path}, f)
        self.file_manager.close()
        self.root.clear_widgets()
        self.root.add_widget(self.build())

    def exit_file_manager(self, *args):
        self.file_manager.close()

if __name__ == "__main__":
    CombinedBotApp().run()
