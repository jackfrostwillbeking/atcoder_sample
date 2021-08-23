A = gets().chomp.to_i
B = gets().chomp.to_i

exit if !( 1 <= A && A <= 10**100 && 1 <= B && B <= 10**100 )
puts  A == B ? 'EQUAL' : A > B ? 'GREATER' : 'LESS'