class Stack
	def initialize
		@stack = []
		@count = 0
	end
	def push(n)
		@stack.push(n)
		@count += 1
	end
	def pop
		unless is_empty
			@stack.pop
			@count -= 1
		end
	end
	def stack
		return @stack
	end
	def count
		return @count
	end
	def is_empty
		return true if @count == 0
		return false
	end
	
end

stack = Stack.new
stack.push(2)
stack.push(3)
print stack.stack
stack.pop()
print stack.stack
