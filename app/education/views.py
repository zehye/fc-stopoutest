from django.shortcuts import render

from education.models import School, Student


def index(request):
    return render(request, 'education/index.html')


def school_list(request):
    schools = School.objects.all()
    context = {
        'schools': schools,
    }
    return render(request, 'education/school_list.html', context)


def school_detail(request, school_id):
    school = School.objects.get(id=school_id)
    context = {
        'school': school
    }
    return render(request, 'education/school_detail.html', context)


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'education/student_list.html', context)


def student_detail(request, student_id):

    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'education/student_detail.html', context)
