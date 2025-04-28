def DiffeHellman(p:int, g:int):
    private_key_A = int(input("Enter A's Private Key"))
    private_key_B = int(input("Enter Bs Private Key"))
    
    public_key_A = (g ** private_key_A) % p
    public_key_B =  (g **private_key_B) % p
    
    print(f"Pub key of A: {public_key_A}")
    print(f"Pub key of B: {public_key_B}")
    
    shared_secret_A = (public_key_B ** private_key_A) % p
    shared_secret_B = (public_key_A ** private_key_B) % p
    
    print(f" Shared Secret by A {shared_secret_A}")
    print(f" Shared Secret by B {shared_secret_B}")
    
    if shared_secret_A == shared_secret_B:
        print("Key Matched! Key Exch Successfull")
    else:
        print("Do not Match, Just like you and Her")
        
if __name__ =="__main__":
    DiffeHellman(23, 5)