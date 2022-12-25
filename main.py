'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import subprocess


a = 0
while (a < 999):
    def cmd_test():
    # cmd = 'cmd.exe d:/start.bat'
    p = subprocess.Popen("cmd.exe /c" + "d:/start.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    curline = p.stdout.readline()



    a = a + 1 
    