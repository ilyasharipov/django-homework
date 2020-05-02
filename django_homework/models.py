from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=32, null=False)
    surname = models.CharField(max_length=32, null=False)

    def __str__(self):
        return f'{self.surname} {self.name}'

    def __repr__(self):
        return f'Student(name={self.name}, surname={self.surname})'

    def average_mark(self):
        student_values = Score.objects.all()
        student_id = self.id
        average_mark = 0

        for student_value in student_values:
            subject_count = len(Subject.objects.all())
            if student_value.student.id == student_id:
                average_mark += student_value.value
        return average_mark / subject_count

class Subject(models.Model):
    name = models.TextField()

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    value = models.IntegerField(default=0)
