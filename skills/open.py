import webbrowser

class Open:
    def __init__(self, input):
        self.input = []
        for i in input:
            self.input = i


    def Open_sesame(self):
        if "youtub" in self.input:
            print("in if-else")
            webbrowser.open_new_tab("https://www.youtube.com")
            return True
        elif 'googl'in self.input:
            webbrowser.open_new_tab("https://www.google.com")
            return True
        elif 'вк' in self.input:
            webbrowser.open_new_tab("https://vk.com")
            return True
        else:
            return "Простите я вас не поняла"
        
# op = Open()
# op.Open_sesame("открой ВКонтакте")