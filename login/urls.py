from django.urls import path
from .views import login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', login, name="login"),

    path('logout/', logout, name="logout"),
    ## Recuperación pass
	path('reset-password', PasswordResetView.as_view(), name='password_reset'),
	path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]