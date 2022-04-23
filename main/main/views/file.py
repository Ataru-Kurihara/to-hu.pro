import glob
import os

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ValidationError


#  特定のフォルダーの全ファイル

class File(APIView):

    def get(self, request, *args, **kwargs):
        file_id = kwargs['dir_id']
        files = glob.glob(f"/minecraft/computer/{file_id}", recursive=True)
        projects = []
        di = {}
        try:
            for filename in os.listdir(files[0]):
                projects.append(filename)
                for i in projects:
                    with open(os.path.join(files[0], i), "r") as f:
                        file = f.read()
                        di[i] = file
            data = {
                'response': {
                    'file_id': file_id,
                    'path': files,
                    "projects": di
                }
            }
            return Response(data)
        except IndexError:
            raise NotFound

    # 新規ファイルを作成
    def post(self, request, *args, **kwargs):
        dir_id = kwargs.get('dir_id')
        data = request.data
        file_name = data.get('file_name')
        code = data.get('code')
        # すでにファイルが存在する場合
        if os.path.exists(f"/minecraft/computer/{dir_id}/{file_name}"):
            raise NotFound
        # ファイル名が10文字以上
        elif len(file_name) >= 10:
            raise ValidationError("ファイル名は10文字以内")
        # ファイル名に"/"が含まれる
        elif file_name in "/":
            raise ValidationError("/は含まない")
        else:
            f = open(f"/minecraft/computer/{dir_id}/{file_name}", "w")
            f.write(code)
            f.close()
            return Response({"success": True})

    # ファイルを更新
    def patch(self, request, *args, **kwargs):
        dir_id = kwargs.get('dir_id')
        data = request.data
        file_name = data.get('file_name')
        code = data.get('code')
        if os.path.exists(f"/minecraft/computer/{dir_id}/{file_name}"):
            with open(f"/minecraft/computer/{dir_id}/{file_name}", "w") as fp:
                fp.write(code)
            return Response({"success": True})
        else:
            raise ValidationError("すでにファイルが存在します")  # すでにファイルが存在する

    # ファイルを削除
    def delete(self, request, *args, **kwargs):
        dir_id = kwargs.get('dir_id')
        data = request.data
        file_name = data.get('file_name')
        if os.path.exists(f"/minecraft/computer/{dir_id}/{file_name}"):
            os.remove(f"/minecraft/computer/{dir_id}/{file_name}")
        else:
            raise NotFound  # ファイルが無い
        return Response({"success": True, "DeleteFile": file_name})
