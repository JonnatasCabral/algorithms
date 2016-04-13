class Queue
	def initialize
		@queue = []
		@queue_count = 0
	end

	def push(n)
		@queue.push(n)
		@queue_count += 1
	end
	def pop
		return 'Queue Empty' if is_empty
		@queue.shift
		@queue_count -= 1
	end
	def is_empty
		return true if @queue_count == 0
		return false 
	end
	def queue
		return @queue
	end
end

queue = Queue.new
queue.push 2
queue.push 5
queue.push 10
print queue.queue
queue.pop
queue.pop
print queue.queue