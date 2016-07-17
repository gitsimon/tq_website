from django.conf.urls import url

from payment import views

urlpatterns = [
    url(r'^auth/counterpayment/(?P<usi>[a-zA-Z0-9]{6})/details/$',
        views.CounterPaymentDetailView.as_view(),
        name='counterpayment_detail'),
    url(r'^auth/counterpayment/$',
        views.CounterPaymentIndexView.as_view(),
        name='counterpayment_index'),
    url(r'^payment/(?P<usi>[a-zA-Z0-9]{6})/payed/$', views.VoucherPaymentSuccessView.as_view(),
        name='voucherpayment_success'),
    url(r'^payment/(?P<usi>[a-zA-Z0-9]{6})/$', views.VoucherPaymentIndexView.as_view(),
        name='voucherpayment_index'),
    url(r'^auth/coursepayment/$',
        views.CoursePaymentIndexView.as_view(),
        name='coursepayment_index'),
    url(r'^auth/coursepayment/(?P<course>[0-9]*)/$', views.CoursePaymentDetailView.as_view(),
        name='coursepayment_detail'),
    url(r'^auth/coursepayment/(?P<course>[0-9]*)/(?P<usi>[a-zA-Z0-9]{6})/$',
        views.CoursePaymentConfirm.as_view(),
        name='coursepayment_confirm'),
    url(r'^auth/coursepayment/(?P<course>[0-9]*)/(?P<usi>[a-zA-Z0-9]{6})/paid/$',
        views.CoursePaymentConfirm.as_view(),
        name='coursepayment_payed'),
]
