from api.models import Todo
from api.serializers.todo_serializer import TodoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

from django.http import JsonResponse

    # return JsonResponse(data["results"])
def test(request):

        return JsonResponse(
            {
                "result": "サーバーに通信できています"
            }
        )
class TodoView(APIView):

    def get(self, request):
        all_todo = Todo.objects.all()
        print(all_todo)
        serializer = TodoSerializer(all_todo, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        return create_todo(request)
    
    def put(self, request):
        return update_todo_by_id(request)

    def delete(self, request):
        return delete_todo_by_id(request)



def create_todo(request):
    
    todo = Todo.objects.create(
        title=request.data["title"],
        description=request.data["description"],
        completed=request.data["completed"],
        created_by=request.user
    )
   



def get_all_todo_by_user(request):
    
    all_todo = Todo.objects.filter(created_by=request.user)
    serializer = TodoSerializer(all_todo, many=True)
    return Response(serializer.data)

def get_todo_by_user(request, user_id):
    user = User.objects.get(id=user_id)
    all_todo = Todo.objects.filter(created_by=user)
    serializer = TodoSerializer(all_todo, many=True)
    return Response(serializer.data)

def delete_todo_by_id(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return Response({"message": "Todo deleted successfully"})

def delete_todo_by_user(request, user_id):
    user = User.objects.get(id=user_id)
    all_todo = Todo.objects.filter(created_by=user)
    all_todo.delete()
    return Response({"message": "All Todos deleted successfully"})

def update_todo_by_id(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

