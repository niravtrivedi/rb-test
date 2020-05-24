class BaseException(Exception):
	pass

class PermissionDenied(BaseException):
	pass

class UnAuthorized(BaseException):
	pass


class ResultNotFound(BaseException):
	pass