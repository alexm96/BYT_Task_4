import math
from random import shuffle
import time


class ObjectPoolClass(object):
    def __init__(self, seed):
        start_time = time.time()
        self.unique_id = ObjectPoolClass.get_recursive_fibo(seed)
        self._end_time = time.time() - start_time

    @staticmethod
    def get_recursive_fibo(
        n: int,
    ) -> int:  # just needed some method that would be expensive to call
        if n <= 1:
            return n
        else:
            return ObjectPoolClass.get_recursive_fibo(
                n - 1
            ) + ObjectPoolClass.get_recursive_fibo(n - 2)

    def print_creation_time(self):
        print(
            "My id is {id}. You saved {creation_time} seconds by re-using me".format(
                id=self.unique_id, creation_time=self._end_time
            )
        )


class ObjectPool(object):
    def __init__(self, lower_bound, upper_bound):
        self.object_pool = []
        for i in range(lower_bound, upper_bound):
            self.object_pool.append(ObjectPoolClass(seed=i))

    def get_item(self) -> ObjectPoolClass:
        item_to_return = self.object_pool.pop()
        item_to_return.print_creation_time()
        return item_to_return

    def reuse_item(self, item_to_reuse: ObjectPoolClass) -> None:
        self.object_pool.append(item_to_reuse)


if __name__ == "__main__":
    start_time = time.time()
    new_object_pool = ObjectPool(lower_bound=25, upper_bound=35)
    end_time = time.time() - start_time
    print("Time to create pool {}".format(str(end_time)))
    for outer in range(0, 4):
        start_time = time.time()
        max_objects = 10
        living_objects = []
        max_len = len(new_object_pool.object_pool)
        for inner in range(0, max_len):
            living_objects.append(new_object_pool.get_item())
        for item in living_objects:
            new_object_pool.reuse_item(item)
        time_to_reuse = time.time() - start_time
        print(
            "Time to re-use all objects instead {new_time}".format(
                new_time=time_to_reuse
            )
        )
        input()
