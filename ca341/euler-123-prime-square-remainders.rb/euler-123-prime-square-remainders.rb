class PrimeSquareRemainders
    def initialize(n)
        @upper_limit = n
        @least_value = get_least_value(@upper_limit)
    end

    def is_prime(num)
        if num <= 1 then
            return false
        elsif num <= 3 then
            return true
        elsif num % 2 == 0 or num % 3 == 0 then
            return false
        end
        i = 5
        while i * i <= num do
            if num % i == 0 or num % (i + 2) == 0 then
                return false
            end
            i = i + 6
        end
        return true
    end


    def nth_prime(n)
        count = 0
        num = 2
        while count < n do
            if is_prime(num) then
                count = count + 1
            end
            if count == n then
                return num
            end
            num = num + 1
        end
    end

    def get_least_value(a)
        i, r, n = 1, 0, 0
        while r < a.to_i do
            n = nth_prime(i)
            r = (((n - 1) ** i) + ((n + 1) ** i)) % (n * n)
            i = i + 2
        end
        return n
    end

    def to_str()
        to_s
    end

    def to_s()
        @least_value
    end
end

val = PrimeSquareRemainders.new(ARGV[0])
puts val.to_s