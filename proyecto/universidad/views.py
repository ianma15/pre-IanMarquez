from django.shortcuts import render, redirect
from .models import Estudiante, Materia, Solicitud
from .forms import EstudianteForm, MateriaForm, SolicitudForm

def index(request):
    return render(request, 'universidad/index.html')

def estudiante_list(request):
    query = request.GET.get("q")
    if query:
        estudiantes = Estudiante.objects.filter(apellido__contains=query)
    else:
        estudiantes = Estudiante.objects.all()
    context = {"object_list": estudiantes}
    return render(request, "universidad/estudiante_list.html", context)

def materia_list(request):
    query = request.GET.get("q")
    if query:
        materias = Materia.objects.filter(nombre__contains=query)
    else:
        materias = Materia.objects.all()
    context = {"object_list": materias}
    return render(request, "universidad/materia_list.html", context)

def solicitud_list(request):
    query = request.GET.get("q")
    if query:
        solicitudes = Solicitud.objects.filter(materia__nombre__contains=query)
    else:
        solicitudes = Solicitud.objects.all()
    context = {"object_list": solicitudes}
    return render(request, "universidad/solicitud_list.html", context)

def estudiante_create(request):
    if request.method == "GET":
        form = EstudianteForm()
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    return render(request, "universidad/estudiante_create.html", {"form": form})

def materia_create(request):
    if request.method == "GET":
        form = MateriaForm()
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("materia_list")
    return render(request, "universidad/materia_create.html", {"form": form})

def solicitud_create(request):
    if request.method == "GET":
        form = SolicitudForm()
    if request.method == "POST":
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("solicitud_list")
    return render(request, "universidad/solicitud_create.html", {"form": form})
