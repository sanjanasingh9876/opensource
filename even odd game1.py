def find_winner(N):
    digit_sum = sum(int(digit)
for digit in str(N))
    if digit_sum % 2 == 0:
        return "Vignesh"
    else:
        return "Charan"
N=int(input().strip())
print(find_winner(N))
