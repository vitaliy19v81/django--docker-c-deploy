from django.urls import path
from .views import HomeView, SchoolGradesView, get_school_grades, validate_class_in_school, \
    ClassroomAddView, unique_validate_class_in_school, ClassroomUpdateView, ClassroomDeleteView, \
    CurrentClassroomAddView, CurrentClassroomUpdateView, CurrentClassroomDeleteView, \
    CurrentClassroomListView, SubjectInClassroomCreateView, \
    SubjectInClassroomListView, PupilInClassListView, SubjectInClassroomUpdateView, \
    validate_lesson_of_classroom, SubjectInClassroomDeleteView, SchoolGradesGet, \
    SchoolGradesPupilTodayGet  # , SchoolScoresGet, \
    #ScheduleLessonGet  # AcademicYearCreateView,
from .views import (HomeView, PupilAddView, SchoolLessonCreateView, validate_lesson,
                    LessonDeleteView, PupilDeleteView
                    )


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]