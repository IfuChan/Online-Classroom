from django.db import models
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import DeleteView, FormView, UpdateView
from courseMaterials.models import Course, Semester, lecture
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import courseForm, lectureForm, questionForm
from django.urls import reverse


# Create your views here.

class SemesterView(ListView):
    context_object_name = 'semesters'
    model = Semester
    template_name = 'courseMaterials/semesterView.html'

class CourseView(DetailView):
    context_object_name = 'semesters'
    model = Semester
    template_name = 'courseMaterials/courseView.html'

class CourseView_create(CreateView):
    form_class = courseForm
    context_object_name = 'semesters'
    model = Semester
    template_name = 'courseMaterials/courseView_create.html'

    # def get_success_url(self):
    #     self.object = self.get_object
    #     semester=self.object.semester
    #     return reverse('lectureView', kwargs={'semster':semester.slug})
    # def form_valid(self, form, *args, **kwargs):
    #     self.object = self.get_object()
    #     fm = form.save(commit=False)
    #     fm.Semester = self.object.semester
    #     fm.save()
    #     return HttpResponseRedirect(self.get_success_url())

class LectureView(DetailView):
    context_object_name = 'courses'
    model = Course
    template_name = 'courseMaterials/lectureView.html'

class LectureView2(DetailView, FormView):
    context_object_name = 'lectures'
    model = lecture
    template_name = 'courseMaterials/lectureView2.html'
    form_class = questionForm

    def get_context_data(self, **kwargs):
        context = super(LectureView2, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.form_class
            form_name = 'form'
            form = self.get_form(form_class)

        if form_name=='form' and form.is_valid():
            print("Question form is returned")
            return self.form_valid(form)
    
    def get_success_url(self):
        self.object = self.get_object()
        semester = self.object.Semester
        course = self.object.subject
        return reverse('lecture_view_lec',kwargs={'semester':semester.slug, 
                                'course':course.slug, 'slug':self.object.slug})
        
    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.user_name = self.request.user
        fm.lecture_name = self.object.askquestions.name
        fm.lecture_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LectureView_create(CreateView):
    form_class = lectureForm
    context_object_name = 'course'
    model = Course
    template_name= 'courseMaterials/lectureView_create.html'

    # def get_success_url(self):
    #     self.object = self.get_object
    #     semester=self.object.semester
    #     return reverse('lectureView', kwargs={'semster':semester.slug, 'slug':self.object.slug})

    # def form_valid(self, form, *args, **kwargs):
    #     self.object = self.get_object()
    #     fm = form.save(commit=False)
    #     fm.create_by = self.request.user
    #     fm.Semester = self.object.semester
    #     fm.course = self.object
    #     fm.save()
    #     return HttpResponseRedirect(self.get_success_url())

class LectureView_update(UpdateView):
    fields = ('name', 'position', 'pdf')
    model = lecture
    template_name = 'courseMaterials/lectureView_update.html'
    context_object_name = 'lectures'

class LectureView_delete(DeleteView):
    fields = ('name', 'position', 'pdf')
    model = lecture
    template_name = 'courseMaterials/lectureView_delete.html'
    context_object_name = 'lectures'

    def get_success_url(self):
        semester = self.object.Semester
        course = self.object.subject
        return reverse('lecture_view',kwargs={'semester':semester.slug, 'slug': course.slug})

