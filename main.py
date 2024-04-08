from kivy.app import App
from kivy.uix.button import Button

class HelloWorld(App):
    def build(self):
        main_window = Button(text="hello world")
        return main_window

if __name__ == "__main__":
    app = HelloWorld()
    app.run()