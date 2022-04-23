import glob

from rest_framework.response import Response
from rest_framework.views import APIView


# 全フォルダー一覧

class Files(APIView):

    def get(self, request, *args, **kargs):
        folders = glob.glob("/minecraft/computer/*[!lastid.txt]", recursive=True)
        data = {
            'folders': folders
        }
        return Response(data)
