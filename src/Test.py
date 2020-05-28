from Context import Context
from Route import Route
from view.ListPager import ListPager

if __name__ == '__main__':
    route = Route()
    context = Context()
    route.attach_context(context)
    context.set_route(route)


    while True:
        context.start_view({"name":"home"})
        route.peek().resume()
        ip = input()

