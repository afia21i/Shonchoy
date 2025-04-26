from django.contrib import admin  # Import the admin module
from django.urls import path
from Shonchoy import views  # Assuming your views are in the same directory as urls.py

urlpatterns = [
    path('', views.webpage, name='webpage_root'),  # Maps the root URL
    path('webpage/', views.webpage, name='webpage'), # Maps the /webpage/ URL
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signupsuccessful/', views.signupsuccessful, name='signupsuccessful'),
    path('home/', views.home, name='home'),
    path('mybank/', views.mybank, name='mybank'),
    path('loaninquiries/', views.loaninquiries, name='loaninquiries'),
    path('chartlist/', views.chartlist, name='chartlist'),
    path('currentstatus/', views.currentstatus, name='currentstatus'),
    path('transactionhistory/', views.transactionhistory, name='transactionhistory'),
    path('myloans/', views.myloans, name='myloans'),
    path('logout/', views.logout, name='logout'),

]
