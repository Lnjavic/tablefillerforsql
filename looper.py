import fill

print("\nEnter No of records to fill per table...")
max = int(input())

class looper(fill.filler):
	def __init__(self):
		super().__init__()
		self.loop_member()
		super().get_members()
		self.loop_contr()
		self.loop_benefit()
		self.loop_dependant()

	def loop_member(self):
		c = 0
		while c < max:
			super().fill_table_members()
			print("Filled {} Members".format(c))
			c = c + 1

	def loop_contr(self):
		c = 0
		while c < max/2:
			super().fill_table_contribution()
			print("Filled {} Contribution".format(c))
			c = c + 1

	def loop_benefit(self):
		c = 0
		while c < max/2:
			super().fill_table_benefits()
			print("Filled {} Benefits".format(c))
			c = c + 1

	def loop_dependant(self):
		c = 0
		while c < max/2:
			super().fill_table_dependant()
			print("Filled {} Dependants".format(c))
			c = c + 1


myLoop = looper()