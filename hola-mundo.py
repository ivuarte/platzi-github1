import os

def hello_world():
    nombre = os.getenv("USERNAME")
    print(f"Hello, {nombre} from Github")

if __name__ == '__main__':
	hello_world()
