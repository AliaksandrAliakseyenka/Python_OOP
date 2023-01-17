from string import digits


class RegistrationUser:

	def __init__(self, login, password):
		self.login = login
		# Из def password
		self.password = password

	@property
	def password(self):
		print(f"getter call")
		return self.__password

	@staticmethod
	def is_include_num(new_password):
		for el_digit in digits:
			if el_digit in new_password:
				return True
		return False

	@password.setter
	def password(self, new_password):
		print(f"setter call")

		if not isinstance(new_password, str):
			raise TypeError("Password must be of type string")

		if len(new_password) < 8:
			raise ValueError("Password length must be 8 characters")

		if len(new_password) > 255:
			raise ValueError("Password exceeds 255 characters")

		if not RegistrationUser.is_include_num(new_password):
			raise ValueError("Password must contain numbers")

		self.__password = new_password
