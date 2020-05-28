from view.View import View


class Tip(View):
    def on_creat(self):
        self.need_print = False

    def show(self, data):
        self.data = data
        self.need_print = True
        self.resume()
        self.need_print = False
    def print_content(self):
        print(self.data)


