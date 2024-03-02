from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import StudentForm, AdditionalStudentDataForm, RepresentativeForm
from .models import Student, AdditionalStudentData, Representative, StudentDetail
from academic_data.models import AcademicPeriod, AllNotes, Tuition
from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView
from django.http import JsonResponse

# ESTUDIANTES
@method_decorator(login_required, name="dispatch")
class StudentListView(ListView):
  print('student-list ######################################')
  template_name = "students/students_list.html"
  queryset = Student.objects.select_related("additionalstudentdata", "gender")

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    cedula = self.request.GET.get("cedula", "")
    if cedula:
      self.queryset = self.queryset.filter(identity_card=cedula)

    try:
      latest_academic_period = AcademicPeriod.objects.latest('period')
      context['period'] = latest_academic_period.period
    except AcademicPeriod.DoesNotExist:
      context['period'] = None
    context['object_list'] = self.queryset
    return context
  
class StudentDetailView(DetailView):
    model = StudentDetail
    template_name = "students/student_detail.html"
    
    def get_object(self):
        # Obtener el objeto
        try:
          student = StudentDetail.objects.get(student_id=self.kwargs.get("student_id"),periodo=self.kwargs.get("periodo"))
        except:
          student = StudentDetail.objects.filter(student_id=self.kwargs.get("student_id")).order_by('-periodo_id').first()
          print(student)
        return student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el objeto y pasarlo al contexto
        context['student'] = self.get_object()
        return context


@method_decorator(login_required, name="dispatch")
class StudentCreateView(CreateView):
  template_name = "students/student_form.html"
  model = Student
  form_class = StudentForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["additional_info_form"] = AdditionalStudentDataForm
    context["form_action"] = reverse("create-student")
    context["action"] = "REGISTRAR"
    return context

  @transaction.atomic
  def post(self, request, *args, **kwargs):
    student_form = self.form_class(request.POST)
    additional_form = AdditionalStudentDataForm(request.POST)
    if student_form.is_valid() and additional_form.is_valid():
        student = student_form.save()
        additional_data = additional_form.save(commit=False)
        additional_data.student = student
        additional_data.save()
        messages.success(request, "Registro de estudiante exitoso")
        return redirect("students-list")
    else:
        messages.error(request, "No se pudo registrar el estudiante")
        return render(
          request,
          self.template_name,
          {"form": student_form, "additional_info_form": additional_form }
        )


