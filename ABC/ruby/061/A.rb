A,B,C = gets().chomp.split(' ').map { |n| n.to_i }

exit if !( -100 <= A && A <= 100 && -100 <= B && B <= 100 && -100 <= C && C <= 100 )
puts A <= C && C <= B ? 'Yes' : 'No'