s = gets().chomp
exit if !( 1 <= s.length && s.length <= 200000 )
exit if !(/[[:upper:]]/.match(s))

Acounter = 0
Zcounter = 0
s.each_char { |char|
    char == 'A' ? break : Acounter += 1
}
s.reverse.each_char { |char|
    char == 'Z' ? break : Zcounter += 1
}
puts (s.length - Acounter - Zcounter)