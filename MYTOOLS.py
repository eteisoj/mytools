PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def pi_real(N):
    if N <= 0 or N >= 100:
        print("N precisa ser maior do que 0 e menor do  que 100!")
        return None
    else:
        return("3," + PI_INT[:N])

E_INT = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def e_real(N):
    if N <= 0 or N >= 100:
        print("N precisa ser maior do que 0 e menor do  que 100!")
        return None
    else:
        return("2," + E_INT[:N])
    
