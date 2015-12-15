try:
    from kivy.uix.floatlayout import FloatLayout
    from kivy.app import App
    from kivy.properties import ObjectProperty, StringProperty
    from kivy.core.window import Window
except ImportError as e:
    print("Kivy is not installed in your environment. --gui can not be used.")
    exit(1)

class BinterpretWidget(FloatLayout):
    pass

class BinterpretApp(App):
    def build(self):
        Window.size = (750 , 400)
        return BinterpretWidget()
