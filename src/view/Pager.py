from view.ViewGroup import ViewGroup


class Pager(ViewGroup):
    def __init__(self, context, param=None):
        super().__init__()
        self.context = context
