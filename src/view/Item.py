from view.View import View


class Item(View):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def before_print(self):
        print("-------------------------")

    def print_content(self):
        print(self.get_data()['Title'])
        print(self.get_data()['Url'])

    def handle_key(self, key):
        return False
