from framework.http.HttpClientImpl import HttpClientImpl
class JSONHolderService:
    def GetTodo(self, todoId):
        cli = HttpClientImpl()
        # Example GET request to the JSONPlaceholder API
        url = f"https://jsonplaceholder.typicode.com/todos/{todoId}"
        todo = cli.get(url)
        return todo

