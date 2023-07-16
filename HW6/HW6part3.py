from colorama import Fore, Style


class colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            print(f'{Fore.RED}')
        if self.color == 'green':
            print(f'{Fore.GREEN}')
        if self.color == 'magenta':
            print(f'{Fore.MAGENTA}')
        if self.color == 'blue':
            print(f'{Fore.BLUE}')
        if self.color == 'white':
            print(f'{Fore.WHITE}')
        if self.color == 'black':
            print(f'{Fore.BLACK}')
        if self.color == 'yellow':
            print(f'{Fore.YELLOW}')
        if self.color == 'cyan':
            print(f'{Fore.CYAN}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{Style.RESET_ALL}')


with colorizer('red'):
    print('printed in red')
print('printed in default color')
