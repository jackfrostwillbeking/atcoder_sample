array_input=gets.chomp.split(" ")
array_input = array_input.map do | num |
    num.to_i
end
# puts array_input
puts (array_input & [0,1]).length
exit()
exit() if !(1 <= array_input.length) || !(array_input.length <= 10**9)
array_input.each do | num |
    exit() if num - num.to_i != 0 
    exit() if !( 1 <= num ) || !( num <= 200 )
end

tmp_array=[]

count = 0
while array_input.count(0,1) == 1
    array_input.each_with_index { |index,num| if num % 2 == 0 then array_input[index] = (num/2);count += 1 else break end }
end
puts array_input
puts count
puts count / array_input.length
# do | num |
#     tmp_array num % 2 == 0 ? num % 2 : (puts count)
# end
# puts tmp_array