from django.shortcuts import render
from django.views.generic import View
import zmq
import logging
log = logging.getLogger(__name__)

from django.http import JsonResponse

class JSONResponseMixin(object):
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, **response_kwargs)


class IntentVideo(JSONResponseMixin,View):
    def get(self,request):
        # LET'S HAVE LOGIC HERE
        
        zmq_ctx = zmq.Context()
        publisher = zmq_ctx.socket(zmq.PUB)
        publisher.bind("tcp://*:5563")
        publisher.send_multipart([b"P", b"Play Video"])
        publisher.close()
        zmq_ctx.term()
        
        return self.render_to_response({
                                        'result':'OK',
                                        })    


class StopVideo(JSONResponseMixin,View):
    def get(self,request):
        # LET'S HAVE LOGIC HERE

        zmq_ctx = zmq.Context()
        publisher = zmq_ctx.socket(zmq.PUB)
        publisher.bind("tcp://*:5563")
        publisher.send_multipart([b"S", b"Stop Video"])
        publisher.close()
        zmq_ctx.term()

        return self.render_to_response({
                                        'result':'OK',
                                        })    

