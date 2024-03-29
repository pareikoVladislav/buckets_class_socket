import abc
import socket

SIZE = 1
PORT = 9090
DATA_PACKAGE_SIZE = 1024


def start_server():
    """
    :return: Building a socket and binding it to a port. Sending data to the client.
    """
    sock = socket.socket()
    sock.bind(('', PORT))
    sock.listen(SIZE)

    print(f'--- Start listen port {PORT} ---')

    connection, client_address = sock.accept()
    print(f"{client_address} has connected!")

    while 1:
        data = connection.recv(DATA_PACKAGE_SIZE)
        if not data:
            break
        print(data)
        connection.sendall(data)
    sock.close()
    print("Server has closed")


if __name__ == "__main__":
    start_server()


class Bucket:
    """
    THe main class with one param: The amount of water in the bucket
    """

    def __init__(self):
        """
        Initial method. It started when Bucket class would started
        """
        self.water_value = 0

    @abc.abstractmethod
    def pour_water_out_of_the_bucket(self, *args):
        """

        :param args: A bucket into which water will be poured
        :return: The remaining amount of water in the bucket
        """
        pass


class ThreeLBucket(Bucket):
    """
    The class is a child with three methods and parent inheritance.
    """

    def draw_water_in_a_bucket(self):
        """
        :return: When this method is called, the current bucket will be filled.
        """
        self.water_value = 3

    def empty_the_bucket(self):
        """
        :return: Calling this method will reset the current bucket to zero.
        """
        self.water_value = 0

    def pour_water_out_of_the_bucket(self, five_bucket):
        """
        :param five_bucket: Determines which bucket the water will be poured into.
        :return: Determines the amount of water when transferred to another bucket.
        """
        free_value_of_five_bucket = 5 - five_bucket.water_value
        if self.water_value >= free_value_of_five_bucket:
            five_bucket.water_value += free_value_of_five_bucket
            self.water_value -= free_value_of_five_bucket
        else:
            five_bucket.water_value += self.water_value
            self.water_value -= self.water_value


class FiveLBucket(Bucket):
    """
    The class is a child with three methods and parent inheritance.
    """

    def draw_water_in_a_bucket(self):
        """
        :return: When this method is called, the current bucket will be filled.
        """
        self.water_value = 5

    def empty_the_bucket(self):
        """
        :return: Calling this method will reset the current bucket to zero.
        """
        self.water_value = 0

    def pour_water_out_of_the_bucket(self, three_bucket):
        """
        :param three_bucket: Determines which bucket the water will be poured into.
        :return: Determines the amount of water when transferred to another bucket.
        """
        free_value_of_three_bucket = 3 - three_bucket.water_value
        if self.water_value >= 3:
            self.water_value = self.water_value - free_value_of_three_bucket
            three_bucket.water_value += free_value_of_three_bucket
        else:
            three_bucket.water_value += self.water_value
            self.water_value -= self.water_value


bucket = Bucket()  # Create an object of a parent class.
three_l_bucket = ThreeLBucket()  # Create an object of class three-liter bucket
five_l_bucket = FiveLBucket()  # Create an object of a five-liter bucket class

count = 0

template = """
    1 - налить пятилитровое ведро
    2 - Налить трёхлитровое ведро
    3 - вылить пятилитровое ведро
    4 - вылить трёхлитровое ведро
    5 - перелить из пятилитрового в трёхлитровое
    6 - перелить из трёхлитрового в пятилитровое
"""

print(template)

while five_l_bucket.water_value != 4:
    action = input('Enter action: ')

    if action == "1":
        five_l_bucket.draw_water_in_a_bucket()
    elif action == "2":
        three_l_bucket.draw_water_in_a_bucket()
    elif action == "3":
        five_l_bucket.empty_the_bucket()
    elif action == "4":
        three_l_bucket.empty_the_bucket()
    elif action == "5":
        five_l_bucket.pour_water_out_of_the_bucket(three_l_bucket)
    elif action == "6":
        three_l_bucket.pour_water_out_of_the_bucket(five_l_bucket)
    else:
        print('Action not found.')
        continue
    count += 1
    print(count)
    print(f"\r{count} шаг: пятилитровое ведро равно: {five_l_bucket.water_value}, "
          f"трёхлитровое ведро равно: {three_l_bucket.water_value}")
print(f"Поздравляю! Ты решил эту задачу за {count} ходов и "
      f"твоё пятилитровое ведро равно {five_l_bucket.water_value} литрам!")
