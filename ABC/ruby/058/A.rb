array = []
array = gets().chomp.split(' ')
exit if !( (array[0] =~ /^[0-9]+$/) && (array[1] =~ /^[0-9]+$/) && (array[2] =~ /^[0-9]+$/) )
A = array[0].to_i
B = array[1].to_i
C = array[2].to_i

exit if !( 1 <= A && 1 <= B && 1 <= C && A <= 100 && B <= 100 && C <= 100 )

puts B - A == C - B ? 'YES' : 'NO'