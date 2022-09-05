class BaseError(Exception):
    message = 'Неожиданная ошибка'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места на складе'


class NotEnoughProduct(BaseError):
    message = 'Недостаточно товара на складе'


class TooManyDifferentProducts(BaseError):
    message = 'Слишком много разных товаров'


class InvalidRequest(BaseError):
    def __init__(self, *args: object):
        super().__init__(args)
        self.massage = None

    message = 'Неправильный запрос. Попробуйте снова'
