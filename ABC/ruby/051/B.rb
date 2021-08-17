# TLE
ary_input = gets.chomp.split(' ')
K = ary_input[0].to_i
S = ary_input[1].to_i
exit() if !(2 <= K && K <= 2500)
exit() if !(0 <= S && S <= 3*K)

count = 0
X = 0
while X <= K do
    Y = 0
    while Y <= K do
      Z = 0
      Z = S - X - Y
      count += 1 if Z <= K && Z >= 0 
      Y += 1
    end
    X += 1
end
p count