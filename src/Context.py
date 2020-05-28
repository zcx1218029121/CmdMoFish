class Context:
    """
    全局上下文对象 实际上就是个全局变量
    当前只管理路由对象和土司
    """

    def __init__(self):
        """
        :param route:  路由
        """
        self._route = None
        self.run = True

    def get_route(self):
        """
        :return: 当前路由对象
        """
        return self._route

    def start_view(self, intent):
        if self._route is None:
            raise RuntimeError("Route is None")
        self._route.push(intent)

    def set_route(self, route):
        self._route = route

    def finish(self):
        if self.get_route().get_task().size() > 1:
            self.get_route().pop()
        else:
            self.run = False
