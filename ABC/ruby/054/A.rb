a,b = gets().chomp.split(' ')
exit if !(( a =~ /^[0-9]+$/) && ( b =~ /^[0-9]+$/))
A = a.to_i
B = b.to_i
exit if !( 1 <= A && A <= 13 )
exit if !( 1 <= B && B <= 13 )


if A == B then puts 'Draw';exit end
puts ((A-2) % 13 > (B-2) % 13) ? 'Alice' : 'Bob'