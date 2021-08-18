N,M = gets().chomp.split(' ').map { |a| a.to_i }
A = []
B = []
exit if !(( 1 <= M && M <= 50) && ( 1 <= N && N <= 50 ) && ( M <= N ))

(1..N).each {
  A << gets().chomp
}
(1..M).each { |n|
  B << gets().chomp
  if (A[n-1].include? B[n-1]) then next else puts 'No';exit end
}
puts 'Yes'