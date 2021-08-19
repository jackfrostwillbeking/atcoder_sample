N = gets().chomp.to_i
exit if !( 1 <= N && N <= 10**5 )
m = (10**9+7)
res = 1
(1..N).each { |n| res = (res%m)*n }
puts res % m