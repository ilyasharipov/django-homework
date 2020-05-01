# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from .models import *

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        students = Student.objects.all()
        subjects = Subject.objects.all()
        student_subjects_statistics = Score.objects.all()

        print(student_subjects_statistics)
        # for student in students:
        #     # print(student.id)
        #     student_subjects_values.append(Score.objects.filter(student = student))

        #print(student_subjects_values)
        # student = Student.objects.first()
        # print(student)
        # student_subjects_values = Score.objects.filter(student = student)  
        # print(student_subjects_values)
        context.update(
            {
                'students': students,
                'subjects': subjects,
                # 'student_subjects_values': student_subjects_values,
                'student_subjects_statistics': student_subjects_statistics,
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


# class Student:
#     def get_all_students(self):
#         return Student.objects.all()


# class Statistics:
#     # student_id, [Scores]
#     pass

# class Subject:
#     pass

# class Score:
#     # Subject, Student, value
#     pass


                # 'students_statistics': [
                #     {
                #         'id': 1,
                #         'fio': 'Someone',
                #         'timp': 2,
                #         'eis': 3,
                #         'philosophy': 4,
                #         'english': 5,
                #         'sport': 2.3,
                #         'average': 2.3,
                #     }
                # ],
                # 'excellent_students': 'Student A, Student B',
                # 'bad_students': 'Student C, Student D'