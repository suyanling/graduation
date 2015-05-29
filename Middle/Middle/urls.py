# -*- coding: utf-8 -*-
from django.conf.urls import *
from Middle.view import*
from Middle.home import*

# urlpatterns = [

# url(r'^$', 'Middle.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# ]
# 去除urlpatterns原来的写法，采用选择的写法
urlpatterns = patterns("",
                       (r'^testRequest/$', testRequest),
                       (r'^search-form/$', search_form),
                       (r'^search/$', search),
                       (r'^contact/$', contact),
                       (r'^home/$', home),
                       (r'^singlefigure/$', singlefigure),
                       (r'^singlefigure1/$', singlefigure1),
                       (r'^singlefigure2/$', singlefigure2),
                       (r'^mutifigure/$', mutifigure)
                       )
