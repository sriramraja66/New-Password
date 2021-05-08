import os,time

class settings:
    def cls(self):
        os.system('clear')

    def sec(self,sec : int):
        time.sleep(sec)

    def integer_in(self,s):
        i = input(s)
        try:
            if i.isdigit():
                return int(i)
        except:
            print("Not A Number...")
            quit()
            
if __name__ == '__main__':
    s = settings()