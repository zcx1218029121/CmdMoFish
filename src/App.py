from Context import Context
from Route import Route
from view.ViewGroup import ViewGroup


class App(ViewGroup):
    context = None
    run = True

    def on_creat(self, param):
        route = Route()
        context = Context()
        route.attach_context(context)
        context.set_route(route)
        self.context = context

    def start(self):
        self.context.start_view({"name": "home"})
        while self.context.run:
            self.context.get_route().peek().resume()
            ip = input()
            self.context.get_route().peek().dispatch_key(ip)

    def on_exit(self):
        self.pager_task.clear()
        # 结束循环
        self.run = False


if __name__ == '__main__':
    App().start()
