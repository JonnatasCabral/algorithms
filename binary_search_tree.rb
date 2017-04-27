class Node
	def initialize(value)
		@value = value
		@left = nil
		@right = nil
	end
	def get_value
		@value
	end
	def set_value(value)
		@value = value
	end
	def get_left
		@left
	end
	def set_left(left)
		@left = left
	end
	def get_right
		@right
	end
	def set_right(right)
		@right = right
	end
end

class BinaryTree
	@root = nil

	def root
		@root
	end

	def insert(value)
		node = Node.new(value)

		unless @root
			@root = node
			return
		end

		dad_node = nil
		current_node = @root

		while true
			if node.get_value < current_node.get_value
				dad_node = current_node
				current_node = current_node.get_left
			else
				dad_node = current_node
				current_node = current_node.get_right
			end	

			unless current_node
				if node.get_value < dad_node.get_value 
					dad_node.set_left(node)
					return
				else
					dad_node.set_right(node)
					return
				end
			end
		end
	end

	# show pre-order (root-left-right)
	def pre_order_tree(current_node)
		if current_node
			puts current_node.get_value
			pre_order_tree current_node.get_left
			pre_order_tree current_node.get_right
		end
	end

end

tree = BinaryTree.new
tree.insert(10)
tree.insert(2)
tree.insert(31)
tree.insert(11)
tree.insert(93)
tree.insert(19)
tree.insert(23)
tree.insert(4)
tree.insert(67)
tree.pre_order_tree(tree.root)

