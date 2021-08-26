H,W = gets().chomp.split(' ').map { |n| n.to_i }
exit if !( 1 <= H && H <= 100 && 1 <= W && W <= 100 )
B = Array.new(H) { gets().chomp.split(' ') }
header_footer = Array.new(W+2) { '#' }

puts header_footer.join()
H.times { |n|
    puts ("##{B[n].join()}#")
}
puts header_footer.join()