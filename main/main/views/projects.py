import glob

from rest_framework.response import Response
from rest_framework.views import APIView


class Projects(APIView):

    def get(self, request, *args, **kargs):
        files = glob.glob("/minecraft/computer/*[!lastid.txt]", recursive=True)
        data = {
            'date': files
        }
        return Response(data)
