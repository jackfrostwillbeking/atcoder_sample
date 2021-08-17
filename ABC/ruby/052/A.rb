A,B,C,D = gets.chomp.split(' ')
exit if !((A =~ /^[0-9]+$/) && (B =~ /^[0-9]+$/) && (C =~ /^[0-9]+$/) && (D =~ /^[0-9]+$/))
a = A.to_i
b = B.to_i
c = C.to_i
d = D.to_i
exit if !(( 1 <= a && a <= 10**4 ) && ( 1 <= b && b <= 10**4 ) && ( 1 <= c && c <= 10**4 ) && ( 1 <= d && d <= 10**4 ))

puts (a*b >= c*d) ? a*b : c*d