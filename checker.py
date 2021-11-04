def check_value_return_data(s):
    ####kill spaces
	s = s.replace(" ", "")
	####
	s1 =s
	T = True
	Flag = False
	mins = []
	seconds = []
	mins_fl = 0
	seconds_fl = 0

	##### check out other symbols
	for i in range(len(s1)):
		if s1[i].isdigit() == 0 and s1[i] != ':':
			print("failure")
			T = False
			break
###############

####### add digits to list
	if s1.count(':') == 1:
		if T:
			for j in range(len(s1)):
				if s1[j] == ':':
					Flag = True
				if Flag == False:
					mins.append(s1[j])
				else:
					if s1[j] != ':':
						seconds.append(s1[j])
	else:
			print("failure")
			T = False
##########

########Convert digits
	if T:
		for i in range(len(mins)):
			mins_fl = mins_fl + int(mins[i])*(10**(len(mins)-i-1))
		for j in range(len(seconds)):
			seconds_fl = seconds_fl + int(seconds[j])*(10**(len(seconds)-j-1))
	if T:
		return (mins_fl * 60 + seconds_fl) / 60 
	else:
		return -1

def check_cwf(s):
	####kill spaces
	s = s.replace(" ", "")
	####
	s1 =s
	T = True
	Flag = False
	mins = []
	seconds = []
	mins_fl = 0
	seconds_fl = 0

	##### check out other symbols
	for i in range(len(s1)):
		if s1[i].isdigit() == 0 and s1[i] != '.':
			T = False
			break
###############
####### add digits to list
	if s1.count('.') <= 1:
		if T:
			for j in range(len(s1)):
				if s1[j] == '.':
					Flag = True
				if Flag == False:
					mins.append(s1[j])
				else:
					if s1[j] != '.':
						seconds.append(s1[j])
	else:
			T = False

	if T:
		for i in range(len(mins)):
			mins_fl = mins_fl + int(mins[i])*(10**(len(mins)-i-1))
		for j in range(len(seconds)):
			seconds_fl = seconds_fl + int(seconds[j])*(10**(len(seconds)-j-1))
	if T:
		return mins_fl + seconds_fl*10**(-len(seconds))
	else:
		return -1	
