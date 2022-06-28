import datetime

filepath = "log.txt"


def log(file_path):

    def _log(old_function):
        data = []

        def new_function(*args, **kwargs):

            str_time = str(datetime.datetime.now())
            result = str(old_function(*args, **kwargs))
            parameters = ",".join(map(str, args))

            if len(kwargs) > 0:
                parameters = parameters + "," + ",".join([f"{key}={value}" for key, value in kwargs.items()])

            data.append(str_time)
            data.append(old_function.__name__)
            data.append(parameters)
            data.append(result)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(";".join(data))
                file.write("\n")

            return result

        return new_function

    return _log


@log(filepath)
def summ(*args, **kwargs):
    print(f"{args} + {kwargs}")


if __name__ == '__main__':
    summ(1, 4, 6, name_1=22, name_2="qq")

