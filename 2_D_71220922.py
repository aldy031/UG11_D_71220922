def cetakHuruf () :
    huruf=(input("Masukkan kata :"))
    list=(huruf)
    len(huruf)
    if(len(huruf)%2==0) :
        print("Huruf paling ujung pada kata", huruf, "adalah", (huruf[-3:]))
    else :
        print("Huruf paling ujung pada kata", huruf, "adalah",(huruf[:3]))
    return (huruf)
cetakHuruf()