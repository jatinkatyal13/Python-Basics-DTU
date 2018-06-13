try:
	from .library import * # when i use it as a package
except:
	from library import * # when i call it directly

print(__name__)

def main():
	print(add(1, 2))

if __name__ == "__main__":
	main()