@method_decorator(login_required, name="dispatch")
class StudentUpdateView(UpdateView):
  template_name = "students/student_form.html"
  model = Student
  form_class = StudentForm

  def get_object(self, queryset=None):
    return Student.objects.get(pk=self.kwargs.get("student_id"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    student = self.get_object()
    context["form_action"] = reverse("update-student", kwargs={"student_id": student.id})
    context["additional_info_form"] = AdditionalStudentDataForm(instance=student.additionalstudentdata)
    context["action"] = "ACTUALIZAR"
    return context

  @transaction.atomic
  def post(self, request, *args, **kwargs):
    student = self.get_object()
    student_form = self.form_class(request.POST, instance=student)
    additional_form = AdditionalStudentDataForm(request.POST, instance=student.additionalstudentdata)
    if student_form.is_valid() and additional_form.is_valid():
      student = student_form.save()
      additional_data = additional_form.save(commit=False)
      additional_data.student = student
      additional_data.save()
      messages.success(request, "Registro de estudiante actualizado")
      return redirect("students-list")
    else:
      messages.error(request, "No se pudo actualizar registro del estudiante")
      return render(
        request,
        self.template_name,
        {"form": student_form, "additional_info_form": additional_form }
      )


@login_required
def delete_student(request, student_id):
  if Student.objects.get(pk=student_id).delete():
    messages.info(request, "Registro de estudiante eliminado")
  return redirect("students-list")


#REPRESENTANTES
@method_decorator(login_required, name="dispatch")
class RepresentativeListView(ListView):
  template_name = "representatives/representatives_list.html"
  queryset = Representative.objects.prefetch_related("students")


@method_decorator(login_required, name="dispatch")
class RepresentativeCreateView(CreateView):
  template_name = "representatives/representative_form.html"
  model = Representative
  form_class = RepresentativeForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["form_action"] = reverse("create-representative")
    context["action"] = "REGISTRAR"
    return context

  @transaction.atomic
  def post(self, request, *args, **kwargs):
    representative_form = self.form_class(request.POST)
    if representative_form.is_valid():
        representative_form.save()
        messages.success(request, "Registro de representante exitoso")
        return redirect("representatives-list")
    else:
        messages.error(request, "No se pudo registrar al representante")
        return render(
          request,
          self.template_name,
          { "form": representative_form }
        )


@method_decorator(login_required, name="dispatch")
class RepresentativeUpdateView(UpdateView):
  template_name = "representatives/representative_form.html"
  model = Representative
  form_class = RepresentativeForm

  def get_object(self, queryset=None):
    return Representative.objects.get(pk=self.kwargs.get("representative_id"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    representative = self.get_object()
    context["form_action"] = reverse("update-representative", kwargs={"representative_id": representative.id})
    context["action"] = "ACTUALIZAR"
    return context

  def post(self, request, *args, **kwargs):
    representative = self.get_object()
    representative_form = self.form_class(request.POST, instance=representative)
    if representative_form.is_valid():
      representative_form.save()
      messages.success(request, "Registro de representante actualizado")
      return redirect("representatives-list")
    else:
      messages.error(request, "No se pudo actualizar registro del representante")
      return render(
        request,
        self.template_name,
        { "form": representative_form }
      )


@login_required
def delete_representative(request, representative_id):
  if Representative.objects.get(pk=representative_id).delete():
    messages.info(request, "Registro de representante eliminado")
  return redirect("representatives-list")



@login_required
def pie_chart_varones_hembras(request):
    period = AcademicPeriod.objects.order_by('-id').first()
    Varones = StudentDetail.objects.filter(periodo_id=period.id).filter(genero='masculino')
    Hembras = StudentDetail.objects.filter(periodo_id=period.id).filter(genero='femenino')
    data = {
        'labels': ['Hembras', 'Varones'],
        'datasets': [{
            'data': [Hembras.count(), Varones.count()],
            'backgroundColor': ['rgba(255, 99, 132, 0.5)', 'rgba(54, 162, 235, 0.5)']
        }]
    }
    return JsonResponse(data)

@login_required
def bar_char_cuadro_honor(request):
    datos = {}
    data_chart = {}
    cantidad_materias = {}
    matriculas_s = {}
    period = AcademicPeriod.objects.order_by('-id').first()
    matriculas = Tuition.objects.filter(academic_period_id=period.id)
    for matricula in matriculas:
      promedio_por_alumno = AllNotes.objects.filter(periodo=period,matricula=matricula.id)
      for item in promedio_por_alumno:
        student_id = item.student_id
        full_name = item.p_nombre +" "+ item.p_apellido +" "+ item.cedula
        if item.student_id not in datos:
          datos[item.student_id] = float(item.definitiva)
          cantidad_materias[item.student_id] = 1
        else:
          datos[item.student_id] += float(item.definitiva)
          cantidad_materias[item.student_id] += 1
        matriculas_s[item.student_id] = matricula
        
      for student_id, total_definitiva in datos.items():
          cantidad_materias_estudiante = cantidad_materias.get(student_id, 1)  # En caso de que no haya materias para el estudiante
          print(f"Estudiante ID: {full_name}, Total Definitiva: {total_definitiva}, Cantidad de Materias: {cantidad_materias_estudiante}")
          promedio = total_definitiva / cantidad_materias_estudiante
          datos[student_id] = promedio

    data_chart = {
    'labels': [],  # Etiquetas para cada estudiante
    'datasets': [{
        'label': [],  # Etiqueta del conjunto de datos
        'data': [],  # Datos de los promedios de notas para cada estudiante
        'backgroundColor': 'rgba(54, 162, 235, 0.5)'  # Color de fondo de las barras
    }]
    }
    for student_id, promedio in datos.items():
      data_chart['datasets'][0]['label'].append(str(matriculas_s[student_id]))
      print(matriculas_s[student_id])
      # Agregar el ID del estudiante como etiqueta
      data_chart['labels'].append(full_name)
      # Agregar el promedio de notas para el estudiante
      data_chart['datasets'][0]['data'].append(promedio)
  
    return JsonResponse(data_chart)
