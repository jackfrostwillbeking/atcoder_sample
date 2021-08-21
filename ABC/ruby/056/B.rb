W,a,b = gets().chomp.split(' ').map { |n| n.to_i }

exit if !( 1 <= W && W <= 10**5 )
exit if !( 1 <= a && a <= 10**5 && 1 <= b && b <= 10**5 )

puts a - ( b + W ) if b + W < a
puts 0 if ( a <= b + W && a >= b ) || ( a <= b && b <= a + W )
puts b - ( a + W ) if a + W < b