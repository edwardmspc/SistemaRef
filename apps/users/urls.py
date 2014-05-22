from django.conf.urls import patterns, include, url
from .views import SignupView, SigninView

urlpatterns = patterns('',
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^signup/(?P<inviter>[\w]+)/$', SignupView.as_view()),
    url(r'^signin/$', SigninView.as_view(), name='signin'),
)
