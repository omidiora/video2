from django.urls import path,include
from .views import CourseListView,CourseDetail,LessonDetailView

app_name='course'
urlpatterns = [
    path('',CourseListView.as_view(), name='list'),
    path('<slug>',CourseDetail.as_view(), name='detail'),
    path('<course_slug>/<lesson_slug>/',LessonDetailView.as_view(), name='lesson-detail'),
]

