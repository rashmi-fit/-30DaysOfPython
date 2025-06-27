# Build cross platform python GUI apps using kivy

# - work with kivy widgets
# - layout the Ui
# - Add events
# use the kV language
# create calculator
# package your application for
# windows, mac
# ios android

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        self.label = Label(text="Hello, Kivy!", font_size="40sp")
        button = Button(text="Click Me")
        button.bind(on_press=self.on_button_click)

        return self.label, button

    def on_button_click(self, instance):
        self.label.text = "Button Clicked!"

if __name__ == "__main__":
    MainApp().run()
