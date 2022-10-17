import sqlite3

# define all variables used
myQuery_str = ""
myQuery_str1 = ""
myQuery_str2 = ""
myQuery_str3 = ""
myQuery_str4 = ""
myQuery_str5 = ""
myTable = "nba_handtracking"
db_connect = "project.sqlite3" # name of the current database
conn = sqlite3.connect(db_connect)


def menu():
	""" menu function to ask user what function is to be performed"""
	options_list = [1, 2, 3, 4, 5, 6, 7] # can add more if more queries are needed

	#prmpt_str = f"\n\t 1 = To show everything in the Table\n\t 2 = To show the points per touch of the champions in the Table\n\t 3 = query2(add query)\n\t 4 = Show Point, Minute and Touch data per player\n\t 5 = Display Time of Possession and Points per Player\n\t 6 = Enter a custom SQL query\n\t Enter any number not listed to exit\n\t\t Enter integer :"
	prmpt_str = f"\n\t 1 = To show everything in the Table\n\t 2 = To show the points per touch of the champions in the Table\n\t 3 = This option shows average paint touches per indivdual and their total wins\n\t 4 = Show Point, Minute and Touch data per player\n\t 5 = Display Time of Possession and Points per Player\n\t 6 = This shows players average seconds per touch and their scoring averages\n\t 7 = Enter a custom SQL query\n\t Enter any number not listed to exit\n\t\t Enter integer :"

	# Each attribute is assigned a number. Show the attributes and allow user to choose a number.

	result_int = "" # declare value before the below code block to keep the value in memory after the block has been execute

	# get an input from user; use exceptions
	while not isinstance((result_int), int):
		try:
			result_int = int(input(prmpt_str))
			if result_int in options_list:
				print(f"\t [+] Option {result_int} chosen.") # create? populate? query or modify a table?
			else:
				print(f"\t [+] Exiting...")
		except ValueError:
			print("\t [-] First Exception Handled: Could not convert data to an integer.")
			print("\t [-] Please select an option listed or exit.")

	if result_int == 1:
		question1(myQuery_str, conn) # call this function if result_int is 1
	if result_int == 2:
		question2(myQuery_str1, conn) # call this function if result_int is 2
	if result_int == 3:
		question3(myQuery_str2, conn) # call this function if result_int is 3
	if result_int == 4:
		question4(myQuery_str3, conn) # call this function if result_int is 4
	if result_int == 5:
		question5(myQuery_str4, conn) # call this function if result_int is 5
	if result_int == 6:
		question6(myQuery_str5, conn) # call this function if result_int is 6
	if result_int == 7:
		custom_query(conn)
	else:
		exit = True
		quit()
	return result_int
# end of menu()


def question1(in_str, conn):
	""" print a welcome message for option 2, QUERY"""
	print("\n\t [+] Welcome to QUERY()")

	#########################
	# Query data in a table
	myQuery_str = f"SELECT * FROM {myTable}"

	print(f" [+] Running Query:\n {myQuery_str}") #run the query
	# Get result from query
	result = conn.execute(myQuery_str)
	print(f" [+] Results from query: ")
	queryInfo_list = result.fetchall()
	for i in queryInfo_list:
		print(f"\t[+] {i}")

	main()
	# end of question1()

def question2(in_str, conn):
	""" print a welcome message for option 2, QUERY"""
	print("\n\t [+] Welcome to QUERY()")
	print("\n\t [+] This shows the average touches per game and average points per touch of the reigning champions the Bucks")

	#########################
	# Query data in a table
	myQuery_str1 = f"select  Touches, PTS_PER_TOUCH, team from {myTable} where team == 'MIL'"

	print(f" [+] Running Query:\n {myQuery_str1}") #run the query
	# Get result from query
	result = conn.execute(myQuery_str1)
	print(f" [+] Results from query: ")
	queryInfo_list = result.fetchall()

	for i in queryInfo_list:
		print(f"\t[+] {i}")

	main()
	# end of question2()

def question3(in_str, conn):
	""" print a welcome message for option 2, QUERY"""
	print("\n\t [+] Welcome to QUERY()")
	print("\n\t [+] This option shows average paint touches per individual and their total wins")

	#########################
	# Query data in a table
	myQuery_str2 = f"select player, team, W, PAINT_TOUCHES from {myTable};"

	print(f" [+] Running Query:\n {myQuery_str2}") #run the query
	# Get result from query
	result = conn.execute(myQuery_str2)
	print(f" [+] Results from query: ")
	queryInfo_list = result.fetchall()

	for i in queryInfo_list:
		print(f"\t[+] {i}")

	main()
	# end of question3()

def question4(in_str, conn):
	""" print a welcome message for option 2, QUERY"""
	print("\n\t [+] Welcome to QUERY()")

	#########################
	# Query data in a table
	myQuery_str3 = f"SELECT player, PTS, Min, Touches FROM {myTable} WHERE Pts > 10 AND Min > 25"

	print(f" [+] Running Query:\n {myQuery_str3}") #run the query
	# Get result from query
	result = conn.execute(myQuery_str3)
	print(f" [+] Results from query: ")
	queryInfo_list = result.fetchall()

	for i in queryInfo_list:
		print(f"\t[+] {i}")

	main()
	# end of question4()

def question5(in_str, conn):
	""" print a welcome message for option 2, QUERY"""
	print("\n\t [+] Welcome to QUERY()")

	#########################
	# Query data in a table
	myQuery_str4 = f"SELECT player, Time_of_Poss, PTS FROM {myTable} WHERE Time_of_Poss > 1"

	print(f" [+] Running Query:\n {myQuery_str4}") #run the query
	# Get result from query
	result = conn.execute(myQuery_str4)
	print(f" [+] Results from query: ")
	queryInfo_list = result.fetchall()

	for i in queryInfo_list:
		print(f"\t[+] {i}")

	main()
	# end of question5()

def question6(in_str, conn):
	""" print a welcome message for option 2, QUERY"""
	print("\n\t [+] Welcome to QUERY()")
	print("\n\t [+] This shows players average seconds per touch and their scoring averages")
	
	#########################
	# Query data in a table
	myQuery_str5 = f"select player, time_of_poss, pts from {myTable}"

	print(f" [+] Running Query:\n {myQuery_str5}") #run the query
	# Get result from query
	result = conn.execute(myQuery_str5)
	print(f" [+] Results from query: ")
	queryInfo_list = result.fetchall()

	for i in queryInfo_list:
		print(f"\t[+] {i}")

	main()
	# end of query()

def custom_query(conn):
	""" Allow the user to enter a custom query """
	print("\n\t [+] Table name: nba_handtracking")
	query = input("\tEnter a custom SQL query: ")

	print(f" [+] Running Query:\n {query}") #run the query
	# Get result from query
	result = conn.execute(query)
	print(f" [+] Results from query: ")
	queryInfo_list = result.fetchall()

	# Iterate through query results
	for i in queryInfo_list:
		print(f"\t[+] {i}")
	
	main()
	#end of custom_query()

def main():
	# the program actually starts here. The dictionary of table names tables_dict is a global variable and is accessible by all functions, as necessary.
	exit = False
	print("\t Welcome to NBA Statistics! ")
	
	while exit == False:
		result_int = menu()
	
	##########################
	# connect database
	db_connect = "project.sqlite3" # name of the current database
	conn = sqlite3.connect(db_connect)
	# conn.close() # close the database connection

	print("  -- End of program --")
# end of main()


# -----------------------------------------


	

main() # call and run the driver function main().

