from django.urls import path
from .views import StudentListView
from .views import ClassListView
from .views import ClassroomPeriodListView
from .views import CoursesListView
from .views import TeacherListView
from .views import StudentDetailView
from .views import ClassDetailView
from .views import ClassroomPeriodDetailView
from .views import CoursesDetailView
from .views import TeacherDetailView



urlpatterns = [
    path(
        "students/",StudentListView.as_view(),name="student_list_view"
    ),
    path(
        "classes/", ClassListView.as_view(), name="class_list_view"
    ),
    path(
        "periods/", ClassroomPeriodListView.as_view(), name="classroomPeriod_list_view"
    ),
    path(
        "courses/", CoursesListView.as_view(), name="course_list_view" 
    ),
    path(
        "teachers/", TeacherListView.as_view(), name="teachers_list_view"
    ),
     path(
        "students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"
    ),
      path(
        "classes/<int:id>/", ClassDetailView.as_view(), name="class_detail_view"
    ),
     path(
        "classroom_period/<int:id>/", ClassroomPeriodDetailView.as_view(), name="classroom_periods_detail_view"
    ),
     path(
        "courses/<int:id>/", CoursesDetailView.as_view(), name="courses_detail_view"
    ), 
     path(
        "teachers/<int:id>/", TeacherDetailView.as_view(), name="teachers_detail_view"
    )
]

