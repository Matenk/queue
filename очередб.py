from threading import Thread
from queue import Queue
import time

class Table:

    def __init__(self, num_table):
        self.num_table = num_table
        self.is_busy = False # стол свободен
        print(f'Мы принесли {num_table} стол, пока что он свободен.')

    def free_table(self):
        self.is_busy = False # стол свободен
        print(f'Стол номер {self.num_table} свободен.')

    def busy_table(self):
        self.is_busy = True # стол занят
        print(f'Стол номер {self.num_table} занят.')




class Cafe:


    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables
        self.table_num = 1

    def customer_arrival(self):
        customer_num = 1
        while customer_num <= 10:
            customer_num += 1
            print(f'Клиент номер {customer_num} пришел.')
            customer = Customer(customer_num, self)
            customer.start()
            time.sleep(1)

    def serve_customer(self, customer_num):
        for table in tables:
            if not table.is_busy:
                table.busy_table()
                print(f'Клиент номер {customer_num}, сел за стол {self.table_num}')
                self.table_num += 1
                time.sleep(5)
                print(f'Клиент номер {customer_num} покушал и ушёл')
                table.free_table()
                self.check_queue()
                return
            else:
                self.queue.put(customer_num)
                print(f'Посетитель номер {customer_num}, ожидает в очереди стол')

    def check_queue(self):
        if not self.queue.empty():
            customer_num = self.queue.get
            self.serve_customer(customer_num)


class Customer(Thread):
    def __init__(self, num, cafe):
        super().__init__()
        self.num = num
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self.num)







table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)


customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()