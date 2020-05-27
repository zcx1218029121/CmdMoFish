class Context:
    """
    全局上下文对象 实际上就是个全局变量
    当前只管理路由对象
    """

    def __init__(self, route):
        """
        :param route:  路由
        """
        self._route = route

    def get_route(self):
        """
        :return: 当前路由对象
        """
        return self._route

    def start_view(self, intent):
        self._route.push(intent)
