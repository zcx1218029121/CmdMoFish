from Stack import Stack
from view.ListPager import ListPager


class Route:
    # 新的页面请在这里注册
    _route_map = {
        "home": {"pager": ListPager}}
    # 页面栈
    _task = Stack()

    _context = None

    # 当前意图
    _cur_intent = None

    def push(self, intent):
        cur_intent = intent
        m_intent = self._route_map.get(intent["name"])
        pager = m_intent["pager"](self._context)
        self._task.push(pager)

    def peek(self):
        """
        页面出栈
        :return:
        """
        if self._task.is_empty():
            raise RuntimeError("task is empty")
        return self._task.peek()

    def attach_context(self, context):
        self._context = context

    def get_task(self):
        return self._task
