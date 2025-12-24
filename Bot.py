# --- IMPORTS ---
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.list import OneLineAvatarListItem, MDList
from kivymd.uix.list import IconLeftWidget
from kivy.core.window import Window
from functools import partial
from datetime import datetime

Window.size = (400, 700)

# --- SCREENS ---
class LoginScreen(Screen): pass
class HomeScreen(Screen): pass
class WebSearchScreen(Screen): pass
class MessageScreen(Screen): pass
class SendJobScreen(Screen): pass
class TicketScreen(Screen): pass
class TicketsScreen(Screen): pass

# --- KV LAYOUT ---
KV = r'''
ScreenManager:
    id: screen_manager
    LoginScreen:
    HomeScreen:
    WebSearchScreen:
    MessageScreen:
    SendJobScreen:
    TicketScreen:
    TicketsScreen:

<HomeScreen>:
    name: "home"
    MDLabel:
        id: welcome_label
        text: ""
        halign: "left"
        pos_hint: {"x":0.05, "y":0.94}
        theme_text_color: "Custom"
        text_color: 0,0,0,1
    MDFloatLayout:
        canvas.before:
            Color:
                rgba: 0.98, 0.98, 0.98, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [20,]

        MDLabel:
            text: "[b]Smart Bot Hub 🤖[/b]"
            markup: True
            halign: "center"
            font_style: "H4"
            font_name: "C:\\Windows\\Fonts\\calibri.ttf"
            pos_hint: {"center_y": 0.85}
            theme_text_color: "Custom"
            text_color: 0,0,0,1

        MDRectangleFlatIconButton:
            text: "Send Job Email"
            icon: "email"
            pos_hint: {"center_x": 0.5, "center_y": 0.65}
            on_release: app.switch_screen("sendjob")

        MDRectangleFlatIconButton:
            text: "Ask Web Bot"
            icon: "web"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release: app.switch_screen("web")

        MDRectangleFlatIconButton:
            text: "Send Custom Message"
            icon: "message-text"
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            on_release: app.switch_screen("message")

        MDRectangleFlatIconButton:
            text: "Create Ticket"
            icon: "ticket-outline"
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_release: app.switch_screen("ticket")

        MDRectangleFlatIconButton:
            text: "Logout"
            icon: "logout"
            pos_hint: {"x":0.75, "y":0.92}
            on_release: app.logout()

        MDRectangleFlatIconButton:
            text: "View Tickets"
            icon: "clipboard-list"
            pos_hint: {"center_x": 0.5, "center_y": 0.06}
            on_release: app.view_tickets_screen()

<WebSearchScreen>:
    name: "web"
    MDFloatLayout:
        canvas.before:
            Color:
                rgba: 0.98, 0.98, 0.98, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [20,]

        MDLabel:
            text: "[b]Web Search[/b]"
            markup: True
            halign: "center"
            font_style: "H5"
            font_name: "C:\\Windows\\Fonts\\calibri.ttf"
            pos_hint: {"center_y": 0.8}
            theme_text_color: "Custom"
            text_color: 0,0,0,1

        MDTextField:
            id: search_input
            hint_text: "Enter search query"
            pos_hint: {"center_x":0.5, "center_y":0.55}
            size_hint_x: 0.85

        MDRectangleFlatIconButton:
            text: "Search"
            icon: "web"
            pos_hint: {"center_x":0.5, "center_y":0.38}
            on_release: app.do_web_search()

        MDRectangleFlatIconButton:
            text: "Back"
            icon: "arrow-left"
            pos_hint: {"x":0.05, "y":0.9}
            on_release: app.switch_screen("home")

<LoginScreen>:
    name: "login"
    MDFloatLayout:
        canvas.before:
            Color:
                rgba: 0.98, 0.98, 0.98, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [20,]

        MDLabel:
            text: "[b]Please Log In[/b]"
            markup: True
            halign: "center"
            font_style: "H5"
            font_name: "C:\\Windows\\Fonts\\calibri.ttf"
            pos_hint: {"center_y": 0.84}
            theme_text_color: "Custom"
            text_color: 0,0,0,1

        MDTextField:
            id: username
            hint_text: "Username"
            pos_hint: {"center_x":0.5, "center_y":0.62}
            size_hint_x: 0.85

        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            pos_hint: {"center_x":0.5, "center_y":0.5}
            size_hint_x: 0.85

        MDRectangleFlatIconButton:
            text: "Login"
            icon: "login"
            pos_hint: {"center_x":0.5, "center_y":0.36}
            on_release: app.login()

<MessageScreen>:
    name: "message"
    MDFloatLayout:
        canvas.before:
            # very pale lavender so black text is clearly visible
            Color:
                rgba: 0.99, 0.96, 0.99, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [20,]

        MDLabel:
            text: "[b]Send a Message[/b]"
            markup: True
            halign: "center"
            font_style: "H5"
            font_name: "C:\\Windows\\Fonts\\calibri.ttf"
            pos_hint: {"center_y": 0.78}
            theme_text_color: "Custom"
            text_color: 0,0,0,1

        MDTextField:
            id: message_input
            hint_text: "Type your message here"
            pos_hint: {"center_x":0.5, "center_y":0.55}
            size_hint_x: 0.85
            multiline: True
            text_color: 0,0,0,1
            hint_text_color: 0.45,0.45,0.45,1

        MDRectangleFlatIconButton:
            text: "Send"
            icon: "send"
            pos_hint: {"center_x":0.5, "center_y":0.38}
            on_release: app.send_message()

        MDRectangleFlatIconButton:
            text: "Back"
            icon: "arrow-left"
            pos_hint: {"x":0.05, "y":0.9}
            on_release: app.switch_screen("home")

<TicketScreen>:
    name: "ticket"
    MDFloatLayout:
        canvas.before:
            Color:
                rgba: 0.98, 0.99, 1, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [20,]

        MDLabel:
            text: "[b]Create Ticket[/b]"
            markup: True
            halign: "center"
            font_style: "H5"
            font_name: "C:\\Windows\\Fonts\\calibri.ttf"
            pos_hint: {"center_y": 0.86}
            theme_text_color: "Custom"
            text_color: 0,0,0,1

        MDTextField:
            id: ticket_title
            hint_text: "Ticket title"
            pos_hint: {"center_x":0.5, "center_y":0.68}
            size_hint_x: 0.85
            text_color: 0,0,0,1
            hint_text_color: 0.45,0.45,0.45,1

        MDTextField:
            id: ticket_desc
            hint_text: "Describe the issue"
            pos_hint: {"center_x":0.5, "center_y":0.5}
            size_hint_x: 0.85
            multiline: True
            text_color: 0,0,0,1
            hint_text_color: 0.45,0.45,0.45,1

        MDRectangleFlatIconButton:
            text: "Submit Ticket"
            icon: "ticket-confirm"
            pos_hint: {"center_x":0.5, "center_y":0.3}
            on_release: app.create_ticket()

        MDRectangleFlatIconButton:
            text: "Back"
            icon: "arrow-left"
            pos_hint: {"x":0.05, "y":0.9}
            on_release: app.switch_screen("home")

<TicketsScreen>:
    name: "tickets"
    MDFloatLayout:
        canvas.before:
            Color:
                rgba: 0.98, 0.98, 1, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [20,]

        MDLabel:
            text: "[b]Tickets[/b]"
            markup: True
            halign: "center"
            font_style: "H5"
            font_name: "C:\\Windows\\Fonts\\calibri.ttf"
            pos_hint: {"center_y": 0.94}
            theme_text_color: "Custom"
            text_color: 0,0,0,1

        ScrollView:
            pos_hint: {"x":0.05, "y":0.06}
            size_hint: 0.9, 0.78
            MDList:
                id: tickets_list

        MDRectangleFlatIconButton:
            text: "Back"
            icon: "arrow-left"
            pos_hint: {"x":0.05, "y":0.9}
            on_release: app.switch_screen("home")

<SendJobScreen>:
    name: "sendjob"
    MDFloatLayout:
        canvas.before:
            # very pale mint green so black text is clearly visible
            Color:
                rgba: 0.98, 1, 0.98, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [20,]

        MDLabel:
            text: "[b]Job Email Sender[/b]"
            markup: True
            halign: "center"
            font_style: "H5"
            font_name: "C:\\Windows\\Fonts\\calibri.ttf"
            pos_hint: {"center_y": 0.9}
            theme_text_color: "Custom"
            text_color: 0,0,0,1

        MDTextField:
            id: recipient
            hint_text: "Recipient email"
            pos_hint: {"center_x":0.5, "center_y":0.68}
            size_hint_x: 0.85
            text_color: 0,0,0,1
            hint_text_color: 0.45,0.45,0.45,1

        MDTextField:
            id: subject
            hint_text: "Subject"
            pos_hint: {"center_x":0.5, "center_y":0.56}
            size_hint_x: 0.85
            text_color: 0,0,0,1
            hint_text_color: 0.45,0.45,0.45,1

        MDTextField:
            id: job_body
            hint_text: "Message body"
            pos_hint: {"center_x":0.5, "center_y":0.44}
            size_hint_x: 0.85
            multiline: True
            text_color: 0,0,0,1
            hint_text_color: 0.45,0.45,0.45,1

        MDRectangleFlatIconButton:
            text: "Send Job"
            icon: "email-send"
            pos_hint: {"center_x":0.5, "center_y":0.28}
            on_release: app.send_job()

        MDRectangleFlatIconButton:
            text: "Back"
            icon: "arrow-left"
            pos_hint: {"x":0.05, "y":0.9}
            on_release: app.switch_screen("home")
'''

