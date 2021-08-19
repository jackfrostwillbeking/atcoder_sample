N = gets().chomp.to_i
exit if !( 1 <= N && N <= 100 )

puts (800*N - ((N / 15).to_i)*200)