from django.shortcuts import render
from django.views.generic import View

import logging
log = logging.getLogger(__name__)

from django.http import JsonResponse

class JSONResponseMixin(object):
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)


class IntentVideo(JSONResponseMixin,View):
    def get_data(self,ctx):
        log.debug(repr(ctx))
        return ctx
    
    def get(self,request):
        log.debug(repr(request))
        pass
    
    
    

