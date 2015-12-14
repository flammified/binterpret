try:
    from kivy.app import App
    from kivy.uix.widget import Widget
except ImportError as e:
    print("Kivy is not installed in your environment. --gui can not be used.")
    exit(1)

class BinterpretWidget(Widget):
    pass

class BinterpretApp(App):
    def build(self):
        return BinterpretWidget()
