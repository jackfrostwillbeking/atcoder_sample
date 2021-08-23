N,M = gets().chomp.split(' ').map { |n| n.to_i }
loads = []
M.times {
    loads << gets().chomp.split(' ').map { |n| n.to_i }
}
exit if !( 2 <= N && N <= 50 && 2 <= M && M <= 50 )

loads.each { |load|
    exit if load[0] == load[1]
    exit if !(1 <= load[0] && load[0] <= N)
    exit if !(1 <= load[1] && load[1] <= N)
}

(1..N).each { |count|
    res = loads.flatten.count(count)
    puts res if res != 0
}