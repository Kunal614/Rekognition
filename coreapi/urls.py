# from rest_framework.decorators import api_view
from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.ImageFr.as_view(), name='image_api'),
    path('old_video/', views.VideoFr.as_view(), name='video_api'),
    path('embed/', views.EMBEDDING.as_view(), name='embed_api'),
    path('video/', views.AsyncVideoFr.as_view(), name='celery_test_api'),
    path('feedback/', views.FeedbackFeature.as_view(), name='feedback_api'),
    path('nsfw/', views.NsfwRecognise.as_view(), name='nsfw'),
    path('ytstream/', views.StreamVideoFr.as_view(), name='youtube_process'),
    path('simface/', views.SimilarFace.as_view(), name='similar_face'),

]
