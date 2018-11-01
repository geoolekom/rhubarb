import argparse
import json

from rhubarb.storage import task_queue, tasks

parser = argparse.ArgumentParser(description='Введите название задачи и аргументы в формате JSON.')
parser.add_argument('task_name', type=str)
parser.add_argument('--params', type=str, default='{}')


def cli_queue():
    args = parser.parse_args()
    params = json.loads(args.params)
    task_queue.put((args.task_name, params))


def main():
    while True:
        task_name, kwargs = task_queue.get()
        if task_name in tasks:
            result = tasks[task_name](**kwargs)
            print(result)


def run_cli():
    print('Зарегистрированные задачи:')
    for name in tasks:
        print(f'- {name}')
    cli_queue()
    try:
        main()
    except KeyboardInterrupt:
        print('Остались незавершенные задачи.')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

if __name__ == '__main__':
    run_cli()
