import argparse
import json

from rhubarb.app import DefaultApp, registered_tasks

parser = argparse.ArgumentParser(description='Введите название задачи и аргументы в формате JSON.')
parser.add_argument('task_name', type=str)
parser.add_argument('--params', type=str, default='{}')


def run_cli():
    app = DefaultApp()
    args = parser.parse_args()
    params = json.loads(args.params)
    app.queue_task(args.task_name, params)

    app.run()

if __name__ == '__main__':
    run_cli()
