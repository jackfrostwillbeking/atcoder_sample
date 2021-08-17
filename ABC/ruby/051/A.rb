input = gets.chomp
exit() if input.length != 19
exit() if !(input[5] == ',' && input[13] == ',')
exit() if /[[:upper:]]/.match(input)
puts input.gsub(/,/,' ')