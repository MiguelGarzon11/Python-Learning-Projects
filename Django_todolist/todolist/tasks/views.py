from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.order_by('-id') # Trae todas las vistas y las ordena por ID
    return render(request, 'task_list.html', {'tasks': tasks}) # Renderiza el template con las tareas.

def add_task(request):
    if request.method == 'POST': # Si el metodo es POST significa que se envió un formulario
        title = request.POST.get('title')
        print(" add_task recibio title =", repr(title)) # Obtenemos el valor del campo 'title' del formulario
        if title: # Si el campo no está vacio
            Task.objects.create(title=title) # Creamos una nueva tarea en la base de datos (Guarda la tarea)
            print("Tarea creada en base de datos")
        return redirect('task_list') # Redirigimos a la lista de tareas después de agregarla

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) # Busca la tarea con le ID especificado si no la encuentra devuelve un error 404
    task.completed = True # Cambia el estado a completado
    task.save() # Guarda los cambios en la base de datos
    return redirect('task_list') # Redirige nuevamente a la lista de tareas

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) # Busca la tarea por id, si no la encuentra da error 404.
    task.delete() # Elimina la tarea de la base de datos
    return redirect('task_list') # Redirige nuevamente a la lista de tareas

