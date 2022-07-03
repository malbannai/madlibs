def main():
	print("Mad libs where libs get mad. \nStart below:\n")
	number = input("Enter a number from 1 to 12: ")
	noun = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	sent = input("Enter any sentence: ")
	varb = input("Enter a verb: ")
	print(f"\nThe story goes...\nIt was {number} o'clock when I heard a knock at the door. I opened the door and there was a box full of {noun} with a note saying \"From Mr. {name}.\" Just as I closed the door I heard a scream \"{sent.upper()}.\" I froze in place and all I could do was {varb}.")




if __name__ == '__main__':
	main()