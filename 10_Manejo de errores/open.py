# def main():
#     open("/path/to/mars.jpg")

# if __name__ == '__main__':
#     main()

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudó encontrar el archivo")


if __name__ == '__main__':
    main()