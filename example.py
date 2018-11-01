import rhubarb


@rhubarb.task(name='multiprint')
def multi_print(msg, count=10):
    return '\n'.join(msg for _ in range(count))


class Multiply(rhubarb.BaseTask):
    name = 'multiply'
    json_schema = {'type': 'object',
                   'properties': {
                       'operands': {'type': 'array',
                                    'minItems': 1,
                                    'items': {'type': 'number'}}
                   },
                   'required': ['operands']}

    def run(self, operands):
        result = 1
        for op in operands:
            result *= op
        return result


if __name__ == '__main__':
    rhubarb.run_cli()