# --- MAIN APP ---
class CombinedBotApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        root = Builder.load_string(KV)
        root.transition = FadeTransition(duration=0.12)  # subtle transition
        # app state
        self.authenticated = False
        self.user = None
        self.tickets = []  # simple in-memory ticket store
        # start at login screen
        root.current = 'login'
        return root

    def switch_screen(self, name):
        # use fade transition and a subtle fade-in animation for the target screen
        from kivy.animation import Animation
        self.root.transition = FadeTransition(duration=0.12)
        screen = self.root.get_screen(name)
        # start from transparent and fade in
        screen.opacity = 0
        self.root.current = name
        Animation(opacity=1, duration=0.12).start(screen)

    def do_web_search(self):
        try:
            query = self.root.get_screen('web').ids.search_input.text.strip()
            if not query:
                self.notify("Please enter a search query.")
                return
            import webbrowser
            from urllib.parse import quote_plus
            url = "https://www.google.com/search?q=" + quote_plus(query)
            webbrowser.open(url)
        except Exception as e:
            self.notify(f"Search failed: {e}")

    def login(self):
        try:
            uname = self.root.get_screen('login').ids.username.text.strip()
            pwd = self.root.get_screen('login').ids.password.text.strip()
            if not uname or not pwd:
                self.notify("Please enter both username and password.")
                return
            # simple auth: accept any non-empty credentials (demo)
            self.authenticated = True
            self.user = uname
            # update welcome label
            try:
                self.root.get_screen('home').ids.welcome_label.text = f"Welcome, {self.user}"
            except Exception:
                pass
            # clear password field
            self.root.get_screen('login').ids.password.text = ""
            self.switch_screen('home')
        except Exception as e:
            self.notify(f"Login failed: {e}")

    def logout(self):
        self.authenticated = False
        self.user = None
        self.root.current = 'login'

    def create_ticket(self):
        try:
            title = self.root.get_screen('ticket').ids.ticket_title.text.strip()
            desc = self.root.get_screen('ticket').ids.ticket_desc.text.strip()
            if not title:
                self.notify("Please enter a ticket title.")
                return
            ticket = {"title": title, "desc": desc, "user": self.user, "status": "Open", "created": datetime.now().isoformat()}
            self.tickets.append(ticket)
            self.notify(f"Ticket created: {title}")
            # clear fields
            self.root.get_screen('ticket').ids.ticket_title.text = ""
            self.root.get_screen('ticket').ids.ticket_desc.text = ""
        except Exception as e:
            self.notify(f"Create ticket failed: {e}")

    def view_tickets(self):
        try:
            if not self.tickets:
                self.notify("No tickets yet.")
                return
            # build text list
            parts = []
            for i, t in enumerate(self.tickets, 1):
                parts.append(f"{i}. {t['title']} (by {t.get('user','unknown')})\n{t['desc']}")
            text = "\n\n".join(parts)
            self.notify(text)
        except Exception as e:
            self.notify(f"View tickets failed: {e}")

    def view_tickets_screen(self):
        """Populate the TicketsScreen list and switch to it."""
        try:
            screen = self.root.get_screen('tickets')
            lst = screen.ids.tickets_list
            lst.clear_widgets()
            # add items
            for i, t in enumerate(self.tickets):
                text = f"{t['title']} — {t['status']}"
                item = OneLineAvatarListItem(text=text)
                # show icon at left
                icon = IconLeftWidget(icon='ticket-outline')
                item.add_widget(icon)
                # bind selecting to show details
                item.bind(on_release=partial(self.show_ticket_detail, i))
                lst.add_widget(item)
            self.switch_screen('tickets')
        except Exception as e:
            self.notify(f"Failed to load tickets: {e}")

    def show_ticket_detail(self, index, *args):
        """Show a popup with ticket details and allow status changes."""
        try:
            t = self.tickets[index]
            from kivy.uix.boxlayout import BoxLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            from kivy.uix.popup import Popup

            content = BoxLayout(orientation='vertical', spacing=8, padding=8)
            lbl = Label(text=f"Title: {t['title']}\nBy: {t.get('user','unknown')}\n\n{t['desc']}\n\nStatus: {t['status']}\nCreated: {t.get('created','')}", halign='left', valign='top')
            lbl.bind(width=lambda inst, w: setattr(inst, 'text_size', (w, None)))
            btn_layout = BoxLayout(size_hint_y=None, height='40dp', spacing=8)
            btn_close = Button(text='Close')
            btn_inprog = Button(text='In Progress')
            btn_close_ticket = Button(text='Close Ticket')

            def set_status(new_status, *_):
                t['status'] = new_status
                popup.dismiss()
                self.view_tickets_screen()

            btn_layout.add_widget(btn_inprog)
            btn_layout.add_widget(btn_close_ticket)
            btn_layout.add_widget(btn_close)
            btn_inprog.bind(on_release=lambda *_: set_status('In Progress'))
            btn_close_ticket.bind(on_release=lambda *_: set_status('Closed'))
            btn_close.bind(on_release=lambda *_: popup.dismiss())
            content.add_widget(lbl)
            content.add_widget(btn_layout)
            popup = Popup(title=f"Ticket: {t['title']}", content=content, size_hint=(0.9, 0.7))
            popup.open()
        except Exception as e:
            self.notify(f"Show ticket failed: {e}")

    def send_message(self):
        try:
            msg = self.root.get_screen('message').ids.message_input.text.strip()
            if not msg:
                self.notify("Please enter a message to send.")
                return
            # placeholder: just show confirmation
            self.notify("Message sent:\n" + msg)
            self.root.get_screen('message').ids.message_input.text = ""
        except Exception as e:
            self.notify(f"Send failed: {e}")

    def send_job(self):
        try:
            recip = self.root.get_screen('sendjob').ids.recipient.text.strip()
            subj = self.root.get_screen('sendjob').ids.subject.text.strip()
            body = self.root.get_screen('sendjob').ids.job_body.text.strip()
            if not recip:
                self.notify("Please enter a recipient email.")
                return
            # placeholder: simulate queuing an email
            self.notify(f"Job email queued to {recip}\nSubject: {subj}")
            self.root.get_screen('sendjob').ids.recipient.text = ""
            self.root.get_screen('sendjob').ids.subject.text = ""
            self.root.get_screen('sendjob').ids.job_body.text = ""
        except Exception as e:
            self.notify(f"Send job failed: {e}")

    def notify(self, msg: str):
        """Show a modal popup that stays until user taps OK."""
        try:
            if getattr(self, "_popup", None) and getattr(self, "_popup_label", None):
                self._popup_label.text = msg
                return
            from kivy.uix.boxlayout import BoxLayout
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            from kivy.uix.popup import Popup

            content = BoxLayout(orientation="vertical", spacing=10, padding=10)
            lbl = Label(text=msg, halign="left", valign="middle", size_hint_y=None)
            lbl.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)))
            lbl.bind(texture_size=lambda inst, ts: setattr(inst, "height", ts[1]))
            btn = Button(text="OK", size_hint_y=None, height="40dp")
            popup = Popup(title="Notice", content=content, size_hint=(0.8, 0.5), auto_dismiss=False)
            btn.bind(on_release=lambda *_: popup.dismiss())
            self._popup = popup
            self._popup_label = lbl
            popup.bind(on_dismiss=lambda *_: setattr(self, "_popup", None))
            popup.bind(on_dismiss=lambda *_: setattr(self, "_popup_label", None))
            content.add_widget(lbl)
            content.add_widget(btn)
            popup.open()
        except Exception as e:
            print("notify failed:", e)

if __name__ == "__main__":
    CombinedBotApp().run()
