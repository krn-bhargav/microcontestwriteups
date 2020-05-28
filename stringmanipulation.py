import libmicrocontest,sys,os,time

def main():
    con = libmicrocontest.commence_contest(42,'kapslock','')
    s1 = con.get_str('s1')
    s2 = con.get_str('s2')
    print('[+]s1 :: '+str(s1))
    print('[+]s2 :: '+str(s2))
    s3 = str(s1)+str(s2)
    print('[+]s3 :: '+str(s3))
    con.append_answer('s3',s3)
    print(con.submit_answer())

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()