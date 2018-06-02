

from django.utils.deprecation import MiddlewareMixin

class myMiddle(MiddlewareMixin):
    def process_request(self,request):
        print(request.GET.get("a"))


