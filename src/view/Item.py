from view.View import View


class Item(View):
    def __init__(self, data):
        super().__init__(data)

    def before_print(self):
        print("-------------------------")

    def print_content(self):
        print(self.get_data())

    def handle_key(self, key):
        if key == "1":
            print("儿子消费"+key)
            return True
        else:
            print("儿子不消费"+key)
            return False
