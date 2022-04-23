import glob
import os

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView


# 特定のファイルの中身

class Projects(APIView):

    def get(self, request, *args, **kwargs):
        dir_id = kwargs['dir_id']
        folder_name = kwargs['folder_name']
        files = glob.glob(f"/minecraft/computer/{dir_id}", recursive=True)
        projects = []
        di = {}
        try:
            for filename in os.listdir(files[0]):
                projects.append(filename)
                for i in projects:
                    with open(os.path.join(files[0], i), "r") as f:
                        file = f.read()
                        di[i] = file

            project_name = di[folder_name]
            data = {
                'response': {
                    'file_name': dir_id,
                    'path': files,
                    "code": project_name
                }
            }
            return Response(data)
        except KeyError:
            raise NotFound
