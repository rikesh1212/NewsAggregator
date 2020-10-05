# NewsAggregator
News Aggreator is a RESTful API service which scrapes data from two websites. The websites link can be seen in the news/views.py. It is designed using DJANGORESTFRAMEWORK and token authentication is implemented. The periodic updates of the content has been done using WEBSOCKETS implemented through Django Channels and DJANGOCHANNELSRESTFRAMEWORK. For more information regarding Django Channels Rest Framework, please follow https://github.com/hishnash/djangochannelsrestframework.

 # Installation:
Try:
pip install requirements.txt

## For running, please try:
python manage.py runserver

## For integrating with front end,

in routing.py, view_as_consumer can be used
```

from djangochannelsrestframework.consumers import view_as_consumer


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^front(end)/$", view_as_consumer(YourDjangoView)),
        ])
    ),
 })

```

