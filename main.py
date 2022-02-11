import os
import json
import argparse


class Prime():
    def __init__(self, number):
        """
        Prime class that enumerates prime
        numbers within a given range
        :param number:
        """
        self.number = number

    def get_prime_numbers(self) -> list:
        """
        Return list of prime numbers
        :return:
        """
        response = [2, 3]

        for num in range(self.number):
            if num > 0:
                lower, upper = (num * 6) - 1, (num * 6) + 1
                if lower < self.number > upper:
                    response.append(lower)
                    response.append(upper)

        return response

    def checkpoint(self, position):
        """
        Marks the results of the last execution
        of this program
        :param position:
        :return:
        """
        dict_obj = {}
        dict_obj.__setitem__('numbers', [p for p in position])
        with open('.checkpoint', mode='w') as f:
            json.dump(dict_obj, f)
        f.close()

    def run(self):
        """
        Main program
        :return:
        """
        position = {}

        response = [p for p in self.get_prime_numbers()]

        if os.path.isfile('.checkpoint'):
            with open('.checkpoint', mode='r') as f:
                dict_obj = json.load(f)
                position = [int(n) for n in dict_obj['numbers']]
            f.close()

        self.checkpoint(response)

        if not position:
            response = [str(r) for r in response]

        else:
            col_same = sorted(set(response).intersection(position))
            same = [f"{c}*" for c in col_same]
            diff = [str(d) for d in set(response).difference(position)]
            response = same + diff

        return response


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--number", dest='number', type=int)
    args = parser.parse_args()

    print(Prime(args.number).run())
