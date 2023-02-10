def foo (s):
    n = int (s)
    print(n)
    assert n != 0,'sss'
    return n + 19
def main():
    foo(1)

main()
