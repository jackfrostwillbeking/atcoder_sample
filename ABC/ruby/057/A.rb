A,B = gets().chomp.split(' ').map { |n| n.to_i }

exit if !( 0 <= A && A <= 23 && 0 <= B && B <= 23 )

puts  A + B  < 24 ? A + B : A + B - 24 