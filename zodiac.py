class Zodiac:
	def __init__(self, name, symbol, month1, month2, start_day1, end_day1, start_day2, end_day2):
		self.name = name
		self.symbol = symbol
		self.month1 = month1
		self.month2 = month2
		self.start_day1 = start_day1
		self.end_day1 = end_day1
		self.start_day2 = start_day2
		self.end_day2 = end_day2	
	def __str__(self):
		print('\nYour zodiac sign is "{}", your zodiac symbol is "{}".'.format(self.name, self.symbol))

	
horoscopes =  [Zodiac("Aries", "The Ram", "march", "april", 21, 31, 1, 19), Zodiac("Taurus", "The Bull", "april", "may", 20, 30, 1, 20), Zodiac("Gemini", "The Twin", "may", "june", 21, 31, 1, 20), Zodiac("Cancer", "The Crab", "june", "july", 21, 31, 1, 22),  Zodiac("Leo", "The Lion", "july", "august", 23, 31, 1, 22), Zodiac("Virgo", "The Virgin", "august", "september", 23, 31, 1, 22), Zodiac("Libra", "The Scales", "september", "october", 23, 30, 1, 22), Zodiac("Scorpio", "The Scorpion", "october", "november", 23, 31, 1, 21), Zodiac("Saggitarius", "The Archer", "november", "december", 22, 31, 1, 21), Zodiac("Capricorn", "The Goat", "december", "january", 22, 31, 1, 19), Zodiac("Aquarius", "The Water Bearer", "january", "february", 20, 31, 1, 18), Zodiac("Pisces", "The Fish", "february", "march", 19, 31, 1, 20)]

def func(horoscopes):
	month_input = input("Enter month of birth (e.g. may): ")
	day_input = int(input("\nEnter day of birth (e.g. 30): "))
	for horoscope in horoscopes:
		for val in range(horoscope.start_day1, horoscope.end_day1 + 1):
			if month_input.lower() == horoscope.month1:
				if day_input == val:
						return horoscope.__str__()
			elif month_input.lower() == horoscope.month1[:3]:
					if day_input == val:
						return horoscope.__str__()
					
	for horoscope in horoscopes:
		for val in range(horoscope.start_day2, horoscope.end_day2 + 2):
			if month_input.lower() == horoscope.month2:
				if day_input == val:
						return horoscope.__str__()
			elif month_input.lower() == horoscope.month2[:3]:
				if day_input == val:
						return horoscope.__str__()
					

func(horoscopes)