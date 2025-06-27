from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        # Load an image from the local filesystem
        img = Image(source='/Users/rmn7591/Documents/Repositories/-30DaysOfPython/season3/Building GUIs with Kivy/abcd.png')  # Replace with your image path
        return img


if __name__ == "__main__":
    MainApp().run()
