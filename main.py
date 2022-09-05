from entity.courier import Courier
from entity.exceptions import InvalidRequest, BaseError

from entity.request import Request
from entity.shop import Shop
from entity.store import Store

store = Store(items={
    'печеньки': 25,
    'собачка': 25,
    'елка': 24
})

shop = Shop(items={
    'печеньки': 25,
    'собачка': 25,
    'елка': 24
})

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    print('\nДобрый день!\n')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_item()}')

        user_input = input(
            'Введите запрос\n'
            'Введите стоп или stop, если хотите закончить\n'
        )

        if user_input in ('stop', 'стоп'):
            break
        try:
            request = Request(request=user_input)
        except InvalidRequest as error:
            print(error.massage)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )
        try:
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
