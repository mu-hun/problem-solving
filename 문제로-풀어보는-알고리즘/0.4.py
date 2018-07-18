class QueueClass():

	def __init__(self):
		self.QUEUE_CAPACITY = 8

		self.queue = [None] * self.QUEUE_CAPACITY
		self.head = 0
		self.tail = -1
		self.queue_size = 0

	def enqueue(self, n :int):
		if self.queue_size == self.QUEUE_CAPACITY:
			print("queue full!")
			return
		self.tail = (self.tail + 1) % self.QUEUE_CAPACITY
		self.queue_size = self.queue_size + 1
		self.queue[self.tail] = n

	def dequeue(self):
		if self.queue_size == 0:
			print("queue empty!")
			return
		self.head += (self.head + 1) % self.QUEUE_CAPACITY
		self.queue_size = self.queue_size - 1
		return self.queue[self.head - 1]

	def main(self):
		while True:
			number = int(input("input number: "))
			if number > 0:
				self.enqueue(number)
			elif number == 0:
				print(self.dequeue())
			if number < 0:
				return print(self.queue)


if __name__ == '__main__':
	QueueClass().main()