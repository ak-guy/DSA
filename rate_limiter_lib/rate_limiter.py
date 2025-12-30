from abc import ABC, abstractmethod


class BaseRateLimiter(ABC):
    @abstractmethod
    def allow_request(self, request): ...

    def get_user_identity(self, request):
        http_xff = request.META.get("HTTP_X_FORWARDED_FOR")
        remote_address = request.META.get("REMOTE_ADDR")
