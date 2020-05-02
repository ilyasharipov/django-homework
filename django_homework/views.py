# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from .models import *

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        statistics = Statistics()

        context.update(
            {
                'students': statistics.students,
                'subjects': statistics.subjects,
                'student_subjects_scores': statistics.student_subjects_scores,
                'excellent_students': statistics.excellent_students,
                'bad_students': statistics.bad_students
            }
        )
        return context

class Statistics:

    students = Student.objects.all()
    subjects = Subject.objects.all()
    student_subjects_scores = Score.objects.all()

    def excellent_students(self):
        students = Student.objects.all()
        excellent_students = []

        for student in students:
            if student.average_mark() >= 4.5:
                excellent_students.append(student)
        return excellent_students

    def bad_students(self):
        students = Student.objects.all()
        bad_students = []

        for student in students:
            if student.average_mark() < 3.0:
                bad_students.append(student)
        return bad_students
