from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class Tab(models.Model):
    class Meta:
        db_table = 'tag'
        
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Todo(models.Model):
    class Meta:
        db_table = 'todo'

    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.content