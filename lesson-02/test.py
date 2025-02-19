import os

def main():
    print(os.environ)
    print(os.getenv('IS_DEBUG'))

main()
