def main():
	print("Mad libs where libs get mad. \nStart below:\n")
	time = input("Enter a time from 1 to 12: ")
	items = input("Enter a items (plural): ")
	name = input("Enter a name: ")
	scream = input("Enter any sentance: ")
	action = input("Enter a verb: ")
	print(f"\nThe story goes...\nIt was {time} o'clock when I heard a knock at the door. I opened the door and there was a box full of {items} with a note saying \"From Mr. {name}.\" Just as I closed the door I heard a scream \"{scream.upper()}.\" I froze in place and all I could do was {action}.")




if __name__ == '__main__':
	main()