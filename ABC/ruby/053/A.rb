x = gets().chomp
exit if !(x =~ /^[0-9]+$/)
X = x.to_i
exit if !( 1 <= X && X <= 3000 )

puts  X < 1200 ? 'ABC' : 'ARC'