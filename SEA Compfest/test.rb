# insert_dash = ->(number) {
#     state = false
#     array = number.to_s.split('')
#     for i in array do
#         if(!state)
#             if(i.to_i.odd?)
#                 state = true
#                 print i
#             else
#                 print i
#             end
#         elsif (state && i.to_i.odd?)
#             print "-#{i}"
#             state = true
#         else
#             state = false
#         end
#     end
#     puts
# }

# insert_dash.(13579)

# high_and_low = ->(string) {
#     array = string.split(' ').map {|i| i.to_i}
#     low = 0
#     high = array.length - 1
#     (array.length/2 + 1).times {|i| 
#         if(array[low] > array[high])
#             high -= 1
#         elsif (array[low] < array[high])
#             low += 1
#         end
#     }
#     high_final = high
#     low = 0
#     high = array.length - 1
#     (array.length/2 + 1).times {|i| 
#         if(array[low] < array[high])
#             high -= 1
#         elsif (array[low] > array[high])
#             low += 1
#         end
#     }
#     low_final = low

#     puts "#{array[high_final]} #{array[low_final]}"

# }

# high_and_low.("-1 -1")

# find_longest = ->(array) {
#     longest = nil
#     size = 0
#     array.length.times {|i|
#         if(array[i].to_s.length > size)
#             longest=array[i]
#             size = array[i].to_s.length
#         end
#     }
#     puts "#{longest}"
# }

# find_longest.([1,100,200])

# def group_and_count(array)
#     hash_temp = {}
#     array.each {|i| 
#         if(!hash_temp.include?(i))
#             hash_temp[i] = array.count(i)
#         end
#     }
#     return hash_temp
# end

# puts group_and_count([1,1,2,2,2,3])

# def checkerboard(integer)
#     state = false
#     checker = ""
#     if(integer%2 != 0)
#         integer.times {
#             integer.times {
#                 if(!state)
#                     checker += "[r]"
#                     state=!state
#                 else 
#                     checker += "[b]"
#                     state=!state
#                 end
#             }
#             checker += "\n"
#         }
#     else
#         integer.times {
#             integer.times {
#                 if(!state)
#                     checker += "[r]"
#                     state=!state
#                 else 
#                     checker += "[b]"
#                     state=!state
#                 end
#             }
#             checker += "\n"
#             state=!state
#         }
#     end
#     return checker
# end

# puts checkerboard(5)

# def descending(integer)
#     integer = integer.to_s.split('').sort {|a,b| b <=> a}
#     return integer.join('').to_i
# end

# puts descending(21445) # will return 54421
# puts descending(145263) # will return 654321
# puts descending(1254859723) # will return 9875543221

# def in_array(sub,array)
#     temp = []
#     sub.each { |i|
#         array.each { |j|
#             if(j.include?(i))
#                 temp.push i
#                 break
#             end           
#         }
#     }
#     return temp
# end

# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# print in_array(a1, a2) 
# # will return: ["arp", "live", "strong"]

# a1 = ["tarp", "mice", "bull"]
# print in_array(a1, a2)
# # will return: []

# def unique_sum(array)
#     sum = 0
#     state = false
#     before = []
#     array.each { |i|
#         if(!state)
#             sum += i
#             before.push i
#             state = true
#         else
#             if(before.include? i)
#                 next
#             else
#                 sum += i
#                 before.push i
#             end
#         end     
#     }
#     sum
# end

# puts unique_sum([1, 2, 3])
# # return 6

# puts unique_sum([1, 3, 8, 1, 8])
# # return 12

# puts unique_sum([-1, -1, 5, 2, -7])
# # return -1

# spoken    = lambda { |x| puts x.capitalize}
# spoken.call("Aloha") # return "Aloha."

# shouted   = lambda { |x| puts x.upcase }
# shouted.call("Aloha") # return "ALOHA."

# whispered = lambda { |x| puts x.downcase }
# whispered.call("Aloha") # return "aloha."

# greet = ->(lam,string) {
#     lam.call(string)
# }

# greet.call(spoken, "Halo")     # return "Halo."
# greet.call(shouted, "Halo")    # return "HALO!"
# greet.call(whispered, "Halo")  # return "halo."

# require 'date'

# user_name = ARGV.first # gets the first argument
# prompt = '> '

# puts "Hi #{user_name}."
# puts "I'd like to ask you a few questions."
# puts "In what year were you born, #{user_name}? "
# puts prompt
# year = gets.chomp.to_i

# puts "Alright, so you're #{Date.today.year - year} years old now."

# filename = ARGV.first

# # Here is how you open a file in write mode in Ruby
# output_stream = open(filename, "r")

# # Here is how you read the content of a file in Ruby
# output_stream.read()

# # Don't forget to close the file afterward
# output_stream.close

# def test(*args)
#     puts args
# end

# test(username:"asdasd",password:'asgasgasg')

# def add(*integer)
#     first,*last = integer
#     last.each { |i|
#         first += i
#     }
#     first
# end

# def substract(*integer)
#     first, *last = integer
#     last.each { |i|
#         first -= i
#     }
#     first
# end

# def calculate(*args)
#     methods = args[-1].is_a?(Hash) ? (args[-1].values[0] ? args.pop.keys[0] : :add) : :add
#     method(methods).call(*args)
# end
